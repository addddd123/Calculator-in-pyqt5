# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Calculator-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_7.sizePolicy().hasHeightForWidth())
        self.push_7.setSizePolicy(sizePolicy)
        self.push_7.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.push_7.setObjectName("push_7")
        self.gridLayout.addWidget(self.push_7, 5, 0, 1, 2)
        self.push_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_3.sizePolicy().hasHeightForWidth())
        self.push_3.setSizePolicy(sizePolicy)
        self.push_3.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.push_3.setObjectName("push_3")
        self.gridLayout.addWidget(self.push_3, 2, 2, 1, 1)
        self.push_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_minus.sizePolicy().hasHeightForWidth())
        self.push_minus.setSizePolicy(sizePolicy)
        self.push_minus.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(225, 225, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 127);\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"\n"
"}")
        self.push_minus.setObjectName("push_minus")
        self.gridLayout.addWidget(self.push_minus, 2, 3, 1, 1)
        self.pus_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pus_plus.sizePolicy().hasHeightForWidth())
        self.pus_plus.setSizePolicy(sizePolicy)
        self.pus_plus.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(225, 225, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 127);\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"\n"
"}")
        self.pus_plus.setObjectName("pus_plus")
        self.gridLayout.addWidget(self.pus_plus, 1, 3, 1, 1)
        self.push_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_2.sizePolicy().hasHeightForWidth())
        self.push_2.setSizePolicy(sizePolicy)
        self.push_2.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.push_2.setObjectName("push_2")
        self.gridLayout.addWidget(self.push_2, 2, 1, 1, 1)
        self.push_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_4.sizePolicy().hasHeightForWidth())
        self.push_4.setSizePolicy(sizePolicy)
        self.push_4.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.push_4.setObjectName("push_4")
        self.gridLayout.addWidget(self.push_4, 3, 0, 1, 1)
        self.push_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_clear.sizePolicy().hasHeightForWidth())
        self.push_clear.setSizePolicy(sizePolicy)
        self.push_clear.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.push_clear.setObjectName("push_clear")
        self.gridLayout.addWidget(self.push_clear, 1, 0, 1, 2)
        self.push_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_1.sizePolicy().hasHeightForWidth())
        self.push_1.setSizePolicy(sizePolicy)
        self.push_1.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.push_1.setObjectName("push_1")
        self.gridLayout.addWidget(self.push_1, 2, 0, 1, 1)
        self.push_del = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_del.sizePolicy().hasHeightForWidth())
        self.push_del.setSizePolicy(sizePolicy)
        self.push_del.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.push_del.setObjectName("push_del")
        self.gridLayout.addWidget(self.push_del, 1, 2, 1, 1)
        self.push_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_div.sizePolicy().hasHeightForWidth())
        self.push_div.setSizePolicy(sizePolicy)
        self.push_div.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(225, 225, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 127);\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"\n"
"}")
        self.push_div.setObjectName("push_div")
        self.gridLayout.addWidget(self.push_div, 5, 3, 1, 1)
        self.push_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_9.sizePolicy().hasHeightForWidth())
        self.push_9.setSizePolicy(sizePolicy)
        self.push_9.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.push_9.setObjectName("push_9")
        self.gridLayout.addWidget(self.push_9, 5, 2, 1, 1)
        self.push_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_mul.sizePolicy().hasHeightForWidth())
        self.push_mul.setSizePolicy(sizePolicy)
        self.push_mul.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(225, 225, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 127);\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"\n"
"}")
        self.push_mul.setObjectName("push_mul")
        self.gridLayout.addWidget(self.push_mul, 3, 3, 1, 1)
        self.push_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_6.sizePolicy().hasHeightForWidth())
        self.push_6.setSizePolicy(sizePolicy)
        self.push_6.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.push_6.setObjectName("push_6")
        self.gridLayout.addWidget(self.push_6, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"\n" "color: rgb(255, 255, 255);"
"")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.push_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_5.sizePolicy().hasHeightForWidth())
        self.push_5.setSizePolicy(sizePolicy)
        self.push_5.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.push_5.setObjectName("push_5")
        self.gridLayout.addWidget(self.push_5, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(85, 0, 255);\n"
"    \n"
"    ;\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(195, 188, 200);\n"
"\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(225, 225, 112);\n"
"border-radius:30px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 127);\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.push_1.clicked.connect(self.method_1)
        self.push_2.clicked.connect(self.method_2)
        self.push_3.clicked.connect(self.method_3)
        self.push_4.clicked.connect(self.method_4)
        self.push_5.clicked.connect(self.method_5)
        self.push_6.clicked.connect(self.method_6)
        self.pushButton.clicked.connect(self.method_7)
        self.pushButton_3.clicked.connect(self.method_8)
        self.pushButton_4.clicked.connect(self.method_9)
        self.push_7.clicked.connect(self.method_zero)
        self.push_9.clicked.connect(self.method_point)
        self.pus_plus.clicked.connect(self.method_plus)
        self.push_minus.clicked.connect(self.method_min)
        self.push_mul.clicked.connect(self.method_mult)
        self.pushButton_5.clicked.connect(self.method_div)
        self.push_del.clicked.connect(self.method_del)
        self.push_div.clicked.connect(self.method_equal)
        self.push_clear.clicked.connect(self.method_clear)

    def method_1(self):
        text=self.label.text()
        self.label.setText(text+"1")       
    def method_2(self):
        text=self.label.text()
        self.label.setText(text+"2")
    def method_3(self):
        text=self.label.text()
        self.label.setText(text+"3")
    def method_4(self):
        text=self.label.text()
        self.label.setText(text+"4")
    def method_5(self):
        text=self.label.text()
        self.label.setText(text+"5")
    def method_6(self):
        text=self.label.text()
        self.label.setText(text+"6")
    def method_7(self):
        text=self.label.text()
        self.label.setText(text+"7")
    def method_8(self):
        text=self.label.text()
        self.label.setText(text+"8")
    def method_9(self):
        text=self.label.text()
        self.label.setText(text+"9")  


    def method_zero(self):
        text=self.label.text()
        self.label.setText(text+"0") 
    def method_point(self):
        text=self.label.text()
        self.label.setText(text+".")

    def method_plus(self):
        text=self.label.text()
        self.label.setText(text+"+") 
    def method_min(self):
        text=self.label.text()
        self.label.setText(text+"-") 
    def method_mult(self):
        text=self.label.text()
        self.label.setText(text+"*") 
    def method_div(self):
        text=self.label.text()
        self.label.setText(text+"/") 
 
    def method_plus(self):
        text=self.label.text()
        self.label.setText(text+"+") 
    def method_del(self):
        text=self.label.text()
        if text=="Wrong input":
                self.label.setText("") 
        else:
                self.label.setText(text[:len(text)-1]) 
    def method_clear(self):
        text=self.label.text()
        self.label.setText("") 
 
    def method_equal(self):
        text=self.label.text()
        try:
                ans=eval(text)
                self.label.setText(str(ans))
        except:
                self.label.setText("Wrong input") 
 


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.push_7.setText(_translate("MainWindow", "0"))
        self.push_7.setShortcut(_translate("MainWindow", "0"))
        self.push_3.setText(_translate("MainWindow", "3"))
        self.push_3.setShortcut(_translate("MainWindow", "3"))
        self.push_mul.setShortcut(_translate("MainWindow", "*"))
        self.push_minus.setText(_translate("MainWindow", "-"))
        self.push_minus.setShortcut(_translate("MainWindow", "-"))
        self.pus_plus.setText(_translate("MainWindow", "+"))
        self.pus_plus.setShortcut(_translate("MainWindow", "+"))
        self.push_2.setText(_translate("MainWindow", "2"))
        self.push_4.setText(_translate("MainWindow", "4"))
        self.push_clear.setText(_translate("MainWindow", "Clear"))
        self.push_clear.setShortcut(_translate("MainWindow", "Del"))
        
        self.push_1.setText(_translate("MainWindow", "1"))
        self.push_1.setShortcut(_translate("MainWindow", "1"))
        self.push_2.setText(_translate("MainWindow", "2"))
        self.push_2.setShortcut(_translate("MainWindow", "2"))
        self.push_3.setText(_translate("MainWindow", "3"))
        self.push_3.setShortcut(_translate("MainWindow", "3"))
        self.push_4.setText(_translate("MainWindow", "4"))
        self.push_4.setShortcut(_translate("MainWindow", "4"))
        
        self.push_del.setText(_translate("MainWindow", "Del"))
        self.push_del.setShortcut(_translate("MainWindow", "Backspace"))
        
        self.push_div.setText(_translate("MainWindow", "="))
        self.push_div.setShortcut(_translate("MainWindow", "="))
        self.push_div.setShortcut(_translate("MainWindow", "Enter"))
        self.push_9.setText(_translate("MainWindow", "."))
        self.push_mul.setShortcut(_translate("MainWindow", "*"))
        self.push_mul.setText(_translate("MainWindow", "x"))
        self.push_mul.setShortcut(_translate("MainWindow", "*"))
        self.push_6.setText(_translate("MainWindow", "6"))
        self.push_6.setShortcut(_translate("MainWindow", "6"))
        self.push_5.setText(_translate("MainWindow", "5"))
        self.push_5.setShortcut(_translate("MainWindow", "5"))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton.setShortcut(_translate("MainWindow", "7"))
        self.pushButton_3.setText(_translate("MainWindow", "8"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "8"))
        self.pushButton_4.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setShortcut(_translate("MainWindow", "9"))
        self.pushButton_5.setText(_translate("MainWindow", "/"))
        self.pushButton_5.setShortcut(_translate("MainWindow", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

