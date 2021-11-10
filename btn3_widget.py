from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json
import datetime

widget3_class = uic.loadUiType("btn3_widget.ui")[0]


class Ui_btn3_widget(widget3_class, QtWidgets.QWidget):
    def init(self, id, month):
        pass
