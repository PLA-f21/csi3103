from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json
import numpy

widget1_class = uic.loadUiType("btn1_widget.ui")[0]


class Ui_btn1_widget(widget1_class, QtWidgets.QWidget):
    def change_week(self, week, id):
        date = " "

        with open("data/user_data.json") as f:
            user_data = json.load(f)

        num_sleep = []
        num_active = []
        start_label = "  "
        end_label = "  "
        num_out_time = "  "
        self.sleep_start_numpy = []
        self.sleep_end_numpy = []
        self.sleep_len_numpy = []
        self.active_numpy = []

        for day in week:
            try:
                num_sleep.append(
                    user_data["sleep_time"][id][str(day.month)][str(day.day)]
                )
                start_label += "{:^5}  ".format(
                    user_data["sleep_time"][id][str(day.month)][str(day.day)][
                        "start"
                    ]
                )
                end_label += "{:^5}  ".format(
                    user_data["sleep_time"][id][str(day.month)][str(day.day)][
                        "end"
                    ]
                )
            except:
                num_sleep.append({"start": "18:0", "end": "18:0"})
                start_label += "       "
                end_label += "       "

            try:
                num_active.append(
                    user_data["out_time"][id][str(day.month)][str(day.day)]
                )
                if user_data["out_time"][id][str(day.month)][str(day.day)]:
                    num_out_time += "{:^5}  ".format(
                        self.cal_min_to_str(
                            user_data["out_time"][id][str(day.month)][str(day.day)]
                        )
                    )
                    self.active_numpy.append(user_data["out_time"][id][str(day.month)][str(day.day)])
                else:
                    num_out_time += "       "
            except:
                num_active.append(0)
                num_out_time += "       "

            date += "{:^5}  ".format(str(day.month) + "." + str(day.day))

        date = date[:-2]
        self.sleep_start_label.setText(start_label)
        self.sleep_end_label.setText(end_label)
        self.sleep_range.setText(date)
        self.active_range.setText(date)
        self.active_time_label.setText(num_out_time)

        self.draw_active(num_active)
        self.draw_sleep(num_sleep)
        self.set_sleep_text()
        self.set_active_text()

    def set_sleep_text(self):
        if not (len(self.sleep_start_numpy) == 0 or len(self.sleep_end_numpy) == 0 or len(self.sleep_len_numpy) == 0):
            start = numpy.std(self.sleep_start_numpy)
            end = numpy.std(self.sleep_end_numpy)
            len_mean = numpy.mean(self.sleep_len_numpy)

            msg = ""
            if start == 0 or start and end == 0:
                msg += "????????? ????????? ???????????? "
            else:
                if start < 30:
                    msg += "?????? ????????? ?????? ??????????????????! "
                elif start > 150:
                    msg += "?????? ????????? ?????? ???????????????! "

                if end < 30:
                    msg += "?????? ????????? ?????? ??????????????????! "
                elif end > 150:
                    msg += "?????? ????????? ?????? ???????????????! "

                msg += "?????? ?????? ??????????????? " + str(int(len_mean / 60)) + "?????? " + str(int(len_mean) % 60) + "????????????. "
                if len_mean > 480 :
                    msg += "????????? ?????? ????????? ????????? ?????????! ????????? ?????? ????????? ?????? ???????????? ??????????????? ????????????? "
                elif 420 < len_mean:
                    msg += "????????? ?????? ????????? ????????? ?????????!"
                elif len_mean < 360:
                    msg += "??????????????? 6?????? ???????????? ???????????? ????????? ?????? ????????? ??????????????? ??????. 7?????? ????????? ????????? ????????? ????????? ?????? ???????????????. "
                else:
                    msg += "????????? ?????? ??????????????? ????????????, ?????? ????????????????????? ?????? ?????? ?????? ?????????! ?????? ??????????????? 7???????????? 8?????? ???????????? ??????. "

            self.text_browser_sleep.append(msg)
        else:
            self.text_browser_sleep.clear()

    def set_active_text(self):
        self.text_browser_active.clear()
        sum = numpy.sum(self.active_numpy)
        msg = ""

        msg += "?????? ?????? " + str(int(sum / 60)) + "?????? " + str(int(sum % 60)) + "??? ?????? ???????????????!\n"
        if sum > 360:
            msg += "?????? ????????? ????????????! ????????? ????????? ?????? ?????? ??? ?????????.\n"
        elif sum < 180:
            msg += "?????? ????????? ????????????. ????????? ??????????????? ????????? ???????????? ??? ????????????!\n"

        if len(self.active_numpy) < 3 :
            msg += "?????? ????????? ????????????. ?????? ?????? ????????? ????????? ???????????? ?????? ????????????? "

        self.text_browser_active.append(msg)


    def set_deltatime_bar(self, widget, dict):
        map1 = list(map(int, dict["start"].split(":")))
        map2 = list(map(int, dict["end"].split(":")))

        if map1[0] >= 18:
            map1[0] -= 24
        if map2[0] >= 18:
            map2[0] -= 24

        pos1 = (map1[0] + 6) * 60 + map1[1]
        pos2 = (map2[0] + 6) * 60 + map2[1]
        if pos1 and pos2:
            self.sleep_start_numpy.append(pos1)
            self.sleep_end_numpy.append(pos2)
            self.sleep_len_numpy.append(pos2 - pos1)

        ypos = float(720 - pos2) * 81 / 720 + 100
        len = (pos2 - pos1) * 81 / 720

        widget.setGeometry(widget.pos().x(), ypos, widget.size().width(), len)

    def draw_sleep(self, num_sleep):
        self.set_deltatime_bar(self.sleep_bar_1, num_sleep[0])
        self.set_deltatime_bar(self.sleep_bar_2, num_sleep[1])
        self.set_deltatime_bar(self.sleep_bar_3, num_sleep[2])
        self.set_deltatime_bar(self.sleep_bar_4, num_sleep[3])
        self.set_deltatime_bar(self.sleep_bar_5, num_sleep[4])
        self.set_deltatime_bar(self.sleep_bar_6, num_sleep[5])
        self.set_deltatime_bar(self.sleep_bar_7, num_sleep[6])

    def cal_min_to_str(self, min):
        hour = str(int(min / 60))
        min = str(int(min) % 60)
        return str(hour) + ":" + str(min)

    def set_active_bar(self, widget, num):
        len = num * 81 / 720
        ypos = 160 - len
        widget.setGeometry(widget.pos().x(), ypos, widget.size().width(), len)

    def draw_active(self, num_active):
        self.set_active_bar(self.active_bar_1, num_active[0])
        self.set_active_bar(self.active_bar_2, num_active[1])
        self.set_active_bar(self.active_bar_3, num_active[2])
        self.set_active_bar(self.active_bar_4, num_active[3])
        self.set_active_bar(self.active_bar_5, num_active[4])
        self.set_active_bar(self.active_bar_6, num_active[5])
        self.set_active_bar(self.active_bar_7, num_active[6])

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

    def set_living_score(self, id):
        with open("data/user_data.json") as f:
            user_data = json.load(f)

        living_score = user_data["living_score"][id]["score"]
        worst = user_data["living_score"][id]["worst"]

        if living_score > 79:
            msg = "?????? ???????????? ????????? ?????? ?????? ??? ?????????!\n ????????? ????????? ????????????, ????????? ?????? ????????? ??????????????? ?????? ?????? ?????????!"
        elif worst == "activation_score":
            msg = f"?????? ???????????? ????????? ??????????????? ????????? ???????????????!\n ??????????????? ??????????????? ?????? {user_data['living_score'][id]['activation_rate']}%??????!"
        elif worst == "outing_score":
            msg = f"?????? ???????????? ????????? ??????????????? ????????? ???????????????!\n ??????????????? ??????????????? ?????? {user_data['living_score'][id]['outing_rate']}%??????!"
        elif worst == "pill_score":
            msg = "?????? ????????? ????????? ??????????????? ????????? ??????!"
        elif worst == "snack_score":
            msg = "???????????? ?????? ???????????? ?????? ?????? ????????????! ?????? ?????? ?????? ???????????????!"
        else:
            msg = ""
        rank = 0
        my_score = user_data["living_score"][id]["score"]  # id example) id = "228"
        for uid in user_data["living_score"].keys():
            if (
                float(my_score) <= float(user_data["living_score"][uid]["score"])
            ) and uid != "average":
                rank += 1

        rate = rank * 100 // (len(user_data["living_score"]) - 1)

        msg += f"\n\n??????????????? ??????????????? ?????? {rate}%??????!"
        self.text_browser_score.append(str(living_score))
        self.text_browser_total.append(msg)
