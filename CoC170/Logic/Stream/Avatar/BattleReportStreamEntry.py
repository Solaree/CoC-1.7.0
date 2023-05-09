import json
from Utils.Writer import Writer

from Logic.Stream.Avatar.AvatarStreamEntry import *

config = json.load(open("config.json", "r"))


class BattleReportStreamEntry(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
    
    def encode(self):

        self.writeInt(2)  # StreamEntryType

        AvatarStreamEntry.encode(self)

        self.writeString(config['townhall'])  # BattleLogJSON

        self.writeByte(1)  # IsRevengeUsed