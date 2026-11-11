# -*- coding: UTF-8 -*-

'''
Module
    icrc.py
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
    Structural interface for CRC-8 checksum calculation and verification.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class ICRC8(Protocol):
    '''
        Structural protocol defining CRC-8 operations.

        It defines:

            :methods:
                | calculate - Computes CRC-8 checksum for given data bytes.
                | verify - Verifies that data matches an expected CRC-8 checksum.
    '''

    def calculate(self, data: bytes) -> int:
        '''
            Computes CRC-8 checksum for given data bytes.

            :param data: Input byte sequence.
            :return: Computed CRC-8 checksum integer (0..255).
        '''

    def verify(self, data: bytes, expected_crc: int) -> bool:
        '''
            Verifies that data matches an expected CRC-8 checksum.

            :param data: Input byte sequence.
            :param expected_crc: Expected CRC-8 checksum integer (0..255).
            :return: True if checksum matches, False otherwise.
        '''
