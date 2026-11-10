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
    Unit tests for CLI class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import MagicMock

from ats_utilities.exceptions import ATSRuntimeError, ATSValueError
from ats_utilities.option.imanager import IOptionManager

from tetrapoder.infrastructure.cli.engine import CLI
from tetrapoder.infrastructure.cli.setup.bundle import CLIBundle
from tetrapoder.infrastructure.command.bundle import CommandBundle
from tetrapoder.infrastructure.command.idefinition import ICommandDefinition
from tetrapoder.infrastructure.command.iexecutor import ICommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLI(TestCase):
    '''
        Test cases verifying CLI engine adapter.

        It defines:

            :methods:
                | setUp - Initializes mock parser and command bundle.
                | test_cli_initialization - Verifies CLI initialization.
                | test_cli_to_str - Verifies string representation of CLI.
                | test_cli_run_success - Verifies successful command dispatch.
                | test_cli_run_command_not_found - Verifies unknown command handling.
                | test_cli_run_exceptions - Verifies exception handling during parsing.
    '''

    def setUp(self) -> None:
        '''
            Initializes mock CLI collaborators before each test.

            :exceptions: None.
        '''
        self.mock_parser = MagicMock(spec=IOptionManager)
        self.mock_definition = MagicMock(spec=ICommandDefinition)
        self.mock_definition.name = 'robot'
        self.mock_executor = MagicMock(spec=ICommandExecutor)

        cmd_bundle = CommandBundle(
            definition=self.mock_definition,
            executor=self.mock_executor,
        )
        self.bundle = CLIBundle(
            parser=self.mock_parser,
            commands=[cmd_bundle],
        )

    def test_cli_initialization(self) -> None:
        '''
            Verifies CLI initialization.

            :exceptions: None.
        '''
        cli: CLI = CLI(bundle=self.bundle)
        self.assertTrue(cli.is_initialized())
        self.mock_parser.register_commands.assert_called_once_with(
            [self.mock_definition]
        )

    def test_cli_to_str(self) -> None:
        '''
            Verifies string representation of CLI.

            :exceptions: None.
        '''
        cli: CLI = CLI(bundle=self.bundle)
        self.assertIn('CLI', str(cli))

    def test_cli_run_success(self) -> None:
        '''
            Verifies successful command dispatch and return values.

            :exceptions: None.
        '''
        cli: CLI = CLI(bundle=self.bundle)
        self.mock_parser.parse_command.return_value = (
            'robot', {'action': 'ping'}
        )
        expected: dict[str, object] = {'returncode': 0, 'stdout': 'OK', 'stderr': ''}
        self.mock_executor.execute.return_value = expected

        result: dict[str, object] = cli.run()
        self.assertEqual(result, expected)
        self.mock_executor.execute.assert_called_once_with(
            params={'action': 'ping'}
        )

    def test_cli_run_command_not_found(self) -> None:
        '''
            Verifies error handling when command is unregistered.

            :exceptions: None.
        '''
        cli: CLI = CLI(bundle=self.bundle)
        self.mock_parser.parse_command.return_value = ('unknown', {})
        result: dict[str, object] = cli.run()
        self.assertEqual(result['returncode'], 1)
        self.assertIn('not found', str(result['stderr']))

    def test_cli_run_exceptions(self) -> None:
        '''
            Verifies exception handling during parsing.

            :exceptions: None.
        '''
        cli: CLI = CLI(bundle=self.bundle)
        self.mock_parser.parse_command.side_effect = ATSValueError('Missing option')
        result: dict[str, object] = cli.run()
        self.assertEqual(result['returncode'], 1)
        self.assertIn('Missing option', str(result['stderr']))

        self.mock_parser.parse_command.side_effect = ATSRuntimeError('Parsing error')
        result_runtime: dict[str, object] = cli.run()
        self.assertEqual(result_runtime['returncode'], 1)
        self.assertIn('Parsing error', str(result_runtime['stderr']))


if __name__ == '__main__':
    main()
