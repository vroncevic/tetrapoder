# -*- coding: UTF-8 -*-

'''
Module
    command_id_test.py
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
    Unit tests for CommandId enumeration.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.command_id import CommandId

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCommandId(TestCase):
    '''
        Test cases verifying CommandId enumeration.

        It defines:

            :methods:
                | test_command_values - Verifies integer values for command IDs.
    '''

    def test_command_values(self) -> None:
        '''
            Verifies integer values for command IDs.

            :exceptions: None.
        '''
        self.assertEqual(CommandId.PING, 0x01)
        self.assertEqual(CommandId.STOP, 0x02)
        self.assertEqual(CommandId.SET_SPEED, 0x03)
        self.assertEqual(CommandId.GAIT_STEP, 0x10)
        self.assertEqual(CommandId.QUEUE_KEYFRAME, 0x20)
        self.assertEqual(CommandId.CLEAR_QUEUE, 0x21)


if __name__ == '__main__':
    main()
