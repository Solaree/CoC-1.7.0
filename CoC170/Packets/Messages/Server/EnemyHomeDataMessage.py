from Utils.Writer import Writer
from Logic.ClientHome import LogicClientHome
from Logic.ClientAvatar import LogicClientAvatar


class EnemyHomeDataMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24107

    def encode(self):

        self.writeInt(0)  # SecondsSinceLastSave

        LogicClientHome.encode(self)  # LogicClientHome

        LogicClientAvatar.encode(self)  # OwnerLogicClientAvatar
        LogicClientAvatar.encode(self)  # AttackerLogicClientAvatar

        self.writeInt(0)  # AttackSource
        self.writeInt(1)  # AvatarStreamEntryID