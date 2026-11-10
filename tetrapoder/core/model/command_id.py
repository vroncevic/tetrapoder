# -*- coding: UTF-8 -*-

'''
Module
    command_id.py
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
    Enumeration of binary wire protocol command identifiers (PC -> Robot).
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


class CommandId(IntEnum):
    '''
        Enumeration of command identifiers supported by robot controller.

        It defines:

            :attributes:
                | PING - Heartbeat ping query.
                | STOP - Emergency stop / servo disable.
                | SET_SPEED - Set global speed scaling factor.
                | GAIT_STEP - Execute predefined gait step or posture.
                | SET_LEG_SITE - Direct Cartesian target for a leg.
                | SET_LEG_ANGLES - Direct servo angles for a single leg.
                | QUEUE_KEYFRAME - Enqueue joint angles keyframe into memory pool.
                | CLEAR_QUEUE - Clear motion queue and release keyframes.
                | GET_STATUS - Request telemetry status frame.
                | RESET_ERRORS - Clear error flags on controller.
    '''

    PING = 0x01
    STOP = 0x02
    SET_SPEED = 0x03
    GAIT_STEP = 0x10
    SET_LEG_SITE = 0x11
    SET_LEG_ANGLES = 0x12
    QUEUE_KEYFRAME = 0x20
    CLEAR_QUEUE = 0x21
    GET_STATUS = 0x30
    RESET_ERRORS = 0x31
