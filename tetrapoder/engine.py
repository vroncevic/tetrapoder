# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Engine orchestrating initialization and execution of tetrapoder.
'''

from __future__ import annotations

from collections.abc import Mapping
from logging import INFO, ERROR
from sys import stdout

from ats_utilities.base.engine import Base
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.logger.ilogger import ILogger

from tetrapoder.infrastructure.cli.icli import ICLI
from tetrapoder.setup.bundle import TetrapoderBundle
from tetrapoder.setup.validator import TetrapoderBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Tetrapoder(Base):
    '''
        Engine orchestrating the initialization and execution of tetrapoder.

        It defines:

            :attributes:
                | _is_initialized - Flag indicating whether engine is initialized.
                | _logger - Logger instance for operational status and error logging.
                | _cli - Inbound CLI adapter for command execution.
            :methods:
                | __init__ - Initializes the tetrapoder engine with bundle.
                | process - Processes the tetrapoder CLI commands.
                | get_version - Gets the engine version string.
    '''

    _is_initialized: bool
    _logger: ILogger
    _cli: ICLI

    def __init__(self, bundle: TetrapoderBundle) -> None:
        '''
            Initializes the tetrapoder engine with bundle.

            :param bundle: TetrapoderBundle containing adapters and services.
            :exceptions: None.
        '''
        self._is_initialized = False

        try:
            TetrapoderBundleValidator.validate(bundle)
            super().__init__(bundle.base)
            self._cli = bundle.cli
            self._is_initialized = self._cli.is_initialized()
            self._logger = self.get_context().logger
            self._logger.write_log(INFO, '✅ tetrapoder: engine initialized successfully!')

        except (ATSValueError, ATSTypeError) as exc:
            stdout.write(f'❌ tetrapoder: {exc}!\n')

        except Exception as exc:
            stdout.write(f'❌ tetrapoder unexpected exception: {exc}!\n')

    def process(self, verbose: bool = False) -> bool:
        '''
            Processes the tetrapoder commands.

            :param verbose: Enable verbose output.
            :return: True if successful, False otherwise.
            :exceptions: None.
        '''
        result: Mapping[str, object] = {}

        try:
            if self.is_initialized():
                self._logger.write_log(INFO, '🔥 Starting execution command...')
                result = self._cli.run()
                self._logger.write_log(INFO, '✅ Execution finished!')

                if result.get('returncode') != 0:
                    err_msg: str = str(result.get('stderr') or 'failed!')
                    self._logger.write_log(ERROR, f'❌ tetrapoder: {err_msg}')
                    return False

                out_msg: str = str(result.get('stdout') or '')
                if out_msg:
                    self._logger.write_log(INFO, f'ℹ️ {out_msg}')

                self._logger.write_log(INFO, '✅ tetrapoder: done!')
                return True

            stdout.write('❌ tetrapoder: engine not initialized!\n')
            return False

        except (ATSValueError, ATSTypeError) as exc:
            stdout.write(f'❌ tetrapoder: {exc}!\n')
            return False

        except Exception as exc:
            stdout.write(f'❌ tetrapoder unexpected exception: {exc}!\n')
            return False

    def get_version(self) -> str:
        '''
            Gets the engine version.

            :return: Version string.
            :exceptions: None.
        '''
        return __version__
