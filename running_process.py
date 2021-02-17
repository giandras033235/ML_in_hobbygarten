import os
import sys

pid = str(os.getpid())
pidfile = "/tmp/mydaemon.pid"

if os.path.isfile(pidfile):
    print ("%s already exists, exiting" % pidfile)
    sys.exit()
open(pidfile, 'w').write(pid)
try:
    print("asd")
finally:
    os.unlink(pidfile)