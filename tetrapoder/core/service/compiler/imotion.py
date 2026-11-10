# -*- coding: UTF-8 -*-

'''
Module
    imotion.py
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
    Structural interface for motion plan binary compilation.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.plan_command import PlanCommand

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IMotionCompiler(Protocol):
    '''
        Structural protocol defining motion plan compilation to binary protocol streams.

        It defines:

            :methods:
                | compile - Compiles MotionPlan into contiguous binary byte sequence.
                | compile_command - Compiles a single motion command into wire-level frame.
    '''

    def compile(self, plan: MotionPlan) -> bytes:
        '''
            Compiles all commands in the plan into binary frames with CRC-8 checksums.

            :param plan: Target MotionPlan instance.
            :return: Contiguous bytes representing the wire protocol transmission.
        '''

    def compile_command(self, cmd: PlanCommand) -> bytes:
        '''
            Compiles a single motion command into wire-level binary frame.

            :param cmd: PlanCommand instance to compile.
            :return: Formatted wire-level frame bytes.
        '''
