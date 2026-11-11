# -*- coding: UTF-8 -*-

'''
Module
    itransport_test.py
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
    Unit tests for ITransport structural protocol.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.service.transport.itransport import ITransport

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MockTransport:
    '''
        Mock transport implementation of ITransport protocol for unit testing.

        It defines:

            :attributes:
                | is_channel_open - Flag tracking open status.
            :methods:
                | open - Sets channel open.
                | close - Sets channel closed.
                | write - Records bytes written.
                | read - Returns empty bytes.
                | is_open - Returns open state.
    '''

    is_channel_open: bool

    def __init__(self) -> None:
        '''
            Initializes MockTransport.

            :exceptions: None.
        '''
        self.is_channel_open = False

    def open(self) -> None:
        '''
            Sets channel open.

            :exceptions: None.
        '''
        self.is_channel_open = True

    def close(self) -> None:
        '''
            Sets channel closed.

            :exceptions: None.
        '''
        self.is_channel_open = False

    def write(self, data: bytes) -> int:
        '''
            Returns data byte count.

            :param data: Input data.
            :return: Byte length.
            :exceptions: None.
        '''
        return len(data)

    def read(self, size: int) -> bytes:
        '''
            Returns empty bytes.

            :param size: Number of bytes requested.
            :return: Empty bytes.
            :exceptions: None.
        '''
        return b'\x00' * size

    def is_open(self) -> bool:
        '''
            Returns open state.

            :return: True if channel open.
            :exceptions: None.
        '''
        return self.is_channel_open


class TestITransport(TestCase):
    '''
        Test cases verifying ITransport protocol conformance.

        It defines:

            :methods:
                | test_structural_conformance - Verifies MockTransport satisfies ITransport.
    '''

    def test_structural_conformance(self) -> None:
        '''
            Verifies MockTransport satisfies ITransport.

            :exceptions: None.
        '''
        transport: MockTransport = MockTransport()
        self.assertTrue(isinstance(transport, ITransport))


if __name__ == '__main__':
    main()
