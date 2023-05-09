import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class LogicAllianceSettingsChangedCommand(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 6

    def encode(self):

        self.writeInt(config['AllianceHighID'])
        self.writeInt(config['AllianceLowID'])

        self.writeInt(config['AllianceBadge'])