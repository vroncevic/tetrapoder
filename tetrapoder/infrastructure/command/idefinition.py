# -*- coding: UTF-8 -*-

'''
Module
    idefinition.py
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
    Structural interface for CLI command metadata definitions.
'''

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from ats_utilities.option.command.data import OptionData

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class ICommandDefinition(Protocol):
    '''
        Structural protocol defining CLI command metadata.

        It defines:

            :methods:
                | name - Command subcommand name string.
                | help_text - Command help string for CLI usage.
                | options - Sequence of OptionData arguments.
    '''

    @property
    def name(self) -> str:
        '''
            Returns the command subcommand name.

            :return: Subcommand name string.
        '''

    @property
    def help_text(self) -> str:
        '''
            Returns the help description of the command.

            :return: Command help string.
        '''

    @property
    def options(self) -> Sequence[OptionData]:
        '''
            Returns sequence of option descriptors for argument parser.

            :return: Sequence of OptionData.
        '''
