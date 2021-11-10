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

            place_toilet = user_data["place_toilet"][id]
            place_kitchen = user_data["place_kitchen"][id]
            place_living = user_data["place_living"][id]

            for i in reversed(range(self.layout_graph.count())):
                self.layout_graph.itemAt(i).widget().setParent(None)

            self.fig = matplotlib.pyplot.Figure()
            self.canvas = FigureCanvasQTAgg(self.fig)

            self.layout_graph.addWidget(self.canvas)
            ratio = [user_data["place_toilet"][id], user_data["place_kitchen"][id], user_data["place_living"][id]]
            labels = ['Toilet', 'Kitchen', 'Living room']

            self.graph = self.canvas.figure.subplots()
            self.graph.pie(ratio, labels=labels, autopct='%.1f%%', counterclock=False, colors=["#80FF72", "#7EE8FA", "#7FF2BD"])


            self.title_label.setText(str(month) + "월 한 달 돌아보기")
        else:
            for i in reversed(range(self.layout_graph.count())):
                self.layout_graph.itemAt(i).widget().setParent(None)

            self.title_label.setText(str(month) + "월은 분석할 데이터가 없습니다..")



