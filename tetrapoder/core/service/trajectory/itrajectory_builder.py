# -*- coding: UTF-8 -*-

'''
Module
    itrajectory_builder.py
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
    Structural interface for trajectory keyframe sequence builder.
'''

from __future__ import annotations

from typing import Protocol, Self, runtime_checkable

from tetrapoder.core.model.foot_position import FootPosition
from tetrapoder.core.model.leg_angles import LegAngles
from tetrapoder.core.model.motion_plan import MotionPlan

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class ITrajectoryBuilder(Protocol):
    '''
        Structural protocol defining trajectory keyframe sequence builder.

        It defines:

            :methods:
                | add_keyframe - Solves IK and enqueues joint keyframe from Cartesian coordinates.
                | add_joint_keyframe - Directly enqueues joint angles in degrees.
                | build - Constructs immutable MotionPlan from accumulated commands.
    '''

    def add_keyframe(self, leg: int, target: FootPosition, duration_ms: int = 200) -> Self:
        '''
            Computes inverse kinematics on PC and enqueues joint angle keyframe.

            :param leg: Leg index (0..3) or 0xFF for all legs.
            :param target: FootPosition Cartesian coordinates in mm.
            :param duration_ms: Interpolation duration in ms.
            :return: Self for method chaining.
        '''

    def add_joint_keyframe(self, leg: int, angles: LegAngles, duration_ms: int = 200) -> Self:
        '''
            Enqueues keyframe with explicit joint angles in degrees.

            :param leg: Leg index (0..3) or 0xFF for all legs.
            :param angles: LegAngles shaft angles in degrees (0..180).
            :param duration_ms: Interpolation duration in ms.
            :return: Self for method chaining.
        '''

    def build(self) -> MotionPlan:
        '''
            Constructs immutable MotionPlan from accumulated commands.

            :return: Immutable MotionPlan instance.
        '''
