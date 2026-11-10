# -*- coding: UTF-8 -*-

'''
Module
    irunner.py
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
    Structural interface for motion plan execution runner.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.service.runner.itransport import ITransport

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IMotionRunner(Protocol):
    '''
        Structural protocol defining motion plan execution runner.

        It defines:

            :methods:
                | execute - Streams motion plan frames with ACK/NACK validation.
                | ping - Verifies robot heartbeat connectivity.
    '''

    def execute(self, plan: MotionPlan, transport: ITransport) -> bool:
        '''
            Executes compiled motion plan commands over hardware transport.

            :param plan: MotionPlan container to execute.
            :param transport: Hardware transport instance.
            :return: True if all commands acknowledged, False otherwise.
        '''

    def ping(self, transport: ITransport) -> bool:
        '''
            Sends heartbeat ping and checks for pong response.

            :param transport: Hardware transport instance.
            :return: True if pong response received, False otherwise.
        '''
