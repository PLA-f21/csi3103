from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json

widget1_class = uic.loadUiType("btn1_widget.ui")[0]


class Ui_btn1_widget(widget1_class, QtWidgets.QWidget):
    def change_week(self, week):
        date = ""
        for day in week[:6]:
            date += str(day.month) + "." + str(day.day) + "   "
        date += str(week[6].month) + "." + str(week[6].day)
        self.sleep_range.setText(date)
        self.active_range.setText(date)

    def set_eating_table(self, weak, id):
        for i in range(len(weak)):
            self.eat_table.horizontalHeaderItem(i).setText(str(weak[i].day))

        with open("data/user_data.json") as f:
            user_data = json.load(f)

        for col in range(7):
            day = str(weak[col].day)
            eat_time = user_data["eat_time"][id]["8"][day]
            self.eat_table.item(0, col).setText(eat_time["breakfast"])
            self.eat_table.item(1, col).setText(eat_time["lunch"])
            self.eat_table.item(2, col).setText(eat_time["dinner"])
