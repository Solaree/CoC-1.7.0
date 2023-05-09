from Utils.Writer import Writer


class AllianceFullEntry(Writer):

    def encode(self):

        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeString("SolarLand")  # AllianceName
    
        self.writeInt(13000000)  # AllianceBadge

        self.writeInt(0)  # AllianceType
        self.writeInt(1)  # NumberOfMembers
        self.writeInt(1000)  # Score

        self.writeString("Lox")  # AllianceDescription
        
        self.writeInt(1)  # AllianceMembers

        self.writeInt(0)  # AvatarHighID
        self.writeInt(1)  # AvatarLowID

        self.writeString(None)  # FacebookID
        self.writeString("Solar")  # Name

        self.writeInt(0)  # Role
        self.writeInt(99)  # ExpLevel
        self.writeInt(9999)  # Score

        self.writeByte(1)

        self.writeInt(0)  # HomeHighID
        self.writeInt(1)  # HomeHighID