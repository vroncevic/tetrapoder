# -*- coding: UTF-8 -*-

'''
Module
    motion_plan.py
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
    High-level motion plan model storing ordered sequences of robot commands.
'''

from __future__ import annotations

from typing import Self

from tetrapoder.core.model.plan_command import PlanCommand

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MotionPlan:
    '''
        Defines high-level MotionPlan container for choreographies and keyframes.

        It defines:

            :attributes:
                | _commands - Internal list of sequential plan commands.
            :methods:
                | __init__ - Initializes empty motion plan container.
                | add_command - Appends a command to the execution plan.
                | commands - Returns immutable tuple of commands.
                | count - Returns total number of commands in plan.
                | clear - Clears all commands from plan.
    '''

    _commands: list[PlanCommand]

    def __init__(self) -> None:
        '''
            Initializes empty motion plan container.

            :exceptions: None.
        '''
        self._commands = []

    def add_command(self, cmd_id: int, payload: bytes, description: str = '') -> Self:
        '''
            Appends a command to the execution plan.

            :param cmd_id: Numeric command identifier.
            :param payload: Serialized payload bytes.
            :param description: Human-readable command description.
            :return: Self for method chaining.
            :exceptions: None.
        '''
        self._commands.append(PlanCommand(cmd_id=cmd_id, payload=payload, description=description))
        return self

    @property
    def commands(self) -> tuple[PlanCommand, ...]:
        '''
            Returns immutable tuple of commands in sequence.

            :return: Immutable tuple of plan commands.
            :exceptions: None.
        '''
        return tuple(self._commands)

    def count(self) -> int:
        '''
            Returns total number of commands in plan.

            :return: Integer count of commands.
            :exceptions: None.
        '''
        return len(self._commands)

    def clear(self) -> None:
        '''
            Clears all commands from plan.

            :exceptions: None.
        '''
        self._commands.clear()
