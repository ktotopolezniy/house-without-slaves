from PyQt5.QtCore import Qt
from PyQt5.Qtwidgets import QApplication, QWidgets, QLabel, QHBoxLayout

app= QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Моё первое приложение')
my_win.move(900, 70)
my_win.resize(400, 200)
winner = QLabel('Shto-to')
my_win.show()
button1 = QPushButton ('1')
button2 = QPushButton ('2')
button3 = QPushButton ('3')
button4 = QPushButton ('4')
button5 = QPushButton ('5')

layoutV = QHBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWiget(button1, apligment = Qt.AlignLeft)
layoutH1.addWiget(button2, apligment = Qt.AlignRight)
layoutH1.addWiget(button3, apligment = Qt.AlignCenter)
layoutH1.addWiget(button4, apligment = Qt.AlignLeft)
layoutH1.addWiget(button5, apligment = Qt.AlignRight)

layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
window.setLayout(layoutV)
window.setLayout(layoutV)
my_win.show()
app.exes_()








