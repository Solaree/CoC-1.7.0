import json
from Utils.Writer import Writer
from Packets.Messages.Client.SendGlobalChatLineMessage import *

config = json.load(open("config.json", "r"))


class GlobalChatLineMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24715

    def encode(self):

        self.writeString(config['GlobalChatLineMessage'])  # Message
        self.writeString("DebugManager")  # AvatarName

        self.writeInt(99)  # AvatarExpLevel

        self.writeInt(0)
        self.writeInt(1)

        self.writeInt(0)
        self.writeInt(1)

        self.writeByte(1)  # IsInAlliance

        self.writeInt(config['AllianceHighID'])
        self.writeInt(config['AllianceLowID'])

        self.writeString(config['AllianceName'])

        self.writeInt(config['AllianceBadge'])