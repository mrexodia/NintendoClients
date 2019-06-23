from nintendo.nex import backend, authentication, datastoresmm, common
from nintendo.games import SMM

import argparse
import logging
import base64

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("-host", default="127.0.0.1")
parser.add_argument("-port", type=int, default=59900)
parser.add_argument("-username", default="guest")
parser.add_argument("-password", default="MMQea3n!fsik")
parser.add_argument("-token", default="token")
args = parser.parse_args()

backend = backend.BackEndClient()
backend.configure(SMM.ACCESS_KEY, SMM.NEX_VERSION)

backend.connect(args.host, args.port)

auth_info = authentication.AuthenticationInfo()
auth_info.token = args.token
auth_info.server_version = SMM.SERVER_VERSION

backend.login(
	args.username, args.password,
	auth_info, None
)

client = datastoresmm.DataStoreSmmClient(backend.secure_client)

import time
time.sleep(20)

response = client.method79(0)
print("response: {}".format(response))

import time
time.sleep(20)

response = client.method79(0)
print("response: {}".format(response))

backend.close()
