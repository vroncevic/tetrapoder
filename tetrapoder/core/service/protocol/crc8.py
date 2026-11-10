# -*- coding: UTF-8 -*-

'''
Module
    crc8.py
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
    CRC-8 checksum algorithm implementation with polynomial 0x07.
'''

from __future__ import annotations

from typing import ClassVar

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CRC8:
    '''
        Defines class CRC8 implementing ICRC8 contract structurally.
        Computes CRC-8 with generator polynomial 0x07 (x^8 + x^2 + x + 1).

        It defines:

            :attributes:
                | POLYNOMIAL - Generator polynomial constant 0x07.
            :methods:
                | calculate - Computes CRC-8 checksum over bytes.
                | verify - Checks if data matches expected checksum.
    '''

    POLYNOMIAL: ClassVar[int] = 0x07

    @classmethod
    def calculate(cls, data: bytes) -> int:
        '''
            Computes CRC-8 checksum over input bytes.

            :param data: Byte sequence to hash.
            :return: Computed CRC-8 byte value (0..255).
            :exceptions: None.
        '''
        crc: int = 0
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if (crc & 0x80) != 0:
                    crc = ((crc << 1) ^ cls.POLYNOMIAL) & 0xFF
                else:
                    crc = (crc << 1) & 0xFF
        return crc

    @classmethod
    def verify(cls, data: bytes, expected_crc: int) -> bool:
        '''
            Verifies that data matches the expected CRC-8 checksum.

            :param data: Input byte sequence.
            :param expected_crc: Expected CRC-8 byte value.
            :return: True if checksum matches, False otherwise.
            :exceptions: None.
        '''
        return cls.calculate(data) == (expected_crc & 0xFF)
