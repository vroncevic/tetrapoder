# -*- coding: UTF-8 -*-

'''
Module
    decoder_test.py
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
    Unit tests for TelemetryDecoder service.
'''

from __future__ import annotations

from struct import pack
from unittest import TestCase, main

from tetrapoder.core.model.exceptions.protocol_error import ProtocolError
from tetrapoder.core.model.imu_telemetry import ImuTelemetry
from tetrapoder.core.service.telemetry.decoder import TelemetryDecoder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestTelemetryDecoder(TestCase):
    '''
        Test cases verifying TelemetryDecoder payload parsing.

        It defines:

            :methods:
                | test_decode_valid_payload - Verifies decoding valid 12-byte IMU payload.
                | test_decode_invalid_length - Verifies ProtocolError on invalid payload length.
                | test_is_valid_payload - Verifies payload length validation check.
    '''

    def test_is_valid_payload(self) -> None:
        '''
            Verifies payload length validation check.

            :exceptions: None.
        '''
        decoder: TelemetryDecoder = TelemetryDecoder()
        self.assertTrue(decoder.is_valid_payload(b'\x00' * 12))
        self.assertFalse(decoder.is_valid_payload(b'\x00' * 11))
        self.assertFalse(decoder.is_valid_payload(b'\x00' * 13))

    def test_decode_valid_payload(self) -> None:
        '''
            Verifies decoding valid 12-byte IMU payload.

            :exceptions: None.
        '''
        decoder: TelemetryDecoder = TelemetryDecoder()
        payload: bytes = pack('>hhhhhh', 125, -50, 50, -20, 980, 15)
        telemetry: ImuTelemetry = decoder.decode(payload)

        self.assertAlmostEqual(telemetry.roll, 12.5)
        self.assertAlmostEqual(telemetry.pitch, -5.0)
        self.assertAlmostEqual(telemetry.accel_x, 0.05)
        self.assertAlmostEqual(telemetry.accel_y, -0.02)
        self.assertAlmostEqual(telemetry.accel_z, 0.98)
        self.assertAlmostEqual(telemetry.gyro_z, 1.5)

    def test_decode_invalid_length(self) -> None:
        '''
            Verifies ProtocolError on invalid payload length.

            :exceptions: None.
        '''
        decoder: TelemetryDecoder = TelemetryDecoder()
        with self.assertRaises(ProtocolError):
            decoder.decode(b'\x00' * 11)

        with self.assertRaises(ProtocolError):
            decoder.decode(b'\x00' * 13)


if __name__ == '__main__':
    main()
