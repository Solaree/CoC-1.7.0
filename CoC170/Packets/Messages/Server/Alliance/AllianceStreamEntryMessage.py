import json
from Utils.Writer import Writer

from Logic.Stream.Alliance.StreamEntry import *

config = json.load(open("config.json", "r"))


class AllianceStreamEntryMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24312

    def encode(self):

        StreamEntry.encode(self)