import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class AvatarStreamEntry(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device

    def encode(self):

        # StreamEntryType FIRST

        self.writeInt(config['AccountHighID'])  # HighID
        self.writeInt(config['AccountLowID'])  # LowID

        # self.writeInt(config['SenderHomeHighID'])  # SenderAvatarHighID
        # self.writeInt(config['SenderHomeLowID'])  # SenderAvatarLowID

        self.writeString(config['Name'])  # SenderName

        self.writeInt(config['SenderLevel'])  # SenderLevel
        self.writeInt(config['SenderMessageAgeSeconds'])  # AgeSeconds

        self.writeByte(0)  # IsRemoved
        self.writeByte(1)  # IsNew