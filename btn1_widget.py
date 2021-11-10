from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json

widget1_class = uic.loadUiType("btn1_widget.ui")[0]

class Ui_btn1_widget(widget1_class, QtWidgets.QWidget):
    def change_week(self, week, id):
        date = ''

        with open("data/user_data.json") as f:
            user_data = json.load(f)

        num_sleep = []

        for day in week:
            try:
                num_sleep.append(user_data["sleep_time"][str(id)][str(day.month)][str(day.day)])
            except:
                num_sleep.append({"start" : "0:0", "end" : "0:0"})
                print(0)
            date += "{:^5}  ".format(str(day.month)+ '.' + str(day.day))

        date = date
        self.sleep_range.setText(date)
        self.active_range.setText(date)

        self.draw_sleep(num_sleep)

    def set_deltatime(self, widget, dict):
        map1 = map(int, dict["start"].split(":"))
        map2 = map(int, dict["end"].split(":"))

        if map1[0] > map2[0]:
            map1[0] -= 24

        pos1 = map1[0] * 60 + map1[1]
        pos2 = map2[0] * 60 + map2[1]

        print(pos1, pos2)

        len = pos2 - pos1



    def draw_sleep(self, num_sleep):
        self.set_deltatime(self.sleep_bar_1,num_sleep[0])

