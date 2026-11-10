# -*- coding: UTF-8 -*-

'''
Module
    executor_test.py
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
    Unit tests for TetrapoderCommandExecutor.
'''

from __future__ import annotations

from os import remove
from os.path import exists
from unittest import TestCase, main
from unittest.mock import patch

from tetrapoder.core.service.runner.motion_runner import MotionRunner
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


class TestTetrapoderCommandExecutor(TestCase):
    '''
        Test cases verifying TetrapoderCommandExecutor execution strategy.

        It defines:

            :methods:
                | test_compile_action - Verifies execution of compile action.
                | test_gait_action - Verifies execution of gait action.
                | test_ping_action - Verifies execution of ping action.
                | test_ping_action_failure - Verifies execution of ping returning false.
                | test_definition_and_str - Verifies get_definition and string representation.
    '''

    def test_compile_action(self) -> None:
        '''
            Verifies execution of compile action.

            :exceptions: None.
        '''
        definition: TetrapoderCommandDefinition = TetrapoderCommandDefinition()
        executor: TetrapoderCommandExecutor = TetrapoderCommandExecutor(definition)
        output_file: str = '/tmp/test_executor_motion.bin'

        try:
            result = executor.execute(params={'action': 'compile', 'output': output_file, 'gait': 'sit'})
            self.assertEqual(result.get('returncode'), 0)
            self.assertTrue(exists(output_file))
        finally:
            if exists(output_file):
                remove(output_file)

    def test_gait_action(self) -> None:
        '''
            Verifies execution of gait action.

            :exceptions: None.
        '''
        definition: TetrapoderCommandDefinition = TetrapoderCommandDefinition()
        executor: TetrapoderCommandExecutor = TetrapoderCommandExecutor(definition)
        result = executor.execute(params={'action': 'gait', 'gait': 'walk'})
        self.assertEqual(result.get('returncode'), 0)
        self.assertIn('Generated', str(result.get('stdout')))
        result_wave = executor.execute(params={'action': 'gait', 'gait': 'wave'})
        self.assertEqual(result_wave.get('returncode'), 0)

    def test_ping_action(self) -> None:
        '''
            Verifies execution of ping action.

            :exceptions: None.
        '''
        definition: TetrapoderCommandDefinition = TetrapoderCommandDefinition()
        executor: TetrapoderCommandExecutor = TetrapoderCommandExecutor(definition)
        result = executor.execute(params={'action': 'ping', 'port': '/dev/non_existent_tty_device'})
        self.assertEqual(result.get('returncode'), 1)

    def test_ping_action_failure(self) -> None:
        '''
            Verifies execution of ping returning false.

            :exceptions: None.
        '''
        definition: TetrapoderCommandDefinition = TetrapoderCommandDefinition()
        executor: TetrapoderCommandExecutor = TetrapoderCommandExecutor(definition)
        with patch.object(MotionRunner, 'ping', return_value=False):
            result = executor.execute(params={'action': 'ping', 'port': '/dev/null'})
            self.assertEqual(result.get('returncode'), 1)

    def test_definition_and_str(self) -> None:
        '''
            Verifies get_definition and string representation.

            :exceptions: None.
        '''
        definition: TetrapoderCommandDefinition = TetrapoderCommandDefinition()
        executor: TetrapoderCommandExecutor = TetrapoderCommandExecutor(definition)
        self.assertEqual(executor.get_definition(), definition)
        self.assertTrue(isinstance(str(executor), str))


if __name__ == '__main__':
    main()
