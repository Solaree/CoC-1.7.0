import json
from Utils.Writer import Writer

from Logic.Stream.Alliance.StreamEntry import *

config = json.load(open("config.json", "r"))


class JoinRequestAllianceStreamEntry(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device

    def encode(self):

        self.writeInt(3) # StreamEntryType

        StreamEntry.encode(self)

        self.writeInt(config['AccountHighID'])  # HighID
        self.writeInt(config['AccountLowID'])  # LowID

        self.writeString(config['AllianceJoinRequestMessage'])  # Message
        self.writeString(config['Name'])  # ResponderName

        self.writeInt(0)  # State