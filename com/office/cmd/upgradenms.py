#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    hostnames = """
172.16.60.186
172.16.60.187
172.16.60.190
    """.strip().splitlines();
    pathname = "/var/data/upgrade/local/cloud_3.8.0_upgrade_commsky_20170417152331.zip ";
    for hostname in hostnames:
        print "scp %s root@%s:%s"%(pathname, hostname, pathname)
        print ""