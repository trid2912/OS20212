import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self, state = {"barber": "sleeping", "customers": 0, "mutex": "unlock", "waiting": 0, "chairs": 4,
                                "barber's chair": None, "waiting room": [None, None, None, None], "lock_mutex": None,
                                "state": "Barbershop open for business...", "addCustom": 1}) :
        super(MainWindow,self).__init__()
        loadUi("gui.ui", self)
        self.state = state

        self.customer1.setText(state["waiting room"][0])
        self.customer2.setText(state["waiting room"][1])
        self.customer3.setText(state["waiting room"][2])
        self.customer4.setText(state["waiting room"][3])

        self.barberChair.setText(state["barber's chair"])
        self.lblstate.setText(state["state"])

        self.barberState.setText(state["barber"])
        self.numberCustomer.setText(str(state["customers"]))
        self.mutex.setText(state["mutex"])
        self.waiting.setText(str(state["waiting"]))
        self.chair.setText(str(state["chairs"]))

        self.btnExplain.clicked.connect(self.clickExplain)
        self.btnSolution.clicked.connect(self.changeScreen)
        self.btnVisual.clicked.connect(self.clickVisualization)
        self.prev.clicked.connect(self.clickPrevious)
        self.next.clicked.connect(self.clickNext)
        self.addCustom.clicked.connect(self.clickAddCustomer)
    def changeScreen(self):
        nextwindow = MainWindow(self.state)
        widget.addWidget(nextwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def clickExplain(self):
        pass
    def clickSolution(self):
        pass
    def clickVisualization(self):
        pass
    def clickPrevious(self):
        pass
    def clickNext(self):
        if self.state["mutex"] == "lock":
            if self.state["lock_mutex"] == "barber":
                self.state["state"] = "Barber sees a customer, locks the mutex and calls the customer."
            else:
                self.state["state"] = self.state["lock_mutex"] + " sits down and releases the mutex."
            self.state["mutex"] = "unlock"
            self.state["lock_mutex"] = None
        self.changeScreen()
    def clickAddCustomer(self):
        if self.state["mutex"] == "unlock":
            if self.state["chairs"] > 0:
                for i in range(0,4):
                    if self.state["waiting room"][i] == None:
                        self.state["waiting room"][i] = "Customer #"+ str(self.state["addCustom"])
                        break
                self.state["state"] = "Customer #"+ str(self.state["addCustom"]) + " arrives and locks the mutex to see if they will wait."
                self.state["customers"] += 1
                self.state["mutex"] = "lock"
                self.state["lock_mutex"] = "Customer #"+ str(self.state["addCustom"])
                self.state["waiting"] += 1
                self.state["chairs"] -= 1
                self.state["addCustom"] += 1
            else:
                self.state["state"] = "Customer #"+ str(self.state["addCustom"]) + " sees the full waiting room, releases the mutex and leaves."
        else:
            self.state["state"] = "Mutex is lock so customer #" + str(self.state["addCustom"]) + " cannot go to waiting room."
        self.changeScreen()
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)
widget.setFixedHeight(550)
widget.setFixedWidth(880)
widget.show()
sys.exit(app.exec_())