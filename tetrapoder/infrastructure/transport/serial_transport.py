# -*- coding: UTF-8 -*-

'''
Module
    serial_transport.py
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
    PySerial hardware transport adapter implementing ITransport structurally.
'''

from __future__ import annotations

from serial import Serial, SerialException

from tetrapoder.core.model.exceptions.runner_error import RunnerError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SerialTransport:
    '''
        Defines class SerialTransport implementing ITransport contract structurally.
        Wraps PySerial communication channel with robust error handling.

        It defines:

            :attributes:
                | _port - Serial port device path.
                | _baudrate - Transmission baud rate.
                | _timeout - Read timeout in seconds.
                | _serial - Underlying PySerial handle or None.
            :methods:
                | __init__ - Initializes SerialTransport adapter parameters.
                | open - Opens the serial port communication channel.
                | close - Closes active serial port connection.
                | write - Transmits raw bytes to serial port.
                | read - Receives bytes from serial port.
                | is_open - Checks if serial port channel is currently active.
    '''

    _port: str
    _baudrate: int
    _timeout: float
    _serial: Serial | None

    def __init__(self, port: str = '/dev/ttyUSB0', baudrate: int = 57600, timeout: float = 1.0) -> None:
        '''
            Initializes SerialTransport adapter parameters.

            :param port: Serial port identifier string.
            :param baudrate: Transmission baud rate integer.
            :param timeout: Timeout duration in seconds.
            :exceptions: None.
        '''
        self._port = port
        self._baudrate = baudrate
        self._timeout = timeout
        self._serial = None

    def open(self) -> None:
        '''
            Opens the serial port communication channel.

            :exceptions:
                | RunnerError: If serial port cannot be opened.
        '''
        if self._serial is not None and self._serial.is_open:
            return

        try:
            self._serial = Serial(
                port=self._port,
                baudrate=self._baudrate,
                timeout=self._timeout
            )
        except (OSError, SerialException) as exc:
            raise RunnerError(f'Cannot open serial port {self._port}: {exc}') from exc

    def close(self) -> None:
        '''
            Closes active serial port connection.

            :exceptions: None.
        '''
        if self._serial is not None and self._serial.is_open:
            self._serial.close()
        self._serial = None

    def write(self, data: bytes) -> int:
        '''
            Transmits raw bytes to serial port.

            :param data: Byte sequence to transmit.
            :return: Number of bytes written.
            :exceptions:
                | RunnerError: If transport is closed or writing fails.
        '''
        if self._serial is None or not self._serial.is_open:
            raise RunnerError('Cannot write to closed serial transport')

        try:
            return self._serial.write(data)
        except (OSError, SerialException) as exc:
            raise RunnerError(f'Serial write failed: {exc}') from exc

    def read(self, size: int) -> bytes:
        '''
            Receives bytes from serial port.

            :param size: Number of bytes to read.
            :return: Bytes read from serial interface.
            :exceptions:
                | RunnerError: If transport is closed or reading fails.
        '''
        if self._serial is None or not self._serial.is_open:
            raise RunnerError('Cannot read from closed serial transport')

        try:
            return self._serial.read(size)
        except (OSError, SerialException) as exc:
            raise RunnerError(f'Serial read failed: {exc}') from exc

    def is_open(self) -> bool:
        '''
            Checks if serial port channel is currently active.

            :return: True if active and open, False otherwise.
            :exceptions: None.
        '''
        return self._serial is not None and self._serial.is_open
