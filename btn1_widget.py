from PyQt5 import QtCore, QtGui, QtWidgets, uic

widget1_class = uic.loadUiType("btn1_widget.ui")[0]

class Ui_btn1_widget(widget1_class, QtWidgets.QWidget):
    def change_week(self, week):
        date = ''
        for day in week[:6]:
            date += str(day.month)+ '.' + str(day.day) + '   '
        date += str(week[6].month) + '.' + str(week[6].day)
        self.sleep_range.setText(date)
        self.active_range.setText(date)
