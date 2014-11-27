from questions.javascript import *
import random

class Question():
	def __init__(self, question, answer, option2, option3, option4, explanation):
		self.question = question
		self.answer = answer
		self.option2 = option2
		self.option3 = option3
		self.option4 = option4
		self.explanation = explanation

class ListQuestions():
	def __init__(self, directory = "/questions"):
		self.directory = directory
		self.questions_javascript = []
		for question in javascript:
			self.questions_javascript.append(Question(question[0], question[1], question[2], question[3], question[4], question[5]))

	def get_question_javascript(self):
		return self.questions_javascript[random.randint(0, len(self.questions_javascript) - 1 )]
