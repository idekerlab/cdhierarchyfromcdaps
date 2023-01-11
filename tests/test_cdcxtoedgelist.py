#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cdhierarchyfromcdaps
----------------------------------

Tests for `cdhierarchyfromcdaps` module.
"""

import os
import sys
import unittest
import tempfile
import shutil
import io
import stat
import json
from unittest.mock import MagicMock
from cdhierarchyfromcdaps import cdhierarchyfromcdapscmd


class Testcdhierarchyfromcdaps(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_args_all_defaults(self):
        myargs = ['inputarg']
        res = cdhierarchyfromcdapscmd._parse_arguments('desc', myargs)
        self.assertEqual('inputarg', res.input)
        self.assertEqual(None, res.weight)
        self.assertEqual(False, res.failonmissingweight)
        self.assertEqual(0.0, res.default)


if __name__ == '__main__':
    sys.exit(unittest.main())
