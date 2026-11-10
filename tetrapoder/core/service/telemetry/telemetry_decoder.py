# -*- coding: UTF-8 -*-

'''
Module
    telemetry_decoder.py
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
    Concrete implementation of binary telemetry payload decoder.
'''

from __future__ import annotations

from struct import unpack
from typing import ClassVar

from tetrapoder.core.model.exceptions.protocol_error import ProtocolError
from tetrapoder.core.model.imu_telemetry import ImuTelemetry

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TelemetryDecoder:
    '''
        Defines class TelemetryDecoder implementing ITelemetryDecoder contract structurally.
        Decodes binary wire payload into ImuTelemetry value object.

        It defines:

            :attributes:
                | PAYLOAD_LENGTH - Expected byte length of IMU telemetry payload (12 B).
                | ANGLE_SCALE - Scaling divisor for tenths of degree values (10.0).
                | ACCEL_SCALE - Scaling divisor for milli-g acceleration values (1000.0).
            :methods:
                | decode - Decodes binary wire payload into ImuTelemetry value object.
                | is_valid_payload - Checks if payload conforms to expected IMU wire size.
    '''

    PAYLOAD_LENGTH: ClassVar[int] = 12
    ANGLE_SCALE: ClassVar[float] = 10.0
    ACCEL_SCALE: ClassVar[float] = 1000.0

    def is_valid_payload(self, payload: bytes) -> bool:
        '''
            Checks if payload conforms to expected IMU wire size.

            :param payload: Raw wire payload bytes.
            :return: True if valid, False otherwise.
            :exceptions: None.
        '''
        return len(payload) == self.PAYLOAD_LENGTH

    def decode(self, payload: bytes) -> ImuTelemetry:
        '''
            Decodes binary wire payload into ImuTelemetry value object.

            :param payload: Raw wire payload bytes of length 12.
            :return: Decoded ImuTelemetry instance.
            :exceptions:
                | ProtocolError: If payload length is invalid or cannot be unpacked.
        '''
        if len(payload) != self.PAYLOAD_LENGTH:
            raise ProtocolError(
                f'Invalid IMU payload length {len(payload)}: expected {self.PAYLOAD_LENGTH} bytes'
            )

        r_raw, p_raw, ax_raw, ay_raw, az_raw, gz_raw = unpack('>hhhhhh', payload)

        return ImuTelemetry(
            roll=r_raw / self.ANGLE_SCALE,
            pitch=p_raw / self.ANGLE_SCALE,
            accel_x=ax_raw / self.ACCEL_SCALE,
            accel_y=ay_raw / self.ACCEL_SCALE,
            accel_z=az_raw / self.ACCEL_SCALE,
            gyro_z=gz_raw / self.ANGLE_SCALE,
        )
