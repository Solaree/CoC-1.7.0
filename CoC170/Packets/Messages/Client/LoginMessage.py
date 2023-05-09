from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.LoginOkMessage import *
from Packets.Messages.Server.OwnHomeDataMessage import *
from Packets.Messages.Server.Avatar.AvatarStreamMessage import *
from Packets.Messages.Server.Alliance.AllianceStreamMessage import *
from Packets.Messages.Server.Alliance.AllianceStreamEntryMessage import *


class LoginMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)

    def decode(self):
        pass

    def process(self):
        LoginOkMessage(self.device).Send()
        OwnHomeDataMessage(self.device).Send()
        #AvatarStreamEntryMessage(self.client, self.player).Send()
        AllianceStreamMessage(self.device).Send()
        AllianceStreamEntryMessage(self.device).Send()