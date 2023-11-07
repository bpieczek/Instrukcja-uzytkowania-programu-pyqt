from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5 import uic
import sys
import random

class RandomNumberApp(QWidget):
    def __init__(self):
       super().__init__()
       uic.loadUi('generator.ui', self)

       self.generate_button.clicked.connect(self.generate_numbers)
       self.sum_button.clicked.connect(self.calculate_sum)
       self.max_button.clicked.connect(self.find_max)
       self.min_button.clicked.connect(self.find_min)
       self.sort_button.clicked.connect(self.sort_numbers)

       self.numbers = []

    def generate_numbers(self):
       try:
           min_value = int(self.min_edit.text())
           max_value = int(self.max_edit.text())
       except ValueError:
           QMessageBox.warning(self, 'Uwaga!', 'Prosze wprowadź poprawne liczby')
           return

       self.sum_label.setText("Suma:")
       self.max_label.setText("Maksimum:")
       self.min_label.setText("Minimum:")
       self.sort_label.setText("Pierwsze 15 posortowanych liczb:")
       self.numbers = [random.randint(min_value, max_value) for _ in range(50)]

    def calculate_sum(self):
        if not self.numbers:
            QMessageBox.warning(self, 'Uwaga!', 'Na początku musisz wygenerować liczby!')
            return

        sum_value = sum(self.numbers)
        self.sum_label.setText(str(f"Suma: {sum_value}"))

    def find_max(self):
        if not self.numbers:
            QMessageBox.warning(self, 'Uwaga!', 'Na początku musisz wygenerować liczby!')
            return

        max_value = max(self.numbers)
        self.max_label.setText(str(f"Maksimum: {max_value}"))

    def find_min(self):
      if not self.numbers:
          QMessageBox.warning(self, 'Uwaga!', 'Na początku musisz wygenerować liczby!')
          return

      min_value = min(self.numbers)
      self.min_label.setText(str(f"Minimum: {min_value}"))

    def sort_numbers(self):
        if not self.numbers:
            QMessageBox.warning(self, 'Uwaga!', 'Na początku musisz wygenerować liczby!')
            return

        sorted_numbers = sorted(self.numbers)
        self.sort_label.setText(f"Pierwsze 15 posortowanych liczb: {', '.join(map(str, sorted_numbers[:15]))}")

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = RandomNumberApp()
   ex.show()
   sys.exit(app.exec_())
