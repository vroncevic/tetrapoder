# -*- coding: UTF-8 -*-

'''
Module
    choreography_builder_test.py
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
    Unit tests for ChoreographyBuilder class.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.command_id import CommandId
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.service.trajectory.choreography_builder import ChoreographyBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestChoreographyBuilder(TestCase):
    '''
        Test cases verifying ChoreographyBuilder actions and speed settings.

        It defines:

            :methods:
                | test_actions_and_speed - Verifies speed, wave action, and emergency stop.
                | test_build_empty - Verifies building empty plan by default.
    '''

    def test_actions_and_speed(self) -> None:
        '''
            Verifies speed, wave action, and emergency stop.

            :exceptions: None.
        '''
        builder: ChoreographyBuilder = ChoreographyBuilder([])
        builder.set_speed(5).action_wave(2).emergency_stop()
        plan: MotionPlan = builder.build()
        self.assertEqual(len(plan.commands), 3)
        self.assertEqual(plan.commands[0].cmd_id, int(CommandId.SET_SPEED))
        self.assertEqual(plan.commands[1].cmd_id, int(CommandId.GAIT_STEP))
        self.assertEqual(plan.commands[2].cmd_id, int(CommandId.STOP))

    def test_build_empty(self) -> None:
        '''
            Verifies building empty plan by default.

            :exceptions: None.
        '''
        builder: ChoreographyBuilder = ChoreographyBuilder([])
        plan: MotionPlan = builder.build()
        self.assertEqual(len(plan.commands), 0)


if __name__ == '__main__':
    main()
