import json
from Utils.Writer import Writer

from Logic.Rank.RankingEntry import *

config = json.load(open("config.json", "r"))


class AvatarRankingEntry(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device

    def encode(self):

        RankingEntry.encode(self)
        
        self.writeInt(config['ExpLevel'])  # ExpLevel

        self.writeInt(config['HomeHighID'])
        self.writeInt(config['HomeLowID'])

        self.writeByte(1)  # IsInAlliance
        
        self.writeInt(config['AllianceHighID'])
        self.writeInt(config['AllianceLowID'])

        self.writeString(config['AllianceName'])

        self.writeInt(config['AllianceBadge'])