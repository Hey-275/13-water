# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 675)
        Form.setMinimumSize(QtCore.QSize(1200, 675))
        Form.setMaximumSize(QtCore.QSize(1200, 675))
        #Form.setStyleSheet("QWidget#Form{\n"
#"    border-image: url(:/game_picture/image/record_background.jpg);\n"
#"}")
        self.head = QtWidgets.QPushButton(Form)
        self.head.setGeometry(QtCore.QRect(1040, 40, 131, 141))
        #self.head.setStyleSheet("QPushButton#head{\n"
#"    border-image: url(:/game_picture/image/user_head.jpg);\n"
#"}")
        self.head.setText("")
        self.head.setObjectName("head")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(30, 30, 93, 28))
        self.back_button.setObjectName("back_button")
        self.start_button = QtWidgets.QPushButton(Form)
        self.start_button.setGeometry(QtCore.QRect(470, 540, 141, 41))
        self.start_button.setObjectName("start_button")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 290, 481, 102))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tow_poker_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.tow_poker_1.setMinimumSize(QtCore.QSize(75, 100))
        self.tow_poker_1.setMaximumSize(QtCore.QSize(75, 16777215))
        self.tow_poker_1.setObjectName("tow_poker_1")
        self.horizontalLayout_2.addWidget(self.tow_poker_1)
        self.tow_poker_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.tow_poker_2.setMinimumSize(QtCore.QSize(75, 100))
        self.tow_poker_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.tow_poker_2.setObjectName("tow_poker_2")
        self.horizontalLayout_2.addWidget(self.tow_poker_2)
        self.tow_poker_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.tow_poker_3.setMinimumSize(QtCore.QSize(75, 100))
        self.tow_poker_3.setMaximumSize(QtCore.QSize(75, 16777215))
        self.tow_poker_3.setObjectName("tow_poker_3")
        self.horizontalLayout_2.addWidget(self.tow_poker_3)
        self.tow_poker_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.tow_poker_4.setMinimumSize(QtCore.QSize(0, 100))
        self.tow_poker_4.setMaximumSize(QtCore.QSize(75, 16777215))
        self.tow_poker_4.setObjectName("tow_poker_4")
        self.horizontalLayout_2.addWidget(self.tow_poker_4)
        self.tow_poker_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.tow_poker_5.setMinimumSize(QtCore.QSize(75, 100))
        self.tow_poker_5.setMaximumSize(QtCore.QSize(75, 16777215))
        self.tow_poker_5.setObjectName("tow_poker_5")
        self.horizontalLayout_2.addWidget(self.tow_poker_5)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(330, 420, 495, 102))
        self.layoutWidget1.setMinimumSize(QtCore.QSize(0, 100))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.three_poker_1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.three_poker_1.setMinimumSize(QtCore.QSize(0, 100))
        self.three_poker_1.setMaximumSize(QtCore.QSize(75, 16777215))
        self.three_poker_1.setObjectName("three_poker_1")
        self.horizontalLayout_3.addWidget(self.three_poker_1)
        self.three_poker_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.three_poker_2.setMinimumSize(QtCore.QSize(0, 100))
        self.three_poker_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.three_poker_2.setObjectName("three_poker_2")
        self.horizontalLayout_3.addWidget(self.three_poker_2)
        self.three_poker_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.three_poker_3.setMinimumSize(QtCore.QSize(0, 100))
        self.three_poker_3.setMaximumSize(QtCore.QSize(75, 16777215))
        self.three_poker_3.setObjectName("three_poker_3")
        self.horizontalLayout_3.addWidget(self.three_poker_3)
        self.three_poker_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.three_poker_4.setMinimumSize(QtCore.QSize(0, 100))
        self.three_poker_4.setMaximumSize(QtCore.QSize(75, 16777215))
        self.three_poker_4.setObjectName("three_poker_4")
        self.horizontalLayout_3.addWidget(self.three_poker_4)
        self.three_poker_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.three_poker_5.setMinimumSize(QtCore.QSize(0, 100))
        self.three_poker_5.setMaximumSize(QtCore.QSize(75, 16777215))
        self.three_poker_5.setObjectName("three_poker_5")
        self.horizontalLayout_3.addWidget(self.three_poker_5)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(340, 160, 241, 102))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.one_poker_1 = QtWidgets.QPushButton(self.layoutWidget2)
        self.one_poker_1.setMinimumSize(QtCore.QSize(75, 100))
        self.one_poker_1.setMaximumSize(QtCore.QSize(75, 100))
        self.one_poker_1.setObjectName("one_poker_1")
        self.horizontalLayout.addWidget(self.one_poker_1)
        self.one_poker_2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.one_poker_2.setMinimumSize(QtCore.QSize(75, 100))
        self.one_poker_2.setMaximumSize(QtCore.QSize(75, 100))
        self.one_poker_2.setObjectName("one_poker_2")
        self.horizontalLayout.addWidget(self.one_poker_2)
        self.one_poker_3 = QtWidgets.QPushButton(self.layoutWidget2)
        self.one_poker_3.setMinimumSize(QtCore.QSize(75, 100))
        self.one_poker_3.setMaximumSize(QtCore.QSize(75, 100))
        self.one_poker_3.setObjectName("one_poker_3")
        self.horizontalLayout.addWidget(self.one_poker_3)
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(120, 200, 131, 294))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(80)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setStyleSheet("font: 26pt \"华文琥珀\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setStyleSheet("font: 26pt \"华文琥珀\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_2.setStyleSheet("font: 26pt \"华文琥珀\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.game_id = QtWidgets.QLabel(Form)
        self.game_id.setGeometry(QtCore.QRect(480, 50, 171, 71))
        self.game_id.setStyleSheet("font: 20pt \"华文琥珀\";")
        self.game_id.setObjectName("game_id")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(330, 60, 121, 51))
        self.label_4.setStyleSheet("font: 20pt \"华文琥珀\";")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        self.back_button.clicked.connect(Form.return_to_user_platform)
        self.start_button.clicked.connect(Form.show_poker)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.back_button.setText(_translate("Form", "返回"))
        self.start_button.setText(_translate("Form", "出牌"))
        self.tow_poker_1.setText(_translate("Form", "PushButton"))
        self.tow_poker_2.setText(_translate("Form", "PushButton"))
        self.tow_poker_3.setText(_translate("Form", "PushButton"))
        self.tow_poker_4.setText(_translate("Form", "PushButton"))
        self.tow_poker_5.setText(_translate("Form", "PushButton"))
        self.three_poker_1.setText(_translate("Form", "PushButton"))
        self.three_poker_2.setText(_translate("Form", "PushButton"))
        self.three_poker_3.setText(_translate("Form", "PushButton"))
        self.three_poker_4.setText(_translate("Form", "PushButton"))
        self.three_poker_5.setText(_translate("Form", "PushButton"))
        self.one_poker_1.setText(_translate("Form", "PushButton"))
        self.one_poker_2.setText(_translate("Form", "PushButton"))
        self.one_poker_3.setText(_translate("Form", "PushButton"))
        self.label.setText(_translate("Form", "第一敦"))
        self.label_3.setText(_translate("Form", "第二敦"))
        self.label_2.setText(_translate("Form", "第三敦"))
        self.game_id.setText(_translate("Form", "game_id"))
        self.label_4.setText(_translate("Form", "战局ID:"))
