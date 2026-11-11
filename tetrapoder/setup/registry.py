# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Registry for creating and validating tetrapoder bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from tetrapoder.infrastructure.cli.icli import ICLI
from tetrapoder.setup.bundle import TetrapoderBundle
from tetrapoder.setup.dep_validator import TetrapoderBundleDependenciesValidator
from tetrapoder.setup.dependencies import TetrapoderBundleDependencies
from tetrapoder.setup.keys import TetrapoderBundleKeys
from tetrapoder.setup.validator import TetrapoderBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TetrapoderBundleRegistry:
    '''
        Encapsulates core components for simplification of tetrapoder bundle creation.

        It defines:

            :methods:
                | create_bundle - Creates the tetrapoder bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: TetrapoderBundleDependencies) -> TetrapoderBundle:
        '''
            Creates the tetrapoder bundle from dependencies.

            :param dependencies: The tetrapoder bundle dependencies.
            :return: The validated tetrapoder bundle.
            :exceptions:
                | ATSValueError: The dependencies or bundle must be provided and valid.
                | ATSTypeError: The dependencies or bundle attributes must match types.
        '''
        TetrapoderBundleDependenciesValidator.validate(dependencies)

        base_bundle: BaseBundle | None = (
            dependencies.get(TetrapoderBundleKeys.DEPENDENCY_BASE)
            if dependencies else None
        )
        cli_adapter: ICLI | None = (
            dependencies.get(TetrapoderBundleKeys.DEPENDENCY_CLI)
            if dependencies else None
        )

        bundle: TetrapoderBundle = TetrapoderBundle(
            base=base_bundle,
            cli=cli_adapter,
        )
        TetrapoderBundleValidator.validate(bundle)
        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version string.

            :return: Registry version string.
            :exceptions: None.
        '''
        return __version__
