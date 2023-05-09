from Utils.Reader import Reader
from Packets.Messages.Server.Avatar.AvatarRankingListMessage import *


class AskForAvatarRankingListMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        AvatareRankingListMessage(self.device).Send()