# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/max/Documents/ZebraHead22/Polina/exam_people/infogypsies_time.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExamPeople(object):
    def setupUi(self, ExamPeople):
        ExamPeople.setObjectName("ExamPeople")
        ExamPeople.resize(520, 480)
        ExamPeople.setMinimumSize(QtCore.QSize(520, 480))
        self.centralwidget = QtWidgets.QWidget(ExamPeople)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.csvfile_label = QtWidgets.QLabel(self.centralwidget)
        self.csvfile_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.csvfile_label.setObjectName("csvfile_label")
        self.verticalLayout.addWidget(self.csvfile_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browse_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.browse_btn.setObjectName("browse_btn")
        self.horizontalLayout_2.addWidget(self.browse_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.const_time = QtWidgets.QCheckBox(self.centralwidget)
        self.const_time.setTristate(False)
        self.const_time.setObjectName("const_time")
        self.horizontalLayout_3.addWidget(self.const_time)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lesson_time_label = QtWidgets.QLabel(self.centralwidget)
        self.lesson_time_label.setMinimumSize(QtCore.QSize(112, 0))
        self.lesson_time_label.setObjectName("lesson_time_label")
        self.horizontalLayout_3.addWidget(self.lesson_time_label)
        self.lesson_time = QtWidgets.QSpinBox(self.centralwidget)
        self.lesson_time.setMinimumSize(QtCore.QSize(90, 0))
        self.lesson_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lesson_time.setMaximum(360)
        self.lesson_time.setSingleStep(5)
        self.lesson_time.setProperty("value", 120)
        self.lesson_time.setObjectName("lesson_time")
        self.horizontalLayout_3.addWidget(self.lesson_time)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.persent = QtWidgets.QSpinBox(self.centralwidget)
        self.persent.setMinimumSize(QtCore.QSize(90, 0))
        self.persent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.persent.setMaximum(240)
        self.persent.setSingleStep(5)
        self.persent.setProperty("value", 80)
        self.persent.setObjectName("persent")
        self.horizontalLayout_3.addWidget(self.persent)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.people_table = QtWidgets.QTableWidget(self.centralwidget)
        self.people_table.setColumnCount(3)
        self.people_table.setObjectName("people_table")
        self.people_table.setRowCount(0)
        self.people_table.horizontalHeader().setVisible(True)
        self.people_table.horizontalHeader().setCascadingSectionResizes(True)
        self.people_table.horizontalHeader().setDefaultSectionSize(150)
        self.people_table.horizontalHeader().setHighlightSections(True)
        self.people_table.horizontalHeader().setMinimumSectionSize(30)
        self.people_table.horizontalHeader().setSortIndicatorShown(True)
        self.people_table.horizontalHeader().setStretchLastSection(True)
        self.people_table.verticalHeader().setVisible(True)
        self.people_table.verticalHeader().setCascadingSectionResizes(True)
        self.people_table.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.people_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.process_btn = QtWidgets.QPushButton(self.centralwidget)
        self.process_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.process_btn.setObjectName("process_btn")
        self.horizontalLayout.addWidget(self.process_btn)
        self.export_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.export_btn.setObjectName("export_btn")
        self.horizontalLayout.addWidget(self.export_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout.addWidget(self.exit_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ExamPeople.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExamPeople)
        QtCore.QMetaObject.connectSlotsByName(ExamPeople)

    def retranslateUi(self, ExamPeople):
        _translate = QtCore.QCoreApplication.translate
        ExamPeople.setWindowTitle(_translate("ExamPeople", "Exam People"))
        self.csvfile_label.setText(_translate("ExamPeople", "Browse .csv or.xlsx file"))
        self.browse_btn.setText(_translate("ExamPeople", "Browse"))
        self.const_time.setText(_translate("ExamPeople", "90 minutes"))
        self.lesson_time_label.setText(_translate("ExamPeople", "Lesson time (min):"))
        self.label.setText(_translate("ExamPeople", "%"))
        self.people_table.setSortingEnabled(True)
        self.process_btn.setText(_translate("ExamPeople", "Process"))
        self.export_btn.setText(_translate("ExamPeople", "Export"))
        self.exit_btn.setText(_translate("ExamPeople", "Exit"))
