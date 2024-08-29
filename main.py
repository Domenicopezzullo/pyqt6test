import sys
import requests
from PyQt6.QtWidgets import QLabel, QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = QLabel("US Debt Fetcher", self)
        self.button = QPushButton("Fetch Debt", self)
        self.debtlabel = QLabel("0", self)
        self.InitUI()

    def InitUI(self):
        # Window properties
        self.setFixedSize(500, 175)
        self.setWindowTitle("US Debt Fetcher")

        # Title label
        self.title.setGeometry(0, 10, 500, 40)
        self.title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # Debt label
        self.debtlabel.setGeometry(200, 50, 100, 40)
        self.debtlabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Fetch button
        self.button.setGeometry(200, 100, 100, 40)
        self.button.clicked.connect(self.buttonclick)  # Connecting button click

    def buttonclick(self):
        try:
            url = "https://global-economy-analytics.p.rapidapi.com/usNationalDebt"
            headers = {
                "x-rapidapi-key": "72bca9a31fmsh9987779364c1b79p12dcffjsn39416790287e",
                "x-rapidapi-host": "global-economy-analytics.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers)
            data = response.json()
            debt_value = data.get("usNationalDebt", "N/A")
            self.debtlabel.setText(debt_value)
            self.debtlabel.setGeometry(185, 50, 100, 40)
            self.debtlabel.adjustSize()
        except Exception as e:
            self.debtlabel.setText("Error fetching data")
            print(f"Error: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
