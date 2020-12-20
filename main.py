import psycopg2
import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from windows import add_new_awardui
from windows import add_new_equipui
from windows import add_new_groupui
from windows import add_new_requestui
from windows import add_new_sanctui
from windows import add_new_setui
from windows import add_new_shiftui
from windows import add_newclintui
from windows import add_newui
from windows import enterui
from windows import err_box
from windows import mainW
from windows import reg_diag
from windows import upd_workui


class program:
    def __init__(self):
        """
        # Подключение к БД
        self.conn = psycopg2.connect(dbname='postgres', user='postgres',
                                     password='ttblue2020', host='localhost')
        """
        # Управление запросами
        # self.cursor = self.conn.cursor()

    def onExit(self):
        self.conn.close()
