import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from explanation import Ui_ExplanationWindow
from solution import Ui_Solution
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
        self.btnSolution.clicked.connect(self.clickSolution)
        self.btnVisual.clicked.connect(self.clickVisualization)
        self.prev.clicked.connect(self.clickPrevious)
        self.next.clicked.connect(self.clickNext)
        self.addCustom.clicked.connect(self.clickAddCustomer)
    def changeScreen(self):
        nextwindow = MainWindow(self.state)
        widget.addWidget(nextwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def clickExplain(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ExplanationWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clickSolution(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Solution()
        self.ui.setupUi(self.window)
        self.window.show()
    def clickVisualization(self):
        pass
    def clickPrevious(self):
        widget.removeWidget(widget.currentWidget())
        widget.setCurrentIndex(widget.currentIndex()-1)

    def clickNext(self):
        if self.state["mutex"] == "lock":
            if self.state["lock_mutex"] == "barber":
                self.state["state"] = "Barber walks "+ self.state["waiting room"][0] +" to the barber's chair and releases the mutex."
                self.state["barber's chair"] = self.state["waiting room"][0]
                self.state["waiting room"].pop(0)
                self.state["waiting room"].append(None)
                self.state["customers"] -= 1
                self.state["waiting"] -= 1
                self.state["chairs"] += 1
                
            elif self.state["lock_mutex"] not in self.state["waiting room"]:
                self.state["state"] = self.state["lock_mutex"] + " sees the full waiting room, releases the mutex and leaves."
            else:
                self.state["state"] = self.state["lock_mutex"] + " sits down and releases the mutex."
            self.state["mutex"] = "unlock"
            self.state["lock_mutex"] = None
        else:
            if self.state["barber"] == "sleeping":
                self.state["barber"] = "Awake"
            if self.state["barber's chair"] == None and self.state["waiting"] > 0:
                self.state["state"] = "Barber sees a customer, locks the mutex and calls the customer."
                self.state["mutex"] = "lock"
                self.state["lock_mutex"] = "barber"
            elif self.state["barber's chair"] != None:
                self.state["state"] = "Barber finishes cutting "+ self.state["barber's chair"] + " 's hair."
                self.state["barber's chair"] = None
                self.state["mutex"] = "unlock"
            elif self.state["barber's chair"] == None and self.state["waiting"] == 0:
                self.state["barber"] = "sleeping"
                self.state["state"] = "Barber sees no customers and instantly falls asleep."
        self.changeScreen()
    def clickAddCustomer(self):
        if self.state["mutex"] == "unlock":
            
            for i in range(0,4):
                if self.state["waiting room"][i] == None:
                    self.state["waiting room"][i] = "Customer #"+ str(self.state["addCustom"])
                    break
            self.state["state"] = "Customer #"+ str(self.state["addCustom"]) + " arrives and locks the mutex to see if they will wait."
            self.state["mutex"] = "lock"
            self.state["lock_mutex"] = "Customer #"+ str(self.state["addCustom"])
            if self.state["chairs"] > 0:    
                self.state["customers"] += 1
                self.state["waiting"] += 1
                self.state["chairs"] -= 1
                self.state["addCustom"] += 1
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