# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from xivo_lib_rest_client import HTTPCommand
from xivo_confd_client.util import url_join


class WizardCommand(HTTPCommand):

    resource = 'wizard'

    def create(self, body, timeout=300):
        url = url_join(self.resource)
        response = self.session.post(url, body, timeout=timeout)
        return response.json()

    def get(self):
        url = url_join(self.resource)
        response = self.session.get(url)
        return response.json()

    def discover(self):
        url = url_join(self.resource, "discover")
        response = self.session.get(url)
        return response.json()

    def __call__(self):
        return self.get()
