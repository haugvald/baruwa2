# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# Baruwa - Web 2.0 MailScanner front-end.
# Copyright (C) 2010-2012  Andrew Colin Kissa <andrew@topdog.za.net>
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"Accounts audit messages"

try:
    from pylons.i18n.translation import _
except ImportError:
    from baruwa.lib.misc import _


QUEUERELEASE_MSG = _("Queued Message-ID: %(m)s released to %(a)s")
QUEUEDELETE_MSG = _("Queued Message-ID: %(m)s deleted from %(q)s queue")
QUEUEPREVIEW_MSG = _("Queued Message-ID: %(m)s preview")
QUEUEDOWNLOAD_MSG = _("Queued Message-ID: %(m)s downloaded attachment %(a)s")
HOSTSTATUS_MSG = _("Node status for: %(n)s viewed")
HOSTSALINT_MSG = _("Node lint status for: %(n)s viewed")
HOSTBAYES_MSG = _("Node bayes stats for: %(n)s viewed")
AUDITLOGEXPORT_MSG = _("Audit log exported")


__all__ = [
    'QUEUERELEASE_MSG',
    'QUEUEDELETE_MSG',
    'QUEUEPREVIEW_MSG',
    'QUEUEDOWNLOAD_MSG',
    'HOSTSTATUS_MSG',
    'HOSTSALINT_MSG',
    'HOSTBAYES_MSG',
    'AUDITLOGEXPORT_MSG',
]