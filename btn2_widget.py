from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json

widget1_class = uic.loadUiType("btn2_widget.ui")[0]


class Ui_btn2_widget(widget1_class, QtWidgets.QWidget):
    def change_week(self, week, id):
        pass