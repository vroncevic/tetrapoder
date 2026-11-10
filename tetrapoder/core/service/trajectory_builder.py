# -*- coding: UTF-8 -*-

'''
Module
    trajectory_builder.py
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
    Builder for Cartesian trajectory keyframes and choreographic actions.
'''

from __future__ import annotations

from struct import pack
from typing import Self

from tetrapoder.core.model.foot_position import FootPosition
from tetrapoder.core.model.leg_angles import LegAngles
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.service.command_id import CommandId
from tetrapoder.core.service.gait_type import GaitType
from tetrapoder.core.service.kinematics_solver import KinematicsSolver

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
        Constructs Cartesian keyframes, joint angle targets, and choreographic actions.

        It defines:

            :attributes:
                | _plan - Reference to target MotionPlan instance.
            :methods:
                | __init__ - Initializes TrajectoryBuilder with target MotionPlan.
                | add_keyframe - Solves IK and enqueues joint keyframe from Cartesian coordinates.
                | add_joint_keyframe - Directly enqueues joint angles in degrees.
                | set_speed - Sets robot speed multiplier (1..10).
                | action_wave - Adds wave gesture command.
                | emergency_stop - Adds stop command.
    '''

    _plan: MotionPlan

    def __init__(self, plan: MotionPlan) -> None:
        '''
            Initializes TrajectoryBuilder with target MotionPlan.

            :param plan: Target MotionPlan container.
            :exceptions: None.
        '''
        self._plan = plan

    def add_keyframe(self, leg: int, target: FootPosition, duration_ms: int = 200) -> Self:
        '''
            Computes inverse kinematics on PC and enqueues joint angle keyframe.

            :param leg: Leg index (0..3) or 0xFF for all legs.
            :param target: FootPosition Cartesian coordinates in mm.
            :param duration_ms: Interpolation duration in ms.
            :return: Self for chaining.
            :exceptions: None.
        '''
        target_leg: int = 0 if leg == 0xFF else (leg & 0x03)
        angles: LegAngles = KinematicsSolver.solve(target_leg, target)
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
        c_i16, f_i16, t_i16 = angles.to_tenths()
        payload: bytes = pack('>BhhhH', leg & 0xFF, c_i16, f_i16, t_i16, duration_ms & 0xFFFF)
        desc: str = (
            f'Joint keyframe leg {leg}: ({angles.coxa:.1f}°, {angles.femur:.1f}°, '
            f'{angles.tibia:.1f}°) over {duration_ms}ms'
        )
        self._plan.add_command(int(CommandId.QUEUE_KEYFRAME), payload, desc)
        return self

    def set_speed(self, speed: int) -> Self:
        '''
            Sets global speed multiplier (1..10).

            :param speed: Speed multiplier integer.
            :return: Self for chaining.
            :exceptions: None.
        '''
        clamped_speed: int = max(1, min(10, speed))
        payload: bytes = pack('>B', clamped_speed)
        self._plan.add_command(int(CommandId.SET_SPEED), payload, f'Set Speed {clamped_speed}')
        return self

    def action_wave(self, count: int = 2) -> Self:
        '''
            Adds hand wave choreographic action.

            :param count: Number of wave cycles.
            :return: Self for chaining.
            :exceptions: None.
        '''
        payload: bytes = pack('>BB', int(GaitType.HAND_WAVE), count & 0xFF)
        self._plan.add_command(int(CommandId.GAIT_STEP), payload, f'Wave {count} times')
        return self

    def emergency_stop(self) -> Self:
        '''
            Adds emergency stop command.

            :return: Self for chaining.
            :exceptions: None.
        '''
        self._plan.add_command(int(CommandId.STOP), b'', 'Emergency Stop')
        return self
