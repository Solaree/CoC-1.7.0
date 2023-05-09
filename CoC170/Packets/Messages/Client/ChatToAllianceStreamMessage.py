import json
from Utils.Reader import Reader

from Packets.Messages.Server.Alliance.AllianceStreamEntryMessage import *


class ChatToAllianceStreamMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):

        global AllianceMessage
        AllianceMessage = self.readString()  # Message

    def process(self):
        AllianceStreamEntryMessage(self.device).Send()