from PyQt5.QtWidgets import QApplication, QWidget
from random import choice, shuffle
app = QApplication([])

from main_window import*

class Question():
    def __init__(self, question, cor_unswer, wrong_unswer1,wrong_unswer2, wrong_unswer3):
        self.question = question
        self.answer = cor_unswer
        self.wrong_answer1 = wrong_unswer1
        self.wrong_answer2 = wrong_unswer2
        self.wrong_answer3 = wrong_unswer3
        self.attempts = 0
        self.correct = 0
    
    def got_right(self):
        self.attempts += 1
        self.correct += 1
        # print('Це правильна відповідь!')

    def got_wrong(self):
        self.attempts += 1
        # print("Відповідь невірна")


q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

questions = [q1, q2, q3, q4]
random_question = choice(questions)
# print(random_question)
def clear_rbnt():
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_question(current_question):
    clear_rbnt()
    
    AnswerBox.hide()
    RadioGroupBox.show()
    
    lb_quest.setText(current_question.question)
    
    radio_list = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
    shuffle(radio_list)

    global answer
    answer = radio_list[0]
    wrong_answer1 = radio_list[1]
    wrong_answer2 = radio_list[2]
    wrong_answer3 = radio_list[3]

    answer.setText(current_question.answer)
    wrong_answer1.setText(current_question.wrong_answer1)
    wrong_answer2.setText(current_question.wrong_answer2)
    wrong_answer3.setText(current_question.wrong_answer3)

    btn_ok.setText('Відповісти')

def check_answer():
    RadioGroupBox.hide()
    AnswerBox.show()
    btn_ok.setText('Наступне')

    if  answer.isChecked():
        lb_result.setText('Відповідь вірна!')
        lb_correct.setText(answer.text())
    else:
        lb_result.setText('Відповідь НЕ вірна!')
        lb_correct.setText(answer.text())

def click_OK():
    if btn_ok.text() == 'Відповісти':
        check_answer()
    else:
        random_question = choice(questions)
        show_question(random_question)




window_width = 650
window_height = 500
question_window = QWidget()
question_window.resize(window_width,window_height)
question_window.move(300,300)
question_window.setWindowTitle("Memory Card")

question_window.setLayout(main_v_layout)

show_question(random_question)
btn_ok.clicked.connect(click_OK)

question_window.show()
app.exec_()