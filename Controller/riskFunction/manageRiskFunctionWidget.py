from qtpy import QtWidgets

from UI.riskFunction.manageRiskFunctionWidget import Ui_ManageRiskFunction

class manageRiskFunction_Widget(QtWidgets.QWidget, Ui_ManageRiskFunction):
    def __init__(self, parent=None):
        super(manageRiskFunction_Widget, self).__init__(parent)
        self.setupUi(self)

        # self.initUI()
        # self.connectSignalsSlots()

    