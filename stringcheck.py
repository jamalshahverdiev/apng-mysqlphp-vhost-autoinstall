#!/bin/env python2.7

import sys, os

arg1 = raw_input('Xahis olunur setir daxil edesiniz: ')
if arg1 == str or len(arg1) != 1: 
    print("Yalniz 1 ve ya 2 reqemini birlikde olmamaqla daxil etmek mumkundur.")
    sys.exit()
elif len(arg1) == 1 and (arg1 == 1 or arg1 == 2):
    print(arg1, "daxil etdiniz...")
    pass

print("Code davam edir")
