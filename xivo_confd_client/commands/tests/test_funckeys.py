# -*- coding: utf-8 -*-
# Copyright (C) 2015 Avencall
# SPDX-License-Identifier: GPL-3.0+

from ..funckeys import FuncKeysCommand
from hamcrest import assert_that
from hamcrest import equal_to
from hamcrest import none

from xivo_confd_client.tests import TestCommand


class TestFuncKeys(TestCommand):

    Command = FuncKeysCommand

    def test_get_template_funckey(self):
        template_id = 2
        position = 1
        expected_url = "/funckeys/templates/{}/{}".format(template_id, position)
        expected_content = {'blf': True,
                            'destination': {'exten': '1234', 'href': None, 'type': 'custom'},
                            'id': 32,
                            'inherited': True,
                            'label': 'pouet',
                            'links': []}

        self.set_response('get', 200, expected_content)

        result = self.command.get_template_funckey(template_id, position)

        self.session.get.assert_called_once_with(expected_url)
        assert_that(result, equal_to(expected_content))

    def test_delete_template_funckey(self):
        template_id = 2
        position = 1
        expected_url = "/funckeys/templates/{}/{}".format(template_id, position)

        self.set_response('delete', 204)

        result = self.command.delete_template_funckey(template_id, position)

        self.session.delete.assert_called_once_with(expected_url)
        assert_that(result, none())

    def test_update_template_funckey(self):
        template_id = 2
        position = 1
        expected_url = "/funckeys/templates/{}/{}".format(template_id, position)
        funckey = {'blf': False}

        self.set_response('put', 204)

        result = self.command.update_template_funckey(template_id, position, funckey)

        self.session.put.assert_called_once_with(expected_url, funckey)
        assert_that(result, none())
