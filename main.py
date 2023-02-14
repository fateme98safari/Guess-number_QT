import random
from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_check.clicked.connect(self.check)
        self.ui.btn_reset.clicked.connect(self.reset)
        self.computer_choice=random.randint(1,60)
        self.counter=0



    def check(self):
        for i in range(7):
            if int(self.ui.lineEdit.text())<self.computer_choice:
                self.ui.lineEdit_2.setText("Go Up")
                self.ui.lineEdit.setText(" ")
                self.counter+=1
                self.ui.lineEdit_3.setText(str(self.counter))
                if self.counter==7:
                    self.ui.lineEdit_2.setText("YOU FIELD")

            elif int(self.ui.lineEdit.text())>self.computer_choice:
                self.ui.lineEdit_2.setText("Go Down")
                self.ui.lineEdit.setText(" ")
                self.counter+=1
                self.ui.lineEdit_3.setText(str(self.counter))
                if self.counter==7:
                    self.ui.lineEdit_2.setText("YOU FIELD")
                
            elif int(self.ui.lineEdit.text())==self.computer_choice:
                self.ui.lineEdit_2.setText("YOU WIN")
                self.counter+=1
                self.ui.lineEdit_3.setText(str(self.counter))
                msg_box=QMessageBox()
                msg_box.setText("play again?")
                msg_box.exec()
                self.reset()


            if self.ui.lineEdit_2.text()=="YOU FIELD":
                msg_box=QMessageBox()
                msg_box.setText("The correct answer was : " + str(self.computer_choice) + "play again?")
                msg_box.exec()
                self.reset()

    def reset(self):
        self.computer_choice=random.randint(1,60)
        self.ui.lineEdit_2.setText(" ")      
        self.ui.lineEdit_3.setText(" ")
        self.ui.lineEdit.setText(" ")
        self.counter=0


app=QApplication(sys.argv)
# MainWindow.setWindowTitle("Guess number")
window=MainWindow()
window.show()



app.exec()