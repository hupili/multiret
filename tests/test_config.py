#-*-coding:utf-8-*-

import os
import glob
import sys
import json
import shutil

DIR_TEST = os.path.abspath(os.path.dirname(__file__))
DIR_TMP = os.path.join(DIR_TEST, "tmp")
DIR_ROOT = os.path.dirname(DIR_TEST)
DIR_MULTI = os.path.join(DIR_ROOT, "src")
sys.path.append(DIR_MULTI)

WRONG_RESULT_ERROR = "wrong result"
NO_SUCH_KEY_ERROR_TEMPLATE = "no such key: %s"

class TestBase(object):

    @classmethod
    def clean_up(klass, path, wildcard):
        os.chdir(path)
        for rm_file in glob.glob(wildcard):
            os.unlink(rm_file)

    @classmethod
    def setup_class(klass):
        sys.stderr.write("\nRunning %s\n" % klass)
        if not os.path.isdir(DIR_TMP):
            print "makedirs"
            os.makedirs(DIR_TMP)

    @classmethod
    def teardown_class(klass):
        klass.clean_up(DIR_TEST, "*.py?")
        klass.clean_up(DIR_ROOT, "*.py?")
        shutil.rmtree(DIR_TMP)

if __name__ == '__main__':
    pass
