#!/opt/homebrew/bin/python3

import os
import pickle

class Save:

    def __init__(self):
        pass

    def writeObjectToFile(self, obj, path):
        self.filepath = self.convertToRelativePath(path)
        
        with open(self.filepath, "wb") as f:
            pickle.dump(str(obj), f)

    def loadObjectFromFile(self, path):
        self.filepath = self.convertToRelativePath(path)

        obj = None 

        with open(self.filepath, "r") as f:
            obj = pickle.load(f)

        return obj

    def convertToRelativePath(self, path):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)



