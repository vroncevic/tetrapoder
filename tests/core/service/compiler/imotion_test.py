# -*- coding: UTF-8 -*-

'''
Module
    imotion_test.py
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
    Unit tests for IMotionCompiler structural protocol.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.service.compiler.imotion import IMotionCompiler
from tetrapoder.core.service.compiler.motion import MotionCompiler
from tetrapoder.core.service.crc8.crc import CRC8
from tetrapoder.core.service.protocol.frame import ProtocolFrameBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestIMotionCompiler(TestCase):
    '''
        Test cases verifying IMotionCompiler protocol conformance.

        It defines:

            :methods:
                | test_structural_conformance - Verifies MotionCompiler satisfies IMotionCompiler.
    '''

    def test_structural_conformance(self) -> None:
        '''
            Verifies MotionCompiler satisfies IMotionCompiler.

            :exceptions: None.
        '''
        self.assertTrue(isinstance(MotionCompiler(ProtocolFrameBuilder(CRC8())), IMotionCompiler))


if __name__ == '__main__':
    main()
