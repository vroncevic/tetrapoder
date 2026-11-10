# -*- coding: UTF-8 -*-

'''
Module
    igait_plan_builder.py
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
    Structural interface for robot gait sequence builder.
'''

from __future__ import annotations

from typing import Protocol, Self, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IGaitPlanBuilder(Protocol):
    '''
        Structural protocol defining standard quadruped gait sequence builder.

        It defines:

            :methods:
                | stand - Appends standing posture command.
                | sit - Appends sitting posture command.
                | walk - Appends forward or backward walk command.
                | turn - Appends turn left or turn right command.
    '''

    def stand(self) -> Self:
        '''
            Appends standing posture command.

            :return: Self for method chaining.
        '''

    def sit(self) -> Self:
        '''
            Appends sitting posture command.

            :return: Self for method chaining.
        '''

    def walk(self, steps: int = 1, backward: bool = False) -> Self:
        '''
            Appends forward or backward walk command.

            :param steps: Number of walk cycles.
            :param backward: True to walk backward, False for forward.
            :return: Self for method chaining.
        '''

    def turn(self, steps: int = 1, to_right: bool = False) -> Self:
        '''
            Appends turn left or turn right command.

            :param steps: Number of turn cycles.
            :param to_right: True to turn right, False to turn left.
            :return: Self for method chaining.
        '''
