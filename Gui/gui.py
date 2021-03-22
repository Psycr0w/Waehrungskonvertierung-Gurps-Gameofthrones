from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 254)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 261, 41))
        self.textEdit.setObjectName("textEdit")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(283, 50, 55, 17))
        self.radioButton.setObjectName("radioButton")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(9, 92, 410, 121))
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(344, 47, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(clicked)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 21))
        self.menubar.setObjectName("menubar")

        self.menuW_hrungskonvertierung = QtWidgets.QMenu(self.menubar)
        self.menuW_hrungskonvertierung.setObjectName("menuW_hrungskonvertierung")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuW_hrungskonvertierung.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Monde"))
        self.pushButton.setText(_translate("MainWindow", "Konvertieren"))
        self.menuW_hrungskonvertierung.setTitle(_translate("MainWindow", "Währungskonvertierung"))