# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade as oe


@oe.migrate()
def migrate(cr, version):
    oe.rename_columns([
        ('prev_sprint', None),
        ('next_sprint', None),
        ('sprint_type', None),
    ])
