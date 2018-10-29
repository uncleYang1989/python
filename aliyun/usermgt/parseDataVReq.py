#!/usr/bin/python
# encoding=utf8
# ss = """
# mber&enforcement_type=enf_1&commuteType=am    getArterialSpeed?grid_id=6301f9905d6ffa1412ac94c82…type=number&enforcement_type=enf_1&commuteType=am    getPublicService?grid_id=6301f9905d6ffa1412ac94c82…type=number&enforcement_type=enf_1&commuteType=am    getPublicTravel?grid_id=6301f9905d6ffa1412ac94c82a…type=number&enforcement_type=enf_1&commuteType=am    getSituationManage?grid_id=6301f9905d6ffa1412ac94c…type=number&enforcement_type=enf_1&commuteType=am    getDutyStaff?grid_id=6301f9905d6ffa1412ac94c82a6e7…type=number&enforcement_type=enf_1&commuteType=am    getMachineInspection?grid_id=6301f9905d6ffa1412ac9…type=number&enforcement_type=enf_1&commuteType=am    getTrafficCountOut?grid_id=6301f9905d6ffa1412ac94c…type=number&enforcement_type=enf_1&commuteType=am    getTrafficCountIn?grid_id=6301f9905d6ffa1412ac94c8…type=number&enforcement_type=enf_1&commuteType=am    getTrafficCountStore?grid_id=6301f9905d6ffa1412ac9…type=number&enforcement_type=enf_1&commuteType=am    getCongestindexWarn?grid_id=6301f9905d6ffa1412ac94…type=number&enforcement_type=enf_1&commuteType=am    getSpeedWarn?grid_id=6301f9905d6ffa1412ac94c82a6e7…type=number&enforcement_type=enf_1&commuteType=am    getSafeIndexWarn?grid_id=6301f9905d6ffa1412ac94c82…type=number&enforcement_type=enf_1&commuteType=am    getEnforcementInfo?grid_id=6301f9905d6ffa1412ac94c…ot_typ=congestion&head_type=number&commuteType=am    getSituationManageInfo?grid_id=6301f9905d6ffa1412a…type=number&enforcement_type=enf_1&commuteType=am    getTrafficCountOnway?grid_id=6301f9905d6ffa1412ac9…type=number&enforcement_type=enf_1&commuteType
# e=enf_1&commuteType=am    getCongestIndex?grid_id=6301f9905d6ffa1412ac94c82a…type=number&enforcement_type=enf_1&commuteType=am    getDelayIndex?grid_id=6301f9905d6ffa1412ac94c82a6e…type=number&enforcement_type=enf_1&commuteType=am    getArterialSpeed?grid_id=6301f9905d6ffa1412ac94c82…type=number&enforcement_type=enf_1&commuteType=am    getExpressSpeed?grid_id=6301f9905d6ffa1412ac94c82a…type=number&enforcement_type=enf_1&commuteType=am    getHighwaySpeed?grid_id=6301f9905d6ffa1412ac94c82a…type=number&enforcement_type=enf_1&commuteType=am    getSafeIndex?grid_id=6301f9905d6ffa1412ac94c82a6e7…type=number&enforcement_type=enf_1&commuteType=am    getBannerInfo?grid_id=6301f9905d6ffa1412ac94c82a6e…type=number&enforcement_type=enf_1&commuteType=am    getSituation?grid_id=6301f9905d6ffa1412ac94c82a6e7…type=number&enforcement_type=enf_1&commuteType=am    getTrafficCount?grid_id=6301f9905d6ffa1412ac94c82a…type=number&enforcement_type=enf_1&commuteType=am    getTeamHealth?grid_id=6301f9905d6ffa1412ac94c82a6e…type=number&enforcement_type=enf_1&commuteType=am    getFocusAttentionOut?grid_id=6301f9905d6ffa1412ac9…type=number&enforcement_type=enf_1&commuteType=am
# teType=am    getAllBannerInfo?token=123&grid_id=6301f9905d6ffa1…type=number&enforcement_type=enf_1&commuteType=am    getSituationManageInfo?grid_id=6301f9905d6ffa1412a…type=number&enforcement_type=enf_1&commuteType=am    getCongestIndex?grid_id=6301f9905d6ffa1412ac94c82a…type=number&enforcement_type=enf_1&commuteType=am    getEnforcementHeadInfo?grid_id=6301f9905d6ffa1412a…type=number&enforcement_type=enf_1&commuteType=am    getSafeControl?grid_id=6301f9905d6ffa1412ac94c82a6…type=number&enforcement_type=enf_1&commuteType=am    getCommuteGridInfo?grid_id=6301f9905d6ffa1412ac94c…type=number&enforcement_type=enf_1&commuteType=am    getWeather?grid_id=6301f9905d6ffa1412ac94c82a6e79a…type=number&enforcement_type=enf_1&commuteType=am    getCommuteGridInfo?grid_id=6301f9905d6ffa1412ac94c…ongestion&head_type=number&enforcement_type=enf_1    getTrafficCountRemain?grid_id=6301f9905d6ffa1412ac…type=number&enforcement_type=enf_1&commuteType=am    getTrafficForecast?grid_id=6301f9905d6ffa1412ac94c…type=number&enforcement_type=enf_1&commuteType=am    getOnwayCar?grid_id=6301f9905d6ffa1412ac94c82a6e79…type=number&enforcement_type=enf_1&commuteType=am    
#     """.strip().split("\n")
# reqs = []
# for s in ss:
#     tmp = s.split("    ")
#     reqs.extend(tmp)
# newReqs = []
# for req in reqs:
#     newReqs.append(req.split("?")[0])
#     
# for req in sorted(set(newReqs)):
#     print req
# # print set(newReqs)
# print len(set(newReqs))

sss = """
getAllBannerInfo
getArterialSpeed
getBannerInfo
getCommuteGridInfo
getCongestIndex
getCongestindexWarn
getDelayIndex
getDutyStaff
getEnforcementHeadInfo
getExpressSpeed
getFocusAttentionOut
getHighwaySpeed
getMachineInspection
getOnwayCar
getPublicService
getPublicTravel
getSafeControl
getSafeIndex
getSafeIndexWarn
getSituation
getSituationManage
getSpeedWarn
getTeamHealth
getTrafficCount
getTrafficCountIn
getTrafficCountOnway
getTrafficCountOut
getTrafficCountRemain
getTrafficCountStore
getTrafficForecast
getWeather
getAllBannerInfo
getArterialSpeed
getBannerInfo
getCommuteGridInfo
getCongestindexWarn
getDutyStaff
getEnforcementHeadInfo
getEnforcementInfo?enforcement_type=enf_1
getExpressSpeed
getFocusAttention
getFocusAttentionOut
getHighwaySpeed
getMachineInspection
getTrafficCountCarType
getTrafficCountIn
getTrafficCountOnwaySort
getTrafficCountOut
getTrafficCountStore
getTrafficCount
getTrafficCountOnway
getOnwayCar
getOnwayWarn
getPublicService
getPublicTravel
getSafeControl
getSafeIndex
getDelayIndex
getCongestIndex
getSafeIndexWarn
getSituation
getSituationManageInfo?situation_type=EVENT_GROUP_002
getSituationManageInfo?situation_type=EVENT_GROUP_003
getSituationManageInfo?situation_type=EVENT_GROUP_006
getSpeedWarn
getTeamHealth
getWeather
getLinkFeature
getEmergencyRaocheng
""".strip().split("\n")
for i in sorted(set(sss)):
    print i
