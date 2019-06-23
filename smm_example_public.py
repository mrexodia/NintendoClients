from nintendo.nex import backend, authentication, ranking, datastore, datastoresmm, common
from nintendo.games import SMM
from nintendo import account
import requests
import hashlib
import struct

import logging
logging.basicConfig(level=logging.DEBUG)

#Device id can be retrieved with a call to MCP_GetDeviceId on the Wii U
#Serial number can be found on the back of the Wii U
DEVICE_ID = ...
SERIAL_NUMBER = ...
SYSTEM_VERSION = ...
REGION = ...
COUNTRY = ...
DEVICE_CERT = ...

USERNAME = ... #Nintendo network id
plain_password = ...
pid = ...
data = struct.pack("<I", pid) + b"\x02\x65\x43\x46" + plain_password.encode("ascii")
PASSWORD = hashlib.sha256(data).digest().hex()

SYSTEM_TITLE_ID = 0x0005001010040200
#SYSTEM_UNIQUE_ID = 0x402
SYSTEM_APPLICATION_VERSION = 0xC4

api = account.AccountAPI()
api.set_device(DEVICE_ID, SERIAL_NUMBER, SYSTEM_VERSION, REGION, COUNTRY, DEVICE_CERT)
api.set_title(SYSTEM_TITLE_ID, SYSTEM_APPLICATION_VERSION)
api.login(USERNAME, PASSWORD, hash=True)

SMM_TITLE_ID = 0x000500001018DD00
SMM_VERSION = 0x110
SMM_GAME_SERVER_ID = 0x1018DB00

api.set_title(SMM_TITLE_ID, SMM_VERSION)
nex_token_smm = api.get_nex_token(SMM_GAME_SERVER_ID)

backendclient = backend.BackEndClient(SMM.ACCESS_KEY, SMM.NEX_VERSION)
backendclient.connect(nex_token_smm.host, nex_token_smm.port)

auth_info = authentication.AuthenticationInfo()
auth_info.token = nex_token_smm.token
auth_info.server_version = SMM.SERVER_VERSION

backendclient.login(nex_token_smm.username, nex_token_smm.password, auth_info, None)

client = datastoresmm.DataStoreSmmClient(backendclient.secure_client)

courseids = [
    65620908,
    65620917,
    65457532,
    65320977,
    65498934,
    65359084,
    65320972,
    65403280,
    65031806,
    65313929,
    65335952,
    65566924,
    65591832,
    64984758,
    65509915,
    65737778,
    64818299,
    65299472,
    65476794,
    64818295,
    64736583,
    64110419,
    64287571,
    65231410,
    63218115,
    65151623,
    65150467,
    65498928,
    65670447,
    64641559,
    65556905,
    65335948,
    65461379,
    65165020,
    63238749,
    65108642,
    64277352,
    65269274,
    64287557,
    64641555,
    64742271,
    64110413,
    65515653,
    64756444,
    64033060,
    64985820,
    65682717,
    63612433,
    63030649,
    64731452,
    65296748,
    65186506,
    65269291,
    64558715,
    65155869,
    28268626,
    61518443,
    64939673,
    60038102,
    65369347,
    65582711,
    65615211,
    65646455,
    64822966,
    65514085,
    65623593,
    65605875,
    65494207,
    35681763,
    65634622,
    64412356,
    65659805,
    52668374,
    64603129,
    64504220,
    65449816,
    65127115,
    62978544,
    64883297,
    35302598,
    65653287,
    64756461,
    63496175,
    65477979,
    65385731,
    65193317,
    65336638,
    65388518,
    63824721,
    65620631,
    65250618,
    63816108,
    65695556,
    65314602,
    64162478,
    65173605,
    65239681,
    65579866,
    64704670,
    65446452,
    63580552,
    65740999,
    65188834,
    63164526,
    65600285,
    65669719,
    62438376,
    63738500,
    64883444,
    64882777,
    64882443,
    65365388,
    65492521,
    65270655,
    63783697,
    65097400,
    63905625,
    65439404,
    64882961,
    62735901,
    64883469,
    64882422,
    64651714,
    64883537,
    64882434,
    61778354,
    64883314,
    65176844,
    64019917,
    65130688,
    64882756,
    21340114,
    61914308,
    64883367,
    63767091,
    64721236,
    64883516,
    65488476,
    58730112,
    64927424,
    63463114,
    53773848,
    63135977,
    63942447,
    65369069,
    63589544,
    64448845,
    61184308,
    60710981,
    60700333,
    58990905,
    59598949,
    59777640,
    59390756,
    64468989,
    60710955,
    64195238,
    60700346,
    64769937,
    64600158,
    60700289,
    65668444,
    65330174,
    60700339,
    60700351,
    59806818,
    65174820,
    64026169,
    61765392,
    63466475,
    63413462,
    63033398,
    64882966,
    60700329,
    60027494,
    64882988,
    59936357,
    65277057,
    64244184,
    59470046,
    64973969,
    63703860,
    63767073,
    64883442,
    63628928,
    54204638,
    59516847,
    64576281,
    64882885,
    65285524,
    65512567,
    63703201,
    63265973,
    63531898,
    60994097,
    64882740,
    63850591,
    65177098,
    64314946,
    63119899,

    64796618,
    49695667,
    28119175,
    2102808,
    3866296,
    44749176,
    43512485,
    38335933,
    32687002,
    6818589,
    54260699,
    12343975,
    12499078,
    11929021,
    14447983,
    29671550,
    65504125,
    43675498,
    55821900,
    3776669,
    54423439,
    57942629,
    21978868,
    53604070,
    34656348,
    34167531,
    4426626,
    57848250,
    59692947,
    13216490,
    10758639,
    9251468,
    6522051,
    53888266,
    52021457,
    6241058,
    52195690,
    21620316,
    7675467,
    25747081,
    63912035,
    25464845,
    30489825,
    38271970,
    5176861,
    19595780,
    5236596,
    5478370,
    40908729,
    47116716,
]


def save_stream(outfile, func):
    settings = backend.Settings("default.cfg")
    settings.set("nex.access_key", SMM.ACCESS_KEY)
    settings.set("nex.version", SMM.NEX_VERSION)
    settings.set("prudp.silence_timeout", 10.0)
    stream = common.streams.StreamOut(settings)
    func(stream)
    f = open(outfile, "wb")
    f.write(stream.get())
    f.close()


def make_metaparam(miipid):
    param = datastoresmm.DataStoreGetMetaParam()
    param.data_id = 0
    param.persistence_target = datastoresmm.PersistenceTarget()
    param.persistence_target.owner_id = miipid
    param.persistence_target.persistence_id = 0
    param.access_password = 0
    param.result_option = 4
    return param


final_courseurls = []

i = 0
while i < len(courseids):
    courseparam = datastoresmm.MethodParam50()
    courseparam.magic = 0
    courseparam.unk = 0x27
    courseparam.data_ids = []
    for j in range(0, min(len(courseids) - i, 50)):
        courseparam.data_ids.append(courseids[i + j])
    courseresponse = client.method50(courseparam)
    coursedatas, courseresults = courseresponse.infos, courseresponse.results
    save_stream("coursedatas{}.bin".format(i), lambda s: s.list(coursedatas, s.add))

    miiparams = []
    coursedata: datastoresmm.DataStoreInfoStuff
    for coursedata in coursedatas:
        miiparams.append(make_metaparam(coursedata.info.owner_id))

    miiresponse = client.get_metas_multiple_param(miiparams)
    miidatas, miiresults = miiresponse.infos, miiresponse.results
    save_stream("miidatas{}.bin".format(i), lambda s: s.list(miidatas, s.add))

    smm_miiparam = datastoresmm.MethodParam50()
    smm_miiparam.magic = 0x11E1A300
    smm_miiparam.unk = 0x27
    smm_miiparam.data_ids = []
    miidata: datastoresmm.DataStoreMetaInfo
    for miidata in miidatas:
        smm_miiparam.data_ids.append(miidata.data_id)

    smm_miiresponse = client.method50(smm_miiparam)
    smm_miidatas, smm_miiresults = smm_miiresponse.infos, smm_miiresponse.results
    save_stream("smm_miidatas{}.bin".format(i), lambda s: s.list(smm_miidatas, s.add))

    for coursedata in coursedatas:
        req_param = datastoresmm.DataStorePrepareGetParam()
        req_param.data_id = coursedata.info.data_id
        req_param.lock_id = 0
        req_param.persistence_target = datastoresmm.PersistenceTarget()
        req_param.persistence_target.owner_id = 0
        req_param.persistence_target.persistence_id = 0xFFFF
        req_param.access_password = 0
        req_param.extra_data = ["WUP", "4", "EUR", "97", "PL", ""]
        req_info: datastoresmm.DataStoreReqGetInfo
        req_info = client.prepare_get_object(req_param)
        final_courseurls.append(req_info.url)

        rankingparam = datastoresmm.UnknownStruct2()
        rankingparam.data_id = coursedata.info.data_id
        rankingparam.unk2 = 0
        rankingdata: datastoresmm.CourseRecordInfo
        rankingdata = client.method72(rankingparam)
        save_stream("ranking{}.bin".format(coursedata.info.data_id), lambda s: s.add(rankingdata))

        best_miiparams = [make_metaparam(rankingdata.world_record_pid), make_metaparam(rankingdata.first_clear_pid)]
        best_miiresponse = client.get_metas_multiple_param(best_miiparams)
        best_miis, best_results = best_miiresponse.infos, best_miiresponse.results
        save_stream("best_miidatas{}.bin".format(coursedata.info.data_id), lambda s: s.list(best_miis, s.add))

        smm_miiparam = datastoresmm.MethodParam50()
        smm_miiparam.magic = 0x11E1A300
        smm_miiparam.unk = 0x27
        smm_miiparam.data_ids = []
        miidata: datastoresmm.DataStoreMetaInfo
        for miidata in best_miis:
            smm_miiparam.data_ids.append(miidata.data_id)

        best_smm_miiresponse = client.method50(smm_miiparam)
        best_smm_miidatas, best_smm_miiresults = best_smm_miiresponse.infos, best_smm_miiresponse.results
        save_stream("best_smm_miidatas{}.bin".format(coursedata.info.data_id), lambda s: s.list(best_smm_miidatas, s.add))

        unkparam = datastoresmm.UnknownStruct4()
        unkparam.unk1 = coursedata.info.data_id
        unkparam.unk2 = 3
        unkdatas = client.method54(unkparam)
        save_stream("unkdatas{}.bin".format(coursedata.info.data_id), lambda s: s.list(unkdatas, s.qbuffer))

    i += 50

f = open("final_courseurls.txt", "wb")
for url in final_courseurls:
    f.write(url.encode("utf8"))
    f.write(b"\n")
f.close()

backendclient.close() 