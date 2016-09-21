# -*- coding: utf-8 -*-

# Copyright (C) 2015-2016 Avencall
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

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import (LineExtensionRelation,
                                         IncallExtensionRelation)


class ExtensionRelation(object):

    def __init__(self, builder, extension_id):
        self.extension_id = extension_id
        self.line_extension_relation = LineExtensionRelation(builder)
        self.incall_extension_relation = IncallExtensionRelation(builder)

    @extract_id
    def add_line(self, line_id):
        return self.line_extension_relation.associate(line_id, self.extension_id)

    @extract_id
    def remove_line(self, line_id):
        return self.line_extension_relation.dissociate(line_id, self.extension_id)

    def get_line(self):
        return self.line_extension_relation.get_by_extension(self.extension_id)

    def list_lines(self):
        return self.line_extension_relation.list_by_extension(self.extension_id)

    def list_extension(self):
        return self.incall_extension_relation.list_by_extension(self.extension_id)


class ExtensionsCommand(CRUDCommand):

    resource = 'extensions'

    relation_cmd = ExtensionRelation
