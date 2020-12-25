import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from windows import enterui


def main():
    app = QtWidgets.QApplication(sys.argv)
    enter = enterui.enter()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
