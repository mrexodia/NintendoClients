from nintendo.nex import backend, service, kerberos, \
    authentication, secure, datastoresmm, common

import base64


def read_file(file):
    f = open(file, "rb")
    data = f.read()
    f.close()
    return data


smm_mario100 = read_file("smm_mario100.bin")
smm_miidata = read_file("smm_miidata.bin")
# hardcoded mii 1781058687
miidata2 = base64.b64decode("""AB4CAAAAAAAAAAAAAAARAgAAYacvAgAAAAB/zChqAAAAAAkAaXdoczEwODQAAQCM
AEJQRkMAAAABAAAAAAAAAAAAAAAAAAEAAAMAADBaxrslIMRw8JQm6C+4rm7VkAQA
AAAAXzBLMGgwAAAAAAAAAAAAAAAAAABHNwAAIQECZKQYIEVGFIESF2gNAAApAlFI
UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC/7gAAAAAAAAAAAAAAAAAAAAAAAAAAAAUA
AAAAAAAAAAAFAAAAAwAAAAAnjDqBHwAAACeMOoEfAAAAWgAAAAAAAAAAAAAAAQAA
J4w6gR8AAAAAAD4/nAAAAAEAAAACADEACQAAAAAaAAAAAAAUAAAAuQoAAAAAAAC5
CgAAAAAAAAAAAAAAGgAAAAEAFAAAAEsGAAAAAAAASwYAAAAAAAAAAAAAABoAAAAC
ABQAAAADAwAAAAAAAAMDAAAAAAAAAAAAAAAaAAAAAwAUAAAA4SAAAAAAAAC5CgAA
AAAAAAAAAAAAGgAAAAQAFAAAAJYaAAAAAAAAuQoAAAAAAAAAAAAAABoAAAAFABQA
AAAhAAAAAAAAACEAAAAAAAAAAAAAAAAaAAAABgAUAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAGgAAAAcAFAAAABoAAAAAAAAAGgAAAAAAAAAAAAAAABoAAAAIABQAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAA==""")
smm_coursedata = read_file("smm_coursedata.bin")
smm_unkdata = read_file("smm_unkdata.bin")
smm_rankings = read_file("smm_rankings.bin")


class SmmDataProvider:
    def __init__(self, settings):
        self.settings = settings
        self.mario100 = self.init_mario100_data()
        self.mii_data_id, self.mii_data_pid = self.init_mii_data()
        self.course_data = self.init_course_data()
        self.unkdata = self.init_unkdata()
        self.rankings = self.init_rankings()

    def init_mario100_data(self):
        global smm_mario100
        stream = common.streams.StreamIn(smm_mario100, self.settings)
        return stream.list(datastoresmm.DataStoreInfoStuff)

    def init_mii_data(self):
        global smm_miidata
        global miidata2
        stream = common.streams.StreamIn(smm_miidata, self.settings)
        infos = stream.list(datastoresmm.DataStoreInfoStuff)
        stream = common.streams.StreamIn(miidata2, self.settings)
        stuff = stream.extract(datastoresmm.DataStoreInfoStuff)
        infos.append(stuff)
        mii_data_id, mii_data_pid = {}, {}

        info: datastoresmm.DataStoreInfoStuff
        for info in infos:
            mii_data_id[info.info.data_id] = info
            mii_data_pid[info.info.owner_id] = info.info.data_id
        return mii_data_id, mii_data_pid

    def init_course_data(self):
        global smm_coursedata
        stream = common.streams.StreamIn(smm_coursedata, self.settings)
        infos = stream.list(datastoresmm.DataStoreInfoStuff)
        course_data = {}
        info: datastoresmm.DataStoreInfoStuff
        for info in infos:
            if info.info.data_id == 21340114:
                continue
            course_data[info.info.data_id] = info
        return course_data

    def init_unkdata(self):
        global smm_unkdata
        stream = common.streams.StreamIn(smm_unkdata, self.settings)
        count = stream.u32()
        unkdata = {}
        for i in range(0, count):
            data_id = stream.u64()
            buffers = stream.list(stream.qbuffer)
            unkdata[data_id] = buffers
        return unkdata

    def init_rankings(self):
        global smm_rankings
        stream = common.streams.StreamIn(smm_rankings, self.settings)
        rankings = {}
        infos = stream.list(datastoresmm.CourseRecordInfo)
        ranking: datastoresmm.CourseRecordInfo
        for ranking in infos:
            rankings[ranking.data_id] = ranking
        return rankings

    def get_mario100_data(self):
        return self.mario100

    def get_mii_data_pid(self, pid):
        if pid in self.mii_data_pid:
            return self.mii_data_id[self.mii_data_pid[pid]]
        return None

    def get_mii_data_id(self, data_id):
        if data_id in self.mii_data_id:
            return self.mii_data_id[data_id]
        return None

    def get_course_data(self, data_id):
        if data_id in self.course_data:
            return self.course_data[data_id]
        return None

    def get_unkdata(self, data_id):
        if data_id in self.unkdata:
            return self.unkdata[data_id]
        return None

    def get_ranking(self, data_id):
        if data_id in self.rankings:
            return self.rankings[data_id]
        return None
