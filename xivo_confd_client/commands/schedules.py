# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.crud import CRUDCommand


class SchedulesCommand(CRUDCommand):

    resource = 'schedules'
