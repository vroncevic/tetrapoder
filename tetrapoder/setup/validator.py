# -*- coding: UTF-8 -*-

'''
Module
    validator.py
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
    Validator for tetrapoder bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

from tetrapoder.infrastructure.cli.icli import ICLI
from tetrapoder.setup.bundle import TetrapoderBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TetrapoderBundleValidator:
    '''
        Validator for the tetrapoder bundle.

        It defines:

            :methods:
                | validate - Validates the tetrapoder bundle.
                | is_valid - Checks if the tetrapoder bundle is valid.
    '''

    @classmethod
    def validate(cls, bundle: TetrapoderBundle) -> None:
        '''
            Validates the tetrapoder bundle.

            :param bundle: The tetrapoder bundle to be validated.
            :exceptions:
                | ATSValueError: The bundle must be provided and have non-None attributes.
                | ATSTypeError: The bundle attributes must match required interfaces.
        '''
        ctx: str = 'tetrapoder_bundle_validator::validate(...)'
        msg_bundle_none: str = 'the tetrapoder bundle must be provided'
        msg_bundle_istype: str = 'the tetrapoder bundle must be an instance of TetrapoderBundle'
        msg_base_none: str = 'the base bundle must be provided'
        msg_cli_none: str = 'the cli adapter must be provided'
        msg_base_istype: str = 'the base bundle must be an instance of BaseBundle'
        msg_cli_istype: str = 'the cli adapter must be an instance of ICLI'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, TetrapoderBundle, ctx, msg_bundle_istype)

        not_none(bundle.base, ctx, msg_base_none)
        not_none(bundle.cli, ctx, msg_cli_none)

        istype(bundle.base, BaseBundle, ctx, msg_base_istype)
        istype(bundle.cli, ICLI, ctx, msg_cli_istype)

    @classmethod
    def is_valid(cls, bundle: TetrapoderBundle) -> bool:
        '''
            Checks if the tetrapoder bundle is valid.

            :param bundle: The tetrapoder bundle to check.
            :return: True if valid, False otherwise.
            :exceptions: None.
        '''
        try:
            cls.validate(bundle)
            return True
        except (ATSValueError, ATSTypeError):
            return False
