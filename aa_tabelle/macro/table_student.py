#! /bin/env python

from TableGenerator import *


class studentTabGenerator(TableGenerator):

    OUTPUT_FILE_PATH = 'table_student.tex'
    HEADER_ROW       = ['0.001', '0.005', '0.010', '0.025', '0.050', '0.0159',
                        '0.200', '0.300', '0.400', '0.425']
    HEADER_COLUMN    = range(2, 21) + [25] + range(30, 51, 10) +\
        range(100, 501, 100) + ['\\infty']

    def setTableValue(self):
        if self.Column == '\\infty':
            dof = 100000
        else:
            dof = int(self.Column)
        value = -ROOT.TMath.StudentQuantile(float(self.Row), dof)
        rowLabel    = 't_{%s}' % self.Row
        columnLabel = '%s' % self.Column
        self.Table.setValue(rowLabel, columnLabel, value, 5)


if __name__ == '__main__':
    tabGenerator = studentTabGenerator('\\nu')
    tabGenerator.run()
