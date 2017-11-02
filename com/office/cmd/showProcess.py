import commands
sts, text = commands.getstatusoutput("ps aux |grep deploy")
lines = text.split("\n")
exist = False
for line in lines:
    if line.startswith("commsky") and line.endswith("/usr/bin/python ./deploy_service.py"):
        exist = True
        break
import sys
if exist:
    sys.exit(0)
else:
    sys.exit(1)

