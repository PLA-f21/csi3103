from PyQt5 import QtCore, QtGui, QtWidgets, uic

widget1_class = uic.loadUiType("btn1_widget.ui")[0]

class Ui_btn1_widget(widget1_class, QtWidgets.QWidget):
    def change_week(self, week):
        for day in week:
            print(day.day)
