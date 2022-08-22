import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton ,QSpinBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QLineEdit
from PyQt5 import QtCore
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp


class App(QWidget):



    def __init__(self):
        super().__init__()
        self.title = '个性短语编辑器'
        self.left = 700
        self.top = 400
        self.width = 420
        self.height = 70
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # 输入框1
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 17)
        self.textbox.resize(80, 30)

        # 限制第一个输入框只能输入英文
        reg = QRegExp('[a-zA-Z]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)
        self.textbox.setValidator(validator)

        # 排序值
        self.ranknum = QSpinBox(self)
        self.ranknum.setMinimum(1)
        self.ranknum.setMaximum(20)
        self.ranknum.move(105, 20)
        # 输入框2
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(160, 17)
        self.textbox2.resize(140, 30)

        # 按钮
        self.button = QPushButton('Add', self)
        self.button.move(310, 17)




        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()



    @pyqtSlot()
    def on_click(self):
        filename = 'myphrase.ini'
        pinyin = self.textbox.text()
        num = self.ranknum.text()
        word = self.textbox2.text()
        self.textbox.setText('')
        self.textbox2.setText('')
        self.ranknum.setMaximum(1)
        self.ranknum.setMaximum(20)
        # 判断两个内容是否为空
        if pinyin == '' or word == '':
            pass
        else:
            print(pinyin+"="+num+","+word)
            with open(filename, "a",encoding = "utf8") as f:
                f.write(pinyin+"="+num+","+word)
                f.write('\n')
                f.close()
                # print('已写入')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exit(app.exec_())
