from Utils.Reader import Reader

from Packets.Messages.Server.AvailableServerCommandMessage import *
from Packets.Messages.Server.Alliance.AllianceStreamMessage import *
from Packets.Messages.Server.Alliance.AllianceStreamEntryMessage import *


class JoinAllianceMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        
        self.readInt()  # HighID
        self.readInt()  # LowID
    
    def process(self):
        AllianceStreamMessage(self.device).Send()
        AllianceStreamEntryMessage(self.device).Send()