#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

ACTIVATE_SCRIPT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                 "venv/bin/activate_this.py")
execfile(ACTIVATE_SCRIPT, dict(__file__=ACTIVATE_SCRIPT))

from Crypto.Cipher import AES


PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AES_MODE = AES.MODE_CBC

def main():
    input_string = raw_input("你要看哪个题目的solution? 输入编号(1,2,..):\n")
    answer_code = raw_input("输入此题对应的解题密钥:\n")
    solution_filename = "practice" + input_string + ".py"
    solution_filepath = os.path.join(PROJECT_ROOT_DIR,
                                     "solutions/" + solution_filename)
    if os.path.exists(solution_filepath):
        try:
            suite = AES.new(answer_code, AES_MODE, answer_code)
        except ValueError:
            print "错误: 检查你的answer code是否正确!"
            sys.exit(1)
        print suite.decrypt(open(solution_filepath, 'r').read())
    else:
        print "没有编号为'%s', 名字叫做'solutions/practice%s.py'的文件存在" % (input_string, input_string)

    return 0

if __name__ == "__main__":
    sys.exit(main())
