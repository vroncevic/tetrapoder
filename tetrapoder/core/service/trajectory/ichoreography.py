# -*- coding: UTF-8 -*-

'''
Module
    ichoreography.py
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
    Structural interface for robot choreography and action sequence builder.
'''

from __future__ import annotations

from typing import Protocol, Self, runtime_checkable

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
class IChoreographyBuilder(Protocol):
    '''
        Structural protocol defining robot choreography and action sequence builder.

        It defines:

            :methods:
                | set_speed - Sets global speed multiplier.
                | action_wave - Adds hand wave choreographic gesture command.
                | emergency_stop - Adds emergency stop command.
                | build - Constructs immutable MotionPlan from accumulated commands.
    '''

    def set_speed(self, speed: int) -> Self:
        '''
            Sets global speed multiplier (1..10).

            :param speed: Speed multiplier integer.
            :return: Self for method chaining.
        '''

    def action_wave(self, count: int = 2) -> Self:
        '''
            Adds hand wave choreographic action.

            :param count: Number of wave cycles.
            :return: Self for method chaining.
        '''

    def emergency_stop(self) -> Self:
        '''
            Adds emergency stop command.

            :return: Self for method chaining.
        '''

    def build(self) -> MotionPlan:
        '''
            Constructs immutable MotionPlan from accumulated commands.

            :return: Immutable MotionPlan instance.
        '''
