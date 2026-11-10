# -*- coding: UTF-8 -*-

'''
Module
    keys.py
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
    Runtime components and interface constraints for the CLI bundle.
'''

from __future__ import annotations

from collections.abc import Sequence
from types import MappingProxyType
from typing import ClassVar

from ats_utilities.option.imanager import IOptionManager

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CLIBundleKeys:
    '''
        Runtime components and interface constraints for the CLI bundle.

        It defines:

            :attributes:
                | DEPENDENCY_PARSER - Parser interface key for CLI bundle dependencies.
                | DEPENDENCY_COMMANDS - Commands sequence key for CLI bundle dependencies.
                | OPTION_PARSER - Parser option key for CLI bundle options.
            :methods:
                | get_dependency_to_type - Returns dependency to type mapping.
                | get_option_to_type - Returns option to type mapping.
    '''

    DEPENDENCY_PARSER: ClassVar[str] = 'parser'
    DEPENDENCY_COMMANDS: ClassVar[str] = 'commands'

    OPTION_PARSER: ClassVar[str] = 'parser'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of CLI bundle dependencies to their expected types.

            :return: MappingProxyType mapping dependency keys to types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_PARSER: IOptionManager,
            cls.DEPENDENCY_COMMANDS: Sequence,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of CLI bundle options to their expected types.

            :return: MappingProxyType mapping option keys to types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_PARSER: IOptionManager,
        })
