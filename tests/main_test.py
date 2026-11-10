# -*- coding: UTF-8 -*-

'''
Module
    main_test.py
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
    Unit tests for main entry point module.
'''

from __future__ import annotations

from unittest import TestCase, main as unittest_main
from unittest.mock import MagicMock, patch

from main import main

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestMain(TestCase):
    '''
        Test cases verifying main entry point execution.

        It defines:

            :methods:
                | test_main_execution - Verifies main() bootstraps and runs engine.
    '''

    @patch('main.Tetrapoder')
    def test_main_execution(self, mock_engine_cls: MagicMock) -> None:
        '''
            Verifies main() bootstraps and runs engine.

            :param mock_engine_cls: Mocked Tetrapoder engine class.
            :exceptions: None.
        '''
        mock_instance = MagicMock()
        mock_instance.process.return_value = True
        mock_engine_cls.return_value = mock_instance

        result: bool = main()
        self.assertTrue(result)
        mock_instance.process.assert_called_once()


if __name__ == '__main__':
    unittest_main()
