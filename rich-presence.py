#!/usr/bin/env python3

from pypresence import Presence
import psutil
import time

"""
Check README.md if you need help to change the code
"""

client_id = "356875221078245376"
RPC = Presence(client_id=client_id)
RPC.connect()

RPC.update(start=int(time.time()))

while True:
    if any(map(lambda x: (x.name().lower() == "overwatch.exe"), psutil.process_iter())) == False:
        quit()

    time.sleep(15)
