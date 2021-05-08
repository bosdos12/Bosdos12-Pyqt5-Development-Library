from PyQt5 import QtCore, QtGui, QtWidgets
#from PySide.QtGui import QFrame

#///////////////////////////////////////////////////////////////////////////////////////////////////////

# @p = percentage;
# @s = style;
# @a = app;
# @a gives the function the app data, the function then looks for @s, the @s is either "w" or "h" (width, height);
# based of the @s, the function returns the size of the screen by percentage of the @s dimension;
def PercentageValue(p, s, a):
    width = a.primaryScreen().size().width()
    height = a.primaryScreen().size().height()
    if (p > 0) and p <= 100:
        if s == "h":
            return int((p/100)*height)
        elif s == "w":
            return int((p/100)*width)

        else:
            print(f"Invalid argument, please enter either 'v' or 'h' as the first parameter,\n{str(s)} is invalid;") 
    else:
        print(f"Please enter a percentage value between 0 and 100,\n{str(p)} is invalid;")

#///////////////////////////////////////////////////////////////////////////////////////////////////////
# Horizontal line;
#class QHLine(QFrame):
#    def __init__(self):
#        super(QHLine, self).__init__()
#        self.setFrameShape(QFrame.HLine)
#        self.setFrameShadow(QFrame.Sunken)
# Vertical Line;
#class QVLine(QFrame):
#    def __init__(self):
#        super(QVLine, self).__init__()
#        self.setFrameShape(QFrame.VLine)
#        self.setFrameShadow(QFrame.Sunken)
#///////////////////////////////////////////////////////////////////////////////////////////////////////
class AnimatedButton(QtWidgets.QPushButton):
    def __init__(self, parent, startColor, endColor, width, height, buttonText):
        super().__init__(parent)

        self.setMinimumSize(width, height)
        self.setText(buttonText)

        self.color1 = endColor
        self.color2 = startColor
        #QtGui.QColor(240, 53, 218)
        #QtGui.QColor(61, 217, 245)

        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0.00001,
            endValue=0.9999,
            duration=250
        )

    def _animate(self, value):
        qss = f"""
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: rgb(255, 255, 255);
            border-style: solid;
            border-radius:21px;
            border: 2px solid gray;
        """
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        qss += grad
        self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)


#///////////////////////////////////////////////////////////////////////////////////////////////////////
class adakCheckButton(QtWidgets.QPushButton):
    def __init__(self, parent, width, height):
        super().__init__(parent)

        self.setFixedSize(width, height)                             # Setting a fixed size;
        self.setFont(QtGui.QFont("Arial", (height//4)+(width//4)))   # Setting a font size;

        self.isChecked = False                          # The state keeper for clicked/not clicked;
        self.clicked.connect(self.setCheckedProperly)   # Calling the function setCheckedProperly to set the checked state of the button;

    def setCheckedProperly(self):
        if self.isChecked:
            self.isChecked = False
            self.setText("")
        else:
            self.isChecked = True
            self.setText("✔")

    





# TESTS #
"""
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 300)

        a = adakCheckButton(self, 100, 100)



        ye = QtWidgets.QPushButton("touch me", self, clicked=lambda: print(a.isChecked))
        ye.move(200, 200)

        self.show()

app = QtWidgets.QApplication([])
mw = MainWindow()
app.exec_()
"""
