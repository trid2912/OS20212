# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time


class Ui_Dialog(object):
    def setupUi(self, Dialog, cus = None):
        Dialog.setObjectName("Dialog")
        Dialog.resize(859, 535)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 841, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnExplain = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnExplain.setObjectName("btnExplain")
        self.horizontalLayout.addWidget(self.btnExplain)
        self.btnSolution = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSolution.setObjectName("btnSolution")
        self.horizontalLayout.addWidget(self.btnSolution)
        self.btnVisual = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnVisual.setObjectName("btnVisual")
        self.horizontalLayout.addWidget(self.btnVisual)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 181, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(560, 70, 181, 21))
        self.label_2.setObjectName("label_2")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(0, 120, 281, 211))
        self.listView.setObjectName("listView")
        self.customer3 = QtWidgets.QLabel(Dialog)
        self.customer3.setGeometry(QtCore.QRect(0, 230, 281, 41))
        self.customer3.setObjectName("customer3")
        self.customer1 = QtWidgets.QLabel(Dialog)
        self.customer1.setGeometry(QtCore.QRect(0, 120, 281, 51))
        self.customer1.setObjectName("customer1")
        self.customer2 = QtWidgets.QLabel(Dialog)
        self.customer2.setGeometry(QtCore.QRect(0, 180, 281, 41))
        self.customer2.setObjectName("customer2")
        self.customer4 = QtWidgets.QLabel(Dialog)
        self.customer4.setGeometry(QtCore.QRect(0, 280, 281, 41))
        self.customer4.setObjectName("customer4")
        self.listView_2 = QtWidgets.QListView(Dialog)
        self.listView_2.setGeometry(QtCore.QRect(550, 120, 261, 211))
        self.listView_2.setObjectName("listView_2")
        self.numberCustomer = QtWidgets.QLabel(Dialog)
        self.numberCustomer.setGeometry(QtCore.QRect(730, 160, 55, 31))
        self.numberCustomer.setObjectName("numberCustomer")
        self.chair = QtWidgets.QLabel(Dialog)
        self.chair.setGeometry(QtCore.QRect(730, 280, 55, 21))
        self.chair.setObjectName("chair")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(560, 130, 231, 21))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(560, 240, 141, 31))
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(560, 200, 141, 31))
        self.label_12.setObjectName("label_12")
        self.waiting = QtWidgets.QLabel(Dialog)
        self.waiting.setGeometry(QtCore.QRect(730, 240, 55, 31))
        self.waiting.setObjectName("waiting")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(560, 160, 141, 31))
        self.label_10.setObjectName("label_10")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(560, 280, 141, 21))
        self.label_3.setObjectName("label_3")
        self.barberState = QtWidgets.QLabel(Dialog)
        self.barberState.setGeometry(QtCore.QRect(730, 130, 55, 21))
        self.barberState.setObjectName("barberState")
        self.mutex = QtWidgets.QLabel(Dialog)
        self.mutex.setGeometry(QtCore.QRect(730, 200, 55, 31))
        self.mutex.setObjectName("mutex")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(310, 80, 111, 16))
        self.label_4.setObjectName("label_4")
        self.listView_3 = QtWidgets.QListView(Dialog)
        self.listView_3.setGeometry(QtCore.QRect(290, 120, 251, 51))
        self.listView_3.setObjectName("listView_3")
        self.barberChair = QtWidgets.QLabel(Dialog)
        self.barberChair.setGeometry(QtCore.QRect(300, 130, 231, 31))
        self.barberChair.setObjectName("barberChair")
        self.prev = QtWidgets.QPushButton(Dialog)
        self.prev.setGeometry(QtCore.QRect(310, 300, 93, 28))
        self.prev.setObjectName("prev")
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(420, 300, 93, 28))
        self.next.setObjectName("next")
        self.addCustom = QtWidgets.QPushButton(Dialog)
        self.addCustom.setGeometry(QtCore.QRect(100, 350, 93, 28))
        self.addCustom.setObjectName("addCustom")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnExplain.setText(_translate("Dialog", "Explaination"))
        self.btnSolution.setText(_translate("Dialog", "Solution"))
        self.btnVisual.setText(_translate("Dialog", "Visualization"))
        self.label.setText(_translate("Dialog", "Waiting Room"))
        self.label_2.setText(_translate("Dialog", "State"))
        self.customer3.setText(_translate("Dialog", "TextLabel"))
        self.customer1.setText(_translate("Dialog", "TextLabel"))
        self.customer2.setText(_translate("Dialog", "TextLabel"))
        self.customer4.setText(_translate("Dialog", "TextLabel"))
        self.numberCustomer.setText(_translate("Dialog", "TextLabel"))
        self.chair.setText(_translate("Dialog", "TextLabel"))
        self.label_11.setText(_translate("Dialog", "Barber"))
        self.label_13.setText(_translate("Dialog", "Waiting"))
        self.label_12.setText(_translate("Dialog", "Mutex"))
        self.waiting.setText(_translate("Dialog", "TextLabel"))
        self.label_10.setText(_translate("Dialog", "Customers"))
        self.label_3.setText(_translate("Dialog", "Chairs"))
        self.barberState.setText(_translate("Dialog", "TextLabel"))
        self.mutex.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "Barber\'s chair"))
        self.barberChair.setText(_translate("Dialog", "TextLabel"))
        self.prev.setText(_translate("Dialog", "Prev"))
        self.next.setText(_translate("Dialog", "Next"))
        self.addCustom.setText(_translate("Dialog", "Add customer"))

    def clickExplaination():
        pass
    def clickSolution():
        pass
    def clickVisualization():
        pass
    def clickAddCustomer():
        pass
    def clickPrev():
        pass
    def clickNext():
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    