from Utils.Writer import Writer
from Packets.Commands.Server.LogicAllianceUnitReceivedCommand import *


class LogicAllianceSettingsChangedCommand(Writer):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass
    def process(self):
        LogicAllianceUnitReceivedCommand(self.device).Send()