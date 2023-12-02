from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
lbl = QLabel("У якому році математичка вселилася в демона?")
ans1 = QRadioButton("ХЗ")
ans2 = QRadioButton("7516348751278516287 до нашої ери")

main_line = QVBoxLayout()
main_line.addWidget((lbl))

h1 = QHBoxLayout()
h1.addWidget(ans1)
h1.addWidget(ans2)
main_line.addLayout(h1)

def true_var_1():
    msg = QMessageBox()
    msg.setText("Молодець правельно!!!!!!")
    msg.exec()

ans1.clicked.connect(true_var_1)

def true_var_2():
    msg = QMessageBox()
    msg.setText("не правельно")
    msg.exec()

ans2.clicked.connect(true_var_2)

window.setLayout(main_line)
window.show()
app.exec()



