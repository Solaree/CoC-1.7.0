from Utils.Writer import Writer


class LogicDiamondsAddedCommand(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 5

    def encode(self):

        self.writeInt(0)
        self.writeInt(1)