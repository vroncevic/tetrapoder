# -*- coding: UTF-8 -*-

'''
Module
    definition.py
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
    Command metadata definition for tetrapoder CLI operations.
'''

from __future__ import annotations

from collections.abc import Sequence

from ats_utilities.option.command.data import OptionData
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TetrapoderCommandDefinition:
    '''
        CLI subcommand metadata definition for tetrapoder.

        It defines:

            :methods:
                | name - Returns the command name.
                | help_text - Returns the command help text.
                | options - Returns the sequence of command options.
                | __str__ - Returns the command definition as string representation.
    '''

    @property
    def name(self) -> str:
        '''
            Returns the command name.

            :return: The command name.
            :exceptions: None.
        '''
        return 'robot'

    @property
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
            :exceptions: None.
        '''
        return 'Tetrapod motion compiler, kinematics solver, and execution manager'

    @property
    def options(self) -> Sequence[OptionData]:
        '''
            Returns the command options.

            :return: Sequence of command options.
            :exceptions: None.
        '''
        return [
            OptionData(
                name='--port',
                help_text='Serial port device path (e.g. /dev/ttyUSB0)',
                action=None,
                default='/dev/ttyUSB0',
                required=False,
                choices=None,
                nargs=None,
            ),
            OptionData(
                name='--baud',
                help_text='Serial communication baudrate',
                action=None,
                default=57600,
                required=False,
                choices=None,
                nargs=None,
            ),
            OptionData(
                name='--action',
                help_text='Action to perform: ping, compile, run, gait',
                action=None,
                default='ping',
                required=False,
                choices=['ping', 'compile', 'run', 'gait'],
                nargs=None,
            ),
            OptionData(
                name='--gait',
                help_text='Gait to generate: stand, sit, walk, wave',
                action=None,
                default='stand',
                required=False,
                choices=['stand', 'sit', 'walk', 'wave'],
                nargs=None,
            ),
            OptionData(
                name='--output',
                help_text='Output binary file path for compilation',
                action=None,
                default='motion.bin',
                required=False,
                choices=None,
                nargs=None,
            ),
        ]

    def __str__(self) -> str:
        '''
            Returns string representation of command definition.

            :return: String representation.
            :exceptions: None.
        '''
        return to_str(self)
