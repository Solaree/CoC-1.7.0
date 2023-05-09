from Utils.Reader import Reader
from Packets.Messages.Server.VisitedHomeDataMessage import *


class VisitHomeMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):

        self.readInt()  # HighID
        self.readInt()  # LowID

    def process(self):

        VisitedHomeDataMessage(self.device).Send()