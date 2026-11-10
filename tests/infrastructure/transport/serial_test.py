# -*- coding: UTF-8 -*-

'''
Module
    serial_test.py
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
    Unit tests for SerialTransport adapter.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.exceptions.runner_error import RunnerError
from tetrapoder.infrastructure.transport.serial import SerialTransport

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestSerialTransport(TestCase):
    '''
        Test cases verifying SerialTransport adapter behavior.

        It defines:

            :methods:
                | test_initialization - Verifies adapter initialization values and is_open status.
                | test_closed_write_error - Verifies exception raised when writing to closed port.
                | test_closed_read_error - Verifies exception raised when reading from closed port.
    '''

    def test_initialization(self) -> None:
        '''
            Verifies adapter initialization values and is_open status.

            :exceptions: None.
        '''
        transport: SerialTransport = SerialTransport(port='/dev/test_fake_port', baudrate=115200)
        self.assertFalse(transport.is_open())

    def test_closed_write_error(self) -> None:
        '''
            Verifies exception raised when writing to closed port.

            :exceptions: None.
        '''
        transport: SerialTransport = SerialTransport()
        with self.assertRaises(RunnerError):
            transport.write(b'\x01')

    def test_closed_read_error(self) -> None:
        '''
            Verifies exception raised when reading from closed port.

            :exceptions: None.
        '''
        transport: SerialTransport = SerialTransport()
        with self.assertRaises(RunnerError):
            transport.read(5)


if __name__ == '__main__':
    main()
