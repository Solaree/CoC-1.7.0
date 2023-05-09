from Utils.Writer import Writer
from Packets.Commands.Server.LogicJoinAllianceCommand import *


class AllianceJoinOkMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24303

    def encode(self):
        LogicJoinAllanceCommand.encode(self)