import json
from Utils.Writer import Writer

from Logic.Stream.Avatar.AvatarStreamEntry import *

config = json.load(open("config.json", "r"))


class AllianceInvationAvatarStreamEntry(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device

    def encode(self):

        self.writeInt(4)  # StreamEntryType

        AvatarStreamEntry.encode(self)

        self.writeInt(config['AllianceHighID'])  # AllianceHighID
        self.writeInt(config['AllianceLowID'])  # AllianceLowID

        self.writeString(config['AllianceName'])  # AllianceName

        self.writeInt(config['AllianceBadge'])  # AllianceBadge