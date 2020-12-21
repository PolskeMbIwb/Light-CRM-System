import psycopg2
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from windows import (mainW, err_box, enterui,
                     add_newclintui,
                     add_new_shiftui,
                     add_new_setui,
                     add_new_sanctui,
                     add_new_requestui,
                     add_new_groupui,
                     add_new_equipui,
                     add_new_awardui,
                     reg_diag, login, upd_workui)


class App:
    def __init__(self):
        """
        Подключение к БД, создание курсора для управления запросами
        """
        """
        self.conn = psycopg2.connect(dbname='postgres', user='postgres',
                                     password='ttblue2020', host='localhost')
        self.cursor = self.conn.cursor()
        """
        """
        Инициализация всех окон программы
        """
        self.regW = reg_diag.reg_diag()
        self.loginW = login.login()
        self.mainWin = mainW.mainW()
        self.upd_work = upd_workui.upd_workui()
        self.err = err_box.err_box()
        self.enter = enterui.enter()
        self.add_award = add_new_awardui.new_award()
        self.add_equip = add_new_equipui.new_equip()
        self.add_group = add_new_groupui.new_group()
        self.add_set = add_new_setui.new_set()
        self.add_client = add_newclintui.new_client()
        self.add_sanct = add_new_sanctui.new_sanct()
        self.add_request = add_new_requestui.new_req()
        self.add_shift = add_new_shiftui.new_shift()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
