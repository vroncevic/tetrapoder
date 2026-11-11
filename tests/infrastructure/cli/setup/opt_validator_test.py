# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
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
    Unit tests for CLIBundleOptionsValidator.
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

from tetrapoder.infrastructure.cli.setup.opt_validator import CLIBundleOptionsValidator
from tetrapoder.infrastructure.cli.setup.options import CLIBundleOptions
from tetrapoder.setup.bundle import TetrapoderBundle
from tetrapoder.setup.factory import TetrapoderBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLIBundleOptionsValidator(TestCase):
    '''
        Test cases verifying CLIBundleOptionsValidator.

        It defines:

            :methods:
                | test_validate_success - Verifies validation of properly formed CLI options.
                | test_validate_none - Verifies validation failure on None options.
                | test_validate_not_mapping - Verifies validation failure on non-mapping.
                | test_validate_invalid_attr - Verifies validation failure on invalid attribute type.
                | test_is_valid_success - Verifies is_valid returns True for valid options.
                | test_is_valid_failure - Verifies is_valid returns False on validation failure.
    '''

    def test_validate_success(self) -> None:
        '''
            Verifies validation of properly formed CLI options.

            :exceptions: None.
        '''
        bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        opts: CLIBundleOptions = {
            'parser': bundle.base.option_manager,
        }
        CLIBundleOptionsValidator.validate(opts)

    def test_validate_none(self) -> None:
        '''
            Verifies validation failure on None options.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            CLIBundleOptionsValidator.validate(None)  # type: ignore[arg-type]

    def test_validate_not_mapping(self) -> None:
        '''
            Verifies validation failure on non-mapping.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError):
            CLIBundleOptionsValidator.validate('not_mapping')  # type: ignore[arg-type]

    def test_validate_invalid_attr(self) -> None:
        '''
            Verifies validation failure on invalid attribute type.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError):
            CLIBundleOptionsValidator.validate({'parser': 'invalid_parser'})  # type: ignore[arg-type]

    def test_is_valid_success(self) -> None:
        '''
            Verifies is_valid returns True for valid options.

            :exceptions: None.
        '''
        bundle: TetrapoderBundle = TetrapoderBundleFactory.create_bundle()
        opts: CLIBundleOptions = {
            'parser': bundle.base.option_manager,
        }
        self.assertTrue(CLIBundleOptionsValidator.is_valid(opts))

    def test_is_valid_failure(self) -> None:
        '''
            Verifies is_valid returns False on validation failure.

            :exceptions: None.
        '''
        self.assertFalse(CLIBundleOptionsValidator.is_valid(None))  # type: ignore[arg-type]


if __name__ == '__main__':
    main()
