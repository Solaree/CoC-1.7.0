from Utils.Writer import Writer
from Logic.Rank.AvatarRankingEntry import *

class AvatareRankingListMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24401

    def encode(self):

        self.writeInt(0)

        AvatarRankingEntry.encode(self)