import json
from Utils.Writer import Writer
from Logic.ClientAvatar import LogicClientAvatar

config = json.load(open("config.json", "r"))


class NpcDataMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24133

    def encode(self):

        self.writeInt(0)  # SecondsSinceLastSave

        self.writeString("{\"buildings\":[{\"data\":1000001,\"lvl\":7,\"x\":10,\"y\":19},{\"data\":1000011,\"lvl\":5,\"x\":10,\"y\":29},{\"data\":1000011,\"lvl\":5,\"x\":7,\"y\":25},{\"data\":1000011,\"lvl\":5,\"x\":7,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":24},{\"data\":1000012,\"lvl\":5,\"x\":7,\"y\":17},{\"data\":1000012,\"lvl\":5,\"x\":7,\"y\":22},{\"data\":1000012,\"lvl\":5,\"x\":19,\"y\":25},{\"data\":1000012,\"lvl\":5,\"x\":19,\"y\":14},{\"data\":1000018,\"lvl\":0,\"x\":31,\"y\":19,\"units\":[]},{\"data\":1000018,\"lvl\":0,\"x\":31,\"y\":23,\"units\":[]},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":35},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":30,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":29,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":10,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":9,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":8,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":7,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":36},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":35},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":10},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":7},{\"data\":1000010,\"lvl\":5,\"x\":30,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":10},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":32,\"y\":7},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":25},{\"data\":1000008,\"lvl\":9,\"x\":23,\"y\":18},{\"data\":1000008,\"lvl\":9,\"x\":25,\"y\":26},{\"data\":1000008,\"lvl\":9,\"x\":25,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":28},{\"data\":1000013,\"lvl\":5,\"x\":25,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":10,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":10,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":10,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":7,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":8,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":9,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":10,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":26},{\"data\":1000011,\"lvl\":5,\"x\":15,\"y\":29},{\"data\":1000011,\"lvl\":5,\"x\":20,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":13},{\"data\":1000013,\"lvl\":5,\"x\":25,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":10},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":10},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":10},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":10},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":10,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":10,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":10,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":9,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":8,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":7,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":10},{\"data\":1000010,\"lvl\":5,\"x\":29,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":11,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":10,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":9,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":8,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":7,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":6,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":9},{\"data\":1000011,\"lvl\":5,\"x\":20,\"y\":10},{\"data\":1000011,\"lvl\":5,\"x\":15,\"y\":10},{\"data\":1000011,\"lvl\":5,\"x\":10,\"y\":10},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":22},{\"data\":1000018,\"lvl\":0,\"x\":30,\"y\":27,\"units\":[]},{\"data\":1000018,\"lvl\":0,\"x\":29,\"y\":33,\"units\":[]},{\"data\":1000018,\"lvl\":0,\"x\":30,\"y\":31,\"units\":[]},{\"data\":1000018,\"lvl\":0,\"x\":29,\"y\":29,\"units\":[]},{\"data\":1000018,\"lvl\":0,\"x\":30,\"y\":15,\"units\":[]},{\"data\":1000018,\"lvl\":0,\"x\":29,\"y\":13,\"units\":[]},{\"data\":1000018,\"lvl\":0,\"x\":30,\"y\":11,\"units\":[]},{\"data\":1000018,\"lvl\":0,\"x\":29,\"y\":9,\"units\":[]},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":21},{\"data\":1000009,\"lvl\":9,\"x\":18,\"y\":22},{\"data\":1000009,\"lvl\":9,\"x\":18,\"y\":17},{\"data\":1000008,\"lvl\":9,\"x\":23,\"y\":22},{\"data\":1000012,\"lvl\":5,\"x\":13,\"y\":14},{\"data\":1000012,\"lvl\":5,\"x\":13,\"y\":25},{\"data\":1000011,\"lvl\":5,\"x\":14,\"y\":18},{\"data\":1000011,\"lvl\":5,\"x\":14,\"y\":21},{\"data\":1000011,\"lvl\":5,\"x\":25,\"y\":33},{\"data\":1000011,\"lvl\":5,\"x\":25,\"y\":7},{\"data\":1000013,\"lvl\":5,\"x\":10,\"y\":25},{\"data\":1000013,\"lvl\":5,\"x\":10,\"y\":14},{\"data\":1000005,\"lvl\":9,\"x\":16,\"y\":14},{\"data\":1000005,\"lvl\":9,\"x\":16,\"y\":25},{\"data\":1000003,\"lvl\":9,\"x\":7,\"y\":10},{\"data\":1000003,\"lvl\":9,\"x\":7,\"y\":33},{\"data\":1000003,\"lvl\":9,\"x\":7,\"y\":29},{\"data\":1000003,\"lvl\":9,\"x\":7,\"y\":7},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":6},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":7},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":8},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":9},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":10},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":11},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":32},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":33},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":34},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":35},{\"data\":1000010,\"lvl\":5,\"x\":5,\"y\":36}],\"obstacles\":[{\"data\":8000020,\"x\":34,\"y\":30},{\"data\":8000020,\"x\":34,\"y\":12},{\"data\":8000020,\"x\":35,\"y\":9},{\"data\":8000020,\"x\":37,\"y\":4},{\"data\":8000020,\"x\":37,\"y\":20},{\"data\":8000020,\"x\":2,\"y\":24},{\"data\":8000020,\"x\":2,\"y\":14}],\"traps\":[{\"data\":12000001,\"x\":10,\"y\":35},{\"data\":12000001,\"x\":29,\"y\":24},{\"data\":12000001,\"x\":29,\"y\":19},{\"data\":12000001,\"x\":30,\"y\":19},{\"data\":12000001,\"x\":30,\"y\":24},{\"data\":12000001,\"x\":11,\"y\":7},{\"data\":12000001,\"x\":21,\"y\":21},{\"data\":12000001,\"x\":21,\"y\":20},{\"data\":12000000,\"x\":29,\"y\":21},{\"data\":12000000,\"x\":24,\"y\":7},{\"data\":12000000,\"x\":16,\"y\":7},{\"data\":12000000,\"x\":23,\"y\":35},{\"data\":12000000,\"x\":14,\"y\":35},{\"data\":12000000,\"x\":23,\"y\":26},{\"data\":12000000,\"x\":23,\"y\":15},{\"data\":12000001,\"x\":25,\"y\":21},{\"data\":12000001,\"x\":23,\"y\":28},{\"data\":12000001,\"x\":23,\"y\":13},{\"data\":12000001,\"x\":17,\"y\":20},{\"data\":12000001,\"x\":17,\"y\":21}],\"decos\":[{\"data\":18000001,\"x\":33,\"y\":25},{\"data\":18000001,\"x\":33,\"y\":17},{\"data\":18000002,\"x\":36,\"y\":36},{\"data\":18000002,\"x\":36,\"y\":6},{\"data\":18000002,\"x\":33,\"y\":6},{\"data\":18000002,\"x\":33,\"y\":36}],\"respawnVars\":{\"secondsFromLastRespawn\":0,\"respawnSeed\":1529463799,\"obstacleClearCounter\":0}}")

        LogicClientAvatar.encode(self)

        self.writeInt(config['NpcHighID'])  # NpcHighID
        self.writeInt(config['NpcLowID'])  # NpcLowID