# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddNewWorker.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewWorkerForm(object):
    def setupUi(self, NewWorkerForm):
        NewWorkerForm.setObjectName("NewWorkerForm")
        NewWorkerForm.resize(515, 330)
        self.centralwidget = QtWidgets.QWidget(NewWorkerForm)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 281, 261))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 81, 16))
        self.label_8.setObjectName("label_8")
        self.surename = QtWidgets.QLineEdit(self.groupBox)
        self.surename.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.surename.setObjectName("surename")
        self.name = QtWidgets.QLineEdit(self.groupBox)
        self.name.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.name.setObjectName("name")
        self.father_name = QtWidgets.QLineEdit(self.groupBox)
        self.father_name.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.father_name.setObjectName("father_name")
        self.passport_series = QtWidgets.QLineEdit(self.groupBox)
        self.passport_series.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.passport_series.setObjectName("passport_series")
        self.passport_number = QtWidgets.QLineEdit(self.groupBox)
        self.passport_number.setGeometry(QtCore.QRect(120, 140, 113, 20))
        self.passport_number.setObjectName("passport_number")
        self.adress = QtWidgets.QLineEdit(self.groupBox)
        self.adress.setGeometry(QtCore.QRect(120, 170, 113, 20))
        self.adress.setObjectName("adress")
        self.phone = QtWidgets.QLineEdit(self.groupBox)
        self.phone.setGeometry(QtCore.QRect(120, 200, 113, 20))
        self.phone.setObjectName("phone")
        self.department_number = QtWidgets.QComboBox(self.groupBox)
        self.department_number.setGeometry(QtCore.QRect(120, 230, 69, 22))
        self.department_number.setObjectName("department_number")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 20, 171, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_10.setObjectName("label_10")
        self.department_name = QtWidgets.QLabel(self.groupBox_2)
        self.department_name.setGeometry(QtCore.QRect(10, 40, 151, 16))
        self.department_name.setObjectName("department_name")
        self.department_adress = QtWidgets.QLabel(self.groupBox_2)
        self.department_adress.setGeometry(QtCore.QRect(10, 90, 151, 16))
        self.department_adress.setObjectName("department_adress")
        self.cancel_add_worker = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_add_worker.setGeometry(QtCore.QRect(350, 242, 91, 31))
        self.cancel_add_worker.setObjectName("cancel_add_worker")
        self.add_worker = QtWidgets.QPushButton(self.centralwidget)
        self.add_worker.setGeometry(QtCore.QRect(350, 190, 91, 31))
        self.add_worker.setObjectName("add_worker")
        NewWorkerForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewWorkerForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        NewWorkerForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewWorkerForm)
        self.statusbar.setObjectName("statusbar")
        NewWorkerForm.setStatusBar(self.statusbar)

        self.retranslateUi(NewWorkerForm)
        QtCore.QMetaObject.connectSlotsByName(NewWorkerForm)

    def retranslateUi(self, NewWorkerForm):
        _translate = QtCore.QCoreApplication.translate
        NewWorkerForm.setWindowTitle(_translate("NewWorkerForm", "Добавить нового работника"))
        self.groupBox.setTitle(_translate("NewWorkerForm", "Новый работник"))
        self.label.setText(_translate("NewWorkerForm", "Фамилия"))
        self.label_2.setText(_translate("NewWorkerForm", "Имя"))
        self.label_3.setText(_translate("NewWorkerForm", "Отчество"))
        self.label_4.setText(_translate("NewWorkerForm", "Серия паспорта"))
        self.label_5.setText(_translate("NewWorkerForm", "Номер паспорта"))
        self.label_6.setText(_translate("NewWorkerForm", "Адрес проживания"))
        self.label_7.setText(_translate("NewWorkerForm", "Телефон"))
        self.label_8.setText(_translate("NewWorkerForm", "Номер отдела"))
        self.groupBox_2.setTitle(_translate("NewWorkerForm", "Отдел"))
        self.label_9.setText(_translate("NewWorkerForm", "Название отдела:"))
        self.label_10.setText(_translate("NewWorkerForm", "Адрес отдела:"))
        self.department_name.setText(_translate("NewWorkerForm", "TextLabel"))
        self.department_adress.setText(_translate("NewWorkerForm", "TextLabel"))
        self.cancel_add_worker.setText(_translate("NewWorkerForm", "Отмена"))
        self.add_worker.setText(_translate("NewWorkerForm", "Добавить"))
