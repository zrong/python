from zrong import base
import os

workDir = None

class TestDictBase:
    def __init__(self):
        super(TestDictBase, self).__init__()
        self._dict = base.DictBase({"name":"neo", "sex":"unknown"})

    def test_getattr(self):
        self._dict.name;

    def test_setattr(self):
        self._dict.name = "zrong";

    def test_delattr(self):
        del self._dict.name

    def test_dump(self):
        self._dict.dump()

    def test_saveToFile(self):
        fileName = "__TEST_DICT_BASE_WRITE_TO_FILE__.py"
        filePath =  os.path.join(workDir, fileName)
        self._dict.saveToFile(filePath)
        os.remove(filePath)


def setup():
    global workDir
    workDir = os.path.split(os.path.abspath(__file__))[0]

def test_listDir():
    assert len(base.listDir(workDir)) > 0

def test_getFiles():
    assert len(base.getFiles(workDir)) > 0

def test_readFile():
    base.readFile(__file__)

def test_writeFile():
    fileName = "__TEST_WRITE_FILE__.txt"
    filePath =  os.path.join(workDir, fileName)
    base.writeFile(filePath, filePath)
    os.remove(filePath)

