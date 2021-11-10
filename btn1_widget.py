from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json

widget1_class = uic.loadUiType("btn1_widget.ui")[0]


class Ui_btn1_widget(widget1_class, QtWidgets.QWidget):
    def change_week(self, week, id):
        date = " "

        with open("data/user_data.json") as f:
            user_data = json.load(f)

        num_sleep = []
        start_label = "  "
        end_label = "  "

        for day in week:
            try:
                num_sleep.append(
                    user_data["sleep_time"][str(id)][str(day.month)][str(day.day)]
                )
                start_label += "{:^5}  ".format(
                    user_data["sleep_time"][str(id)][str(day.month)][str(day.day)][
                        "start"
                    ]
                )
                end_label += "{:^5}  ".format(
                    user_data["sleep_time"][str(id)][str(day.month)][str(day.day)][
                        "end"
                    ]
                )
            except:
                num_sleep.append({"start": "18:0", "end": "18:0"})
                start_label += "       "
                end_label += "       "
            date += "{:^5}  ".format(str(day.month) + "." + str(day.day))

        date = date[:-2]
        self.sleep_start_label.setText(start_label)
        self.sleep_end_label.setText(end_label)
        self.sleep_range.setText(date)
        self.active_range.setText(date)

        self.draw_sleep(num_sleep)

    def set_deltatime(self, widget, dict):
        map1 = list(map(int, dict["start"].split(":")))
        map2 = list(map(int, dict["end"].split(":")))

        if map1[0] >= 18:
            map1[0] -= 24
        if map2[0] >= 18:
            map2[0] -= 24

        pos1 = (map1[0] + 6) * 60 + map1[1]
        pos2 = (map2[0] + 6) * 60 + map2[1]

        ypos = float(720 - pos2) * 81 / 720 + 100
        len = (pos2 - pos1) * 81 / 720

        widget.setGeometry(widget.pos().x(), ypos, widget.size().width(), len)

    def draw_sleep(self, num_sleep):
        self.set_deltatime(self.sleep_bar_1, num_sleep[0])
        self.set_deltatime(self.sleep_bar_2, num_sleep[1])
        self.set_deltatime(self.sleep_bar_3, num_sleep[2])
        self.set_deltatime(self.sleep_bar_4, num_sleep[3])
        self.set_deltatime(self.sleep_bar_5, num_sleep[4])
        self.set_deltatime(self.sleep_bar_6, num_sleep[5])
        self.set_deltatime(self.sleep_bar_7, num_sleep[6])


    def set_eating_table(self, week, id):
        for i in range(len(week)):
            self.eat_table.horizontalHeaderItem(i).setText(str(week[i].day))

        with open("data/user_data.json") as f:
            user_data = json.load(f)

            for col in range(7):
                month = str(week[col].month)
                day = str(week[col].day)
                try:
                    eat_time = user_data["eat_time"][id][month][day]
                    self.eat_table.item(0, col).setText(eat_time["breakfast"])
                    self.eat_table.item(1, col).setText(eat_time["lunch"])
                    self.eat_table.item(2, col).setText(eat_time["dinner"])
                except:
                    pass

