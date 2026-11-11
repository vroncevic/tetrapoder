# -*- coding: UTF-8 -*-

'''
Module
    itransport.py
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
    Structural interface for byte stream hardware communication transport.
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
class ITransport(Protocol):
    '''
        Structural protocol defining bidirectional byte stream hardware transport.

        It defines:

            :methods:
                | open - Opens transport connection.
                | close - Closes transport connection.
                | write - Sends raw bytes across transport.
                | read - Receives raw bytes from transport.
                | is_open - Checks whether transport connection is currently open.
    '''

    def open(self) -> None:
        '''
            Opens transport connection channel.
        '''

    def close(self) -> None:
        '''
            Closes transport connection channel.
        '''

    def write(self, data: bytes) -> int:
        '''
            Transmits raw bytes over connection.

            :param data: Byte sequence to transmit.
            :return: Number of bytes written.
        '''

    def read(self, size: int) -> bytes:
        '''
            Reads up to size bytes from connection.

            :param size: Number of bytes to read.
            :return: Bytes received from transport.
        '''

    def is_open(self) -> bool:
        '''
            Checks if connection channel is currently open.

            :return: True if open, False otherwise.
        '''
