#!/usr/bin/python
# -*- coding: UTF-8 -*-
from com.office.util import fileUtil
if __name__ == '__main__':
    files = """
sky-core/core-common/src/main/java/com/commsky/core/system/DistributedInfo.java
sky-core/core-common/src/main/java/com/commsky/core/web/PublicFun.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/impl/device/exec/DeviceExecCliHandler.java
sky-nms/nms-webapp/src/main/webapp/js/cst/monitoring/monitoringDevice.js
""".strip().splitlines();

    '''
    备份模式
    '''
    srcDir = "/Users/yangjie/mywork/icode/cloudnms";
    destDir = "/Users/yangjie/Desktop/codebak";
#
    '''
#     恢复模式
#     '''
    srcDir = "/Users/yangjie/Desktop/codebak";
    destDir = "/Users/yangjie/mywork/icode/cloudnms";

    import os
    for f in files:
        fileUtil.mkdir(os.path.dirname(os.path.join(destDir, f)))
        cmd = "cp -rf %s/%s %s/%s" % (srcDir, f, destDir, f);
        print cmd
        os.system(cmd);
