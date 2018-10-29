# HOSTNAME = "http://33.83.11.227/commonuser"
# APPNAME = u"__base__"
# USERS = [["admin", "admin", 15], ["sc_admin", "admin", 16]
#              , ["sc_normal", "admin", 17]];
#   
# HOSTNAME = "http://33.83.11.227/commonuserv2"
# APPNAME = u"__base__"
# USERS = [["userall", "admin", 1],["admin", "admin", 1], ["sc_admin", "admin", 2]
#              , ["sc_normal", "admin", 3]];
#                  

HOSTNAME = "http://33.83.11.227/commonuserv2"
APPNAME = u"__base__"
USERS = [["admin", "admin1", [1, 2]]
         
         ];
#                  
# #  
# HOSTNAME = "http://localhost:8001/common-user"
# APPNAME = u"__base__"
# USERS = [["admin", "admin1", [1, 2]]];
#                

# 
# HOSTNAME = "http://10.125.25.106/common-user"
# APPNAME = u"jyang_app"
# USERS = [["zdadmin", "admin", 181], ["scadmin", "admin", 182]
#              , ["scnormal", "admin", 183]];

if __name__ == "__main__":
    from aliyun.usermgt.dep.createDefaultPerms import importPerms
    from aliyun.usermgt.dep.createDefaultRoles import importRoles
    from aliyun.usermgt.dep.createOrgTree import installOrgs
    from aliyun.usermgt.dep.createDefaultUsers import importUser
    
    importPerms();
    importRoles();
    installOrgs();
    importUser();