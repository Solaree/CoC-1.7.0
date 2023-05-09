from Utils.Writer import Writer
from Logic.ClientHome import LogicClientHome
from Logic.ClientAvatar import LogicClientAvatar


class OwnHomeDataMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24101

    def encode(self):

        self.writeInt(0)  # SecondsSinceLastSave

        LogicClientHome.encode(self)
        LogicClientAvatar.encode(self)