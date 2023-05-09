from Utils.Writer import Writer
from Logic.Stream.Avatar.JoinAllianceResponseAvatarStreamEntry import *
from Logic.Stream.Avatar.AllianceInvationAvatarStreamEntry import *
from Logic.Stream.Avatar.BattleReportStreamEntry import *

class AvatarStreamMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24411
    
    def encode(self):

        # StreamEntryType HERE

        AllianceInvationAvatarStreamEntry.encode(self)
        JoinAllianceResponseAvatarStreamEntry.encode(self)
        BattleReportStreamEntry.encode(self)