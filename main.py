import pandas as pd
import numpy as np
from cryptography.fernet import Fernet
from datetime import datetime
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog
import sys
import time


Database = pd.read_pickle('pass')
f = Database.Key['MastPass']
MP = f.decrypt(Database.at['MastPass','Pass']).decode()
print(MP)
# The data in encrypted form has its own datatype and class, if we save it to CSV, it gets turned into string.
# String cannot be decrypted by library as it is.
# To prevent that, we're using to_pickle().


class UI(object):
    def __init__(self):
        super(UI, self).__init__()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.466, y1:0, x2:0.568, y2:1, stop:0 rgba(38, 150, 250, 255), stop:1 rgba(255, 76, 255, 255));\n"
"border-radius: 20px")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.site = QtWidgets.QLineEdit(self.centralwidget)
        self.site.setGeometry(QtCore.QRect(642, 130, 113, 22))
        self.site.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.site.setObjectName("site")

        self.pass_display = QtWidgets.QLabel(self.centralwidget)
        self.pass_display.setGeometry(QtCore.QRect(551, 272, 230, 31))
        self.pass_display.setStyleSheet("background-color: rgba(255, 255, 255, 120);\n"
"border-radius:10px")
        self.pass_display.setObjectName("pass_display")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(211, 10, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 15px")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.u_display = QtWidgets.QLabel(self.centralwidget)
        self.u_display.setGeometry(QtCore.QRect(551, 238, 231, 31))
        self.u_display.setStyleSheet("background-color: rgba(255, 255, 255, 120);\n"
"border-radius:10px")
        self.u_display.setObjectName("u_display")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 101, 61, 21))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 5px")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.user = QtWidgets.QLineEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(642, 101, 113, 22))
        self.user.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.user.setObjectName("user")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 130, 61, 21))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 5px")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.GetPass = QtWidgets.QPushButton(self.centralwidget)
        self.GetPass.setGeometry(QtCore.QRect(628, 193, 81, 31))
        self.GetPass.setStyleSheet("background-color: rgba(39, 244, 255, 180);\n"
"border-radius: 15px")
        self.GetPass.setObjectName("GetPass")
        self.GetPass.clicked.connect(self.userDat)

        self.LU = QtWidgets.QLabel(self.centralwidget)
        self.LU.setGeometry(QtCore.QRect(551, 340, 231, 31))
        self.LU.setStyleSheet("background-color: rgba(255, 255, 255, 120);\n"
"border-radius:10px")
        self.LU.setObjectName("LU")

        self.s_display = QtWidgets.QLabel(self.centralwidget)
        self.s_display.setGeometry(QtCore.QRect(551, 306, 231, 31))
        self.s_display.setStyleSheet("background-color: rgba(255, 255, 255, 120);\n"
"border-radius:10px")
        self.s_display.setObjectName("s_display")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(540, 90, 256, 301))
        self.graphicsView.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.graphicsView.setObjectName("graphicsView")

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(540, 409, 256, 161))
        self.graphicsView_2.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(591, 420, 49, 21))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 5px")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.addsite = QtWidgets.QLineEdit(self.centralwidget)
        self.addsite.setGeometry(QtCore.QRect(641, 449, 113, 22))
        self.addsite.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.addsite.setObjectName("addsite")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(591, 449, 49, 21))
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 5px")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.adduser = QtWidgets.QLineEdit(self.centralwidget)
        self.adduser.setGeometry(QtCore.QRect(641, 420, 113, 22))
        self.adduser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.adduser.setObjectName("adduser")

        self.addpass = QtWidgets.QLineEdit(self.centralwidget)
        self.addpass.setGeometry(QtCore.QRect(642, 479, 113, 22))
        self.addpass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.addpass.setObjectName("addpass")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 479, 51, 21))
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 5px")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(633, 519, 81, 31))
        self.Add.setStyleSheet("background-color: rgba(39, 244, 255, 180);\n"
"border-radius: 15px")
        self.Add.setObjectName("Add")
        self.Add.clicked.connect(self.addu)

        self.mastPass = QtWidgets.QLineEdit(self.centralwidget)
        self.mastPass.setGeometry(QtCore.QRect(642, 160, 113, 22))
        self.mastPass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.mastPass.setObjectName("MastPass")
        self.mastPass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 160, 61, 21))
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 5px")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.Details = QtWidgets.QTableWidget(self.centralwidget)
        self.Details.setGeometry(QtCore.QRect(10, 90, 511, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Details.sizePolicy().hasHeightForWidth())
        self.Details.setSizePolicy(sizePolicy)
        self.Details.setMaximumSize(QtCore.QSize(511, 16777215))
        self.Details.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.Details.setObjectName("Details")
        self.Details.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.Details.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Details.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Details.setHorizontalHeaderItem(2, item)
        self.Details.setColumnWidth(0, 195)
        self.Details.setColumnWidth(1, 150)
        self.Details.setColumnWidth(2, 150)
        self.loaddata()

        self.graphicsView.raise_()
        self.site.raise_()
        self.pass_display.raise_()
        self.label_3.raise_()
        self.u_display.raise_()
        self.label.raise_()
        self.user.raise_()
        self.label_2.raise_()
        self.GetPass.raise_()
        self.LU.raise_()
        self.s_display.raise_()
        self.graphicsView_2.raise_()
        self.label_4.raise_()
        self.addsite.raise_()
        self.label_5.raise_()
        self.adduser.raise_()
        self.addpass.raise_()
        self.label_6.raise_()
        self.Add.raise_()
        self.mastPass.raise_()
        self.label_7.raise_()
        self.Details.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        pswd = 'Password: '
        ud = 'User: '
        sd = 'Site: '
        lud = 'Last Updated: '
        self.pass_display.setText(pswd)
        self.u_display.setText(ud)
        self.s_display.setText(sd)
        self.LU.setText(lud)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Safe"))
        self.label_3.setText(_translate("MainWindow", "Password Safe"))
        self.label.setText(_translate("MainWindow", "User:"))
        self.label_2.setText(_translate("MainWindow", "Site:"))
        self.GetPass.setText(_translate("MainWindow", "Get Password"))
        self.label_4.setText(_translate("MainWindow", "User:"))
        self.label_5.setText(_translate("MainWindow", "Site:"))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.Add.setText(_translate("MainWindow", "Add"))
        self.label_7.setText(_translate("MainWindow", "Acess Key:"))
        item = self.Details.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User"))
        item = self.Details.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Site"))
        item = self.Details.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last Updated"))


    def userDat(self):
        user = self.user.text()
        acckey = self.mastPass.text()
        if user not in Database.index:
            self.u_display.setText('User Not Found!')
        else:
            if acckey == MP:
                det = Collect(user)
                pswd = "Password: " + det[0]
                ud = 'User: ' + user
                sd = 'Site: ' + det[1]
                lud = 'Last Updated: ' + det[2]
                print(pswd)
                self.pass_display.setText(pswd)
                self.u_display.setText(ud)
                self.s_display.setText(sd)
                self.LU.setText(lud)
            else:
                self.pass_display.setText('Incorrect Access Key')

    def addu(self):
        user = self.adduser.text()
        site = self.addsite.text()
        pswd = self.addpass.text()
        Add(user, pswd, site)
        print('added', Database)
        self.updata()

    def updata(self):
        self.Details.clearContents()
        self.loaddata()

    def loaddata(self):
        self.Details.setRowCount(len(Database))
        row = 0
        table = self.Details
        for user in Database.index:
            table.setItem(row, 0, QtWidgets.QTableWidgetItem(user))
            table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(Database.Site[user])))
            table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(Database.DnT[user])))
            row += 1


def main():
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = UI()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())


# to add an id just put Add(user,pswd,site)
def Add(user, pswd, site):
    pkey = Fernet.generate_key()
    fernet = Fernet(pkey)
    now = datetime.now()
    pswdencd = fernet.encrypt(pswd.encode())
    curtime = now.strftime("%d/%m/%Y %H:%M:%S")
    Database.loc[user, :] = [pswdencd, fernet, site, curtime]
    # We can't store Key as it in Database.
    # The Fernet(pkey) value generated everytime, even for same key is different
    # so we're storing Fernet(pkey) as it is
    Database.to_pickle('pass')


# to get data back use Collect(user)
def Collect(user):
    pswd = Database.Pass[user]
    pfer = Database.Key[user]
    decoded_pass = pfer.decrypt(pswd).decode()
    return [decoded_pass, Database.Site[user], Database.DnT[user]]


main()
#Uid = input("UID:")
#pwd = input("pswd:")
#isite = input("site:")
#Add(Uid, pwd, isite)
#print(Database.DnT[Uid])
#UidC = input("Enter User to be displayed:\n")
#det = Collect(UidC)
#print("Details:")
#print("User:\n", UidC)
#print("Pswd:\n", det[0])
#print("Site:\n", det[1])
#print("Last Saved (date-time):\n", det[2])