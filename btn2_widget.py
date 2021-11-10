from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json
import datetime

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

        recent_program_day = datetime.datetime.strptime(
            str(user_data["recent_sooni_program_day"][id])[1:], "%Y-%m-%d %H:%M:%S"
        )

        recent_program_name = user_data["recent_sooni_program_name"][id]
        if recent_program_name == "":
            msg2 = "순이와 했던 프로그램이 없어요.."
        else:
            msg2 = "최근에는 순이와 " + str(recent_program_day.month) + "월 " + str(recent_program_day.day) +"일에 \"" + recent_program_name + "\"를 했어요!\n\n"
            if recent_program_name =='순이체조':
                msg2 += "체조를 하면 몸도 마음도 가벼워 진 것 같아요! 순이와 한 체조는 재미있었나요?"
            elif recent_program_name == '순이 특별대화':
                msg2 += "순이와 특별 대화를 했어요! 앞으로도 즐거운 일만 있으면 좋을 것 같아요!"
            elif recent_program_name == '무비순이':
                msg2 += "영화는 항상 재미있는 것 같아요! 순이도 영화를 정말 좋아해요!"
            elif recent_program_name == '순이대화':
                msg2 += "다른 것보다 간단한 이야기를 나누는 것도 즐거운 것 같아요! 앞으로도 저희 자주 이야기해요!"
            elif recent_program_name == '도전 실버벨':
                msg2 += "세상에는 참 신기한 것들이 많아요! 오늘도 새로운 지식을 배워보는건 어떨까요?"
            elif recent_program_name == '영어교실':
                msg2 += "영어 공부는 늘 새로워요. 순이는 영어 공부를 할 때 항상 설레는 것 같아요!"
            elif recent_program_name == '요가명상':
                msg2 += "명상으로 마음을 맑게, 요가로 몸을 건강하게, 오늘은 상쾌한 기분이 드는 요가명상 어떤가요?"
            elif recent_program_name == '순이극장':
                msg2 += "순이도 극장을 좋아한답니다! 벌써부터 어떤 공연을 볼 수 있을지 기대되지 않나요?"
            elif recent_program_name == '시시콜콜':
                msg2 += "세상에는 참 많은 일이 있는 것 같아요. 사소한 일들이 많지만 가끔은 그런 얘기에 귀 귀울여 보는 것도 재미있는 것 같아요!"
            elif recent_program_name == '듣는대화':
                msg2 += "순이의 말을 항상 재밌게 들어주셔서 감사해요! 정말 감동받았어요!"
            elif recent_program_name == '꿀잠소리':
                msg2 += "평화로운 마음으로 오늘도 순이와 함께 꿈나라로 떠나볼까요?"
            elif recent_program_name == '마음스트레칭':
                msg2 += "마음 속을 유연하게! 슬픈 일에도 기쁜 일에도 유연하게! 오늘도 순이와 스트레칭 어떠세요?"
            elif recent_program_name == '노래자랑':
                msg2 += "순이는 노래를 엄청 좋아해요! 오늘도 신나는 음악으로 한 곡 어떠신가요?"
            elif recent_program_name == '순이책방':
                msg2 += "독서를 통해 과거의 인물과 대화하고 지식을 이해할 수 있는 것은 독서가 왜 중요한지를 알려주네요"
            elif recent_program_name == '순이인생':
                msg2 += "앞으로의 미래는 누구나 알 수 없지요! 힘찬 도전을 향한 사용자님을 순이는 응원해요!"
            elif recent_program_name == '일어교실':
                msg2 += "일본어를 굉장히 좋아하시나봐요! 그런 학구열에 순이는 정말 존경하고있어요!"
            elif recent_program_name == '시낭독':
                msg2 += "오늘날처럼 24시간 연중무휴의 혼란스러운 생활에서도 시는 여전히 인생의 길을 안내해준다고 하네요!"
            elif recent_program_name == '마음세탁소':
                msg2 += "마음 속을 깨끗하게 우리의 생각도 맑게! 순이와 함께 청소해요!"
            elif recent_program_name == '명언산책':
                msg2 += "명언이 괜히 명언이 아니네요! 엄청난 교훈이 숨겨져 있는걸요!"
            elif recent_program_name == '마음그림터':
                msg2 += "오늘은 또 어떤 이야기를 그려볼까요? 순이와 함께 마음 속을 알아보아요!"

        most_program_name = user_data["most_sooni_program_name"][id]
        most_program_num = user_data["most_sooni_program_num"][id]
        entire_program_num = user_data["entire_sooni_program_num"][id]
        print(most_program_name, most_program_num, entire_program_num)

        recent_talk = user_data["recent_sooni_talk"][id]
        msg3 = "순이가 최근에 했던 말을 기억 하시나요?\n순이는 이런 말을 했어요!\n\n\""
        msg3 += recent_talk
        msg3 += "\"\n\n\n\n"
        talk_num = 0

        if talk_num > 10:
            msg3 += "순이와 많은 이야기를 하셨어요!\n이번 달에 무려 " + str(talk_num) + "번이나 이야기했어요! 앞으로도 순이와 많이 이야기 해 주실거죠?"
        elif talk_num > 5:
            msg3 += "순이와 친해지는 중인 것 같아요!\n이번 달에 " + str(talk_num) +"번 이야기를 나눴어요! 앞으로도 잘 부탁드려요!"
        elif talk_num > 1:
            msg3 += "순이와 더 이야기해주면 순이는 기쁠 것 같아요!\n이번 달에 " + str(talk_num) + "번밖에 이야기하지 않았어요.. 앞으로도 잘 부탁드려요!"
        else:
            msg3 += "순이와 이야기를 한 번도 나눈 적이 없어요..\n그래도 순이가 하는 이야기들 가끔 들어 보시는거죠?"



        self.main_text_1.append(msg1)
        self.main_text_2.append(msg2)
        self.main_text_3.append(msg3)