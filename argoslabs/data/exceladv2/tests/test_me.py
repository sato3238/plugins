"""
====================================
 :mod:`argoslabs.data.exceladv2`
====================================
.. moduleauthor:: Irene Cho <irene@argos-labs.com>
.. note:: ARGOS-LABS License

Description
===========
ARGOS LABS plugin module for Excel Advance II : UnitTest
"""
#
# Authors
# ===========
#
# * Irene Cho
#
# Change Log
# --------
#
#  * [2021/03/29]
#     - 그룹에 "2-Business Apps" 넣음
#  * [2020/04/12]
#     - unittest
#  * [2020/04/06]
#     - starting


################################################################################
import os
import sys
import win32com
from alabs.common.util.vvargs import ArgsError
from unittest import TestCase
from argoslabs.data.exceladv2 import _main as main


################################################################################
# noinspection PyUnresolvedReferences,PyBroadException
class TU(TestCase):

    # ==========================================================================
    @classmethod
    def setUpClass(cls) -> None:
        cls.tdir = os.path.dirname(__file__)
        os.chdir(cls.tdir)
        cls.xlf = os.path.join(cls.tdir, 'sample.xlsx')
        cls.csvf = os.path.join(cls.tdir, 'bar.csv')

    # ==========================================================================
    def test0100_addsheet1(self):
        try:
            r = main(self.xlf, 'Add sheet', '--newfilename', 'new.xlsx',
                     '--newsheet', 'newsheet1')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0110_addsheet2(self):
        try:
            r = main(self.xlf, 'Add sheet',
                     '--newsheet', 'newsheet1','--data_only')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    # def test0120_renamesheet(self):
    #     try:
    #         r = main(self.xlf, 'Rename sheet',
    #                  '--sheetname', 'Sheet2', '--newsheet', 'newsheet2')
    #         self.assertTrue(r == 0)
    #     except ArgsError as e:
    #         sys.stderr.write('\n%s\n' % str(e))
    #         self.assertTrue(False)

    # ==========================================================================
    def test0130_deletesheet(self):
        try:
            r = main(self.xlf, 'Delete sheet',
                     '--sheetname', 'newsheet2')
            self.assertTrue(r == 1)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    # def test0140_xlsxtopdf(self):
    #     try:
    #         try:
    #             win32com.client.Dispatch('Excel.Application')
    #             r = main(self.xlf, 'Print PDF', '--filenamepath', 'sample.pdf')
    #             self.assertTrue(r == 0)
    #         except Exception:
    #             ...
    #     except ArgsError as e:
    #         sys.stderr.write('\n%s\n' % str(e))
    #         self.assertTrue(False)
    #
    # # ==========================================================================
    # def test0150_cvstopdf(self):
    #     try:
    #         try:
    #             win32com.client.Dispatch('Excel.Application')
    #             r = main(self.csvf, 'Print PDF', '--filenamepath', 'bar.pdf')
    #             self.assertTrue(r == 0)
    #         except Exception:
    #             ...
    #     except ArgsError as e:
    #         sys.stderr.write('\n%s\n' % str(e))
    #         self.assertTrue(False)

    # ==========================================================================
    def test0160_blankcol(self):
        try:
            r = main(self.xlf, 'Find first blank col',
                     '--sheetname', 'Sheet1', '--row-num', '2')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # # ==========================================================================
    def test0170_blankrow(self):
        try:
            r = main(self.xlf, 'Find first blank row', '--col-name', 'A')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # # ==========================================================================
    def test0180_col_row_manipulating(self):
        try:
            r = main('foo.xlsx','Insert delete row col','--newfilename','new.xlsx',
                     '--del-row-num', '7-230')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0190_col_row_manipulating_csv(self):
        try:
            r = main(self.csvf, 'Insert delete row col', '--del-col-name', 'A-D',
                     '--newfilename','new.csv')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0200_csv1(self):
        try:
            r = main(self.csvf, 'Find first blank row', '--col-name', 'A')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0210_csv2(self):
        try:
            r = main(self.csvf, 'Find first blank col', '--row-num', '1')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0220_saveas(self):
        try:
            r = main(self.xlf, 'Save As','--newfilename', 'new.csv',
                     '--data_only')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0230_foo(self):
        try:
            r = main('foo.xlsx', 'Find first blank row','--col-name', 'A')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0240_eng(self):
        try:
            r = main(self.xlf, 'Find first blank col', '--row-num', '1')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0250_copy(self):
        try:
            r = main(self.xlf, 'Copy Sheet','--sheetname','Sheet1',
                     '--newsheet','newname')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0260_copy(self):
        try:
            r = main(self.xlf, 'Copy Sheet','--sheetname','Sheet1',
                     '--newsheet','newname', '--data_only')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0270_copy(self):
        try:
            r = main(self.csvf, 'Save As', '--data_only','--newfilename',
                     'new.csv')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
    def test0280_eng(self):
        try:
            r = main('foo.xlsx', 'Find first blank row', '--col-name', 'aa',
                     '--sheetname','Sheet2','--nonecsvrv')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)


    # ==========================================================================
    def test0290_error(self):
        try:
            r = main('foo.xlsx', 'Find first blank row')
            self.assertTrue(r == 9)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)
