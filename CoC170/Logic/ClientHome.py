import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))

class LogicClientHome(Writer):

    def encode(self):

        self.writeInt(0)

        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID

        self.writeString(config['townhall'])  # HomeJSON

        self.writeInt(config['ShieldDurationSeconds'])  # ShieldDurationSeconds
        self.writeInt(0)  # DefenseRating
        self.writeInt(0)  # DefenseKFactor