"""Written by CoderKB"""

import sys
import os
import requests
from bs4 import BeautifulSoup

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog


def analyze_url(url):
    try:
        req = requests.get(url)

        if(req.status_code == 200):
            soup = BeautifulSoup(req.text, 'lxml')
            images = soup.findAll('img', attrs={'class': 'slide_image'})
            return images
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Invalid URL")
            font_4 = QtGui.QFont()
            font_4.setPointSize(14)
            error_dialog.setFont(font_4)
            error_dialog.setWindowTitle("ERROR")
            error_dialog.exec_()
            return ""
    except:
        error_dialog_1 = QtWidgets.QErrorMessage()
        error_dialog_1.showMessage("No Internet")
        font_4 = QtGui.QFont()
        font_4.setPointSize(14)
        error_dialog_1.setFont(font_4)
        error_dialog_1.setWindowTitle("WARNING")
        error_dialog_1.exec_()
        return ""


def download_slides(path, images):
    os.chdir(path)
    folder_name = images[0]['alt'].strip()
    new_name = ""
    for ch in folder_name:
        if(ch.isalpha() or ch == ' '):
            new_name += ch
    folder_name = new_name
    if(not os.path.exists(folder_name)):
        os.mkdir(folder_name)
    os.chdir(folder_name)

    cnt = 1
    for image in images:
        img_name = f"{cnt:03d}.png"
        img_url = image['data-full']

        r = requests.get(img_url)

        with open(img_name, 'wb') as img:
            img.write(r.content)

        cnt += 1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 385)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Courses/slideshare-256.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 11, 400, 36))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 280, 161, 41))
        font = QtGui.QFont()
        font.setFamily("GLYPHICONS Halflings")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 109, 811, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-20, 180, 831, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 210, 761, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        font_1 = QtGui.QFont()
        font_1.setPointSize(12)
        self.lineEdit.setFont(font_1)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 60, 781, 51))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_2.setFocus()
        font_2 = QtGui.QFont()
        font_2.setPointSize(13)
        self.lineEdit_2.setFont(font_2)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.download)
        self.pushButton_2.clicked.connect(self.analyse)
        self.pushButton_3.clicked.connect(self.browse)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.images = ""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Slides Downloader"))
        self.label.setText(_translate("MainWindow", "paste slideshare url"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        self.label_3.setText(_translate("MainWindow", "Slide Share Dowloader"))
        self.label_2.setText(_translate("MainWindow", "Save to"))
        self.pushButton_3.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Analyse"))

    def browse(self):
        file = str(QFileDialog.getExistingDirectory())
        self.lineEdit.setText(file)

    def analyse(self):
        url = self.lineEdit_2.text()
        self.images = analyze_url(url)

    def download(self):
        if(self.images == ""):
            error_dialog_2 = QtWidgets.QErrorMessage()
            error_dialog_2.showMessage("First analyze the proper url")
            error_dialog_2.setWindowTitle("WARNING")
            font_3 = QtGui.QFont()
            font_3.setPointSize(12)
            error_dialog_2.setFont(font_3)
            error_dialog_2.exec_()
        elif(self.lineEdit.text() == "" or not os.path.exists(self.lineEdit.text())):
            error_dialog_4 = QtWidgets.QErrorMessage()
            error_dialog_4.showMessage("Select a valid path to save")
            error_dialog_4.setWindowTitle("Message")
            font_5 = QtGui.QFont()
            font_5.setPointSize(12)
            error_dialog_4.setFont(font_5)
            error_dialog_4.exec_()
        else:
            download_slides(self.lineEdit.text(), self.images)
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText("Download Completed")
            msg_box.setWindowTitle("Status")
            msg_box.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
