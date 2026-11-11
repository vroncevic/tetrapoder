# -*- coding: UTF-8 -*-

'''
Module
    builder.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    tetrapoder is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    tetrapoder is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Builder for Cartesian and joint trajectory keyframes.
'''

from __future__ import annotations

from struct import pack
from typing import Self

from tetrapoder.core.model.command_id import CommandId
from tetrapoder.core.model.leg_angles import LegAngles
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.plan_command import PlanCommand
from tetrapoder.core.model.point3d import Point3D
from tetrapoder.core.service.kinematics.isolver import IKinematicsSolver

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TrajectoryBuilder:
    '''
        Defines class TrajectoryBuilder implementing ITrajectoryBuilder structurally.
        Constructs Cartesian and joint keyframe trajectory sequences.

        It defines:

            :attributes:
                | _commands - Mutable accumulator list of plan commands.
                | _solver - Injected kinematics calculation solver.
            :methods:
                | __init__ - Initializes TrajectoryBuilder with kinematics solver and optional commands.
                | add_keyframe - Solves IK and enqueues joint keyframe from Cartesian coordinates.
                | add_joint_keyframe - Directly enqueues joint angles in degrees.
                | build - Constructs immutable MotionPlan from accumulated commands.
    '''

    _commands: list[PlanCommand]
    _solver: IKinematicsSolver

    def __init__(
        self,
        solver: IKinematicsSolver,
        commands: list[PlanCommand],
    ) -> None:
        '''
            Initializes TrajectoryBuilder with kinematics solver and commands accumulator.

            :param solver: Injected IKinematicsSolver provider.
            :param commands: Injected mutable accumulator list.
            :exceptions: None.
        '''
        self._solver = solver
        self._commands = commands

    def add_keyframe(self, leg: int, target: Point3D, duration_ms: int = 200) -> Self:
        '''
            Computes inverse kinematics on PC and enqueues joint angle keyframe.

            :param leg: Leg index (0..3) or 0xFF for all legs.
            :param target: Point3D Cartesian coordinates in mm.
            :param duration_ms: Interpolation duration in ms.
            :return: Self for chaining.
            :exceptions: None.
        '''
        target_leg: int = 0 if leg == 0xFF else (leg & 0x03)
        angles: LegAngles = self._solver.solve(target_leg, target)
        return self.add_joint_keyframe(leg, angles, duration_ms)

    def add_joint_keyframe(self, leg: int, angles: LegAngles, duration_ms: int = 200) -> Self:
        '''
            Enqueues keyframe with explicit joint angles in degrees.

            :param leg: Leg index (0..3) or 0xFF for all legs.
            :param angles: LegAngles shaft angles in degrees (0..180).
            :param duration_ms: Interpolation duration in ms.
            :return: Self for chaining.
            :exceptions: None.
        '''
        c_i16, f_i16, t_i16 = self._solver.to_tenths(angles)
        payload: bytes = pack('>BhhhH', leg & 0xFF, c_i16, f_i16, t_i16, duration_ms & 0xFFFF)
        desc: str = (
            f'Joint keyframe leg {leg}: ({angles.coxa:.1f}°, {angles.femur:.1f}°, '
            f'{angles.tibia:.1f}°) over {duration_ms}ms'
        )
        self._commands.append(PlanCommand(cmd_id=int(CommandId.QUEUE_KEYFRAME), payload=payload, description=desc))
        return self

    def build(self) -> MotionPlan:
        '''
            Constructs immutable MotionPlan from accumulated commands.

            :return: Immutable MotionPlan instance.
            :exceptions: None.
        '''
        return MotionPlan(commands=tuple(self._commands))
