from Utils.Writer import Writer


class LogicJoinAllianceCommand(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 1

    def encode(self):

        self.writeInt(0)
        self.writeInt(1)

        self.writeString()

        self.writeInt()

        self.writeInt()