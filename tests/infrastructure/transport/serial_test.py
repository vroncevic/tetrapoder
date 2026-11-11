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
from unittest.mock import MagicMock, patch

from serial import SerialException

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
                | test_open_and_close - Verifies opening, already opened check, and closing.
                | test_open_exception - Verifies RunnerError raised when opening fails.
                | test_write_and_read_io - Verifies write and read operations and error handling.
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

    def test_open_and_close(self) -> None:
        '''
            Verifies opening, already opened check, and closing.

            :exceptions: None.
        '''
        transport: SerialTransport = SerialTransport(port='/dev/ttyUSB0')
        mock_ser: MagicMock = MagicMock()
        mock_ser.is_open = True
        with patch('tetrapoder.infrastructure.transport.serial.Serial', return_value=mock_ser):
            transport.open()
            self.assertTrue(transport.is_open())
            transport.open()
            self.assertTrue(transport.is_open())
            transport.close()
            self.assertFalse(transport.is_open())

    def test_open_exception(self) -> None:
        '''
            Verifies RunnerError raised when opening fails.

            :exceptions: None.
        '''
        transport: SerialTransport = SerialTransport(port='/dev/ttyUSB0')
        with patch(
            'tetrapoder.infrastructure.transport.serial.Serial',
            side_effect=SerialException('Device busy')
        ):
            with self.assertRaises(RunnerError):
                transport.open()

    def test_write_and_read_io(self) -> None:
        '''
            Verifies write and read operations and error handling.

            :exceptions: None.
        '''
        transport: SerialTransport = SerialTransport(port='/dev/ttyUSB0')
        mock_ser: MagicMock = MagicMock()
        mock_ser.is_open = True
        mock_ser.write.return_value = 4
        mock_ser.read.return_value = b'test'
        with patch('tetrapoder.infrastructure.transport.serial.Serial', return_value=mock_ser):
            transport.open()
            self.assertEqual(transport.write(b'data'), 4)
            self.assertEqual(transport.read(4), b'test')

            mock_ser.write.side_effect = SerialException('Write error')
            with self.assertRaises(RunnerError):
                transport.write(b'data')

            mock_ser.read.side_effect = SerialException('Read error')
            with self.assertRaises(RunnerError):
                transport.read(4)


if __name__ == '__main__':
    main()
