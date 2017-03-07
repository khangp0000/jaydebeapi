#!/usr/bin/env python
from __future__ import print_function
from os import path
import sys

home=sys.argv[1]
with open(path.join(home, '.jip'), "w") as out:
    print("""[repos:local]
uri={0}/.m2/repository/
type=local

[repos:central]
uri=http://repo1.maven.org/maven2/
type=remote
""".format(home), file=out)
