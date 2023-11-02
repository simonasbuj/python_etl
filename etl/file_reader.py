import glob
import pandas as pd
import xml.etree.ElementTree as ET

from .logger import Logger

class FileReader():
    
    def __init__(self):
        self.logger = Logger("FileReader")

    def we_be(self):
        print("yes and we are using logger")
        self.logger.log("MY MESSAGE")