# MySQL Connector/Python - MySQL driver written in Python.
# Copyright (c) 2013, 2014, Oracle and/or its affiliates. All rights reserved.

# MySQL Connector/Python is licensed under the terms of the GPLv2
# <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>, like most
# MySQL Connectors. There are special exceptions to the terms and
# conditions of the GPLv2 as it is applied to this software, see the
# FOSS License Exception
# <http://www.mysql.com/about/legal/licensing/foss-exception.html>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

"""Unittests code analysis

Requires:
    pylint v1.2.0 or higher
"""

import os
import tests
import logging
import unittest

LOGGER = logging.getLogger(tests.LOGGER_NAME)

_PYLINT_AVAILABLE = True
try:
    from pylint import lint
    from pylint.reporters.text import TextReporter
except ImportError as err:
    LOGGER.warning("pylint not available")
    _PYLINT_AVAILABLE = False

_CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
(_BASE_PATH, _,) = os.path.split(_CURRENT_PATH)
PYLINTRC = os.path.join(_CURRENT_PATH, '..', 'support', 'style', 'pylint.rc')
IGNORE_LIST = ['dbapi.py', 'client_error.py', 'errorcode.py', 'charsets.py']


@unittest.skipIf(not os.path.exists(PYLINTRC), "pylint.rc not available")
class LintTests(tests.MySQLConnectorTests):

    """Class checking coding style"""

    def setUp(self):
        self.pylint_rc_path = PYLINTRC
        self.dir_path = os.path.join('lib', 'mysql', 'connector')
        self.output_file_path = os.path.join(os.getcwd(), 'pylint_output.txt')
        self.pylint_output_file = open(self.output_file_path, "w+")
        self.failed_files = []

    def tearDown(self):
        size = self.pylint_output_file.tell()
        self.pylint_output_file.close()
        if not size:
            os.remove(self.output_file_path)

    @unittest.skipIf(not _PYLINT_AVAILABLE, "pylint not available")
    def test_lint(self):
        """Process modules for pylint tests
        """
        txtreporter = TextReporter(self.pylint_output_file)
        for root, _, files in os.walk(self.dir_path):
            if (['connector', 'django'] ==
                [ os.path.basename(fld) for fld in os.path.split(root)]):
                continue
            for name in files:
                if name.endswith('.py') and name not in IGNORE_LIST:
                    current_path = os.path.join(root, name)
                    lint_args = [
                        current_path,
                        "--rcfile={0}".format(self.pylint_rc_path)
                        ]
                    lint_run = lint.Run(lint_args, reporter=txtreporter,
                                        exit=False)

                    if lint_run.linter.stats['by_msg']:
                        rel_file_path = os.path.join(
                            os.path.relpath(root, _BASE_PATH), name)
                        self.failed_files.append(rel_file_path)

        if self.failed_files:
            file_names = ''
            for file in self.failed_files:
                file_names += file + '\n'
            self.fail('Lint tests failed on following files\n{0}\n'
                      'For more information check {1}.'.format(
                        file_names,
                        os.path.relpath(self.output_file_path, _BASE_PATH)))

