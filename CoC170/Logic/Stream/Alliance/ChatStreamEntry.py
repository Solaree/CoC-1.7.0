import json
from Utils.Writer import Writer

from Logic.Stream.Alliance.StreamEntry import *
from Packets.Messages.Client.ChatToAllianceStreamMessage import *

config = json.load(open("config.json", "r"))


class ChatStreamEntry(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device

    def encode(self):

        self.writeInt(2)  # StreamEntryType

        StreamEntry.encode(self)

        self.writeString(AllianceMessage)  # Message