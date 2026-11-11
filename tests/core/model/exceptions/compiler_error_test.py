# -*- coding: UTF-8 -*-

'''
Module
    compiler_error_test.py
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
    Unit tests for CompilerError exception.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.exceptions.compiler_error import CompilerError
from tetrapoder.core.model.exceptions.tetrapoder_error import TetrapoderError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCompilerError(TestCase):
    '''
        Test cases verifying CompilerError domain exception.

        It defines:

            :methods:
                | test_subclass_and_raise - Verifies CompilerError subclasses TetrapoderError.
    '''

    def test_subclass_and_raise(self) -> None:
        '''
            Verifies CompilerError subclasses TetrapoderError.

            :exceptions: None.
        '''
        with self.assertRaises(TetrapoderError):
            raise CompilerError('Compilation failed')


if __name__ == '__main__':
    main()
