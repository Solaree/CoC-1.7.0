import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))

# Decode data types: 60 - Long (2 Ints), 56 - Int, 52 - Byte, 48 - String, DataRef (1 Int)

class LogicClientAvatar(Writer):

    def encode(self):

        self.writeInt(0)

        self.writeInt(config['AccountHighID'])  # DefaultHighID
        self.writeInt(config['AccountLowID'])  # DefaultLowID

        self.writeInt(config['HomeHighID'])  # CurrentHomeHighID
        self.writeInt(config['HomeLowID'])  # CurrentHomeLowID

        self.writeByte(1)  # IsInAlliance

        self.writeInt(config['AllianceHighID'])  # AllianceHighID
        self.writeInt(config['AllianceLowID'])  # AllianceLowID

        self.writeString(config['AllianceName'])  # AllianceName

        self.writeInt(config['AllianceBadge'])  # AllianceBadge
        self.writeInt(config['AllianceRole'])  # AllianceRole

        self.writeInt(0)
        self.writeInt(10)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString(config['Name'])  # Name
        self.writeString(None)  # FacebookID

        self.writeInt(config['ExpLevel'])   # ExpLevel
        self.writeInt(config['ExpPoints'])  # ExpPoints
        self.writeInt(config['Diamonds'])  # Diamonds
        self.writeInt(0)  # FreeDiamonds
        self.writeInt(0)  # AttackRating
        self.writeInt(0)  # AttackKFactor
        self.writeInt(config['Score'])  # Score

        self.writeByte(0)  # NameSetByUser


        ##### ARAYS #####

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)