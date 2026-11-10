# -*- coding: UTF-8 -*-

'''
Module
    gait_type.py
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
    Enumeration of predefined gait types and postures for quadruped robot.
'''

from __future__ import annotations

from enum import IntEnum

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GaitType(IntEnum):
    '''
        Predefined robot movement and posture gait identifiers.

        It defines:

            :attributes:
                | SIT - Resting seated posture.
                | STAND - Default neutral standing pose.
                | STEP_FORWARD - Forward walking gait.
                | STEP_BACKWARD - Backward walking gait.
                | TURN_LEFT - Counter-clockwise yaw rotation in place.
                | TURN_RIGHT - Clockwise yaw rotation in place.
                | HAND_WAVE - Greeting gesture waving front leg.
    '''

    SIT = 0
    STAND = 1
    STEP_FORWARD = 2
    STEP_BACKWARD = 3
    TURN_LEFT = 4
    TURN_RIGHT = 5
    HAND_WAVE = 6
