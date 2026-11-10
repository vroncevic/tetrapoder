# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
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
    Unit tests for CLIBundleRegistry class.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.infrastructure.cli.setup.bundle import CLIBundle
from tetrapoder.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from tetrapoder.infrastructure.cli.setup.registry import CLIBundleRegistry
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


class TestCLIBundleRegistry(TestCase):
    '''
        Test cases verifying CLIBundleRegistry.

        It defines:

            :methods:
                | test_create_bundle - Verifies bundle creation from valid dependencies.
                | test_get_version - Verifies registry version string.
    '''

    def test_create_bundle(self) -> None:
        '''
            Verifies bundle creation from valid dependencies.

            :exceptions: None.
        '''
        parent_bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        deps: CLIBundleDependencies = {
            'parser': parent_bundle.base.option_manager,
            'commands': (),
        }
        bundle: CLIBundle = CLIBundleRegistry.create_bundle(deps)
        self.assertTrue(isinstance(bundle, CLIBundle))

    def test_get_version(self) -> None:
        '''
            Verifies registry version string.

            :exceptions: None.
        '''
        self.assertEqual(CLIBundleRegistry.get_version(), '1.0.0')


if __name__ == '__main__':
    main()
