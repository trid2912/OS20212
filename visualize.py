import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from explanation import Ui_ExplanationWindow
from solution import Ui_Solution
class MainWindow(QMainWindow):
    def __init__(self, state = {"barber": "sleeping", "customers": 0, "mutex": "unlock", "waiting": 0, "chairs": 4,
                                "barber's chair": None, "waiting room": [], "lock_mutex": None,
                                "state": "Barbershop open for business...", "addCustom": 1, "window": "visualize"}) :
        super(MainWindow,self).__init__()
        self.state = state
        
        if self.state["window"] == "visualize":
            loadUi("visualize.ui", self)
            
            '''
            self.customer1.setText(state["waiting room"][0])
            self.customer2.setText(state["waiting room"][1])
            self.customer3.setText(state["waiting room"][2])
            self.customer4.setText(state["waiting room"][3])
            '''
            for i in range(state["waiting"]):
                self.WaitingList.addItem(state["waiting room"][i])
            self.barberChair.setText(state["barber's chair"])
            self.lblstate.setText(state["state"])

            self.barberState.setText(state["barber"])
            self.numberCustomer.setText(str(state["customers"]))
            self.mutex.setText(state["mutex"])
            self.waiting.setText(str(state["waiting"]))
            self.chair.setText(str(state["chairs"]))

            self.btnVisual.setStyleSheet('QWidget {background-color: %s}' % "white")

            self.next.clicked.connect(self.clickNext)
            self.addCustom.clicked.connect(self.clickAddCustomer)
            self.addChair.clicked.connect(self.clickAddChair)
        elif self.state["window"] == "solution":
            loadUi("solution.ui",self)
            self.btnSolution.setStyleSheet('QWidget {background-color: %s}' % "white")
        elif self.state["window"] == "explanation":
            loadUi("explanation.ui",self)
            self.btnExplain.setStyleSheet('QWidget {background-color: %s}' % "white")
        self.btnExplain.clicked.connect(self.clickExplain)
        self.btnSolution.clicked.connect(self.clickSolution)
        self.btnVisual.clicked.connect(self.clickVisualization)
    def changeScreen(self):
        nextwindow = MainWindow(self.state)
        widget.addWidget(nextwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def clickExplain(self):
        '''
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ExplanationWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        '''
        self.state["window"] = "explanation"
        self.changeScreen()
        
    def clickSolution(self):
        '''
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Solution()
        self.ui.setupUi(self.window)
        self.window.show()
        '''
        self.state["window"] = "solution"
        self.changeScreen()
    def clickVisualization(self):
        self.state["window"] = "visualize"
        self.changeScreen()

    def clickNext(self):
        if self.state["mutex"] == "lock":
            if self.state["lock_mutex"] == "barber":
                self.state["state"] = "Barber walks "+ self.state["waiting room"][0] +" to the barber's chair and releases the mutex."
                self.state["barber's chair"] = self.state["waiting room"][0]
                self.state["waiting room"].pop(0)
                #self.state["customers"] -= 1
                self.state["waiting"] -= 1
                self.state["chairs"] += 1
            else:
                if self.state["chairs"] > 0:    
                    self.state["waiting room"].append( "Customer #"+ str(self.state["addCustom"]) )
                    self.state["state"] = self.state["lock_mutex"] + " sits down and releases the mutex."
                    self.state["customers"] += 1
                    self.state["waiting"] += 1
                    self.state["chairs"] -= 1
                    self.state["addCustom"] += 1
                else:
                    self.state["state"] = self.state["lock_mutex"] + " sees the full waiting room, releases the mutex and leaves."
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
                self.state["customers"] -= 1
                self.state["barber's chair"] = None
                self.state["mutex"] = "unlock"
            elif self.state["barber's chair"] == None and self.state["waiting"] == 0:
                self.state["barber"] = "sleeping"
                self.state["state"] = "Barber sees no customers and instantly falls asleep."
        self.changeScreen()
    def clickAddCustomer(self):
        if self.state["mutex"] == "unlock":
            self.state["state"] = "Customer #"+ str(self.state["addCustom"]) + " arrives and locks the mutex to see if they will wait."
            self.state["mutex"] = "lock"
            self.state["lock_mutex"] = "Customer #"+ str(self.state["addCustom"])
        else:
            self.state["state"] = "Mutex is lock so customer #" + str(self.state["addCustom"]) + " cannot go to waiting room."
        self.changeScreen()
    def clickAddChair(self):
        self.state["chairs"] += 1
        self.changeScreen()
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)
#widget.setFixedHeight(550)
#widget.setFixedWidth(880)
widget.show()
sys.exit(app.exec_())