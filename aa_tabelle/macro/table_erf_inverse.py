#! /bin/env python

from TableGenerator import *
from table_erf      import erfTabGenerator


class erfInverseTabGenerator(erfTabGenerator):

    OUTPUT_FILE_PATH = 'table_erf_inverse.tex'
    HEADER_COLUMN    = [i*0.1 for i in range(30, 60)]

    def setTableValue(self):
        x = self.Column + self.Row/100.
        value = 0.5*(1.0 - ROOT.TMath.Erf(sqrt(0.5)*x)) 
        rowLabel    = '%d'   % self.Row
        columnLabel = '%.1f' % self.Column
        self.Table.setValue(rowLabel, columnLabel, value, 7, forceEng = True)


if __name__ == '__main__':
    tabGenerator = erfInverseTabGenerator('x')
    tabGenerator.run()

