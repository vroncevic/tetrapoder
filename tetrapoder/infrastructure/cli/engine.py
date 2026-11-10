# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    CLI engine implementing inbound command line interface adapter.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.utils.reflection import to_str

from tetrapoder.core.model.exceptions.tetrapoder_error import TetrapoderError
from tetrapoder.infrastructure.cli.setup.bundle import CLIBundle
from tetrapoder.infrastructure.cli.setup.validator import CLIBundleValidator
from tetrapoder.infrastructure.command.iexecutor import ICommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CLI:
    '''
        Adapter that implements CLI commands for the tetrapoder toolchain.

        It defines:

            :attributes:
                | _parser - Argument parser for parsing CLI command args.
                | _executors - Map of command names to command executor instances.
            :methods:
                | __init__ - Initializes the CLI with parser and commands list.
                | run - Parses command line arguments and runs selected command strategy.
                | is_initialized - Checks if the CLI is initialized.
                | __str__ - Returns the CLI as string representation.
    '''

    _parser: IOptionManager
    _executors: Mapping[str, ICommandExecutor]

    def __init__(self, bundle: CLIBundle) -> None:
        '''
            Initializes the CLI with parser and commands list.

            :param bundle: Bundle containing CLI adapters.
            :exceptions:
                | ATSValueError: If bundle fails validation.
                | ATSTypeError:  If bundle attributes have invalid types.
        '''
        CLIBundleValidator.validate(bundle)
        self._parser = bundle.parser
        self._executors = {pair.definition.name: pair.executor for pair in bundle.commands}
        self._parser.register_commands([pair.definition for pair in bundle.commands])

    def run(self) -> Mapping[str, object]:
        '''
            Parses command line arguments and runs selected command strategy.

            :return: The execution result (return code, stdout, and stderr).
            :exceptions: None.
        '''
        try:
            command_name, params = self._parser.parse_command()
            if command_name not in self._executors:
                return {
                    'returncode': 1,
                    'stdout': '',
                    'stderr': f'cli::run - command {command_name} not found',
                }

            executor: ICommandExecutor = self._executors[command_name]
            return executor.execute(params=params)

        except (ATSValueError, ATSTypeError) as exc:
            return {'returncode': 1, 'stdout': '', 'stderr': f'cli::run - error: {exc}'}

        except (TetrapoderError, RuntimeError, OSError, ValueError, TypeError, KeyError) as exc:
            return {
                'returncode': 1,
                'stdout': '',
                'stderr': f'cli::run - unexpected error: {exc}',
            }

    def is_initialized(self) -> bool:
        '''
            Checks if the CLI adapter is initialized.

            :return: True if initialized, False otherwise.
            :exceptions: None.
        '''
        return bool(self._parser and self._executors)

    def __str__(self) -> str:
        '''
            Returns the CLI as string representation.

            :return: The CLI as string representation.
            :exceptions: None.
        '''
        return to_str(self)
