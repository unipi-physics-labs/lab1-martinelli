#! /bin/env python

from TableGenerator import *
from table_student  import studentTabGenerator


class studentInverseTabGenerator(studentTabGenerator):

    OUTPUT_FILE_PATH = 'table_student_inverse.tex'
    HEADER_ROW       = ['0.05', '0.10', '0.25', '0.50', '0.75', '0.6827',
                        '0.95', '0.99', '0.999', '0.9999']

    def setTableValue(self):
        if self.Column == '\\infty':
            dof = 100000
        else:
            dof = int(self.Column)
        value = -ROOT.TMath.StudentQuantile((1.0 - float(self.Row))/2.0, dof)
        rowLabel    = 't_{%s}' % self.Row
        columnLabel = '%s' % self.Column
        self.Table.setValue(rowLabel, columnLabel, value, 5)


if __name__ == '__main__':
    tabGenerator = studentInverseTabGenerator('\\nu')
    tabGenerator.run()
