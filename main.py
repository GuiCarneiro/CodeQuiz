from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.graphics import Color
import time
import threading
import thread
from taskCreator import *


# Declare both screens
class MenuScreen(Screen):
    sound = SoundLoader.load("sounds/click.ogg")

    def click_sound(self):        
        self.sound.play()


class StartScreen(Screen):
    sound = SoundLoader.load("sounds/click.ogg")

    def click_sound(self):        
        self.sound.play()


class ProgressScreen(Screen):
    sound = SoundLoader.load("sounds/click.ogg")

    def click_sound(self):        
        self.sound.play()


class GameActionScreen(Screen):
    errors_made = 0
    round_number = 1
    max_rounds = 10

    task_values = [0, 0, 0, 0, 0, 0]

    current_mode = 1

    def new_game(self):
        self.Tasks = TaskCreator()
        self.round_number = 0
        t1 = threading.Thread(target=self.load_sounds)
        t1.start()
        self.set_next_task()

    def set_next_task(self):
        self.task_values = self.Tasks.get_task(self.current_mode)

        self.ids.task.text = self.task_values[0]
        self.ids.button_1.text = str(self.task_values[2])
        self.ids.button_2.text = str(self.task_values[3])
        self.ids.button_3.text = str(self.task_values[4])
        self.ids.button_4.text = str(self.task_values[5])

        self.ids.label_1.text = "Errors: " + str(self.errors_made)
        self.ids.label_2.text = str(self.current_mode) + str(self.current_mode)
        self.ids.label_3.text = str(self.round_number) + " / " + str(self.max_rounds)

        #set all the button backgrounds back to normal
        self.ids.button_1.background_normal = "./data/normal.png"
        self.ids.button_2.background_normal = "./data/normal.png"
        self.ids.button_3.background_normal = "./data/normal.png"
        self.ids.button_4.background_normal = "./data/normal.png"

    def check_answer(self, button_pressed):
        if self.round_number == self.max_rounds:
            self.manager.current = 'result'
        elif button_pressed.text == self.task_values[1]:
            t1 = threading.Thread(target=self.correct_sound)
            t1.start()

            button_pressed.background_normal = './data/correct.png'

            self.round_number += 1
            self.ids.label_3.text = str(self.round_number) + " / " + str(self.max_rounds)
            
            t2 = threading.Thread(target=self.response)
            t2.start()
        else:
            t1 = threading.Thread(target=self.wrong_sound)
            t1.start()


            self.round_number += 1
            self.ids.label_3.text = str(self.round_number) + " / " + str(self.max_rounds)
            self.errors_made += 1
            self.ids.label_1.text = "Errors: " + str(self.errors_made)
            self.ids.task.markup = True
            self.ids.task.text = '[color=#ff3333]'+self.ids.task.text+'[/color]'
            button_pressed.background_normal = './data/error.png'

            t2 = threading.Thread(target=self.response)
            t2.start()


    def load_sounds(self):
        self.sounds = {}
        self.sounds[0] = SoundLoader.load("sounds/correct.ogg")
        self.sounds[1] = SoundLoader.load("sounds/wrong.ogg")

    def correct_sound(self):
        self.sounds[0].play()

    def wrong_sound(self):
        self.sounds[1].play()

    def response(self):        
        time.sleep(1)
        self.set_next_task()





class ResultScreen(Screen):
    sound = SoundLoader.load("sounds/click.ogg")

    def click_sound(self):
        self.sound.play()

    def calculate_result(self, screen):
        if screen.errors_made <= 1:
            self.ids.star_3.source = './data/star.png'
            self.ids.star_2.source = './data/star.png'
            self.ids.star_1.source = './data/star.png'
            self.ids.label.text = 'Excellent!\n\n'
        elif screen.errors_made <= 3:
            self.ids.star_2.source = './data/star.png'
            self.ids.star_1.source = './data/star.png'
            self.ids.label.text = 'Very good!\n\n Close to perfect. Keep up!'
        elif screen.errors_made <= 5:
            self.ids.star_1.source = './data/star.png'
            self.ids.label.text = 'Good!\n\n Train more!'
        else:
            self.ids.label.text = 'Okay...\n\n Try again to get all the stars!'


class HelpScreen(Screen):
    sound = SoundLoader.load("sounds/click.ogg")

    def click_sound(self):        
        self.sound = SoundLoader.load("sounds/click.ogg")
        self.sound.play()

    def help_text(self):
        return "Here i will provide simple tricks to become faster when\n" \
               "doing mental calculations.\n" \
               "Example: Instead of adding 5 to a digit greater than 5,\n" \
               "its often more simple to subtract 5 and then add 10.\n" \
               " 8 + 5 = ?\n" \
               " 8 - 5 = 3; 3 + 10 = 13\n" \
               "\n"\
               "Or add in two steps, first to get to an more easy number, \n" \
               "then whatever remains.\n" \
               "More will follow soon!\n"


class AboutScreen(Screen):
    sound = SoundLoader.load("sounds/click.ogg")

    def click_sound(self):        
        self.sound.play()

    def about_text(self):
        return "Made by: Jonas\n" \
               "Open source and free of charge \n" \
               "\n" \
               "Features:\n" \
               "  - simple\n" \
               "  - rewarding\n" \
               "  - perfect for kids in elementary school\n" \
               "  - or adults who want to train their brain ;)\n" \
               "  - never gets old, new content is generated procedurally\n" \
               "  - written in Python with the help of Kivy"

class PopUpQuit(Popup):
    pass


class GameApp(App):

    sm = ScreenManager(transition=FadeTransition())

    def build(self):
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(StartScreen(name='start'))
        self.sm.add_widget(ProgressScreen(name='progress'))
        self.sm.add_widget(HelpScreen(name='help'))
        self.sm.add_widget(AboutScreen(name='about'))
        self.sm.add_widget(GameActionScreen(name='game'))
        self.sm.add_widget(ResultScreen(name='result'))
        #Bind to keyboard to make the back button under android work
        Window.bind(on_keyboard=self.handle_keyboard)

        self.title = 'ComputerScienceQuiz'

        return self.sm

    def handle_keyboard(self, window, key, *largs):
        #keycode 273 equals up button, just for test purposes
        if key == 27 or key == 273:
            if self.sm.current_screen.name == 'game':
                popup = PopUpQuit()
                popup.open()
            elif self.sm.current_screen.name == 'menu':
                quit()

            return True


if __name__ == '__main__':
    GameApp().run()