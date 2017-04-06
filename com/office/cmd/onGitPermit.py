#!/usr/bin/python
# -*- coding: UTF-8 -*-
from com.office.util import fileUtil
if __name__ == '__main__':
    files = """
sky-base/install/public/commsky/etc/sky.properties
sky-build/config/dev/application.properties
sky-build/config/prod/application.properties
sky-core/core-common/src/main/java/com/commsky/core/system/DistributedInfo.java
sky-core/core-common/src/main/java/com/commsky/core/system/SystemInfo.java
sky-core/core-shiro/src/main/java/com/commsky/core/shiro/cache/CacheRepositoryHelper.java
sky-core/core-shiro/src/main/java/com/commsky/core/shiro/session/SessionRepository.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/controller/billing/BillingController.java
sky-nms/nms-service/src/main/java/com/commsky/nms/web/services/impl/customer/TokenServiceImpl.java
    """.strip().splitlines();
    destDir = "/Users/yangjie/Desktop/codebak";
    srcDir = "/Users/yangjie/mywork/icode/cloudnms";
     
    destDir = "/Users/yangjie/mywork/icode/cloudnms";
    srcDir = "/Users/yangjie/Desktop/codebak";
    
    import os
    for f in files:
        fileUtil.mkdir(os.path.dirname(os.path.join(destDir, f)))
        cmd = "cp -rf %s/%s %s/%s"%(srcDir,f,destDir,f);
        print cmd
        os.system(cmd);