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

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

required_packages = [
        "Pylons>=1.0",
        "SQLAlchemy>=0.7,<0.8",
        "wtforms",
        "reportlab",
        "python-dateutil<2.0",
        "pyparsing",
        "IPy",
        "pytz",
        "Pillow",
        "Mako",
        "Babel",
        "lxml",
        "celery",
        "py-bcrypt",
        "cracklib",
        "psutil",
        "pyrad",
        "python-ldap",
        "psycopg2",
        "eventlet",
        "pylibmc",
        "M2Crypto",
        "marrow.mailer",
        "repoze.what",
        "repoze.what-pylons",
        "repoze.what.plugins.config",
        "repoze.what.plugins.sql",
        "repoze.who>=1.0,<=1.99",
        "repoze.who.plugins.sa",
        "repoze.who.plugins.ldap",
        "repoze.who-friendlyform",
    ]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='baruwa',
    version='2.0.0',
    description='Baruwa email security',
    long_description=read('README'),
    author='Andrew Colin Kissa',
    author_email='andrew@topdog.za.net',
    url='http://www.baruwa.org',
    install_requires=required_packages,
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    scripts=['bin/import-mbox.py', 'bin/eximqf2mbox.py', 'bin/test-smtpauth.py'],
    test_suite='nose.collector',
    package_data={'baruwa': ['i18n/*/LC_MESSAGES/*.mo']},
    message_extractors={'baruwa': [
           ('**.py', 'python', None),
           ('templates/**.html', 'mako', {'input_encoding': 'utf-8'}),
           ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
           ('public/css/**', 'ignore', None),
           ('public/imgs/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = baruwa.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller

    [paste.global_paster_command]
    update-sa-rules = baruwa.commands.updatesarules:UpdateSaRules
    update-queue-stats = baruwa.commands.queuestats:QueueStats
    celeryd = baruwa.lib.mq.commands:CeleryDaemonCommand
    camqadm = baruwa.lib.mq.commands:CAMQPAdminCommand
    celerybeat = baruwa.lib.mq.commands:CeleryBeatCommand
    celeryev = baruwa.lib.mq.commands:CeleryEventCommand
    send-pdf-reports = baruwa.commands.pdfreport:SendPdfReports
    send-quarantine-reports = baruwa.commands.quarantinereport:QuarantineReports
    prunedb = baruwa.commands.dbclean:DBCleanCommand
    prunequarantine = baruwa.commands.cleanquarantine:CleanQuarantineCommand
    routes = pylons.commands:RoutesCommand
    shell = pylons.commands:ShellCommand
    """,
)
