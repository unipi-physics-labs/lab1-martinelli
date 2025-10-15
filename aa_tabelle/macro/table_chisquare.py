#! /bin/env python

from TableGenerator import *


class chiSquareTabGenerator(TableGenerator):

    HEADER_ROW       = ['0.005', '0.01', '0.025', '0.05', '0.10', '0.25',
                        '0.50' , '0.75', '0.90' , '0.95', '0.975', '0.99',
                        '0.999']

    def setTableValue(self):
        value  = ROOT.TMath.ChisquareQuantile(float(self.Row), self.Column)
        rowLabel    = '\\chi^2_{%s}'   % self.Row
        columnLabel = '%d' % self.Column
        self.Table.setValue(rowLabel, columnLabel, value, 4, 6)


if __name__ == '__main__':
    tabGenerator = chiSquareTabGenerator('\\nu')
    tabGenerator.OUTPUT_FILE_PATH = 'table_chisquare_I.tex'
    tabGenerator.HEADER_COLUMN = [i for i in range(1, 31)]
    tabGenerator.run()
    tabGenerator.reset()
    tabGenerator.OUTPUT_FILE_PATH = 'table_chisquare_II.tex'
    tabGenerator.HEADER_COLUMN = [i for i in range(31, 61)]
    tabGenerator.run()
    tabGenerator.reset()
    tabGenerator.OUTPUT_FILE_PATH = 'table_chisquare_III.tex'
    tabGenerator.HEADER_COLUMN = [i for i in range(61, 91)]
    tabGenerator.run()
