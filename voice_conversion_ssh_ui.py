# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voice_conversion_ssh_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_upload = QtWidgets.QPushButton(self.centralwidget)
        self.pb_upload.setGeometry(QtCore.QRect(270, 150, 131, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb_upload.setFont(font)
        self.pb_upload.setObjectName("pb_upload")
        self.pb_convert = QtWidgets.QPushButton(self.centralwidget)
        self.pb_convert.setGeometry(QtCore.QRect(270, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb_convert.setFont(font)
        self.pb_convert.setObjectName("pb_convert")
        self.pb_download = QtWidgets.QPushButton(self.centralwidget)
        self.pb_download.setGeometry(QtCore.QRect(270, 330, 131, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb_download.setFont(font)
        self.pb_download.setObjectName("pb_download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 200, 21, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 290, 21, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 40, 461, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 70, 521, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 90, 381, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "語音轉換SSH工具"))
        self.pb_upload.setText(_translate("MainWindow", "上傳音檔"))
        self.pb_convert.setText(_translate("MainWindow", "轉換音檔"))
        self.pb_download.setText(_translate("MainWindow", "下載音檔"))
        self.label.setText(_translate("MainWindow", "↓"))
        self.label_2.setText(_translate("MainWindow", "↓"))
        self.label_3.setText(_translate("MainWindow", "1.將上傳的音檔放置在source_wav/，並按下上傳音檔"))
        self.label_4.setText(_translate("MainWindow", "2.按下轉換音檔後，開始轉換，音檔數量越多，轉換速度越慢"))
        self.label_5.setText(_translate("MainWindow", "3.按下下載音檔後，音檔位置在target_wav/"))

