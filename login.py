from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
import ast
import os

class AppWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class FirstWindow(Screen):
    pass

class OldUser(Screen):
    pass

class Olduserblank(Screen):
    pass

class Main(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        return Builder.load_file("Registration.kv")

    def log_in(self, username, password):
        # Check if 'database.txt' exists, if not create it
        if not os.path.exists('database.txt'):
            with open('database.txt', 'w') as f:
                f.write("{}")  # Initialize as an empty dictionary

        with open('database.txt') as f:
            data = f.read()

        # Convert the text to a dictionary
        if data:  # Avoid error if the file is empty
            database = ast.literal_eval(data)
        else:
            database = {}

        if username in database:
            # Check if password matches
            if database[username] == password:
                self.root.current = 'AppWindow'  # Go to the App Window if login is successful
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")

    def sign_up(self, password, username):
        # Check if 'database.txt' exists, if not create it
        if not os.path.exists('database.txt'):
            with open('database.txt', 'w') as f:
                f.write("{}")  # Initialize as an empty dictionary

        with open('database.txt') as f:
            data = f.read()

        # Convert the text to a dictionary
        if data:
            database = ast.literal_eval(data)
        else:
            database = {}

        if username not in database:
            # Add the new user to the dictionary
            database[username] = password

            # Save the updated database back to the file
            with open('database.txt', 'w') as data_file:
                data_file.write(str(database))

            self.root.current = 'AppWindow'  # Go to the App Window after sign-up
        else:
            if username + password in database:
                self.root.current = 'OldUser'
            else:
                print("ERROR")


if __name__ == '__main__':
    Main().run()
