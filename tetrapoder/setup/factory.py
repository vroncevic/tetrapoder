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
    Factory for creating the tetrapoder bundle.
'''

from __future__ import annotations

from os.path import abspath, dirname, join

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.factory import ContextBundleFactory

from tetrapoder.infrastructure.cli.engine import CLI
from tetrapoder.infrastructure.cli.setup.bundle import CLIBundle
from tetrapoder.infrastructure.cli.setup.factory import CLIBundleFactory
from tetrapoder.infrastructure.cli.setup.options import CLIBundleOptions
from tetrapoder.setup.bundle import TetrapoderBundle
from tetrapoder.setup.dependencies import TetrapoderBundleDependencies
from tetrapoder.setup.keys import TetrapoderBundleKeys
from tetrapoder.setup.opt_validator import TetrapoderBundleOptionsValidator
from tetrapoder.setup.options import TetrapoderBundleOptions
from tetrapoder.setup.registry import TetrapoderBundleRegistry

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TetrapoderBundleFactory:
    '''
        Factory for creating the tetrapoder bundle.

        It defines:

            :attributes:
                | _info_file - Path to default tetrapoder info configuration file.
            :methods:
                | create_bundle - Creates the tetrapoder bundle with optional configuration.
                | get_version - Returns the factory version.
    '''

    _info_file: str = join(
        dirname(dirname(abspath(__file__))), 'infrastructure', 'config', 'tetrapoder.cfg'
    )

    @classmethod
    def create_bundle(cls, options: TetrapoderBundleOptions | None = None) -> TetrapoderBundle:
        '''
            Creates the tetrapoder bundle.

            :param options: Optional bundle configuration options.
            :return: The initialized TetrapoderBundle.
            :exceptions:
                | ATSValueError: If options fail validation.
                | ATSTypeError:  If options have incorrect types.
        '''
        if options is not None:
            TetrapoderBundleOptionsValidator.validate(options)

        info_file: str = (
            options[TetrapoderBundleKeys.OPTION_INFO_FILE]
            if options is not None and TetrapoderBundleKeys.OPTION_INFO_FILE in options
            else cls._info_file
        )

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=False,
                context_bundle=ContextBundleFactory.create_bundle(),
            )
        )

        cli_bundle: CLIBundle = CLIBundleFactory.create_bundle(
            options=CLIBundleOptions(parser=base_bundle.option_manager)
        )

        cli: CLI = CLI(bundle=cli_bundle)

        return TetrapoderBundleRegistry.create_bundle(
            dependencies=TetrapoderBundleDependencies(base=base_bundle, cli=cli)
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version string.

            :return: Factory version string.
            :exceptions: None.
        '''
        return __version__
