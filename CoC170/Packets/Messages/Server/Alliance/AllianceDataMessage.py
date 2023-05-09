from Utils.Writer import Writer
from Logic.AllianceFullEntry import *

class AllianceDataMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24301

    def encode(self):
        AllianceFullEntry.encode(self)