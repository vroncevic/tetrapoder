# -*- coding: UTF-8 -*-

'''
Module
    imotion_runner_test.py
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
    Unit tests for IMotionRunner structural protocol.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.service.runner.imotion_runner import IMotionRunner
from tetrapoder.core.service.runner.motion_runner import MotionRunner

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestIMotionRunner(TestCase):
    '''
        Test cases verifying IMotionRunner protocol conformance.

        It defines:

            :methods:
                | test_structural_conformance - Verifies MotionRunner satisfies IMotionRunner.
    '''

    def test_structural_conformance(self) -> None:
        '''
            Verifies MotionRunner satisfies IMotionRunner.

            :exceptions: None.
        '''
        self.assertTrue(isinstance(MotionRunner(), IMotionRunner))


if __name__ == '__main__':
    main()
