from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
import sys
import pyttsx3
import random


class QuoteApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialize the TTS engine
        self.tts_engine = pyttsx3.init()
        
        # Set up the window
        self.setWindowTitle("Random Quote Generator")
        self.setGeometry(100, 100, 600, 400)
        self.setFixedSize(600, 400)  # Make the window non-resizable
        
        # Quote label
        self.quote_label = QLabel("Click 'Get Quote' to fetch a random quote", self)
        self.quote_label.setWordWrap(True)
        self.quote_label.setFont(QFont("Arial", 14))
        
        # Author label
        self.author_label = QLabel("", self)
        self.author_label.setFont(QFont("Arial", 12))
        self.author_label.setStyleSheet("color: gray;")
        
        # Get Quote button
        self.get_quote_button = QPushButton("Get Quote", self)
        self.get_quote_button.clicked.connect(self.get_quote)
        
        # Read Aloud button
        self.read_aloud_button = QPushButton("Read Aloud", self)
        self.read_aloud_button.clicked.connect(self.read_aloud)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.quote_label)
        layout.addWidget(self.author_label)
        layout.addWidget(self.get_quote_button)
        layout.addWidget(self.read_aloud_button)
        self.setLayout(layout)

    def get_quote(self):
        """Select a random quote from a predefined list and display it."""
        quotes = [
            {"content": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
            {"content": "Success is not the key to happiness. Happiness is the key to success.", "author": "Albert Schweitzer"},
            {"content": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
            {"content": "You miss 100% of the shots you don't take.", "author": "Wayne Gretzky"},
            {"content": "Act as if what you do makes a difference. It does.", "author": "William James"}
        ]

        # Choose a random quote from the list
        quote_data = random.choice(quotes)
        self.quote = quote_data['content']
        self.author = quote_data['author']

        # Update the labels
        self.quote_label.setText(f'"{self.quote}"')
        self.author_label.setText(f"- {self.author}")


    def read_aloud(self):
        """Use TTS to read the current quote."""
        if hasattr(self, 'quote') and hasattr(self, 'author'):
            self.tts_engine.say(f'"{self.quote}" by {self.author}')
            self.tts_engine.runAndWait()
        else:
            self.quote_label.setText("No quote to read")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuoteApp()
    window.show()
    sys.exit(app.exec_())
