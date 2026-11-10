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

from dataclasses import FrozenInstanceError
from unittest import TestCase, main

from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.plan_command import PlanCommand

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
                | test_plan_with_commands - Verifies plan with command sequence.
                | test_immutability - Verifies that MotionPlan cannot be mutated.
    '''

    def test_empty_plan(self) -> None:
        '''
            Verifies empty plan initialization.

            :exceptions: None.
        '''
        plan: MotionPlan = MotionPlan(commands=())
        self.assertEqual(len(plan.commands), 0)
        self.assertEqual(plan.commands, ())

    def test_plan_with_commands(self) -> None:
        '''
            Verifies plan with command sequence.

            :exceptions: None.
        '''
        cmd1: PlanCommand = PlanCommand(cmd_id=1, payload=b'', description='Ping')
        cmd2: PlanCommand = PlanCommand(cmd_id=2, payload=b'\x01', description='Stop')
        plan: MotionPlan = MotionPlan(commands=(cmd1, cmd2))
        self.assertEqual(len(plan.commands), 2)
        self.assertEqual(plan.commands[0].cmd_id, 1)
        self.assertEqual(plan.commands[1].cmd_id, 2)

    def test_immutability(self) -> None:
        '''
            Verifies that MotionPlan cannot be mutated.

            :exceptions: None.
        '''
        plan: MotionPlan = MotionPlan(commands=())
        with self.assertRaises(FrozenInstanceError):
            plan.commands = ()  # type: ignore[misc]


if __name__ == '__main__':
    main()
