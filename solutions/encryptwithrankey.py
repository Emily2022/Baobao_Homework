#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
ACTIVATE_SCRIPT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                 "venv/bin/activate_this.py")
execfile(ACTIVATE_SCRIPT, dict(__file__=ACTIVATE_SCRIPT))

from Crypto.Cipher import AES


if not os.path.exists(sys.argv[2]):
    print "no such input file %s exists!\n" % sys.argv[2]
else:
    suite = AES.new(sys.argv[1], AES.MODE_CBC, sys.argv[1])
    input_content = open(sys.argv[2], 'r').read()
    mod16_res = len(input_content) % 16
    input_content = input_content + " " * (16 - mod16_res)
    open(sys.argv[3], 'w').write(suite.encrypt(input_content))
