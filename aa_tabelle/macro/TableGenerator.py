import os
import sys
import ROOT
import logging
logging.basicConfig(level = logging.DEBUG)

from math  import sqrt
from Table import Table

class TableGenerator:

    def __init__(self, cornerLabel):
        self.Table = Table(cornerLabel)
    
    def run(self):
        for row in self.HEADER_ROW:
            for column in self.HEADER_COLUMN:
                self.Row    = row
                self.Column = column
                self.setTableValue()
        self.Table.dumpToFile(self.OUTPUT_FILE_PATH)

    def reset(self):
        self.Table.reset()
