import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class RankingEntry(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device

    def encode(self):

        self.writeInt(config['AccountHighID'])  # HighID
        self.writeInt(config['AccountLowID'])  # LowID

        self.writeString(config['Name'])  # Name

        self.writeInt(config['Order'])  # Order
        self.writeInt(config['Score'])  # Score