from nintendo.nex import backend, authentication, friends, common
from nintendo.games import Friends, SMM

import argparse
import logging
import base64

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("-host", default="127.0.0.1")
parser.add_argument("-port", type=int, default=60000)
parser.add_argument("-username", default="guest")
parser.add_argument("-password", default="MMQea3n!fsik")
parser.add_argument("-token", default="token")
args = parser.parse_args()

backend = backend.BackEndClient("friends.cfg")
backend.configure(Friends.ACCESS_KEY, Friends.NEX_VERSION)

backend.connect(args.host, args.port)

login_data = authentication.NintendoLoginData()
login_data.token = args.token
backend.login(
	args.username, args.password,
	None, login_data
)

nna_info = friends.NNAInfo()
nna_info.principal_info.pid = 1337
nna_info.principal_info.nnid = "nnid12345678"
nna_info.principal_info.mii.name = "Mii"
nna_info.principal_info.mii.data = base64.b64decode("AAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAEBNAGkAaQAAAAAAAAAAAAAAAAAAAEBAAABrAQJohBQpE8YOwRATRg0ACCWAQUhQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7i")

# NintendoPresenceV2 tells the server about your online status, which
# game you're currently playing, etc. This will be shown to your friends
# in their friend list (unless you disabled this feature).
presence = friends.NintendoPresenceV2()
presence.flags = 1
presence.is_online = True
presence.game_key.title_id = SMM.TITLE_ID_EUR
presence.game_key.title_version = SMM.LATEST_VERSION
presence.unk1 = 1
presence.application_data = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
presence.unk5 = 3
presence.unk6 = 1
presence.unk7 = 3

client = friends.FriendsClient(backend.secure_client)
response = client.get_all_information(
	nna_info, presence,
	common.DateTime.make(15, 11, 1999, 0, 0, 0)
)

backend.close()
