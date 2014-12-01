from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock
import json
import random
import urllib2
import inspect, os

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
		self.questions_python = []
		self.questions_ruby = []
		self.questions_csharp = []
		self.read_questions()

	def get_question_javascript(self):
		return self.questions_javascript[random.randint(0, len(self.questions_javascript) - 1 )]

	def get_question_ruby(self):
		return self.questions_ruby[random.randint(0, len(self.questions_ruby) - 1 )]

	def get_question_csharp(self):
		return self.questions_csharp[random.randint(0, len(self.questions_csharp) - 1 )]

	def get_question_python(self):
		return self.questions_python[random.randint(0, len(self.questions_python) - 1 )]

	def read_questions(self):		
		with open(os.getcwd()+'/questions/questions.json') as json_file:
			json_data = json.load(json_file)
			
			for q in json_data:
				if(q["category"] =="ruby"):
					self.questions_ruby.append(Question(q["quest"], q["answer"], q["option2"], q["option3"], q["option4"], q["explanation"]))
				elif(q["category"]== "python"):
					self.questions_python.append(Question(q["quest"], q["answer"], q["option2"], q["option3"], q["option4"], q["explanation"]))
				elif(q["category"] == "javascript"):
					self.questions_javascript.append(Question(q["quest"], q["answer"], q["option2"], q["option3"], q["option4"], q["explanation"]))
				elif(q["category"] == "csharp"):
					self.questions_csharp.append(Question(q["quest"], q["answer"], q["option2"], q["option3"], q["option4"], q["explanation"]))
				else:
					print("else")		

	def update(self):
		url = 'http://apiquiz.herokuapp.com/export.json'
		response = urllib2.urlopen(url)
		data = json.load(response)

		with open(os.getcwd()+'/questions/questions.json', 'w') as outfile:
			json.dump(data, outfile)

		print(os.getcwd())

		



