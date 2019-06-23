from nintendo.nex import backend, service, kerberos, \
    authentication, secure, datastoresmm, common
from nintendo.games import SMM

import glob
import ntpath

settings = backend.Settings("default.cfg")
settings.set("nex.access_key", SMM.ACCESS_KEY)
settings.set("nex.version", SMM.NEX_VERSION)
settings.set("prudp.silence_timeout", 10.0)

unkdata_files = glob.glob("./smm_scrape/unkdatas*.bin")
unkid = []
unkdata = []
for file in unkdata_files:
    f = open(file, "rb")
    data = f.read()
    f.close()
    stream = common.streams.StreamIn(data, settings)
    blub = stream.list(stream.qbuffer)
    bfile = ntpath.basename(file)
    id = int(bfile[8:-4])
    unkid.append(id)
    unkdata.append(blub)

unkstream = common.streams.StreamOut(settings)
unkstream.u32(len(unkdata))
for i in range(0, len(unkdata)):
    unkstream.u64(unkid[i])
    unkstream.list(unkdata[i], unkstream.qbuffer)

f = open("smm_unkdata.bin", "wb")
f.write(unkstream.get())
f.close()

smm_mii_files = glob.glob("./smm_scrape/*smm_miidatas*.bin")

smm_mii_infos = []

for file in smm_mii_files:
    f = open(file, "rb")
    stream = common.streams.StreamIn(f.read(), settings)
    infos = stream.list(datastoresmm.DataStoreInfoStuff)
    for info in infos:
        smm_mii_infos.append(info)
    f.close()

smm_mii_stream = common.streams.StreamOut(settings)
smm_mii_stream.list(smm_mii_infos, smm_mii_stream.add)
f = open("smm_miidata.bin", "wb")
f.write(smm_mii_stream.get())
f.close()

course_files = glob.glob("./smm_scrape/coursedatas*.bin")
course_infos = []
for file in course_files:
    f = open(file, "rb")
    stream = common.streams.StreamIn(f.read(), settings)
    infos = stream.list(datastoresmm.DataStoreInfoStuff)
    for info in infos:
        course_infos.append(info)
    f.close()

coursedata_stream = common.streams.StreamOut(settings)
coursedata_stream.list(course_infos, coursedata_stream.add)
f = open("smm_coursedata.bin", "wb")
f.write(coursedata_stream.get())
f.close()

ranking_files = glob.glob("./smm_scrape/ranking*.bin")
rankings = []
for file in ranking_files:
    f = open(file, "rb")
    stream = common.streams.StreamIn(f.read(), settings)
    ranking = stream.extract(datastoresmm.CourseRecordInfo)
    rankings.append(ranking)
    f.close()

rankings_stream = common.streams.StreamOut(settings)
rankings_stream.list(rankings, rankings_stream.add)
f = open("smm_rankings.bin", "wb")
f.write(rankings_stream.get())
f.close()

print("END")
