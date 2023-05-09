from Utils.Reader import Reader
from Packets.Messages.Server.Alliance.AllianceDataMessage import *


class AskForAllianceDataMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        self.readInt()  # AllianceHighID
        self.readInt()  # AllianceLowID

    def process(self):
        AllianceDataMessage(self.device).Send()