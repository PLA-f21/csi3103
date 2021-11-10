from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json
import datetime

import matplotlib.pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

widget3_class = uic.loadUiType("btn3_widget.ui")[0]


class Ui_btn3_widget(widget3_class, QtWidgets.QWidget):
    def init(self, id, month):
        if month == 8:
            with open("data/user_data.json") as f:
                user_data = json.load(f)

            self.text_browser_main.clear()
            place_toilet = user_data["place_toilet"][id]
            place_kitchen = user_data["place_kitchen"][id]
            place_living = user_data["place_living"][id]

            for i in reversed(range(self.layout_graph.count())):
                self.layout_graph.itemAt(i).widget().setParent(None)

            self.fig = matplotlib.pyplot.Figure()
            self.canvas = FigureCanvasQTAgg(self.fig)

            self.layout_graph.addWidget(self.canvas)
            ratio = [
                user_data["place_toilet"][id],
                user_data["place_kitchen"][id],
                user_data["place_living"][id],
            ]
            labels = ["Toilet", "Kitchen", "Living room"]

            self.graph = self.canvas.figure.subplots()
            self.graph.pie(
                ratio,
                labels=labels,
                autopct="%.1f%%",
                counterclock=False,
                colors=["#80FF72", "#7EE8FA", "#7FF2BD"],
            )

            self.title_label.setText(str(month) + "월 한 달 돌아보기")

            msg = ""
            max_num = max(ratio)
            if ratio[0] == max_num:
                msg += "화장실에서 가장 많은 시간을 보내셨군요!\n"
                msg += "화장실에서 너무 많은 시간을 보내는건 건강하지 못하다는 증거에요. 검진을 한 번 받아보는게 어때요?\n\n"
            elif ratio[1] == max_num:
                msg += "주방에서 가장 많은 시간을 보내셨군요!\n"
                msg += "혹시 요리사를 준비중이신가요? 순이는 사용자님의 음식이 너무 기대돼요!\n\n"
            elif ratio[2] == max_num:
                msg += "거실에서 가장 많은 시간을 보내셨군요!\n"
                msg += "집 안의 어느 장소보다 가장 넓은 장소! 사용자님의 마음도 바다처럼 넓으실 거에요!\n\n"

            activation_rate = user_data["living_score"][id]["activation_rate"]
            outing_rate = user_data["living_score"][id]["outing_rate"]

            msg += str(month) + " 월달 외출 빈도는 전체 사용자분들 중에서 상위 " + str(outing_rate) + "% 입니다!\n"

            if activation_rate >= 75:
                msg += "다른 분들에 비해 너무 적게 나가시는 것 같아요. 앞으로는 자주 외출하기로 약속!\n\n"
            else:
                msg += "자주 외출을 나가시는 것은 마음을 맑게 해주죠! 앞으로도 자주 나가요!\n\n"

            msg += str(month) + " 월달 활동 점수는 전체 사용자분들 중에서 상위 " + str(activation_rate) + "% 입니다!\n"
            if outing_rate >= 75:
                msg += "다른 분들에 비해 너무 활동이 적으세요. 앞으로는 자주 움직이기로 약속!\n\n"
            else:
                msg += "적절한 신체활동은 건강한 신체로! 건강한 정신으로! 힘차게 생활해요!\n\n"
            self.text_browser_main.append(msg)




        else:
            for i in reversed(range(self.layout_graph.count())):
                self.layout_graph.itemAt(i).widget().setParent(None)
                self.text_browser_main.clear()

            self.title_label.setText(str(month) + "월은 분석할 데이터가 없습니다..")



