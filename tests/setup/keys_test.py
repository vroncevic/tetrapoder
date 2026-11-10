# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
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
    Unit tests for TetrapoderBundleKeys.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.setup.keys import TetrapoderBundleKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestTetrapoderBundleKeys(TestCase):
    '''
        Test cases verifying TetrapoderBundleKeys mappings.

        It defines:

            :methods:
                | test_keys_mapping - Verifies dependency and option type mappings.
    '''

    def test_keys_mapping(self) -> None:
        '''
            Verifies dependency and option type mappings.

            :exceptions: None.
        '''
        deps = TetrapoderBundleKeys.get_dependency_to_type()
        self.assertIn(TetrapoderBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(TetrapoderBundleKeys.DEPENDENCY_CLI, deps)

        opts = TetrapoderBundleKeys.get_option_to_type()
        self.assertIn(TetrapoderBundleKeys.OPTION_INFO_FILE, opts)
        self.assertIn(TetrapoderBundleKeys.OPTION_VERBOSE, opts)


if __name__ == '__main__':
    main()
