#! /bin/env python

from TableGenerator import *


class erfTabGenerator(TableGenerator):

    OUTPUT_FILE_PATH = 'table_erf.tex'
    HEADER_ROW       = [i     for i in range(10)]
    HEADER_COLUMN    = [i*0.1 for i in range(30)]

    def setTableValue(self):
        x = self.Column + self.Row/100.
        value = 0.5*ROOT.TMath.Erf(sqrt(0.5)*x) 
        rowLabel    = '%d'   % self.Row
        columnLabel = '%.1f' % self.Column
        self.Table.setValue(rowLabel, columnLabel, value, 7)


if __name__ == '__main__':
    tabGenerator = erfTabGenerator('x')
    tabGenerator.run()
