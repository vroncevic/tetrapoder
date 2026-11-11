# -*- coding: UTF-8 -*-

'''
Module
    dep_validator_test.py
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
    Unit tests for TetrapoderBundleDependenciesValidator.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.setup.bundle import TetrapoderBundle
from tetrapoder.setup.dep_validator import TetrapoderBundleDependenciesValidator
from tetrapoder.setup.dependencies import TetrapoderBundleDependencies
from tetrapoder.setup.factory import TetrapoderBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestTetrapoderBundleDependenciesValidator(TestCase):
    '''
        Test cases verifying TetrapoderBundleDependenciesValidator.

        It defines:

            :methods:
                | test_is_valid_success - Verifies validation of properly formed dependencies.
                | test_is_valid_failure - Verifies validation failure on invalid dependencies.
    '''

    def test_is_valid_success(self) -> None:
        '''
            Verifies validation of properly formed dependencies.

            :exceptions: None.
        '''
        bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        deps: TetrapoderBundleDependencies = TetrapoderBundleDependencies(base=bundle.base, cli=bundle.cli)
        self.assertTrue(TetrapoderBundleDependenciesValidator.is_valid(deps))

    def test_is_valid_failure(self) -> None:
        '''
            Verifies validation failure on invalid dependencies.

            :exceptions: None.
        '''
        self.assertFalse(TetrapoderBundleDependenciesValidator.is_valid(None))  # type: ignore[arg-type]


if __name__ == '__main__':
    main()
