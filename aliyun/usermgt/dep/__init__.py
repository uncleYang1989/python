#!/usr/bin/python
# encoding=utf8
# from createDefaultPerms import importPerms as importPerms
# from createDefaultRoles import importRoles as importRoles
# from createOrgTree import installOrgs as installOrgs
# from createDefaultUsers import importUser as importUser
# if __name__ == "__main__":
#     l = """
# adm_focusvhc_alarm_content_rt
# adm_focusvhc_alarm_vhccontent_rt"
# adm_alarm_rule_message
# adm_focusvhc_suspect_construction_site
# adm_focusvhc_alarm_vhccontent_rt_sh
# adm_focusvhc_alarm_inter_turnright_vhcflow_rt
# adm_focusvhc_rdseg_30mi_vhcflow_rt
# dwd_tfc_opt_vhc_fakeplate_vhc_rt
# adm_focusvhc_machineshop_truck_info"
# adm_focusvhc_alarm_inter_turnright_vhcflow_rt
# adm_focusvhc_rdseg_30mi_vhcflow_rt
# adm_focusvhc_suspect_construction_site
# adm_focusvhc_trespass_rt 
# adm_focusvhc_fatigue_rt 
# adm_focusvhc_exceed_speed_rt 
# dwd_tfc_opt_vhc_foreign_vhc_rt
# dwd_tfc_opt_vhc_gpsoffline_onroad_rt
# dwd_tfc_opt_vhc_fakeplate_vhc_rt
# adm_focusvhc_grid_5mi_alarmindex
# dws_tfc_vhc_truck_grid_travelvhcnum_rt
# dws_tfc_vhc_truck_grid_travelvhcnum_rt
# adm_focusvhc_alarm_vhccontent_rt_sh"
# dwd_tfc_gps_machineshop_truck_rt
# dwd_tfc_gps_machineshop_truck_rt
# dwd_tfc_gps_machineshop_truck_rt
# adm_focusvhc_trespass_rt
# adm_focusvhc_fatigue_rt
# adm_focusvhc_exceed_speed_rt
# dwd_tfc_opt_vhc_foreign_vhc_rt
# dwd_tfc_opt_vhc_gpsoffline_onroad_rt
# dwd_tfc_opt_vhc_fakeplate_vhc_rt
# dwd_tfc_gps_machineshop_truck_rt
# dwd_tfc_bas_rdnet_link_info
# dwd_tfc_bas_rdnet_inter_info
# adm_focusvhc_suspect_construction_site
# 
# adm_focusvhc_rdseg_vhcflow_d
# adm_focusvhc_rdseg_30mi_vhcflow_rt
# adm_focusvhc_inter_turnright_vhcflow_d
# adm_focusvhc_alarm_inter_turnright_vhcflow_rt
# adm_focusvhc_construction_vhcindex
# dwd_tfc_bas_vhc_info"
# 
# adm_focusvhc_alarm_inter_turnright_vhcflow_rt
# dwd_tfc_bas_rdnet_inter_info"
# adm_focusvhc_rdseg_30mi_vhcflow_rt
# dwd_tfc_bas_vhc_info
# dwd_tfc_ctl_vhc_permit_rt"
# adm_focusvhc_alarm_content_rt
# adm_focusvhc_alarm_vhccontent_rt"
# adm_focusvhc_alarm_content_rt
# adm_focusvhc_alarm_vhccontent_rt
# adm_focusvhc_machineshop_truck_info
# adm_focusvhc_suspect_construction_site"
# adm_focusvhc_alarm_content_rt
# adm_focusvhc_alarm_content_rt
# adm_focusvhc_suspect_construction_site
# adm_focusvhc_alarm_vhccontent_rt
# adm_focusvhc_alarm_vhccontent_rt
# adm_focusvhc_alarm_vhccontent_rt
# adm_focusvhc_alarm_vhccontent_rt
# adm_focusvhc_alarm_vhccontent_rt
# adm_focusvhc_alarm_vhccontent_rt
# adm_focusvhc_grid_5mi_alarmindex
# 
# dwd_tfc_opt_trace_vhc_d
# dwd_tfc_opt_trace_vhc_d
# adm_focusvhc_trespass_rt
# adm_focusvhc_fatigue_rt
# adm_focusvhc_exceed_speed_rt
# dwd_tfc_opt_vhc_foreign_vhc_rt
# dwd_tfc_opt_vhc_gpsoffline_onroad_rt
# dwd_tfc_opt_vhc_fakeplate_vhc_rt
# dwd_tfc_opt_trace_vhc_d
# dwd_tfc_bas_rdnet_link_info
# dwd_tfc_bas_rdnet_inter_info
# adm_focusvhc_suspect_construction_site
# 
# adm_focusvhc_rdseg_vhcflow_d
# adm_focusvhc_rdseg_30mi_vhcflow_rt
# adm_focusvhc_inter_turnright_vhcflow_d
# adm_focusvhc_alarm_inter_turnright_vhcflow_rt
# adm_focusvhc_construction_vhcindex
# dwd_tfc_bas_vhc_info"
# adm_focusvhc_alarm_inter_turnright_vhcflow_rt
# dwd_tfc_bas_rdnet_inter_info"
# adm_focusvhc_rdseg_30mi_vhcflow_rt
# dwd_tfc_bas_vhc_info
# dwd_tfc_ctl_vhc_permit_rt"
# dws_tfc_vhc_udgrid_d_vhcnum_d
# adm_focusvhc_gridalarmtype_alarmnum_d
# adm_focusvhc_gridalarmtype_alarmnum_d
# adm_focusvhc_rdseg_alarmnum_d
# adm_focusvhc_machineshop_truck_info
# dws_tfc_vhc_enterprise_d_onofflinevhcnum_d
# adm_focusvhc_vhc_enterprise_illegalnum_d
# adm_focusvhc_vhc_enterprise_alarmnum_d
# adm_focusvhc_vhc_enterprise_accident_d"
# 
#     """.replace("，" "、").lower();
#     
#     # print len(l.split("\n"))
#     result = []
#     for line in l.split("\n"):
#         tmps  = line.split("、");
#         for tmp in tmps:
#             if tmp:
#                 result.append(tmp);
#         
#     # print len(result)'''
#     # print len(set(result))'''
#     print len(result)
#     print len(sorted(set(result)))
#     for i in sorted(set(result)):
#         if i.startswith("dwd"):
#             print "RDS:dwd_330100:".lower() + i
#         elif i.startswith("dws"):
#             print "RDS:dws_330100:".lower() + i
#         elif i.startswith("adm"):
#             print "RDS:adm_330100:".lower() + i
a = """
    'getOnwayCar'
    'getCongestIndex' 
    'getDelayIndex'
    'getArterialSpeed'
    'getExpressSpeed'
    'getHighwaySpeed'
    'getSafeIndex'
    'getAroundHighwaySpeed'

    'getSituation'
    'getTrafficCountOnway'
    'getTrafficCountRemain'
    'getTrafficCountStore'
    'getTrafficCountOut'
    'getTrafficCountOnwaySort'
    'getTrafficCountCarType'
    'getTrafficForecast'
    'getTrafficCountIn'
    'getTeamHealth'
    'getFocusAttentionOut'
    'getFocusAttention'
    'getCommuteGridInfo'
    'getCommuteRoute'
    
    'getSituationManageInfo'
    'getEnforcementHeadInfo'
    'getEnforcementInfo'
    'getDutyStaff'
    'getPublicTravel'
    'getPublicService'
    'getSafeControl'
    
    
    'getBannerInfo'
    'getWeather'
    
    'getOnwayWarn'
    'getCongestindexWarn'
    'getSpeedWarn'
    'getSafeIndexWarn'

    'getEmergencyRaocheng'
    'getLinkFeature'
    'getMachineInspection'

    """
for s in a.strip().split("\n"):
    if s.strip():
        s = s + ":{'opt':{},'func':[]},"
    print s;
    
    
    
    async (req, data) => {
  let reqApi = req.query.reqApi;
  const lineChat = "YQfixedLineChat";
  const rule = {
    //生命体征
    'getOnwayCar': [lineChat],
    'getCongestIndex': [lineChat],
    'getDelayIndex': [lineChat],
    'getArterialSpeed': [lineChat],
    'getExpressSpeed': [lineChat],
    'getHighwaySpeed': [lineChat],
    'getSafeIndex': [lineChat],
    'getAroundHighwaySpeed': [lineChat],

    //左侧列表
    'getSituation': [],
    'getTrafficCountOnway': [lineChat],
    'getTrafficCountRemain': [lineChat],
    'getTrafficCountStore': [lineChat],
    'getTrafficCountOut': [lineChat],
    'getTrafficCountOnwaySort': [],
    'getTrafficCountCarType': [],
    'getTrafficForecast': [],
    'getTrafficCountIn': [lineChat],
    'getTeamHealth': [],
    'getFocusAttentionOut': [],
    'getFocusAttention': [],
    'getCommuteGridInfo': [],
    'getCommuteRoute': [],

    //右侧列表
    'getSituationManageInfo': [],
    'getEnforcementHeadInfo': [],
    'getEnforcementInfo': [],
    'getDutyStaff': [],
    'getPublicTravel': [],
    'getPublicService': [],
    'getSafeControl': [],

    //地图旗帜
    'getBannerInfo': [],

    //右上角天气
    'getWeather': [],

    //底部报警
    'getOnwayWarn': [],
    'getCongestindexWarn': [],
    'getSpeedWarn': [],
    'getSafeIndexWarn': [],

    //绕城专属
    'getEmergencyRaocheng': [],
    'getLinkFeature': [],
    'getMachineInspection': [],
  }
  return rule[reqApi];
}