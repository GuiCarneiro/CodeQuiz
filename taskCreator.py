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
            explanation_1 = question_javascript.explanation

        elif mode == 2:
            question_ruby = self.questions.get_question_ruby()
            question_1 = question_ruby.question
            answers_1 = question_ruby.answer
            option_1 = question_ruby.answer
            option_2 = question_ruby.option2
            option_3 = question_ruby.option3
            option_4 = question_ruby.option4            
            explanation_1 = question_ruby.explanation
        elif mode == 3:
            question_python = self.questions.get_question_python()
            question_1 = question_python.question
            answers_1 = question_python.answer
            option_1 = question_python.answer
            option_2 = question_python.option2
            option_3 = question_python.option3
            option_4 = question_python.option4            
            explanation_1 = question_python.explanation
        elif mode == 4:
            question_csharp = self.questions.get_question_csharp()
            question_1 = question_csharp.question
            answers_1 = question_csharp.answer
            option_1 = question_csharp.answer
            option_2 = question_csharp.option2
            option_3 = question_csharp.option3
            option_4 = question_csharp.option4            
            explanation_1 = question_csharp.explanation


        operands = [question_1, answers_1]
        answers = [option_1, option_2, option_3, option_4]
        random.shuffle(answers)
        whole_task = operands + answers + [explanation_1]
        return whole_task

