#!/usr/bin/python
# -*- coding: UTF-8 -*-
from com.office.util import fileUtil
if __name__ == '__main__':
    files = """
sky-base/deploy/oem/ruizhang/config_en_US.json
sky-base/deploy/oem/ruizhang/config_zh_CN.json
sky-base/install/gateway/commsky/etc/oem/config_en_US.json
sky-base/install/gateway/commsky/etc/oem/config_zh_CN.json
sky-nms/nms-common/src/main/java/com/commsky/nms/application/NmsOem.java
sky-nms/nms-common/src/main/java/com/commsky/nms/license/LicenseService.java
sky-nms/nms-common/src/main/java/com/commsky/nms/license/impl/LicenseServiceImpl.java
sky-nms/nms-common/src/main/resources/i18n/nms_oem_en_US.properties
sky-nms/nms-common/src/main/resources/i18n/nms_oem_zh_CN.properties
sky-nms/nms-service/src/main/java/com/commsky/nms/web/controller/customer/SystCfgController.java
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
