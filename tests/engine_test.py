# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Unit tests for Tetrapoder engine class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import MagicMock, patch

from ats_utilities.exceptions.ats_value_error import ATSValueError

from tetrapoder.engine import Tetrapoder
from tetrapoder.infrastructure.cli.icli import ICLI
from tetrapoder.setup.bundle import TetrapoderBundle
from tetrapoder.setup.factory import TetrapoderBundleFactory
from tetrapoder.setup.validator import TetrapoderBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestTetrapoderEngine(TestCase):
    '''
        Test cases verifying Tetrapoder engine lifecycle.

        It defines:

            :methods:
                | test_initialization - Verifies engine initialization with valid bundle.
                | test_get_version - Verifies engine version string.
                | test_init_failures - Verifies engine handling of invalid bundle and unexpected error.
                | test_process_uninitialized - Verifies process returns False when uninitialized.
                | test_process_execution - Verifies process execution success and error return.
                | test_process_exceptions - Verifies process handling of raised exceptions.
    '''

    def test_initialization(self) -> None:
        '''
            Verifies engine initialization with valid bundle.

            :exceptions: None.
        '''
        bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        engine: Tetrapoder = Tetrapoder(bundle)
        self.assertTrue(engine.is_initialized())

    def test_get_version(self) -> None:
        '''
            Verifies engine version string.

            :exceptions: None.
        '''
        bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        engine: Tetrapoder = Tetrapoder(bundle)
        self.assertEqual(engine.get_version(), '1.0.0')

    def test_init_failures(self) -> None:
        '''
            Verifies engine handling of invalid bundle and unexpected error.

            :exceptions: None.
        '''
        engine_invalid: Tetrapoder = Tetrapoder(None)  # type: ignore[arg-type]
        self.assertFalse(engine_invalid.is_initialized())

        bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        with patch.object(
            TetrapoderBundleValidator, 'validate', side_effect=RuntimeError('Crash')
        ):
            engine_crash: Tetrapoder = Tetrapoder(bundle)
            self.assertFalse(engine_crash.is_initialized())

    def test_process_uninitialized(self) -> None:
        '''
            Verifies process returns False when uninitialized.

            :exceptions: None.
        '''
        engine: Tetrapoder = Tetrapoder(None)  # type: ignore[arg-type]
        self.assertFalse(engine.process())

    def test_process_execution(self) -> None:
        '''
            Verifies process execution success and error return.

            :exceptions: None.
        '''
        parent_bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.return_value = {'returncode': 0, 'stdout': 'success output'}
        bundle: TetrapoderBundle = TetrapoderBundle(base=parent_bundle.base, cli=mock_cli)
        engine: Tetrapoder = Tetrapoder(bundle)
        self.assertTrue(engine.process())

        mock_cli.run.return_value = {'returncode': 1, 'stderr': 'error output'}
        self.assertFalse(engine.process())

    def test_process_exceptions(self) -> None:
        '''
            Verifies process handling of raised exceptions.

            :exceptions: None.
        '''
        parent_bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.side_effect = ATSValueError('ATS error')
        bundle: TetrapoderBundle = TetrapoderBundle(base=parent_bundle.base, cli=mock_cli)
        engine: Tetrapoder = Tetrapoder(bundle)
        self.assertFalse(engine.process())

        mock_cli.run.side_effect = RuntimeError('Unexpected error')
        self.assertFalse(engine.process())


if __name__ == '__main__':
    main()
