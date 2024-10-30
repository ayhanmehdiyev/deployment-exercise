from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
import sys
import requests
import pyttsx3

class QuoteApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialize the TTS engine
        self.tts_engine = pyttsx3.init()
        
        # Set up the window
        self.setWindowTitle("Random Quote Generator")
        self.setGeometry(100, 100, 800, 600)
        
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
        """Fetch a random quote from the API and display it."""
        try:
            response = requests.get("https://api.quotable.io/random", verify=False)
            if response.status_code == 200:
                quote_data = response.json()
                self.quote = quote_data['content']
                self.author = quote_data['author']
                self.quote_label.setText(f'"{self.quote}"')
                self.author_label.setText(f"- {self.author}")
            else:
                self.quote_label.setText("Failed to retrieve quote")
        except requests.exceptions.RequestException as e:
            self.quote_label.setText("Error fetching quote")
            print("Error:", e)

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
