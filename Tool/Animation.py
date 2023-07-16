from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve

global temp
temp = 0


class UIFunction:
    def __init__(self, parent):
        self.parent = parent

    def MeauFunction(self):
        global temp
        if temp == 0:
            temp = 1
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
            animation.setDuration(200)
            # 曲线效果
            # animation.setEasingCurve(QEasingCurve.OutElastic)
            animation.start()
        else:
            temp = 0
            TarGet = self.parent.widget
            animation = QPropertyAnimation(TarGet)
            animation.setTargetObject(TarGet)
            animation.setPropertyName(b"geometry")
            animation.setStartValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
                                          TarGet.geometry().width(),
                                          TarGet.geometry().height()))
            animation.setEndValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
                                        0,
                                        0))
            animation.setDuration(200)
            # 曲线效果
            # animation.setEasingCurve(QEasingCurve.OutElastic)
            animation.start()


    # def Shaow(self):
    #     self.pushButton_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect())