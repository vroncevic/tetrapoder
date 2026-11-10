# -*- coding: UTF-8 -*-

'''
Module
    definition_test.py
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
    Unit tests for TetrapoderCommandDefinition metadata.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.infrastructure.command.definition import TetrapoderCommandDefinition

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestTetrapoderCommandDefinition(TestCase):
    '''
        Test cases verifying TetrapoderCommandDefinition properties.

        It defines:

            :methods:
                | test_definition_properties - Verifies name, help_text, and options list.
                | test_str_representation - Verifies string representation of definition.
    '''

    def test_definition_properties(self) -> None:
        '''
            Verifies name, help_text, and options list.

            :exceptions: None.
        '''
        definition: TetrapoderCommandDefinition = TetrapoderCommandDefinition()
        self.assertEqual(definition.name, 'robot')
        self.assertIn('Tetrapod', definition.help_text)
        self.assertGreaterEqual(len(definition.options), 4)

    def test_str_representation(self) -> None:
        '''
            Verifies string representation of definition.

            :exceptions: None.
        '''
        definition: TetrapoderCommandDefinition = TetrapoderCommandDefinition()
        self.assertIn('TetrapoderCommandDefinition', str(definition))


if __name__ == '__main__':
    main()
