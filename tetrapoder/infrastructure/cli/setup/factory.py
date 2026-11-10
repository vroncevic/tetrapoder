# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the CLI bundle with registered commands.
'''

from __future__ import annotations

from tetrapoder.infrastructure.cli.setup.bundle import CLIBundle
from tetrapoder.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from tetrapoder.infrastructure.cli.setup.keys import CLIBundleKeys
from tetrapoder.infrastructure.cli.setup.opt_validator import CLIBundleOptionsValidator
from tetrapoder.infrastructure.cli.setup.options import CLIBundleOptions
from tetrapoder.infrastructure.cli.setup.registry import CLIBundleRegistry
from tetrapoder.infrastructure.command.bundle import CommandBundle
from tetrapoder.infrastructure.command.definition import TetrapoderCommandDefinition
from tetrapoder.infrastructure.command.executor import TetrapoderCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CLIBundleFactory:
    '''
        Factory for creating the CLI bundle.

        It defines:

            :methods:
                | create_bundle - Creates the CLI bundle with registered commands.
                | get_version - Returns the factory version.
    '''

    @classmethod
    def create_bundle(cls, options: CLIBundleOptions) -> CLIBundle:
        '''
            Creates the CLI bundle with registered commands.

            :param options: The CLI bundle options.
            :return: The CLI bundle.
            :exceptions:
                | ATSValueError: If options fail validation.
        '''
        CLIBundleOptionsValidator.validate(options)

        definition: TetrapoderCommandDefinition = TetrapoderCommandDefinition()
        executor: TetrapoderCommandExecutor = TetrapoderCommandExecutor(definition)
        command_bundle: CommandBundle = CommandBundle(definition=definition, executor=executor)

        return CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                parser=options[CLIBundleKeys.OPTION_PARSER],
                commands=(command_bundle,)
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version string.

            :return: Factory version string.
            :exceptions: None.
        '''
        return __version__
