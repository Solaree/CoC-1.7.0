from Utils.Reader import Reader
from Packets.Messages.Server.Alliance.AllianceListMessage import *


class AskForJoinableAlliancesListMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        AllianceListMessage(self.device).Send()