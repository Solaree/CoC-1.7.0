from Utils.Reader import Reader
from Packets.Messages.Server.AvailableServerCommandMessage import *


class EndClientTurnMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):

        self.readInt()  # SubTick
        self.readInt()  # Checksum
        self.readInt()  # CommandsCount

    def process(self):
        AvailableServerCommandMessage(self.device).Send()