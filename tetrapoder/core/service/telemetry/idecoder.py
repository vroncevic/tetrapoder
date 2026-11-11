# -*- coding: UTF-8 -*-

'''
Module
    idecoder.py
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
    Structural interface for telemetry frame payload decoder.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

from tetrapoder.core.model.imu_telemetry import ImuTelemetry

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class ITelemetryDecoder(Protocol):
    '''
        Structural protocol defining binary telemetry payload decoder.

        It defines:

            :methods:
                | decode - Decodes binary wire payload into ImuTelemetry value object.
                | is_valid_payload - Checks if payload conforms to expected IMU wire size.
    '''

    def decode(self, payload: bytes) -> ImuTelemetry:
        '''
            Decodes binary wire payload into ImuTelemetry value object.

            :param payload: Raw wire payload bytes.
            :return: Decoded ImuTelemetry instance.
        '''

    def is_valid_payload(self, payload: bytes) -> bool:
        '''
            Checks if payload conforms to expected IMU wire size.

            :param payload: Raw wire payload bytes.
            :return: True if valid, False otherwise.
        '''
