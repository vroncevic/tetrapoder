# -*- coding: UTF-8 -*-

'''
Module
    motion_plan_test.py
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
    Unit tests for MotionPlan model.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.motion_plan import MotionPlan

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestMotionPlan(TestCase):
    '''
        Test cases verifying MotionPlan container behavior.

        It defines:

            :methods:
                | test_empty_plan - Verifies empty plan initialization.
                | test_add_commands - Verifies appending commands and command count.
                | test_clear_plan - Verifies clearing plan commands.
    '''

    def test_empty_plan(self) -> None:
        '''
            Verifies empty plan initialization.

            :exceptions: None.
        '''
        plan: MotionPlan = MotionPlan()
        self.assertEqual(plan.count(), 0)
        self.assertEqual(len(plan.commands), 0)

    def test_add_commands(self) -> None:
        '''
            Verifies appending commands and command count.

            :exceptions: None.
        '''
        plan: MotionPlan = MotionPlan()
        plan.add_command(1, b'', 'Ping')
        plan.add_command(2, b'\x01', 'Stop')
        self.assertEqual(plan.count(), 2)
        self.assertEqual(plan.commands[0].cmd_id, 1)
        self.assertEqual(plan.commands[1].cmd_id, 2)

    def test_clear_plan(self) -> None:
        '''
            Verifies clearing plan commands.

            :exceptions: None.
        '''
        plan: MotionPlan = MotionPlan()
        plan.add_command(1, b'', 'Ping')
        self.assertEqual(plan.count(), 1)
        plan.clear()
        self.assertEqual(plan.count(), 0)


if __name__ == '__main__':
    main()
