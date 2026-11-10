# -*- coding: UTF-8 -*-

'''
Module
    binary_writer.py
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
    Binary filesystem file writer adapter.
'''

from __future__ import annotations

from os.path import exists as file_exists

from tetrapoder.core.model.exceptions.compiler_error import CompilerError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class BinaryWriter:
    '''
        Defines class BinaryWriter implementing IBinaryWriter structurally.
        Persists binary data streams directly to filesystem files.

        It defines:

            :methods:
                | write - Writes raw binary byte sequence to target file path.
                | exists - Checks whether target filesystem file path exists.
    '''

    def write(self, file_path: str, data: bytes) -> int:
        '''
            Writes binary byte sequence to the specified file path.

            :param file_path: Target filesystem file path.
            :param data: Binary byte sequence to persist.
            :return: Number of bytes written to the file.
            :exceptions:
                | CompilerError: If file writing fails due to an I/O error.
        '''
        try:
            with open(file_path, 'wb') as file_handle:
                file_handle.write(data)
            return len(data)
        except OSError as exc:
            raise CompilerError(f'Failed to write binary data to {file_path}: {exc}') from exc

    def exists(self, file_path: str) -> bool:
        '''
            Checks whether target filesystem file path exists.

            :param file_path: Target filesystem file path.
            :return: True if file exists, False otherwise.
            :exceptions: None.
        '''
        return file_exists(file_path)
