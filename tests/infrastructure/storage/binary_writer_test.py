# -*- coding: UTF-8 -*-

'''
Module
    binary_writer_test.py
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
    Unit tests for BinaryWriter file persistence adapter.
'''

from __future__ import annotations

from os import remove
from os.path import exists
from unittest import TestCase, main

from tetrapoder.core.model.exceptions.compiler_error import CompilerError
from tetrapoder.infrastructure.storage.binary_writer import BinaryWriter

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestBinaryWriter(TestCase):
    '''
        Test cases verifying BinaryWriter file persistence.

        It defines:

            :methods:
                | test_write_success - Verifies writing binary data to file.
                | test_write_error - Verifies exception raised on file write failure.
                | test_exists - Verifies checking file existence.
    '''

    def test_write_success(self) -> None:
        '''
            Verifies writing binary data to file.

            :exceptions: None.
        '''
        file_path: str = '/tmp/test_binary_writer.bin'
        writer: BinaryWriter = BinaryWriter()
        data: bytes = b'\xAA\x01\x02\x03'

        try:
            written: int = writer.write(file_path, data)
            self.assertEqual(written, 4)
            self.assertTrue(writer.exists(file_path))
        finally:
            if exists(file_path):
                remove(file_path)

    def test_write_error(self) -> None:
        '''
            Verifies exception raised on file write failure.

            :exceptions: None.
        '''
        writer: BinaryWriter = BinaryWriter()
        with self.assertRaises(CompilerError):
            writer.write('/non_existent_directory_xyz/test.bin', b'\x00')

    def test_exists(self) -> None:
        '''
            Verifies checking file existence.

            :exceptions: None.
        '''
        writer: BinaryWriter = BinaryWriter()
        self.assertFalse(writer.exists('/non_existent_file_path_12345.bin'))


if __name__ == '__main__':
    main()
