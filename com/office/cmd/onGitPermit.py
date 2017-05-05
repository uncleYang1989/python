#!/usr/bin/python
# -*- coding: UTF-8 -*-
from com.office.util import fileUtil
if __name__ == '__main__':
    files = """
sky-nms/nms-common/src/main/java/com/commsky/nms/dist/DeviceDistUtil.java
sky-nms/nms-common/src/main/java/com/commsky/nms/dist/pojo/ApplySyncReqDO.java
sky-nms/nms-common/src/main/java/com/commsky/nms/dist/pojo/CommNcpEventResDO.java
sky-nms/nms-common/src/main/java/com/commsky/nms/dist/pojo/OperateDeviceBean.java
sky-nms/nms-common/src/main/java/com/commsky/nms/dist/pojo/ResultBean.java
sky-nms/nms-common/src/main/java/com/commsky/nms/dist/pojo/StatusReqDO.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/controller/customer/CustomerController.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/controller/device/DeviceController.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/impl/device/exec/DeviceExecApplyAsyncHandler.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/impl/device/exec/DeviceExecApplySyncHandler.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/impl/device/exec/DeviceExecSshHandler.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/impl/device/exec/DeviceExecStatusHandler.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/impl/device/exec/DeviceExecSyncHandler.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/impl/device/exec/DeviceExecUpgradeHandler.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/rest/api/device/impl/DeviceConfigServiceImpl.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/rest/api/device/impl/DeviceServiceImpl.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/upgrade/DeviceUpgradeService.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/upgrade/DeviceUpgradeServiceImpl.java    """.strip().splitlines();

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
