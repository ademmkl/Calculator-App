import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont

class Web(QMainWindow):

    def __init__(self):
        super().__init__()
        self.numList = []
        self.signal = ""
        self.memo = ""
        self.viewPage()
        self.show()

    def equals(self, eq):

        if all([eq == "=", self.signal == "+", len(self.numList) > 0]):
            value = float(self.memo) + float("".join(self.numList))
            self.labelTop.setText("")
            self.label.setText(str(value))
            self.numList.clear()
            self.memo = ""

            for i in str(value):
                self.numList.append(i)

            self.signal = "="

        elif all([eq == "=", self.signal == "-", len(self.numList) > 0]):
            value = float(self.memo) - float("".join(self.numList))
            self.labelTop.setText("")
            self.label.setText(str(value))
            self.numList.clear()
            self.memo = ""

            for i in str(value):
                self.numList.append(i)

            self.signal = "="

        elif all([eq == "=", self.signal == "x", len(self.numList) > 0]):
            value = float(self.memo) * float("".join(self.numList))
            self.labelTop.setText("")
            self.label.setText(str(value))
            self.numList.clear()
            self.memo = ""

            for i in str(value):
                self.numList.append(i)

            self.signal = "="

        elif all([eq == "=", self.signal == "÷", len(self.numList) > 0]):

            if int("".join(self.numList)) != 0:
                value=float(self.memo) / float("".join(self.numList))
                self.labelTop.setText("")
                self.label.setText(str(value))
                self.numList.clear()
                self.memo = ""

                for i in str(value):
                    self.numList.append(i)

                self.signal = "="

            else:
                self.numList.clear()
                self.label.setText("Zero Division Error")

        elif all([eq == "=", self.signal == "%", len(self.numList) > 0]):
            value = float(self.memo)*float("".join(self.numList))/100
            self.labelTop.setText("")
            self.label.setText(str(value))
            self.numList.clear()
            self.memo = ""

            for i in str(value):
                self.numList.append(i)

            self.signal = "="

    def remove(self, delete):

        if delete == "Del" and len(self.numList)==0:
            self.label.setText("0")

        elif all([delete == "Del", len(self.numList) == 2, self.numList[0]=="-"]):
            self.numList.clear()
            self.label.setText("0")

        elif delete == "Del" and len(self.numList) > 1:
            self.numList.pop()
            self.label.setText("".join(self.numList))

        elif delete == "Del" and len(self.numList) == 1:
            self.numList.clear()
            self.label.setText("0")


    def reset(self, c):

        if c == "c":
            self.label.setText("0")
            self.labelTop.setText("")
            self.memo = ""
            self.signal = ""
            self.numList.clear()

    def division(self, divide):

        if divide == "÷":
            self.memo = "".join(self.numList)
            self.numList.clear()
            self.label.setText("0")
            self.labelTop.setText(self.memo + " ÷")
            self.signal = "÷"

    def percent(self, per):

        if per == "%":
            self.memo = "".join(self.numList)
            self.numList.clear()
            self.label.setText("0")
            self.labelTop.setText(self.memo + " %")
            self.signal = "%"

    def multiplication(self, times):

        if times == "x":
            self.memo = "".join(self.numList)
            self.numList.clear()
            self.label.setText("0")
            self.labelTop.setText(self.memo + " x")
            self.signal = "x"

    def subtraction(self, minus):

        if minus == "-":
            self.memo = "".join(self.numList)
            self.numList.clear()
            self.label.setText("0")
            self.labelTop.setText(self.memo+" -")
            self.signal = "-"

    def addition(self, plus):

        if plus == "+":
            self.memo = "".join(self.numList)
            self.numList.clear()
            self.label.setText("0")
            self.labelTop.setText(self.memo+" +")
            self.signal = "+"

    def react(self, number):

        if number != "." and self.signal != "=":
            self.numList.append(number)
            self.label.setText("".join(self.numList))


        elif number != "." and self.signal == "=":
            self.numList.clear()
            self.signal = ""
            self.numList.append(number)
            self.label.setText("".join(self.numList))

    def viewPage(self):

        w = 95
        w_tab = 4
        h = 70
        h_tab = 4

        font="Roadway"

        self.setWindowTitle("Project Calculator")
        self.setGeometry(200, 200, 400, 600)
        self.setMaximumSize(400, 600)
        self.setMinimumSize(400, 600)

        self.labelTop = QLabel(self)
        self.labelTop.setGeometry(16, 30, 368, 40)
        self.labelTop.setFont(QFont(font, 14))

        self.label = QLabel(self)
        self.label.setGeometry(16, 70, 368, 100)
        self.label.setFont(QFont(font, 24))
        self.label.setText("0")

        self.button00 = QPushButton("00", self)
        self.button00.setGeometry(w_tab, 600 - h_tab - h, w, h)
        self.button00.setFont(QFont(font, 14))
        self.button00.clicked.connect(lambda: self.react("00"))

        self.button0 = QPushButton("0", self)
        self.button0.setGeometry(w_tab*2 + w, 600 - h_tab - h, w, h)
        self.button0.setFont(QFont(font, 14))
        self.button0.clicked.connect(lambda: self.react("0"))

        self.buttonVirgul = QPushButton(".", self)
        self.buttonVirgul.setGeometry(w_tab*3 +w*2, 600 - h_tab - h, w, h)
        self.buttonVirgul.setFont(QFont(font, 18))
        self.buttonVirgul.clicked.connect(lambda: self.react("."))

        self.buttonEsittir = QPushButton("=", self)
        self.buttonEsittir.setGeometry(w_tab*4 +w*3, 600 - h_tab - h, w, h)
        self.buttonEsittir.setFont(QFont(font, 14))
        self.buttonEsittir.clicked.connect(lambda: self.equals("="))

        self.button1 = QPushButton("1", self)
        self.button1.setGeometry(w_tab, 600 - h_tab*2 - h*2, w, h)
        self.button1.setFont(QFont(font, 14))
        self.button1.clicked.connect(lambda: self.react("1"))

        self.button2 = QPushButton("2", self)
        self.button2.setGeometry(w_tab*2 +w, 600 - h_tab*2 - h*2, w, h)
        self.button2.setFont(QFont(font, 14))
        self.button2.clicked.connect(lambda: self.react("2"))

        self.button3 = QPushButton("3", self)
        self.button3.setGeometry(w_tab*3 +w*2, 600 - h_tab*2 - h*2, w, h)
        self.button3.setFont(QFont(font, 14))
        self.button3.clicked.connect(lambda: self.react("3"))

        self.buttonTopla = QPushButton("+", self)
        self.buttonTopla.setGeometry(w_tab*4 + w*3, 600 - h_tab*2 - h*2, w, h)
        self.buttonTopla.setFont(QFont(font, 14))
        self.buttonTopla.clicked.connect(lambda: self.addition("+"))

        self.button4 = QPushButton("4", self)
        self.button4.setGeometry(w_tab, 600 - h_tab*3 - h*3, w, h)
        self.button4.setFont(QFont(font, 14))
        self.button4.clicked.connect(lambda: self.react("4"))

        self.button5 = QPushButton("5", self)
        self.button5.setGeometry(w_tab*2 + w, 600 - h_tab*3 - h*3, w, h)
        self.button5.setFont(QFont(font, 14))
        self.button5.clicked.connect(lambda: self.react("5"))

        self.button6 = QPushButton("6", self)
        self.button6.setGeometry(w_tab*3 + w*2, 600 - h_tab*3 - h*3, w, h)
        self.button6.setFont(QFont(font, 14))
        self.button6.clicked.connect(lambda: self.react("6"))

        self.buttonCikar = QPushButton("-", self)
        self.buttonCikar.setGeometry(w_tab*4 + w*3, 600 - h_tab*3 - h*3, w, h)
        self.buttonCikar.setFont(QFont(font, 14))
        self.buttonCikar.clicked.connect(lambda: self.subtraction("-"))

        self.button7 = QPushButton("7", self)
        self.button7.setGeometry(w_tab, 600 - h_tab*4 - h*4, w, h)
        self.button7.setFont(QFont(font, 14))
        self.button7.clicked.connect(lambda: self.react("7"))

        self.button8 = QPushButton("8", self)
        self.button8.setGeometry(w_tab*2 + w, 600 - h_tab*4 - h*4, w, h)
        self.button8.setFont(QFont(font, 14))
        self.button8.clicked.connect(lambda: self.react("8"))

        self.button9 = QPushButton("9", self)
        self.button9.setGeometry(w_tab*3 + w*2, 600 - h_tab*4 - h*4, w, h)
        self.button9.setFont(QFont(font, 14))
        self.button9.clicked.connect(lambda: self.react("9"))

        self.buttonCarp = QPushButton("x", self)
        self.buttonCarp.setGeometry(w_tab*4 + w*3, 600 - h_tab*4 - h*4, w, h)
        self.buttonCarp.setFont(QFont(font, 14))
        self.buttonCarp.clicked.connect(lambda: self.multiplication("x"))

        self.buttonC = QPushButton("C", self)
        self.buttonC.setGeometry(w_tab, 600 - h_tab*5 - h*5, w, h)
        self.buttonC.setFont(QFont(font, 14))
        self.buttonC.clicked.connect(lambda: self.reset("c"))

        self.buttonYuzde = QPushButton("%", self)
        self.buttonYuzde.setGeometry(w_tab*2 + w, 600 - h_tab*5 - h*5, w, h)
        self.buttonYuzde.setFont(QFont(font, 14))
        self.buttonYuzde.clicked.connect(lambda: self.percent("%"))

        self.buttonDelete = QPushButton("Del", self)
        self.buttonDelete.setGeometry(w_tab*3 + w*2, 600 - h_tab*5 - h*5, w, h)
        self.buttonDelete.setFont(QFont(font, 14))
        self.buttonDelete.clicked.connect(lambda: self.remove("Del"))

        self.buttonBol = QPushButton("÷", self)
        self.buttonBol.setGeometry(w_tab*4 + w*3, 600 - h_tab*5 - h*5, w, h)
        self.buttonBol.setFont(QFont(font, 14))
        self.buttonBol.clicked.connect(lambda: self.division("÷"))


if __name__=="__main__":
    app=QApplication(sys.argv)
    web= Web()
    sys.exit(app.exec())