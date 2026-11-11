# -*- coding: UTF-8 -*-

'''
Module
    runner_error_test.py
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
    Unit tests for RunnerError exception.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.exceptions.runner_error import RunnerError
from tetrapoder.core.model.exceptions.tetrapoder_error import TetrapoderError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestRunnerError(TestCase):
    '''
        Test cases verifying RunnerError domain exception.

        It defines:

            :methods:
                | test_subclass_and_raise - Verifies RunnerError subclasses TetrapoderError.
    '''

    def test_subclass_and_raise(self) -> None:
        '''
            Verifies RunnerError subclasses TetrapoderError.

            :exceptions: None.
        '''
        with self.assertRaises(TetrapoderError):
            raise RunnerError('Execution timed out')


if __name__ == '__main__':
    main()
