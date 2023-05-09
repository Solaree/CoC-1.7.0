from Utils.Reader import Reader
from Packets.Messages.Server.Alliance.AllianceRankingListMessage import *


class AskForAllianceRankingListMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        AllianceRankingListMessage(self.device).Send()