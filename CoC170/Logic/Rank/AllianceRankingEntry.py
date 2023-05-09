import json
from Utils.Writer import Writer

from Logic.Rank.RankingEntry import *

config = json.load(open("config.json", "r"))


class AlliancerRankingEntry(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device

    def encode(self):

        RankingEntry.encode(self)

        self.writeInt(config['AllianceBadge'])