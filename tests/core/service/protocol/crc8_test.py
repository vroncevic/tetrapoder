# -*- coding: UTF-8 -*-

'''
Module
    crc8_test.py
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
    Unit tests for CRC8 calculation and verification.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.service.protocol.crc8 import CRC8

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCRC8(TestCase):
    '''
        Test cases verifying CRC8 calculation and verification.

        It defines:

            :methods:
                | test_empty_bytes - Verifies CRC8 on empty bytes is 0.
                | test_known_pattern - Verifies CRC8 on known byte sequence.
                | test_verify_success - Verifies verify method returns True for valid CRC.
                | test_verify_failure - Verifies verify method returns False for invalid CRC.
    '''

    def test_empty_bytes(self) -> None:
        '''
            Verifies CRC8 on empty bytes is 0.

            :exceptions: None.
        '''
        self.assertEqual(CRC8.calculate(b''), 0)

    def test_known_pattern(self) -> None:
        '''
            Verifies CRC8 on known byte sequence.

            :exceptions: None.
        '''
        data: bytes = b'\x01\x02\x03\x04'
        crc: int = CRC8.calculate(data)
        self.assertIsInstance(crc, int)
        self.assertGreaterEqual(crc, 0)
        self.assertLessEqual(crc, 255)

    def test_verify_success(self) -> None:
        '''
            Verifies verify method returns True for valid CRC.

            :exceptions: None.
        '''
        data: bytes = b'Hello Robot'
        crc: int = CRC8.calculate(data)
        self.assertTrue(CRC8.verify(data, crc))

    def test_verify_failure(self) -> None:
        '''
            Verifies verify method returns False for invalid CRC.

            :exceptions: None.
        '''
        data: bytes = b'Hello Robot'
        self.assertFalse(CRC8.verify(data, 0xFF))


if __name__ == '__main__':
    main()
