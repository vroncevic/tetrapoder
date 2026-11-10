# -*- coding: UTF-8 -*-

'''
Module
    gait_planning.py
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
    Demonstration of procedural quadruped locomotion and gait sequencing.
'''

from __future__ import annotations

from sys import exit as sys_exit, stdout

from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.service.compiler.motion_compiler import MotionCompiler
from tetrapoder.core.service.gait.gait_plan_builder import GaitPlanBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def main() -> bool:
    '''
        Demonstrates procedural gait planning with GaitPlanBuilder.

        :return: True if compiled successfully.
        :exceptions: None.
    '''
    builder: GaitPlanBuilder = GaitPlanBuilder()

    # Build sequence of postures and locomotion gaits
    builder.stand()
    builder.walk(steps=3, backward=False)
    builder.turn(steps=2, to_right=False)
    builder.walk(steps=3, backward=True)
    builder.turn(steps=2, to_right=True)
    builder.sit()

    plan: MotionPlan = builder.build()
    data: bytes = MotionCompiler().compile(plan=plan)

    stdout.write(f'Gait planning generated {len(plan.commands)} commands.\n')
    for idx, cmd in enumerate(plan.commands, 1):
        stdout.write(f'  [{idx}] {cmd.description} (cmd_id=0x{cmd.cmd_id:02X}, len={len(cmd.payload)})\n')
    stdout.write(f'Compiled stream: {len(data)} bytes.\n')
    return True


if __name__ == '__main__':
    sys_exit(0 if main() else 1)
