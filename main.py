from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit, QLineEdit, QPushButton
from backend import Chatbot
import sys
import threading

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setWindowTitle("Chatbot")
        self.setMinimumSize(800, 600)
        self.setContentsMargins(20, 20, 20, 20)

        self.setStyleSheet("QPushButton {font: 12pt Hack Nerd Font}")
        self.setStyleSheet("QTextEdit {font: 10pt Hack Nerd Font}")
        self.setStyleSheet("QLineEdit {font: 10pt Hack Nerd Font}")

        # Add chat area
        self.chatarea = QTextEdit(self)
        self.chatarea.setGeometry(10, 10, 480, 320)
        self.chatarea.setReadOnly(True)

        # Add Input area
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add button
        self.submit_button = QPushButton("Send?", self)
        self.submit_button.setGeometry(500, 340, 100, 40)
        self.submit_button.clicked.connect(self.send_message)
        
        self.show()
    
    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chatarea.append(f"<p style='color:#333333>'Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chatarea.append(f"<p style='color:#333333l background-color:#E9E9E9'>Bot: {response}</p>")

app = QApplication(sys.argv)
main_window = ChatbotWindow()
main_window.show()
# main_window.load_data()
sys.exit(app.exec())