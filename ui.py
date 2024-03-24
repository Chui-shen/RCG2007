# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 368)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 192, 72))
        font = QFont()
        font.setFamilies([u"Trebuchet MS"])
        font.setPointSize(48)
        self.label.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(11, 308, 481, 34))
        font1 = QFont()
        font1.setFamilies([u"Trebuchet MS"])
        font1.setPointSize(16)
        self.pushButton.setFont(font1)
        self.outputer = QTextBrowser(self.centralwidget)
        self.outputer.setObjectName(u"outputer")
        self.outputer.setGeometry(QRect(10, 201, 482, 101))
        font2 = QFont()
        font2.setFamilies([u"Trebuchet MS"])
        font2.setPointSize(28)
        self.outputer.setFont(font2)
        self.outputer.setCursorWidth(0)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 87, 120, 25))
        font3 = QFont()
        font3.setFamilies([u"Trebuchet MS"])
        font3.setPointSize(15)
        self.label_2.setFont(font3)
        self.inputer = QPlainTextEdit(self.centralwidget)
        self.inputer.setObjectName(u"inputer")
        self.inputer.setGeometry(QRect(9, 118, 482, 41))
        font4 = QFont()
        font4.setFamilies([u"Trebuchet MS"])
        font4.setPointSize(18)
        self.inputer.setFont(font4)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 170, 120, 25))
        self.label_3.setFont(font3)
        self.first = QPushButton(self.centralwidget)
        self.first.setObjectName(u"first")
        self.first.setGeometry(QRect(200, 10, 161, 41))
        self.first.setFont(font3)
        self.min = QPlainTextEdit(self.centralwidget)
        self.min.setObjectName(u"min")
        self.min.setGeometry(QRect(210, 60, 111, 41))
        self.min.setFont(font4)
        self.max = QPlainTextEdit(self.centralwidget)
        self.max.setObjectName(u"max")
        self.max.setGeometry(QRect(380, 60, 111, 41))
        self.max.setFont(font4)
        self.generator = QPushButton(self.centralwidget)
        self.generator.setObjectName(u"generator")
        self.generator.setGeometry(QRect(370, 10, 121, 41))
        self.generator.setFont(font3)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 60, 41, 41))
        font5 = QFont()
        font5.setFamilies([u"Trebuchet MS"])
        font5.setPointSize(26)
        self.label_4.setFont(font5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RCG", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RCG", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.outputer.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Trebuchet MS'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number: ", None))
        self.inputer.setPlainText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Chosen Ones: ", None))
        self.first.setText(QCoreApplication.translate("MainWindow", u"Initiation", None))
        self.generator.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"~", None))
    # retranslateUi

