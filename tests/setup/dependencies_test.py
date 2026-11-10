# -*- coding: UTF-8 -*-

'''
Module
    dependencies_test.py
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
    Unit tests for TetrapoderBundleDependencies TypedDict.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.setup.bundle import TetrapoderBundle
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


class TestTetrapoderBundleDependencies(TestCase):
    '''
        Test cases verifying TetrapoderBundleDependencies structure.

        It defines:

            :methods:
                | test_typed_dict_keys - Verifies key assignment in TetrapoderBundleDependencies.
    '''

    def test_typed_dict_keys(self) -> None:
        '''
            Verifies key assignment in TetrapoderBundleDependencies.

            :exceptions: None.
        '''
        bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        deps: TetrapoderBundleDependencies = {
            'base': bundle.base,
            'cli': bundle.cli,
        }
        self.assertIn('base', deps)
        self.assertIn('cli', deps)


if __name__ == '__main__':
    main()
