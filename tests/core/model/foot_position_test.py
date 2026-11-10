# -*- coding: UTF-8 -*-

'''
Module
    foot_position_test.py
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
    Unit tests for FootPosition data model.
'''

from __future__ import annotations

from dataclasses import FrozenInstanceError
from unittest import TestCase, main

from tetrapoder.core.model.foot_position import FootPosition

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestFootPosition(TestCase):
    '''
        Test cases verifying FootPosition value object behavior.

        It defines:

            :methods:
                | test_initialization - Verifies attributes initialization and to_tuple conversion.
                | test_immutability - Verifies that FootPosition attributes cannot be modified.
    '''

    def test_initialization(self) -> None:
        '''
            Verifies attributes initialization and to_tuple conversion.

            :exceptions: None.
        '''
        foot: FootPosition = FootPosition(x=10.0, y=20.0, z=-30.0)
        self.assertEqual(foot.x, 10.0)
        self.assertEqual(foot.y, 20.0)
        self.assertEqual(foot.z, -30.0)
        self.assertEqual(foot.to_tuple(), (10.0, 20.0, -30.0))

    def test_immutability(self) -> None:
        '''
            Verifies that FootPosition attributes cannot be modified.

            :exceptions: None.
        '''
        foot: FootPosition = FootPosition(x=0.0, y=0.0, z=0.0)
        with self.assertRaises(FrozenInstanceError):
            foot.x = 5.0  # type: ignore[misc]


if __name__ == '__main__':
    main()
