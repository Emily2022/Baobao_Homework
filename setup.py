#-*- coding: utf-8 -*-
import sys
from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages

NAME = "baobao_practice"
DESCRIPTION = "宝宝的练习题们"
AUTHOR = "Foxfi Ning"
AUTHOR_EMAIL = "foxdoraame@gmail.com"

MODULES=[]
PACKAGES = find_packages(exclude=['tests.*', 'tests', 'solutions.*', 'solutions'])
ENTRY_POINTS = """
[console_scripts]
baobao-look-at-solution=practices.solmain:main
"""

INSTALL_REQUIRES = ["pycrypto"]
TESTS_REQUIRE = ['pytest']


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests/', '--junitxml', 'unittest.xml']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    py_modules=MODULES,
    packages=PACKAGES,
    zip_safe=False,
    entry_points=ENTRY_POINTS,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    cmdclass={'test': PyTest},
)
