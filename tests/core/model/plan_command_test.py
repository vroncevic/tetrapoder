# -*- coding: UTF-8 -*-

'''
Module
    plan_command_test.py
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
    Unit tests for PlanCommand data model.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.plan_command import PlanCommand

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestPlanCommand(TestCase):
    '''
        Test cases verifying PlanCommand data model.

        It defines:

            :methods:
                | test_initialization - Verifies attributes and payload length calculation.
    '''

    def test_initialization(self) -> None:
        '''
            Verifies attributes and payload length calculation.

            :exceptions: None.
        '''
        cmd: PlanCommand = PlanCommand(cmd_id=0x01, payload=b'\x01\x02', description='Test Command')
        self.assertEqual(cmd.cmd_id, 0x01)
        self.assertEqual(cmd.payload, b'\x01\x02')
        self.assertEqual(cmd.description, 'Test Command')
        self.assertEqual(cmd.payload_length(), 2)


if __name__ == '__main__':
    main()
