# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.


"""Tests for template context processors."""

from __future__ import absolute_import, print_function

from flask import render_template_string


def test_context_processor_jwt(app):
    """Test context processor JWT."""
    template = r"""
    {{ jwt() }}
    """
    with app.test_request_context():
        html = render_template_string(template)
        assert 'authorized_token' in html


def test_context_processor_jwt_token(app):
    """Test context processor token JWT."""
    template = r"""
    {{ jwt_token() }}
    """
    with app.test_request_context():
        html = render_template_string(template)
        assert html
