# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
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
    Unit tests for CLIBundleValidator.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.infrastructure.cli.setup.bundle import CLIBundle
from tetrapoder.infrastructure.cli.setup.validator import CLIBundleValidator
from tetrapoder.infrastructure.command.bundle import CommandBundle
from tetrapoder.infrastructure.command.definition import TetrapoderCommandDefinition
from tetrapoder.infrastructure.command.executor import TetrapoderCommandExecutor
from tetrapoder.setup.bundle import TetrapoderBundle
from tetrapoder.setup.factory import TetrapoderBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLIBundleValidator(TestCase):
    '''
        Test cases verifying CLIBundleValidator.

        It defines:

            :methods:
                | test_is_valid_success - Verifies validation of properly formed CLIBundle.
                | test_is_valid_failure - Verifies validation failure on invalid input.
    '''

    def test_is_valid_success(self) -> None:
        '''
            Verifies validation of properly formed CLIBundle.

            :exceptions: None.
        '''
        parent_bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        definition: TetrapoderCommandDefinition = TetrapoderCommandDefinition()
        executor: TetrapoderCommandExecutor = TetrapoderCommandExecutor(definition)
        cmd_bundle: CommandBundle = CommandBundle(definition=definition, executor=executor)
        bundle: CLIBundle = CLIBundle(parser=parent_bundle.base.option_manager, commands=(cmd_bundle,))
        self.assertTrue(CLIBundleValidator.is_valid(bundle))

    def test_is_valid_failure(self) -> None:
        '''
            Verifies validation failure on invalid input.

            :exceptions: None.
        '''
        self.assertFalse(CLIBundleValidator.is_valid(None))  # type: ignore[arg-type]


if __name__ == '__main__':
    main()
