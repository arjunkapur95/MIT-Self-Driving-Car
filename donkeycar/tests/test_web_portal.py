"""
test_web_portal.py

Simple script used to test the web portal from a local machine.

After running this script, connect to the portal by visiting http://localhost:8887/drive
"""

import sys
sys.path.append("..")
sys.path.append("../parts/controllers")

import utils
from web import *

server = LocalWebController()
server.run()
server.update()