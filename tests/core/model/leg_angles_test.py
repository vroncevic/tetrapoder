# -*- coding: UTF-8 -*-

'''
Module
    leg_angles_test.py
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
    Unit tests for LegAngles data model.
'''

from __future__ import annotations

from dataclasses import FrozenInstanceError
from unittest import TestCase, main

from tetrapoder.core.model.leg_angles import LegAngles

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestLegAngles(TestCase):
    '''
        Test cases verifying LegAngles value object behavior.

        It defines:

            :methods:
                | test_initialization - Verifies attributes initialization.
                | test_immutability - Verifies that LegAngles attributes cannot be mutated.
    '''

    def test_initialization(self) -> None:
        '''
            Verifies attributes initialization.

            :exceptions: None.
        '''
        angles: LegAngles = LegAngles(coxa=90.0, femur=45.5, tibia=120.3)
        self.assertEqual(angles.coxa, 90.0)
        self.assertEqual(angles.femur, 45.5)
        self.assertEqual(angles.tibia, 120.3)

    def test_immutability(self) -> None:
        '''
            Verifies that LegAngles attributes cannot be mutated.

            :exceptions: None.
        '''
        angles: LegAngles = LegAngles(coxa=90.0, femur=90.0, tibia=90.0)
        with self.assertRaises(FrozenInstanceError):
            angles.coxa = 100.0  # type: ignore[misc]


if __name__ == '__main__':
    main()
