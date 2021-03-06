#!/usr/bin/python
# encoding=utf8
rolesPerm = {
u"全部应用管理角色":u"""
态势大屏登录
态势大屏-其他-详细信息
权限管理登录
权限管理-页面-管理
权限管理-页面-角色管理
权限管理-页面-组织管理
权限管理-页面-用户管理
公众服务登录
公众服务-页面-审核发布
公众服务-页面-自动发布
公众服务-页面-媒体警情
公众服务-页面-设置管理
公众服务-页面-统计分析
公众服务-页面-信息类型管理
公众服务-页面-信息接口管理
公众服务-页面-互联网系统授权
公众服务-页面-定时播报管理
公众服务-页面-日志管理
公众服务-页面-一路护航身份管理
公众服务-页面-文案模版管理
公众服务-操作-信息编辑
公众服务-操作-信息审核
公众服务-操作-媒介警情处置
警情处置登录
警情处置-页面-自定义区域
警情处置-页面-配置管理
警情处置-页面-警情处置
警情处置-页面-警情查询
警情处置-页面-统计分析
警情处置-操作-警情处置
警情处置-操作-消息通知按钮
重点车辆登录
重点车辆-页面-实时报警
重点车辆-页面-事件查询
重点车辆-页面-规律分析
重点车辆-页面-参数配置
数据魔方登录
数据监控登录
云资源运维平台登录
""",
u"全域数据管理角色": u"""
datav-全市域
datav-市区
datav-主城区据
datav-上城
datav-下城
datav-西湖
datav-江干
datav-拱墅
datav-滨江
datav-下沙
datav-高架
datav-绕城
datav-景区
datav-大江东
datav-萧山
datav-余杭
datav-富阳
datav-临安
datav-桐庐
datav-淳安
datav-建德
upps-全市域
upps-市区
upps-主城区据
upps-上城
upps-下城
upps-西湖
upps-江干
upps-拱墅
upps-滨江
upps-下沙
upps-高架
upps-绕城
upps-景区
upps-大江东
upps-萧山
upps-余杭
upps-富阳
upps-临安
upps-桐庐
upps-淳安
upps-建德
evt-全市域
evt-指挥中心
evt-信号配时中心
evt-上城
evt-下城
evt-西湖
evt-江干
evt-拱墅
evt-滨江
evt-下沙
evt-高架
evt-绕城
evt-景区
evt-大江东
evt-萧山
evt-余杭
evt-富阳
evt-临安
evt-桐庐
evt-淳安
evt-建德
ver-主城区据
ver-上城
ver-下城
ver-西湖
ver-江干
ver-拱墅
ver-滨江
ver-下沙
ver-景区
"""

}


defaultEmptyRoles = u"""
支队领导
办公室
指挥中心
政治处
警务督察处
警务保障处
道路秩序处
事故对策处
法制处
科技化信息处
车管处
宣传处
上城大队
下城大队
西湖大队
江干大队
拱墅大队
滨江大队
下沙大队
高架大队
绕城大队
景区大队
大江东大队
萧山大队
余杭大队
富阳大队
临安大队
桐庐大队
淳安大队
建德大队
"""

roleCodeRelationRaw = u"""
支队领导 330100000000 
办公室 330100001200
道路秩序处 330100000100
事故对策处 330100000300
车管处 330100000400
政治处 330100000600
宣传处 330100000700
法制处 330100000800
科技化信息处 330100000900
警务督察处 330100001300
警务保障处 330100001400
指挥中心 330100001500
上城大队 330102000000
下城大队 330103000000
江干大队 330104000000
拱墅大队 330105000000
西湖大队 330106000000
滨江大队 330108000000
萧山大队 330109000000
余杭大队 330110000000
桐庐大队 330122000000
淳安大队 330127000000
建德大队 330182000000
富阳大队 330183000000
临安大队 330185000000
大江东大队 330186000000
绕城大队 330196000000
景区大队 330197000000
下沙大队 330198000000
高架大队 330199000000
"""

daduiRole = u"""态势大屏登录
态势大屏-其他-详细信息
公众服务登录
公众服务-页面-审核发布
公众服务-页面-自动发布
公众服务-页面-媒体警情
公众服务-操作-信息编辑
警情处置登录
警情处置-页面-自定义区域
警情处置-页面-警情处置
警情处置-页面-警情查询
警情处置-页面-统计分析
警情处置-操作-警情处置
警情处置-操作-消息通知按钮
重点车辆登录
重点车辆-页面-实时报警
重点车辆-页面-事件查询
重点车辆-页面-规律分析"""

roleCodeRelation = {}
for tmp in roleCodeRelationRaw.strip().split("\n"):
    stmp = tmp.split(" ")
    roleCodeRelation[stmp[0]] = stmp[1]

defauleRolePermLimit = {
u"支队领导" :u"""
态势大屏登录
态势大屏-其他-详细信息
公众服务登录
公众服务-页面-审核发布
公众服务-页面-自动发布
公众服务-页面-媒体警情
警情处置登录
警情处置-页面-自定义区域
警情处置-页面-警情处置
警情处置-页面-警情查询
警情处置-页面-统计分析
重点车辆登录
重点车辆-页面-事件查询
重点车辆-页面-规律分析
数据魔方登录
数据监控登录
云资源运维平台登录
""",
u"办公室" :u"""
态势大屏登录
态势大屏-其他-详细信息
""",
u"指挥中心" :u"""
态势大屏登录
态势大屏-其他-详细信息
公众服务登录
公众服务-页面-审核发布
公众服务-页面-自动发布
公众服务-页面-媒体警情
公众服务-页面-设置管理
公众服务-页面-统计分析
公众服务-页面-信息类型管理
公众服务-页面-信息接口管理
公众服务-页面-互联网系统授权
公众服务-页面-定时播报管理
公众服务-页面-日志管理
公众服务-页面-一路护航身份管理
公众服务-页面-文案模版管理
公众服务-操作-信息编辑
公众服务-操作-媒介警情处置
警情处置登录
警情处置-页面-自定义区域
警情处置-页面-配置管理
警情处置-页面-警情处置
警情处置-页面-警情查询
警情处置-页面-统计分析
警情处置-操作-警情处置
警情处置-操作-消息通知按钮
重点车辆登录
重点车辆-页面-实时报警
重点车辆-页面-事件查询
重点车辆-页面-规律分析
""",
u"政治处" :u"""
态势大屏登录
态势大屏-其他-详细信息
""",
u"警务督察处" :u"""
态势大屏登录
态势大屏-其他-详细信息
""",
u"警务保障处" :u"""
态势大屏登录
态势大屏-其他-详细信息
""",
u"道路秩序处" :u"""
态势大屏登录
态势大屏-其他-详细信息
公众服务登录
公众服务-页面-审核发布
公众服务-页面-自动发布
公众服务-页面-媒体警情
公众服务-操作-信息编辑
警情处置登录
警情处置-页面-自定义区域
警情处置-页面-配置管理
警情处置-页面-警情处置
警情处置-页面-警情查询
警情处置-页面-统计分析
警情处置-操作-警情处置
警情处置-操作-消息通知按钮
重点车辆登录
重点车辆-页面-实时报警
重点车辆-页面-事件查询
重点车辆-页面-规律分析
""",
u"事故对策处" :u"""
态势大屏登录
态势大屏-其他-详细信息
警情处置登录
警情处置-页面-自定义区域
警情处置-页面-配置管理
警情处置-页面-警情处置
警情处置-页面-警情查询
警情处置-页面-统计分析
重点车辆登录
重点车辆-页面-实时报警
重点车辆-页面-事件查询
重点车辆-页面-规律分析
""",
u"法制处" :u"""
态势大屏登录
态势大屏-其他-详细信息
重点车辆登录
重点车辆-页面-实时报警
重点车辆-页面-事件查询
重点车辆-页面-规律分析
""",
u"车管处" :u"""
态势大屏登录
态势大屏-其他-详细信息
重点车辆登录
重点车辆-页面-实时报警
重点车辆-页面-事件查询
重点车辆-页面-规律分析
"""
    }
