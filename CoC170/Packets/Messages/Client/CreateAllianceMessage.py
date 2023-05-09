from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.Alliance.AllianceCreateFailedMessage import *


class CreateAllianceMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):

        self.readString()  # AllianceName
        self.readString()  # AllianceDesc

        self.readInt()  # AllianceBadge

        self.readInt()  # AllianceType
        self.readInt()  # RequiredScore

    def process(self):
        AllianceCreateFailedMessage(self.device).Send()