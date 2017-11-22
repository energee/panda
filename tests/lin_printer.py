#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import time
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from panda import Panda

# fake
def sec_since_boot():
  return time.time()

def can_printer():
  p = Panda()

  start = sec_since_boot()
  lp = sec_since_boot()
  msgs = defaultdict(list)
  canbus = int(os.getenv("CAN", 0))
  while True:
    can_recv = p.kline_recv()
    for address, _, dat, src in can_recv:
      print(src)

if __name__ == "__main__":
  can_printer()
