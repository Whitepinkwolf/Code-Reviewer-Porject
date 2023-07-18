from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve

global temp
temp = 0


class UIFunction:
    def __init__(self, parent):
        self.parent = parent
        self.menu_visible = False
        self.sign = self.parent.HidePushButton.text()

    def MeauFunction(self):
        self.sign = self.parent.HidePushButton.text()
        if self.sign == ">":
            print("!11")
            TarGet = self.parent.widget
            animation = QPropertyAnimation(TarGet)
            animation.setTargetObject(TarGet)
            animation.setPropertyName(b"geometry")
            animation.setStartValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
                                          TarGet.geometry().width(),
                                          TarGet.geometry().height()))
            animation.setEndValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
                                        0,
                                        TarGet.geometry().height()))

            animation.setDuration(200)
            animation.start()

            stackedWidget = self.parent.ChangeStackedWidget
            stackedWidget.setGeometry(QRect(stackedWidget.geometry().x() - 131,
                                            stackedWidget.geometry().y(),
                                            stackedWidget.geometry().width(),
                                            stackedWidget.geometry().height()))
        elif self.sign == "<":
            print(123)
            TarGet = self.parent.widget
            animation = QPropertyAnimation(TarGet)
            animation.setTargetObject(TarGet)
            animation.setPropertyName(b"geometry")
            animation.setStartValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
                                          TarGet.geometry().width(),
                                          TarGet.geometry().height()))
            animation.setEndValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
                                            131,
                                            941))
            # animation.setEndValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
            #                             TarGet.geometry().width(),
            #                             TarGet.geometry().height()))
            animation.setDuration(200)
            animation.start()

            stackedWidget = self.parent.ChangeStackedWidget
            stackedWidget.setGeometry(QRect(stackedWidget.geometry().x() + 131,
                                            stackedWidget.geometry().y(),
                                            stackedWidget.geometry().width(),
                                            stackedWidget.geometry().height()))
