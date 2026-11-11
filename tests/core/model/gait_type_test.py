# -*- coding: UTF-8 -*-

'''
Module
    gait_type_test.py
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
    Unit tests for GaitType enumeration.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.gait_type import GaitType

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGaitType(TestCase):
    '''
        Test cases verifying GaitType enumeration.

        It defines:

            :methods:
                | test_gait_values - Verifies integer values for gait types.
    '''

    def test_gait_values(self) -> None:
        '''
            Verifies integer values for gait types.

            :exceptions: None.
        '''
        self.assertEqual(GaitType.SIT, 0)
        self.assertEqual(GaitType.STAND, 1)
        self.assertEqual(GaitType.STEP_FORWARD, 2)
        self.assertEqual(GaitType.STEP_BACKWARD, 3)
        self.assertEqual(GaitType.TURN_LEFT, 4)
        self.assertEqual(GaitType.TURN_RIGHT, 5)
        self.assertEqual(GaitType.HAND_WAVE, 6)


if __name__ == '__main__':
    main()
