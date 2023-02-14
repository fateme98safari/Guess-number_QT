# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Guess_Num.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(445, 232)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 5, 1)

        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
        self.btn_reset.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe Script"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setStrikeOut(False)
        self.btn_reset.setFont(font1)
        self.btn_reset.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(170, 0, 127);")

        self.gridLayout.addWidget(self.btn_reset, 4, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"boeder-radius: 10px;\n"
"")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.btn_check = QPushButton(self.centralwidget)
        self.btn_check.setObjectName(u"btn_check")
        sizePolicy1.setHeightForWidth(self.btn_check.sizePolicy().hasHeightForWidth())
        self.btn_check.setSizePolicy(sizePolicy1)
        self.btn_check.setBaseSize(QSize(46, 33))
        font4 = QFont()
        font4.setFamilies([u"Segoe Print"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.btn_check.setFont(font4)
        self.btn_check.setStyleSheet(u"border-bottom-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"\n"
"background-color: rgb(170, 0, 127);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_check, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 445, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a number between 1-60", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset Game", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_check.setText(QCoreApplication.translate("MainWindow", u"Check", None))
    # retranslateUi

