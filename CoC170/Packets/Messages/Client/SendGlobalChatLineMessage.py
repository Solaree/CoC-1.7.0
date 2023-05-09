import json
import time

from Utils.Reader import Reader
from Logic.Player import Player

from Packets.Messages.Server.Chat.GlobalChatLineMessage import *
from Packets.Messages.Server.OwnHomeDataMessage import *

config = json.load(open("config.json", "r+"))



class SendGlobalChatLineMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):

        global Message
        Message = self.readString()  # Message

    def process(self):

        if "/" in Message:

            if "help" in Message:
                config['GlobalChatLineMessage'] = "Available commands:\n\n/help\n  -> List of all commands.\n/gems (value)\n  -> Send gems update to your OHD.\n/trophies (value)\n  -> Send trophies update to your OHD.\n/lvl (value)\n  -> Send level update to your OHD.\n/expoints (value)\n  -> Send exp level update to your OHD.\n/rename\n  -> Change your name again.\n/prebase [level]\n  -> Load a premade base from level 1 to 8.\n/reset\n  -> Reset your village and start from beginning."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(1)

            if "gems 999" or "gems 1000" in Message:
                config['Diamonds'] = 1000

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Diamonds'])} Diamonds to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "gems 9999" or "gems 10000" in Message:
                config['Diamonds'] = 10000

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Diamonds'])} Diamonds to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "gems 99999" or "gems 100000" in Message:
                config['Diamonds'] = 100000

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Diamonds'])} Diamonds to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "gems 999999" or "gems 1000000 "in Message:
                config['Diamonds'] = 1000000

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Diamonds'])} Diamonds to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "gems 9999999" or "gems 10000000" in Message:
                config['Diamonds'] = 10000000

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Diamonds'])} Diamonds to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "lvl 5" in Message:
                config['ExpLevel'] = 5

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpLevel'])} ExpLevel to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "lvl 9" or "lvl 10" in Message:
                config['ExpLevel'] = 10

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpLevel'])} ExpLevel to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "lvl 15" in Message:
                config['ExpLevel'] = 15

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpLevel'])} ExpLevel to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "lvl 20" in Message:
                config['ExpLevel'] = 20

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpLevel'])} ExpLevel to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "lvl 25" in Message:
                config['ExpLevel'] = 25

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpLevel'])} ExpLevel to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "lvl 50" in Message:
                config['ExpLevel'] = 50

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpLevel'])} ExpLevel to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "lvl 99" or "lvl 100" in Message:
                config['ExpLevel'] = 100

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpLevel'])} ExpLevel to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "expoints 99" or "expoints 100" in Message:
                config['ExpPoints'] = 100

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpPoints'])} ExpPoints to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "expoints 250" in Message:
                config['ExpPoints'] = 250

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpPoints'])} ExpPoints to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "expoints 500" in Message:
                config['ExpPoints'] = 500

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpPoints'])} ExpPoints to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "expoints 999" or "expoints 1000" in Message:
                config['ExpPoints'] = 1000

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['ExpPoints'])} ExpPoints to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "trophies 99" or "trophies 100" in Message:
                config['Score'] = 100

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Score'])} Trophies to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "trophies 250" in Message:
                config['Score'] = 250

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Score'])} Trophies to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "trophies 500" in Message:
                config['Score'] = 500

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Score'])} Trophies to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "trophies 999" or "trophies 1000" in Message:
                config['Score'] = 1000

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Score'])} Trophies to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "trophies 2500" in Message:
                config['Score'] = 2500

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Score'])} Trophies to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "trophies 5000" in Message:
                config['Score'] = 100

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Score'])} Trophies to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "trophies 9999" or "trophies 10000" in Message:
                config['Score'] = 10000

                config['GlobalChatLineMessage'] = f"Successfully sent {str(config['Score'])} Trophies to your OHD. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()



            UserName = str

            if f"name {UserName}" in Message:
                config['Name'] = UserName
            
                config['GlobalChatLineMessage'] = f"Successfully changed name to {str(config['Name'])}. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if  "reset" or "restart" in Message:
                config['townhall'] = "{\"buildings\":[{\"data\":1000001,\"lvl\":0,\"x\":20,\"y\":16},{\"data\":1000004,\"lvl\":0,\"x\":20,\"y\":12,\"res_time\":4782},{\"data\":1000000,\"lvl\":0,\"x\":25,\"y\":15,\"units\":[]},{\"data\":1000015,\"lvl\":0,\"x\":17,\"y\":17},{\"data\":1000014,\"lvl\":0,\"locked\":true,\"x\":25,\"y\":32}],\"obstacles\":[{\"data\":8000007,\"x\":5,\"y\":13},{\"data\":8000007,\"x\":15,\"y\":29},{\"data\":8000008,\"x\":7,\"y\":7},{\"data\":8000005,\"x\":29,\"y\":4},{\"data\":8000006,\"x\":15,\"y\":37},{\"data\":8000000,\"x\":20,\"y\":4},{\"data\":8000008,\"x\":15,\"y\":22},{\"data\":8000005,\"x\":37,\"y\":18},{\"data\":8000007,\"x\":6,\"y\":4},{\"data\":8000003,\"x\":26,\"y\":10},{\"data\":8000004,\"x\":21,\"y\":9},{\"data\":8000008,\"x\":29,\"y\":21},{\"data\":8000005,\"x\":20,\"y\":36},{\"data\":8000003,\"x\":29,\"y\":34},{\"data\":8000005,\"x\":5,\"y\":29},{\"data\":8000005,\"x\":8,\"y\":10},{\"data\":8000005,\"x\":5,\"y\":17},{\"data\":8000002,\"x\":4,\"y\":33},{\"data\":8000002,\"x\":5,\"y\":21},{\"data\":8000002,\"x\":10,\"y\":32},{\"data\":8000008,\"x\":5,\"y\":37},{\"data\":8000001,\"x\":9,\"y\":4},{\"data\":8000001,\"x\":13,\"y\":31},{\"data\":8000001,\"x\":7,\"y\":35},{\"data\":8000007,\"x\":4,\"y\":9},{\"data\":8000004,\"x\":9,\"y\":23},{\"data\":8000004,\"x\":6,\"y\":26},{\"data\":8000003,\"x\":35,\"y\":21},{\"data\":8000005,\"x\":32,\"y\":28},{\"data\":8000005,\"x\":34,\"y\":13},{\"data\":8000001,\"x\":14,\"y\":18},{\"data\":8000001,\"x\":35,\"y\":5},{\"data\":8000012,\"x\":24,\"y\":30},{\"data\":8000012,\"x\":31,\"y\":10},{\"data\":8000010,\"x\":26,\"y\":38},{\"data\":8000010,\"x\":14,\"y\":5},{\"data\":8000013,\"x\":34,\"y\":33},{\"data\":8000013,\"x\":13,\"y\":9},{\"data\":8000014,\"x\":10,\"y\":17},{\"data\":8000014,\"x\":24,\"y\":7},{\"data\":8000006,\"x\":36,\"y\":26},{\"data\":8000011,\"x\":23,\"y\":34},{\"data\":8000011,\"x\":24,\"y\":37},{\"data\":8000000,\"x\":27,\"y\":35},{\"data\":8000000,\"x\":25,\"y\":35},{\"data\":8000000,\"x\":26,\"y\":30},{\"data\":8000007,\"x\":23,\"y\":32},{\"data\":8000001,\"x\":28,\"y\":31},{\"data\":8000014,\"x\":28,\"y\":29}],\"traps\":[],\"decos\":[],\"respawnVars\":{\"secondsFromLastRespawn\":0,\"respawnSeed\":1529463799,\"obstacleClearCounter\":0}}"
                config['ShieldDurationSeconds'] = 259200
                config['ExpLevel'] = 1
                config['ExpPoints'] = 0
                config['Diamonds'] = 500
                config['Score'] = 0

                config['GlobalChatLineMessage'] = f"Successfully reset game. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "prebase [1]" in Message:
                config['townhall'] = ""

                config['GlobalChatLineMessage'] = f"Successfully changed village data. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "prebase [2]" in Message:
                config['townhall'] = ""

                config['GlobalChatLineMessage'] = f"Successfully changed village data. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "prebase [3]" in Message:
                config['townhall'] = ""

                config['GlobalChatLineMessage'] = f"Successfully changed village data. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "prebase [4]" in Message:
                config['townhall'] = ""

                config['GlobalChatLineMessage'] = f"Successfully changed village data. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "prebase [5]" in Message:
                config['townhall'] = ""

                config['GlobalChatLineMessage'] = f"Successfully changed village data. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "prebase [6]" in Message:
                config['townhall'] = ""

                config['GlobalChatLineMessage'] = f"Successfully changed village data. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "prebase [7]" in Message:
                config['townhall'] = ""

                config['GlobalChatLineMessage'] = f"Successfully changed village data. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            if "prebase [8]" in Message:
                config['townhall'] = "{\"buildings\":[{\"data\":1000001,\"lvl\":7,\"x\":20,\"y\":20},{\"data\":1000004,\"lvl\":9,\"x\":20,\"y\":32,\"res_time\":136582},{\"data\":1000000,\"lvl\":5,\"x\":29,\"y\":7,\"units\":[]},{\"data\":1000015,\"lvl\":0,\"x\":9,\"y\":29},{\"data\":1000014,\"lvl\":3,\"x\":11,\"y\":28},{\"data\":1000004,\"lvl\":9,\"x\":28,\"y\":33,\"res_time\":136596},{\"data\":1000002,\"lvl\":9,\"x\":25,\"y\":9,\"res_time\":136617},{\"data\":1000002,\"lvl\":9,\"x\":13,\"y\":12,\"res_time\":136614},{\"data\":1000015,\"lvl\":0,\"x\":13,\"y\":31},{\"data\":1000003,\"lvl\":9,\"x\":25,\"y\":13},{\"data\":1000005,\"lvl\":9,\"x\":16,\"y\":28},{\"data\":1000006,\"lvl\":9,\"x\":8,\"y\":23,\"unit_prod\":{}},{\"data\":1000008,\"lvl\":9,\"x\":17,\"y\":12},{\"data\":1000008,\"lvl\":9,\"x\":13,\"y\":16},{\"data\":1000002,\"lvl\":9,\"x\":18,\"y\":8,\"res_time\":136607},{\"data\":1000004,\"lvl\":9,\"x\":8,\"y\":26,\"res_time\":136620},{\"data\":1000006,\"lvl\":9,\"x\":25,\"y\":33,\"unit_prod\":{}},{\"data\":1000009,\"lvl\":9,\"x\":17,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":29,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":30,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":26},{\"data\":1000002,\"lvl\":9,\"x\":14,\"y\":8,\"res_time\":136623},{\"data\":1000004,\"lvl\":9,\"x\":9,\"y\":14,\"res_time\":136550},{\"data\":1000005,\"lvl\":9,\"x\":21,\"y\":13},{\"data\":1000003,\"lvl\":9,\"x\":29,\"y\":17},{\"data\":1000000,\"lvl\":5,\"x\":7,\"y\":18,\"units\":[]},{\"data\":1000013,\"lvl\":5,\"x\":25,\"y\":17},{\"data\":1000007,\"lvl\":5,\"x\":21,\"y\":8},{\"data\":1000002,\"lvl\":9,\"x\":30,\"y\":12,\"res_time\":136603},{\"data\":1000004,\"lvl\":9,\"x\":31,\"y\":33,\"res_time\":136609},{\"data\":1000009,\"lvl\":9,\"x\":28,\"y\":21},{\"data\":1000012,\"lvl\":5,\"x\":17,\"y\":20},{\"data\":1000006,\"lvl\":9,\"x\":32,\"y\":24,\"unit_prod\":{}},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":29,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":30,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":23},{\"data\":1000002,\"lvl\":9,\"x\":16,\"y\":32,\"res_time\":136582},{\"data\":1000004,\"lvl\":9,\"x\":28,\"y\":29,\"res_time\":136922},{\"data\":1000008,\"lvl\":9,\"x\":24,\"y\":29},{\"data\":1000013,\"lvl\":5,\"x\":16,\"y\":24},{\"data\":1000000,\"lvl\":5,\"x\":33,\"y\":16,\"units\":[]},{\"data\":1000009,\"lvl\":9,\"x\":20,\"y\":28},{\"data\":1000011,\"lvl\":5,\"x\":20,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":28},{\"data\":1000012,\"lvl\":5,\"x\":24,\"y\":21},{\"data\":1000008,\"lvl\":9,\"x\":28,\"y\":25},{\"data\":1000000,\"lvl\":5,\"x\":32,\"y\":28,\"units\":[]},{\"data\":1000006,\"lvl\":9,\"x\":32,\"y\":21,\"unit_prod\":{}},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":29,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":30,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":30,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":29,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":32},{\"data\":1000003,\"lvl\":9,\"x\":13,\"y\":20},{\"data\":1000005,\"lvl\":9,\"x\":12,\"y\":24},{\"data\":1000009,\"lvl\":9,\"x\":24,\"y\":25},{\"data\":1000011,\"lvl\":5,\"x\":21,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":30,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":29,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":35},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":35},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":35},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":35},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":35}],\"obstacles\":[{\"data\":8000000,\"x\":1,\"y\":22},{\"data\":8000013,\"x\":1,\"y\":15},{\"data\":8000007,\"x\":41,\"y\":25},{\"data\":8000005,\"x\":15,\"y\":1},{\"data\":8000014,\"x\":41,\"y\":1}],\"traps\":[{\"data\":12000000,\"x\":17,\"y\":9},{\"data\":12000000,\"x\":28,\"y\":10},{\"data\":12000001,\"x\":32,\"y\":27},{\"data\":12000001,\"x\":28,\"y\":11},{\"data\":12000000,\"x\":24,\"y\":34},{\"data\":12000000,\"x\":29,\"y\":14},{\"data\":12000000,\"x\":29,\"y\":15},{\"data\":12000001,\"x\":17,\"y\":10},{\"data\":12000001,\"x\":14,\"y\":28},{\"data\":12000000,\"x\":14,\"y\":29},{\"data\":12000000,\"x\":10,\"y\":17},{\"data\":12000000,\"x\":33,\"y\":27},{\"data\":12000000,\"x\":30,\"y\":15},{\"data\":12000001,\"x\":11,\"y\":17},{\"data\":12000001,\"x\":24,\"y\":33}],\"decos\":[],\"respawnVars\":{\"secondsFromLastRespawn\":7200,\"respawnSeed\":534306778,\"obstacleClearCounter\":11}}"

                config['GlobalChatLineMessage'] = f"Successfully changed village data. New OHD will be sent in 3 seconds."
                GlobalChatLineMessage(self.device).Send()
                time.sleep(3)
                OwnHomeDataMessage(self.device).Send()

            else:
                config['GlobalChatLineMessage'] = "ERROR: Value too high or incorrect!"
                GlobalChatLineMessage(self.device).Send()
                time.sleep(1)
        
        else:
            config['GlobalChatLineMessage'] = "ERROR: Command must starts with \"/\"!"
            GlobalChatLineMessage(self.device).Send()
            time.sleep(1)