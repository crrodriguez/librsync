#! /usr/bin/python

# Generate a series of (OFFSET,LENGTH) pairs for testing map_ptr, and
# also the output file that ought to be generated by them.

# Copyright (C) 2000 by Martin Pool
# $Id$

import sys
from random import randint

ntests = 4000

suck = open(sys.argv[3]).read()
filelen = len(suck)

cmdfile = open(sys.argv[1], 'wt')
datafile = open(sys.argv[2], 'wb')

for i in range(ntests):
    off = randint(0, filelen - 1)
    remain = filelen - off
    amount = randint(1, remain)

    cmdfile.write('%d,%d ' % (off,amount))
    datafile.write(suck[off:off+amount])
