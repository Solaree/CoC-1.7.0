from Utils.Writer import Writer

from Logic.Stream.Alliance.ChatStreamEntry import *
from Logic.Stream.Alliance.JoinRequestAllianceStreamEntry import *

class AllianceStreamMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24311

    def encode(self):

        JoinRequestAllianceStreamEntry.encode(self)
        ChatStreamEntry.encode(self)

        # Here must be DonateStreamEntry, but CoC 1.7.0 lib has unclear structure of it