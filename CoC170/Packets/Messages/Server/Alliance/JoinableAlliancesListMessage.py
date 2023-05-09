from Utils.Writer import Writer


class JoinableAlliancesListMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24304

    def encode(self):

        self.writeInt(1)


        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeString("SolarLand")  # AllianceName
    
        self.writeInt(13000000)  # AllianceBadge

        self.writeInt(0)  # AllianceType
        self.writeInt(1)  # NumberOfMembers
        self.writeInt(1000)  # Score
