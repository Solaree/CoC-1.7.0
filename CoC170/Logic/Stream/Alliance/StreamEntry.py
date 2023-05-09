import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class StreamEntry(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
    
    def encode(self):

        # StreamEntryType FIRST

        self.writeInt(config['AccountHighID'])  # HighID
        self.writeInt(config['AccountLowID'])  # LowID

        self.writeString(config['Name'])  # SenderName

        self.writeInt(config['SenderLevel'])  # SenderLevel
        self.writeInt(config['SenderRole'])  # SenderRole
        self.writeInt(config['SenderMessageAgeSeconds'])  # AgeSeconds

        self.writeByte(0)  # IsRemoved