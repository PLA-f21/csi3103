from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json

widget1_class = uic.loadUiType("btn2_widget.ui")[0]


class Ui_btn2_widget(widget1_class, QtWidgets.QWidget):
    def init(self, id, month):
        with open("data/user_data.json") as f:
            user_data = json.load(f)
        if month == 8:
            self.title_label.setText("8월은 참 더웠어요!")
        else:
            self.title_label.setText(str(month) + "월은 분석할 데이터가 없어요..")

        self.main_text_1.clear()
        self.main_text_2.clear()
        self.main_text_3.clear()

        msg1 = ""

        recent_program_day = user_data["recent_sooni_program_day"][id]
        recent_program_name = ""

        msg2 = ""


        recent_talk = user_data["recent_sooni_talk"][id]
        msg3 = "순이가 최근에 했던 말을 기억 하시나요?\n순이는 이런 말을 했어요!\n\n\""
        msg3 += recent_talk
        msg3 += "\"\n\n"
        talk_num = 0

        if talk_num > 10:
            msg3 += "순이와 많은 이야기를 하셨어요!\n이번 달에 무려 " + str(talk_num) + "번이나 이야기했어요! 앞으로도 순이와 많이 이야기 해 주실거죠?"
        elif talk_num > 5:
            msg3 += "순이와 친해지는 중인 것 같아요!\n이번 달에 " + str(talk_num) +"번 이야기를 나눴어요! 앞으로도 잘 부탁드려요!"
        elif talk_num > 1:
            msg3 += "순이와 더 이야기해주면 순이는 기쁠 것 같아요!\n이번 달에 " + str(talk_num) + "번밖에 이야기하지 않았어요.. 앞으로도 잘 부탁드려요!"
        else:
            msg3 += "순이와 이야기를 한 번도 나눈 적이 없어요.. 그래도 순이가 하는 이야기들 가끔 들어 보시는거죠?"



        self.main_text_1.append(msg1)
        self.main_text_2.append(msg2)
        self.main_text_3.append(msg3)