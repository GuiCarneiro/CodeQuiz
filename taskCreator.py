from question import *

class TaskCreator():
    def __init__(self):
        self.questions = ListQuestions()

    def get_task(self, mode=1):
        question_1 = ""
        answers_1 = ""
        option_1 = ""
        option_2 = ""
        option_3 = ""
        option_4 = ""

        if mode == 1:
            question_javascript = self.questions.get_question_javascript()

            question_1 = question_javascript.question
            answers_1 = question_javascript.answer
            option_1 = question_javascript.answer
            option_2 = question_javascript.option2
            option_3 = question_javascript.option3
            option_4 = question_javascript.option4
        elif mode == 2:
            question_1 = "random.randint(0, 5)"
            answers_1 = "random.randint(0, 5)"
            option_1 = answers_1
            option_2 = "1"
            option_3 = "1"
            option_4 = "3"
        elif mode == 3:
            question_1 = "random.randint(0, 5)"
            answers_1 = "random.randint(0, 5)"
            option_1 = answers_1
            option_2 = "1"
            option_3 = "1"
            option_4 = "3"
        elif mode == 4:
            question_1 = "random.randint(0, 5)"
            answers_1 = "random.randint(0, 5)"
            option_1 = answers_1
            option_2 = "1"
            option_3 = "1"
            option_4 = "3"


        operands = [question_1, answers_1]
        answers = [option_1, option_2, option_3, option_4]
        random.shuffle(answers)
        whole_task = operands + answers
        return whole_task

