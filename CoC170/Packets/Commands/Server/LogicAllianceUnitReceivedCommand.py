from Utils.Writer import Writer


class LogicAllianceUnitReceivedCommand(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 5

    def encode(self):

        self.writeString("Solar")  # Name

        self.writeInt(26000000)  # UnitType