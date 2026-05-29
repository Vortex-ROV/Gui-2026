# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pilot guiWMuatC.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setStyleSheet(u"QFrame{\n"
"  border-radius: 0px\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.MainWidget = QStackedWidget(self.centralwidget)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setGeometry(QRect(0, 0, 1920, 1080))
        self.MainWidget.setMinimumSize(QSize(0, 0))
        self.MainWidget.setMaximumSize(QSize(1920, 1080))
        self.ControlWidget = QWidget()
        self.ControlWidget.setObjectName(u"ControlWidget")
        self.ControlWidget.setMaximumSize(QSize(1920, 1080))
        self.mainFrame = QFrame(self.ControlWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 1920, 1080))
        self.mainFrame.setStyleSheet(u"")
        self.mainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TopWidget = QStackedWidget(self.mainFrame)
        self.TopWidget.setObjectName(u"TopWidget")
        self.TopWidget.setMinimumSize(QSize(0, 0))
        self.TopWidget.setMaximumSize(QSize(16777215, 60))
        self.TopWidget.setStyleSheet(u"")
        self.MainTobbarwidget = QWidget()
        self.MainTobbarwidget.setObjectName(u"MainTobbarwidget")
        self.MainTobbarwidget.setMinimumSize(QSize(0, 0))
        self.MainTobbarwidget.setMaximumSize(QSize(1920, 60))
        self.MainTobbarwidget.setStyleSheet(u"")
        self.topBar = QFrame(self.MainTobbarwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setGeometry(QRect(0, 0, 1920, 62))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topBar.sizePolicy().hasHeightForWidth())
        self.topBar.setSizePolicy(sizePolicy)
        self.topBar.setMinimumSize(QSize(0, 62))
        self.topBar.setMaximumSize(QSize(1920, 60))
        self.topBar.setStyleSheet(u"QFrame#topBar {\n"
"background: qlineargradient(\n"
"x1:0, y1:0, x2:0, y2:1,\n"
"stop:0 rgb(2, 5, 18),\n"
"stop:0.05 rgb(8, 12, 35),\n"
"stop:1 rgb(5, 18, 50)\n"
");\n"
"border: none;\n"
"border-left: 2px solid rgb(201, 169, 97);\n"
"border-top: 2px solid rgb(201, 169, 97);\n"
"border-right: 2px solid rgb(201, 169, 97);\n"
"border-bottom:none;\n"
"min-height: 60px;\n"
"}")
        self.topBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.topBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lefticonsbar = QFrame(self.topBar)
        self.lefticonsbar.setObjectName(u"lefticonsbar")
        self.lefticonsbar.setMinimumSize(QSize(0, 0))
        self.lefticonsbar.setMaximumSize(QSize(180, 60))
        self.lefticonsbar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lefticonsbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.lefticonsbar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.lefticonsbar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menubutton = QPushButton(self.lefticonsbar)
        self.Menubutton.setObjectName(u"Menubutton")
        self.Menubutton.setMinimumSize(QSize(0, 0))
        self.Menubutton.setMaximumSize(QSize(60, 56))
        self.Menubutton.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(45, 95, 140, 100);  /* Your lighter blue with transparency */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 45, 65);  /* Solid darker navy */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(20, 45, 65);  /* Keep solid while holding */\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/iCONS/menu2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Menubutton.setIcon(icon)
        self.Menubutton.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.Menubutton)

        self.Teambutton = QPushButton(self.lefticonsbar)
        self.Teambutton.setObjectName(u"Teambutton")
        self.Teambutton.setMinimumSize(QSize(0, 0))
        self.Teambutton.setMaximumSize(QSize(60, 56))
        self.Teambutton.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(32, 70, 98, 100);  /* Navy with transparency */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 45, 65);  /* Solid darker navy */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(20, 45, 65);  /* Keep solid while holding */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;\n"
"    color: rgb(140, 140, 140);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/iCONS/team.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Teambutton.setIcon(icon1)
        self.Teambutton.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.Teambutton)

        self.camerasbutton = QPushButton(self.lefticonsbar)
        self.camerasbutton.setObjectName(u"camerasbutton")
        self.camerasbutton.setMinimumSize(QSize(0, 0))
        self.camerasbutton.setMaximumSize(QSize(60, 56))
        self.camerasbutton.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color: transparent;\n"
"\n"
"color: white;\n"
"\n"
"border: none;\n"
"\n"
"border-radius: 5px;\n"
"\n"
"padding: 6px 14px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgba(155, 115, 45, 100);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"background-color: rgb(20, 45, 65);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/iCONS/two-arrow down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camerasbutton.setIcon(icon2)
        self.camerasbutton.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.camerasbutton)


        self.horizontalLayout_3.addWidget(self.lefticonsbar)

        self.logoframe = QFrame(self.topBar)
        self.logoframe.setObjectName(u"logoframe")
        self.logoframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.logoframe.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.logoframe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(750, 0, 49, 60))
        self.label.setPixmap(QPixmap(u":/Icons/iCONS/titnaslogo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.logoframe)

        self.navigationsicons = QFrame(self.topBar)
        self.navigationsicons.setObjectName(u"navigationsicons")
        self.navigationsicons.setMinimumSize(QSize(0, 60))
        self.navigationsicons.setMaximumSize(QSize(180, 60))
        self.navigationsicons.setFrameShape(QFrame.Shape.StyledPanel)
        self.navigationsicons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.navigationsicons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Minimizebutton = QPushButton(self.navigationsicons)
        self.Minimizebutton.setObjectName(u"Minimizebutton")
        self.Minimizebutton.setMinimumSize(QSize(0, 0))
        self.Minimizebutton.setMaximumSize(QSize(60, 56))
        self.Minimizebutton.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 30);  /* Very soft white hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 50);  /* Slightly more visible when pressed */\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/iCONS/angle-double-small-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Minimizebutton.setIcon(icon3)
        self.Minimizebutton.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.Minimizebutton)

        self.MaximizeButton = QPushButton(self.navigationsicons)
        self.MaximizeButton.setObjectName(u"MaximizeButton")
        self.MaximizeButton.setMinimumSize(QSize(0, 0))
        self.MaximizeButton.setMaximumSize(QSize(60, 56))
        self.MaximizeButton.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(34, 197, 94, 100);  /* Green hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(21, 128, 61);  /* Dark green when pressed */\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/iCONS/arrow-up-right-and-arrow-down-left-from-center.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MaximizeButton.setIcon(icon4)
        self.MaximizeButton.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.MaximizeButton)

        self.Exitbutton = QPushButton(self.navigationsicons)
        self.Exitbutton.setObjectName(u"Exitbutton")
        self.Exitbutton.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Exitbutton.sizePolicy().hasHeightForWidth())
        self.Exitbutton.setSizePolicy(sizePolicy1)
        self.Exitbutton.setMinimumSize(QSize(0, 0))
        self.Exitbutton.setMaximumSize(QSize(60, 56))
        self.Exitbutton.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(220, 53, 53, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(100, 0, 0);  /* Even darker red when pressed */\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/iCONS/x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Exitbutton.setIcon(icon5)
        self.Exitbutton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.Exitbutton)


        self.horizontalLayout_3.addWidget(self.navigationsicons)

        self.TopWidget.addWidget(self.MainTobbarwidget)

        self.verticalLayout_2.addWidget(self.TopWidget)

        self.middlewidget = QStackedWidget(self.mainFrame)
        self.middlewidget.setObjectName(u"middlewidget")
        self.middlewidget.setMinimumSize(QSize(0, 0))
        self.firstcamerasmodewidget = QWidget()
        self.firstcamerasmodewidget.setObjectName(u"firstcamerasmodewidget")
        self.firstcamerasmodewidget.setMinimumSize(QSize(0, 0))
        self.firstcamerasmodewidget.setStyleSheet(u"QFrame#zedmode {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0   rgb(5, 18, 50),\n"
"        stop:0.3 rgb(8, 22, 60),\n"
"        stop:1   rgb(10, 28, 72)\n"
"    );\n"
"    border: 2px solid rgb(201, 169, 97);\n"
"    border-top: none;\n"
"    border-bottom: none;\n"
"    padding: 10px;\n"
"}")
        self.zedmode = QFrame(self.firstcamerasmodewidget)
        self.zedmode.setObjectName(u"zedmode")
        self.zedmode.setGeometry(QRect(0, 0, 1920, 870))
        self.zedmode.setMinimumSize(QSize(0, 0))
        self.zedmode.setMaximumSize(QSize(16777215, 870))
        self.zedmode.setFrameShape(QFrame.Shape.StyledPanel)
        self.zedmode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.zedmode)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.zedleftlabel = QLabel(self.zedmode)
        self.zedleftlabel.setObjectName(u"zedleftlabel")
        self.zedleftlabel.setScaledContents(True)
        self.zedleftlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.zedleftlabel)

        self.middlewidget.addWidget(self.firstcamerasmodewidget)
        self.twoback = QWidget()
        self.twoback.setObjectName(u"twoback")
        self.twoback.setStyleSheet(u"QFrame#twobackcameras {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0   rgb(5, 18, 50),\n"
"        stop:0.3 rgb(8, 22, 60),\n"
"        stop:1   rgb(10, 28, 72)\n"
"    );\n"
"    border: 2px solid rgb(201, 169, 97);\n"
"    border-top: none;\n"
"    border-bottom: none;\n"
"    padding: 10px;\n"
"}")
        self.twobackcameras = QFrame(self.twoback)
        self.twobackcameras.setObjectName(u"twobackcameras")
        self.twobackcameras.setGeometry(QRect(0, 0, 1920, 870))
        self.twobackcameras.setFrameShape(QFrame.Shape.StyledPanel)
        self.twobackcameras.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.twobackcameras)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.rightrear = QLabel(self.twobackcameras)
        self.rightrear.setObjectName(u"rightrear")
        self.rightrear.setScaledContents(True)
        self.rightrear.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.rightrear)

        self.leftrear = QLabel(self.twobackcameras)
        self.leftrear.setObjectName(u"leftrear")
        self.leftrear.setScaledContents(True)
        self.leftrear.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.leftrear)

        self.middlewidget.addWidget(self.twoback)
        self.downcamera = QWidget()
        self.downcamera.setObjectName(u"downcamera")
        self.downcamera.setStyleSheet(u"QFrame#downcameraframe {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0   rgb(5, 18, 50),\n"
"        stop:0.3 rgb(8, 22, 60),\n"
"        stop:1   rgb(10, 28, 72)\n"
"    );\n"
"    border: 2px solid rgb(201, 169, 97);\n"
"    border-top: none;\n"
"    border-bottom: none;\n"
"    padding: 10px;\n"
"}")
        self.downcameraframe = QFrame(self.downcamera)
        self.downcameraframe.setObjectName(u"downcameraframe")
        self.downcameraframe.setGeometry(QRect(0, 0, 1920, 870))
        self.downcameraframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.downcameraframe.setFrameShadow(QFrame.Shadow.Raised)
        self.downcameralabel = QLabel(self.downcameraframe)
        self.downcameralabel.setObjectName(u"downcameralabel")
        self.downcameralabel.setGeometry(QRect(525, 0, 870, 870))
        self.downcameralabel.setScaledContents(True)
        self.downcameralabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.middlewidget.addWidget(self.downcamera)
        self.twocamerasanddown = QWidget()
        self.twocamerasanddown.setObjectName(u"twocamerasanddown")
        self.twocamerasanddown.setStyleSheet(u"QFrame#twocamerasanddownframe {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0   rgb(5, 18, 50),\n"
"        stop:0.3 rgb(8, 22, 60),\n"
"        stop:1   rgb(10, 28, 72)\n"
"    );\n"
"    border: 2px solid rgb(201, 169, 97);\n"
"    border-top: none;\n"
"    border-bottom: none;\n"
"    padding: 10px;\n"
"}")
        self.twocamerasanddownframe = QFrame(self.twocamerasanddown)
        self.twocamerasanddownframe.setObjectName(u"twocamerasanddownframe")
        self.twocamerasanddownframe.setGeometry(QRect(0, 0, 1920, 870))
        self.twocamerasanddownframe.setStyleSheet(u"")
        self.twocamerasanddownframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.twocamerasanddownframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.twocamerasanddownframe)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.twocameras = QFrame(self.twocamerasanddownframe)
        self.twocameras.setObjectName(u"twocameras")
        self.twocameras.setFrameShape(QFrame.Shape.StyledPanel)
        self.twocameras.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.twocameras)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.leftrearcamera = QLabel(self.twocameras)
        self.leftrearcamera.setObjectName(u"leftrearcamera")
        self.leftrearcamera.setMinimumSize(QSize(0, 0))
        self.leftrearcamera.setMaximumSize(QSize(16777215, 16777215))
        self.leftrearcamera.setScaledContents(True)
        self.leftrearcamera.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.leftrearcamera)

        self.rightrearcamera = QLabel(self.twocameras)
        self.rightrearcamera.setObjectName(u"rightrearcamera")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rightrearcamera.sizePolicy().hasHeightForWidth())
        self.rightrearcamera.setSizePolicy(sizePolicy2)
        self.rightrearcamera.setMinimumSize(QSize(0, 0))
        self.rightrearcamera.setMaximumSize(QSize(16777215, 16777215))
        self.rightrearcamera.setScaledContents(True)
        self.rightrearcamera.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.rightrearcamera)


        self.verticalLayout_4.addWidget(self.twocameras)

        self.downwardcamera = QFrame(self.twocamerasanddownframe)
        self.downwardcamera.setObjectName(u"downwardcamera")
        self.downwardcamera.setFrameShape(QFrame.Shape.StyledPanel)
        self.downwardcamera.setFrameShadow(QFrame.Shadow.Raised)
        self.downcamera_2 = QLabel(self.downwardcamera)
        self.downcamera_2.setObjectName(u"downcamera_2")
        self.downcamera_2.setGeometry(QRect(0, 0, 1896, 422))
        self.downcamera_2.setMinimumSize(QSize(0, 0))
        self.downcamera_2.setScaledContents(True)
        self.downcamera_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.downwardcamera)

        self.middlewidget.addWidget(self.twocamerasanddown)
        self.zedanddown = QWidget()
        self.zedanddown.setObjectName(u"zedanddown")
        self.zedanddownframe = QFrame(self.zedanddown)
        self.zedanddownframe.setObjectName(u"zedanddownframe")
        self.zedanddownframe.setGeometry(QRect(0, 0, 1920, 870))
        self.zedanddownframe.setStyleSheet(u"QFrame#zedanddownframe {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0   rgb(5, 18, 50),\n"
"        stop:0.3 rgb(8, 22, 60),\n"
"        stop:1   rgb(10, 28, 72)\n"
"    );\n"
"    border: 2px solid rgb(201, 169, 97);\n"
"    border-top: none;\n"
"    border-bottom: none;\n"
"    padding: 10px;\n"
"}")
        self.zedanddownframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.zedanddownframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.zedanddownframe)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.zedvariants = QFrame(self.zedanddownframe)
        self.zedvariants.setObjectName(u"zedvariants")
        self.zedvariants.setFrameShape(QFrame.Shape.StyledPanel)
        self.zedvariants.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.zedvariants)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, -1, 0)
        self.leftzed = QLabel(self.zedvariants)
        self.leftzed.setObjectName(u"leftzed")
        self.leftzed.setScaledContents(True)
        self.leftzed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.leftzed)


        self.verticalLayout_5.addWidget(self.zedvariants)

        self.downcamera_3 = QFrame(self.zedanddownframe)
        self.downcamera_3.setObjectName(u"downcamera_3")
        self.downcamera_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.downcamera_3.setFrameShadow(QFrame.Shadow.Raised)
        self.downcameralabel_2 = QLabel(self.downcamera_3)
        self.downcameralabel_2.setObjectName(u"downcameralabel_2")
        self.downcameralabel_2.setGeometry(QRect(0, 0, 1896, 422))
        self.downcameralabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.downcamera_3)

        self.middlewidget.addWidget(self.zedanddown)
        self.threeipcameras = QWidget()
        self.threeipcameras.setObjectName(u"threeipcameras")
        self.threeipcamerasframe = QFrame(self.threeipcameras)
        self.threeipcamerasframe.setObjectName(u"threeipcamerasframe")
        self.threeipcamerasframe.setGeometry(QRect(0, 0, 1920, 870))
        self.threeipcamerasframe.setStyleSheet(u"QFrame#threeipcamerasframe {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0   rgb(5, 18, 50),\n"
"        stop:0.3 rgb(8, 22, 60),\n"
"        stop:1   rgb(10, 28, 72)\n"
"    );\n"
"    border: 2px solid rgb(201, 169, 97);\n"
"    border-top: none;\n"
"    border-bottom: none;\n"
"    padding: 10px;\n"
"}")
        self.threeipcamerasframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.threeipcamerasframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.threeipcamerasframe)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.twocamerasframe = QFrame(self.threeipcamerasframe)
        self.twocamerasframe.setObjectName(u"twocamerasframe")
        self.twocamerasframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.twocamerasframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.twocamerasframe)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.leftone = QLabel(self.twocamerasframe)
        self.leftone.setObjectName(u"leftone")
        self.leftone.setScaledContents(True)
        self.leftone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.leftone)

        self.rightone = QLabel(self.twocamerasframe)
        self.rightone.setObjectName(u"rightone")
        self.rightone.setScaledContents(True)
        self.rightone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.rightone)


        self.verticalLayout_6.addWidget(self.twocamerasframe)

        self.thirdcameraframe = QFrame(self.threeipcamerasframe)
        self.thirdcameraframe.setObjectName(u"thirdcameraframe")
        self.thirdcameraframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.thirdcameraframe.setFrameShadow(QFrame.Shadow.Raised)
        self.downcamera_4 = QLabel(self.thirdcameraframe)
        self.downcamera_4.setObjectName(u"downcamera_4")
        self.downcamera_4.setGeometry(QRect(0, 0, 1896, 422))
        self.downcamera_4.setScaledContents(True)
        self.downcamera_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.thirdcameraframe)

        self.middlewidget.addWidget(self.threeipcameras)

        self.verticalLayout_2.addWidget(self.middlewidget)

        self.bottomwidget = QStackedWidget(self.mainFrame)
        self.bottomwidget.setObjectName(u"bottomwidget")
        self.bottomwidget.setMinimumSize(QSize(0, 0))
        self.bottomwidget.setMaximumSize(QSize(1920, 150))
        self.bottomwidget.setStyleSheet(u"QFrame#bottomBar {\n"
"    background-color: rgb(26, 58, 82); /* Navy Deep */\n"
"    border: 3px solid rgb(201, 169, 97); /* All sides gold */\n"
"    border-top: none; /* Remove top border */\n"
"    padding: 10px 15px;\n"
"    min-height: 60px;\n"
"}\n"
"")
        self.bottomBarwidget = QWidget()
        self.bottomBarwidget.setObjectName(u"bottomBarwidget")
        self.bottomBarwidget.setMinimumSize(QSize(0, 0))
        self.bottomBarwidget.setMaximumSize(QSize(1920, 150))
        self.bottomBarwidget.setStyleSheet(u"QFrame#bottomBar {\n"
"background: qlineargradient(\n"
"x1:0, y1:0, x2:0, y2:1,\n"
"stop:0 rgb(10, 28, 72),\n"
"stop:0.5 rgb(7, 20, 55),\n"
"stop:1 rgb(3, 12, 38)\n"
");\n"
"border: 2px solid rgb(201, 169, 97);\n"
"border-top: none;\n"
"padding: 10px 15px;\n"
"min-height: 60px;\n"
"}")
        self.bottomBar = QFrame(self.bottomBarwidget)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setGeometry(QRect(0, 0, 1920, 150))
        self.bottomBar.setMinimumSize(QSize(0, 82))
        self.bottomBar.setMaximumSize(QSize(1920, 150))
        self.bottomBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.forward = QLabel(self.bottomBar)
        self.forward.setObjectName(u"forward")
        self.forward.setGeometry(QRect(90, 0, 41, 55))
        self.forward.setPixmap(QPixmap(u":/Icons/iCONS/forward.png"))
        self.forward.setScaledContents(True)
        self.forward.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.backward = QLabel(self.bottomBar)
        self.backward.setObjectName(u"backward")
        self.backward.setGeometry(QRect(90, 87, 41, 55))
        self.backward.setPixmap(QPixmap(u":/Icons/iCONS/down.png"))
        self.backward.setScaledContents(True)
        self.backward.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right = QLabel(self.bottomBar)
        self.right.setObjectName(u"right")
        self.right.setGeometry(QRect(136, 50, 55, 41))
        self.right.setPixmap(QPixmap(u":/Icons/iCONS/right.png"))
        self.right.setScaledContents(True)
        self.right.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left = QLabel(self.bottomBar)
        self.left.setObjectName(u"left")
        self.left.setGeometry(QRect(30, 50, 55, 41))
        self.left.setPixmap(QPixmap(u":/Icons/iCONS/left.png"))
        self.left.setScaledContents(True)
        self.left.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.up = QLabel(self.bottomBar)
        self.up.setObjectName(u"up")
        self.up.setGeometry(QRect(220, 0, 70, 70))
        self.up.setPixmap(QPixmap(u":/Icons/iCONS/two-arrow (1).png"))
        self.up.setScaledContents(True)
        self.up.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.down = QLabel(self.bottomBar)
        self.down.setObjectName(u"down")
        self.down.setGeometry(QRect(220, 70, 70, 70))
        self.down.setPixmap(QPixmap(u":/Icons/iCONS/two-arrow down.png"))
        self.down.setScaledContents(True)
        self.down.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.yawing = QLabel(self.bottomBar)
        self.yawing.setObjectName(u"yawing")
        self.yawing.setGeometry(QRect(310, 0, 140, 145))
        self.yawing.setMinimumSize(QSize(0, 0))
        self.yawing.setPixmap(QPixmap(u":/Icons/iCONS/neutralmode.png"))
        self.yawing.setScaledContents(True)
        self.yawing.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rovmodes = QLabel(self.bottomBar)
        self.rovmodes.setObjectName(u"rovmodes")
        self.rovmodes.setGeometry(QRect(1780, 0, 140, 145))
        self.rovmodes.setPixmap(QPixmap(u":/Icons/iCONS/manualmode.png"))
        self.rovmodes.setScaledContents(True)
        self.rovmodes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grippersbigframe = QFrame(self.bottomBar)
        self.grippersbigframe.setObjectName(u"grippersbigframe")
        self.grippersbigframe.setGeometry(QRect(470, 0, 150, 140))
        self.grippersbigframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.grippersbigframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.grippersbigframe)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.grippersbottomframe = QFrame(self.grippersbigframe)
        self.grippersbottomframe.setObjectName(u"grippersbottomframe")
        self.grippersbottomframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.grippersbottomframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.grippersbottomframe)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.firstgripper = QLabel(self.grippersbottomframe)
        self.firstgripper.setObjectName(u"firstgripper")
        self.firstgripper.setPixmap(QPixmap(u":/Icons/iCONS/firstgripper.png"))
        self.firstgripper.setScaledContents(True)
        self.firstgripper.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.firstgripper)

        self.secondgripper = QLabel(self.grippersbottomframe)
        self.secondgripper.setObjectName(u"secondgripper")
        self.secondgripper.setPixmap(QPixmap(u":/Icons/iCONS/secondgripper.png"))
        self.secondgripper.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.secondgripper)


        self.verticalLayout.addWidget(self.grippersbottomframe)

        self.gripperstopframe = QFrame(self.grippersbigframe)
        self.gripperstopframe.setObjectName(u"gripperstopframe")
        self.gripperstopframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.gripperstopframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.gripperstopframe)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.thirdgripper = QLabel(self.gripperstopframe)
        self.thirdgripper.setObjectName(u"thirdgripper")
        self.thirdgripper.setPixmap(QPixmap(u":/Icons/iCONS/thirdgripper.png"))
        self.thirdgripper.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.thirdgripper)

        self.fourthgripper = QLabel(self.gripperstopframe)
        self.fourthgripper.setObjectName(u"fourthgripper")
        self.fourthgripper.setPixmap(QPixmap(u":/Icons/iCONS/fourthgripper.png"))
        self.fourthgripper.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.fourthgripper)


        self.verticalLayout.addWidget(self.gripperstopframe)

        self.circularProgressBarBase = QFrame(self.bottomBar)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(650, 10, 141, 131))
        self.circularProgressBarBase.setFrameShape(QFrame.Shape.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Shadow.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(16, 0, 118, 118))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 59px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.Shape.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(16, 0, 118, 118))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 59px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.Shape.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Shadow.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(26, 10, 98, 98))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 49px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.Shape.NoFrame)
        self.container.setFrameShadow(QFrame.Shadow.Raised)
        self.Servolabel = QLabel(self.container)
        self.Servolabel.setObjectName(u"Servolabel")
        self.Servolabel.setGeometry(QRect(20, 20, 71, 21))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.Servolabel.setFont(font)
        self.Servolabel.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.Servolabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelPercentage = QLabel(self.container)
        self.labelPercentage.setObjectName(u"labelPercentage")
        self.labelPercentage.setEnabled(True)
        self.labelPercentage.setGeometry(QRect(14, 50, 81, 31))
        font1 = QFont()
        font1.setFamilies([u"Roboto Thin"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.labelPercentage.setFont(font1)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        self.circularProgressBarBase_2 = QFrame(self.bottomBar)
        self.circularProgressBarBase_2.setObjectName(u"circularProgressBarBase_2")
        self.circularProgressBarBase_2.setGeometry(QRect(1620, 0, 141, 131))
        self.circularProgressBarBase_2.setFrameShape(QFrame.Shape.NoFrame)
        self.circularProgressBarBase_2.setFrameShadow(QFrame.Shadow.Raised)
        self.circularProgress_2 = QFrame(self.circularProgressBarBase_2)
        self.circularProgress_2.setObjectName(u"circularProgress_2")
        self.circularProgress_2.setGeometry(QRect(16, 0, 118, 118))
        self.circularProgress_2.setStyleSheet(u"QFrame {\n"
"    border-radius: 59px;\n"
"    background-color: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.75,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0.0  rgba(120, 60, 255, 180),\n"
"        stop:0.5  rgba(40, 10, 100, 120),\n"
"        stop:0.749 rgba(0, 200, 255, 60),\n"
"        stop:1.0  rgba(0, 0, 0, 0)\n"
"    );\n"
"}")
        self.circularProgress_2.setFrameShape(QFrame.Shape.NoFrame)
        self.circularProgress_2.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBg_2 = QFrame(self.circularProgressBarBase_2)
        self.circularBg_2.setObjectName(u"circularBg_2")
        self.circularBg_2.setGeometry(QRect(16, 0, 118, 118))
        self.circularBg_2.setStyleSheet(u"QFrame {\n"
"    border-radius: 59px;\n"
"    background-color: rgba(20, 10, 60, 140);\n"
"}")
        self.circularBg_2.setFrameShape(QFrame.Shape.NoFrame)
        self.circularBg_2.setFrameShadow(QFrame.Shadow.Raised)
        self.container_2 = QFrame(self.circularProgressBarBase_2)
        self.container_2.setObjectName(u"container_2")
        self.container_2.setGeometry(QRect(26, 10, 98, 98))
        self.container_2.setStyleSheet(u"QFrame {\n"
"    border-radius: 49px;\n"
"    background-color: rgb(15, 10, 40);\n"
"}\n"
"")
        self.container_2.setFrameShape(QFrame.Shape.NoFrame)
        self.container_2.setFrameShadow(QFrame.Shadow.Raised)
        self.Servolabel_2 = QLabel(self.container_2)
        self.Servolabel_2.setObjectName(u"Servolabel_2")
        self.Servolabel_2.setGeometry(QRect(17, 20, 61, 21))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.Servolabel_2.setFont(font2)
        self.Servolabel_2.setStyleSheet(u"background-color: none;\n"
"color: #C8AAFF;")
        self.Servolabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelPercentage_2 = QLabel(self.container_2)
        self.labelPercentage_2.setObjectName(u"labelPercentage_2")
        self.labelPercentage_2.setEnabled(True)
        self.labelPercentage_2.setGeometry(QRect(17, 50, 71, 21))
        font3 = QFont()
        font3.setFamilies([u"Roboto Thin"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.labelPercentage_2.setFont(font3)
        self.labelPercentage_2.setStyleSheet(u"background-color: none;\n"
"color: #C8AAFF;")
        self.labelPercentage_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timerlabel = QLabel(self.bottomBar)
        self.timerlabel.setObjectName(u"timerlabel")
        self.timerlabel.setGeometry(QRect(1470, -10, 141, 54))
        font4 = QFont()
        font4.setPointSize(40)
        font4.setBold(True)
        self.timerlabel.setFont(font4)
        self.timerlabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.timerlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.startButton_2 = QPushButton(self.bottomBar)
        self.startButton_2.setObjectName(u"startButton_2")
        self.startButton_2.setGeometry(QRect(1500, 46, 91, 31))
        self.startButton_2.setStyleSheet(u"QPushButton#startButton_2 {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #1a4d2e;\n"
"    border-radius: 8px;\n"
"    padding: 8px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton#startButton_2:hover {\n"
"    background-color: #1a1a2e;\n"
"    border: 1px solid #00ff41;\n"
"    color: #00ff41;\n"
"}\n"
"\n"
"QPushButton#startButton_2:pressed {\n"
"    background-color: #0d2e1a;\n"
"    border: 2px solid #00ff41;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#startButton_2:disabled {\n"
"    background-color: #12122a;\n"
"    color: #1a4d2e;\n"
"    border: 1px solid #1a4d2e;\n"
"}")
        self.pauseButton = QPushButton(self.bottomBar)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setGeometry(QRect(1500, 80, 91, 31))
        self.pauseButton.setStyleSheet(u"QPushButton#pauseButton {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #4d3a00;\n"
"    border-radius: 8px;\n"
"    padding: 8px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton#pauseButton:hover {\n"
"    background-color: #1a1a2e;\n"
"    border: 1px solid #f2a623;\n"
"    color: #f2a623;\n"
"}\n"
"\n"
"QPushButton#pauseButton:pressed {\n"
"    background-color: #2e2200;\n"
"    border: 2px solid #f2a623;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#pauseButton:disabled {\n"
"    background-color: #12122a;\n"
"    color: #4d3a00;\n"
"    border: 1px solid #4d3a00;\n"
"}")
        self.restartButton = QPushButton(self.bottomBar)
        self.restartButton.setObjectName(u"restartButton")
        self.restartButton.setGeometry(QRect(1500, 114, 91, 31))
        self.restartButton.setStyleSheet(u"QPushButton#restartButton {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #4d1a1a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton#restartButton:hover {\n"
"    background-color: #1a1a2e;\n"
"    border: 1px solid #ff3b3b;\n"
"    color: #ff3b3b;\n"
"}\n"
"\n"
"QPushButton#restartButton:pressed {\n"
"    background-color: #2e0d0d;\n"
"    border: 2px solid #ff3b3b;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton#restartButton:disabled {\n"
"    background-color: #12122a;\n"
"    color: #4d1a1a;\n"
"    border: 1px solid #4d1a1a;\n"
"}")
        self.bottomwidget.addWidget(self.bottomBarwidget)

        self.verticalLayout_2.addWidget(self.bottomwidget)

        self.MainWidget.addWidget(self.ControlWidget)
        self.welcomeWidget = QWidget()
        self.welcomeWidget.setObjectName(u"welcomeWidget")
        self.welcomeWidget.setMinimumSize(QSize(0, 0))
        self.welcomeScreen = QFrame(self.welcomeWidget)
        self.welcomeScreen.setObjectName(u"welcomeScreen")
        self.welcomeScreen.setGeometry(QRect(0, 0, 1920, 1080))
        self.welcomeScreen.setStyleSheet(u"QFrame#welcomeScreen {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgb(10, 15, 20),      /* Deep black at top */\n"
"        stop:1 rgb(20, 30, 40)       /* Dark navy at bottom */\n"
"    );\n"
"    border: 2px solid rgb(201, 169, 97);  /* Your gold border */\n"
"}")
        self.welcomeScreen.setFrameShape(QFrame.Shape.StyledPanel)
        self.welcomeScreen.setFrameShadow(QFrame.Shadow.Raised)
        self.logoLabel = QLabel(self.welcomeScreen)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(860, 300, 151, 171))
        self.logoLabel.setStyleSheet(u"QLabel#logoLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.logoLabel.setPixmap(QPixmap(u":/Icons/iCONS/titnaslogo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.startButton = QPushButton(self.welcomeScreen)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(670, 520, 521, 111))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(True)
        self.startButton.setFont(font5)
        self.startButton.setStyleSheet(u"QPushButton#startButton {\n"
"    background-color: transparent;\n"
"    color: rgb(201, 169, 97);\n"
"    border: 2px solid rgb(201, 169, 97);\n"
"    border-radius: 8px;\n"
"    padding: 15px 40px;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#startButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 transparent,\n"
"        stop:0.3 rgba(201, 169, 97, 50),\n"
"        stop:1 rgba(201, 169, 97, 100)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#startButton:pressed {\n"
"    background-color: rgb(201, 169, 97);  /* Instant, not animated */\n"
"    color: rgb(10, 15, 20);\n"
"}")
        self.quoteLabel = QLabel(self.welcomeScreen)
        self.quoteLabel.setObjectName(u"quoteLabel")
        self.quoteLabel.setGeometry(QRect(640, 640, 601, 81))
        self.quoteLabel.setStyleSheet(u"QLabel#quoteLabel {\n"
"    color: rgb(201, 169, 97);        /* Gold text */\n"
"    font-size: 18px;\n"
"    font-style: italic;\n"
"    font-weight: 300;\n"
"    background-color: transparent;\n"
"    padding: 20px;\n"
"}\n"
"")
        self.quoteLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Minimizebutton_2 = QPushButton(self.welcomeScreen)
        self.Minimizebutton_2.setObjectName(u"Minimizebutton_2")
        self.Minimizebutton_2.setGeometry(QRect(1736, 3, 60, 60))
        self.Minimizebutton_2.setMinimumSize(QSize(0, 0))
        self.Minimizebutton_2.setMaximumSize(QSize(60, 60))
        self.Minimizebutton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 30);  /* Very soft white hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 50);  /* Slightly more visible when pressed */\n"
"}")
        self.Minimizebutton_2.setIcon(icon3)
        self.Minimizebutton_2.setIconSize(QSize(32, 32))
        self.Exitbutton_2 = QPushButton(self.welcomeScreen)
        self.Exitbutton_2.setObjectName(u"Exitbutton_2")
        self.Exitbutton_2.setGeometry(QRect(1856, 3, 60, 60))
        self.Exitbutton_2.setMinimumSize(QSize(0, 0))
        self.Exitbutton_2.setMaximumSize(QSize(60, 60))
        self.Exitbutton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(220, 53, 53, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(100, 0, 0);  /* Even darker red when pressed */\n"
"}")
        self.Exitbutton_2.setIcon(icon5)
        self.Exitbutton_2.setIconSize(QSize(24, 24))
        self.MaximizeButton_2 = QPushButton(self.welcomeScreen)
        self.MaximizeButton_2.setObjectName(u"MaximizeButton_2")
        self.MaximizeButton_2.setGeometry(QRect(1796, 3, 60, 60))
        self.MaximizeButton_2.setMinimumSize(QSize(0, 0))
        self.MaximizeButton_2.setMaximumSize(QSize(60, 60))
        self.MaximizeButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(34, 197, 94, 100);  /* Green hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(21, 128, 61);  /* Dark green when pressed */\n"
"}")
        self.MaximizeButton_2.setIcon(icon4)
        self.MaximizeButton_2.setIconSize(QSize(28, 28))
        self.Copyrights = QLabel(self.welcomeScreen)
        self.Copyrights.setObjectName(u"Copyrights")
        self.Copyrights.setGeometry(QRect(1780, 1030, 141, 51))
        font6 = QFont()
        font6.setBold(True)
        self.Copyrights.setFont(font6)
        self.Copyrights.setStyleSheet(u"QLabel#Copyrights{\n"
"       color: rgba(255, 255, 255, 128);\n"
"       font-size: 12px;\n"
"       background: transparent;\n"
"       padding: 10px;\n"
"   }")
        self.Copyrights.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MainWidget.addWidget(self.welcomeWidget)
        self.settingspage = QWidget()
        self.settingspage.setObjectName(u"settingspage")
        self.topBar_2 = QFrame(self.settingspage)
        self.topBar_2.setObjectName(u"topBar_2")
        self.topBar_2.setGeometry(QRect(0, 0, 1920, 63))
        sizePolicy.setHeightForWidth(self.topBar_2.sizePolicy().hasHeightForWidth())
        self.topBar_2.setSizePolicy(sizePolicy)
        self.topBar_2.setMinimumSize(QSize(0, 62))
        self.topBar_2.setMaximumSize(QSize(1920, 65))
        self.topBar_2.setStyleSheet(u"QFrame#topBar_2 {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0    rgb(2, 5, 18),\n"
"        stop:0.05 rgb(8, 12, 35),\n"
"        stop:0.5  rgb(6, 16, 46),\n"
"        stop:1    rgb(5, 16, 46)\n"
"    );\n"
"\n"
"    border: none;\n"
"    border-left: 2px solid rgb(201, 169, 97);\n"
"    border-top: 2px solid rgb(201, 169, 97);\n"
"    border-right: 2px solid rgb(201, 169, 97);\n"
"    border-bottom: none;\n"
"\n"
"    min-height: 60px;\n"
"}")
        self.topBar_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.topBar_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.topBar_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lefticonsbar_2 = QFrame(self.topBar_2)
        self.lefticonsbar_2.setObjectName(u"lefticonsbar_2")
        self.lefticonsbar_2.setEnabled(True)
        self.lefticonsbar_2.setMinimumSize(QSize(0, 0))
        self.lefticonsbar_2.setMaximumSize(QSize(180, 60))
        self.lefticonsbar_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lefticonsbar_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.lefticonsbar_2.setFrameShadow(QFrame.Shadow.Raised)
        self.tocontrolframe = QPushButton(self.lefticonsbar_2)
        self.tocontrolframe.setObjectName(u"tocontrolframe")
        self.tocontrolframe.setGeometry(QRect(1, 0, 160, 59))
        self.tocontrolframe.setMinimumSize(QSize(0, 0))
        self.tocontrolframe.setMaximumSize(QSize(200, 70))
        self.tocontrolframe.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(45, 95, 140, 100);  /* Your lighter blue with transparency */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 45, 65);  /* Solid darker navy */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(20, 45, 65);  /* Keep solid while holding */\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/iCONS/angle-circle-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tocontrolframe.setIcon(icon6)
        self.tocontrolframe.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.lefticonsbar_2)

        self.logoframe_2 = QFrame(self.topBar_2)
        self.logoframe_2.setObjectName(u"logoframe_2")
        self.logoframe_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.logoframe_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.logoframe_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(770, 0, 49, 60))
        self.label_2.setPixmap(QPixmap(u"Fugro Presentation V2 (The WashiMachine part 2 unprocessed soap)(1) (1) (1).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.logoframe_2)

        self.navigationsicons_2 = QFrame(self.topBar_2)
        self.navigationsicons_2.setObjectName(u"navigationsicons_2")
        self.navigationsicons_2.setMinimumSize(QSize(0, 60))
        self.navigationsicons_2.setMaximumSize(QSize(180, 60))
        self.navigationsicons_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.navigationsicons_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.navigationsicons_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Minimizebutton_3 = QPushButton(self.navigationsicons_2)
        self.Minimizebutton_3.setObjectName(u"Minimizebutton_3")
        self.Minimizebutton_3.setMinimumSize(QSize(0, 0))
        self.Minimizebutton_3.setMaximumSize(QSize(60, 56))
        self.Minimizebutton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 30);  /* Very soft white hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 50);  /* Slightly more visible when pressed */\n"
"}")
        self.Minimizebutton_3.setIcon(icon3)
        self.Minimizebutton_3.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.Minimizebutton_3)

        self.MaximizeButton_3 = QPushButton(self.navigationsicons_2)
        self.MaximizeButton_3.setObjectName(u"MaximizeButton_3")
        self.MaximizeButton_3.setMinimumSize(QSize(0, 0))
        self.MaximizeButton_3.setMaximumSize(QSize(60, 56))
        self.MaximizeButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(34, 197, 94, 100);  /* Green hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(21, 128, 61);  /* Dark green when pressed */\n"
"}")
        self.MaximizeButton_3.setIcon(icon4)
        self.MaximizeButton_3.setIconSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.MaximizeButton_3)

        self.Exitbutton_3 = QPushButton(self.navigationsicons_2)
        self.Exitbutton_3.setObjectName(u"Exitbutton_3")
        self.Exitbutton_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Exitbutton_3.sizePolicy().hasHeightForWidth())
        self.Exitbutton_3.setSizePolicy(sizePolicy1)
        self.Exitbutton_3.setMinimumSize(QSize(0, 0))
        self.Exitbutton_3.setMaximumSize(QSize(60, 56))
        self.Exitbutton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(220, 53, 53, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(100, 0, 0);  /* Even darker red when pressed */\n"
"}")
        self.Exitbutton_3.setIcon(icon5)
        self.Exitbutton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.Exitbutton_3)


        self.horizontalLayout_6.addWidget(self.navigationsicons_2)

        self.stackedWidget = QStackedWidget(self.settingspage)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 63, 1760, 1017))
        self.rightPanel = QWidget()
        self.rightPanel.setObjectName(u"rightPanel")
        self.controllersettingspanel = QFrame(self.rightPanel)
        self.controllersettingspanel.setObjectName(u"controllersettingspanel")
        self.controllersettingspanel.setGeometry(QRect(0, -1, 1760, 1017))
        self.controllersettingspanel.setStyleSheet(u"QFrame#controllersettingspanel {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.75,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0.0  rgb(8, 20, 58),\n"
"        stop:0.4  rgb(7, 18, 52),\n"
"        stop:0.749 rgb(5, 16, 46),\n"
"        stop:1.0  rgb(5, 18, 50)\n"
"    );\n"
"\n"
"    border: 2px solid rgb(201, 169, 97);\n"
"    border-top: none;\n"
"    border-left: none;\n"
"\n"
"    padding: 10px 15px;\n"
"    min-height: 60px;\n"
"\n"
"    color: #C9A84C;\n"
"}")
        self.controllersettingspanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.controllersettingspanel.setFrameShadow(QFrame.Shadow.Raised)
        self.controllernormal = QLabel(self.controllersettingspanel)
        self.controllernormal.setObjectName(u"controllernormal")
        self.controllernormal.setGeometry(QRect(180, 20, 1281, 531))
        self.controllernormal.setPixmap(QPixmap(u":/Icons/iCONS/xbox360.png"))
        self.controllernormal.setScaledContents(True)
        self.controllernormal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.controllerlateral = QLabel(self.controllersettingspanel)
        self.controllerlateral.setObjectName(u"controllerlateral")
        self.controllerlateral.setGeometry(QRect(180, 350, 1281, 871))
        self.controllerlateral.setPixmap(QPixmap(u":/Icons/iCONS/xbox lateral.png"))
        self.controllerlateral.setScaledContents(True)
        self.controllerlateral.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.controllersettingspanel)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(620, 10, 371, 51))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(31)
        font7.setBold(True)
        self.label_3.setFont(font7)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox = QComboBox(self.controllersettingspanel)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 18, 171, 31))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.PilotName = QLabel(self.controllersettingspanel)
        self.PilotName.setObjectName(u"PilotName")
        self.PilotName.setGeometry(QRect(20, 20, 91, 21))
        self.PilotName.setFont(font6)
        self.PilotName.setStyleSheet(u"QLabel {\n"
"    background-color: none;\n"
"    color: #e0e0ff;\n"
"    border: none;\n"
"    font-size: 20px;\n"
"}")
        self.PilotName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.rightPanel)
        self.yesterpanel = QWidget()
        self.yesterpanel.setObjectName(u"yesterpanel")
        self.yesterframe = QFrame(self.yesterpanel)
        self.yesterframe.setObjectName(u"yesterframe")
        self.yesterframe.setGeometry(QRect(0, -1, 1760, 1017))
        self.yesterframe.setStyleSheet(u"QFrame#yesterframe {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.75,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0.0  rgb(8, 20, 58),\n"
"        stop:0.4  rgb(7, 18, 52),\n"
"        stop:0.749 rgb(5, 16, 46),\n"
"        stop:1.0  rgb(5, 18, 50)\n"
"    );\n"
"\n"
"    border: 2px solid rgb(201, 169, 97);\n"
"    border-top: none;\n"
"    border-left: none;\n"
"\n"
"    padding: 10px 15px;\n"
"    min-height: 60px;\n"
"\n"
"    color: #C9A84C;\n"
"}")
        self.yesterframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.yesterframe.setFrameShadow(QFrame.Shadow.Raised)
        self.yesterlabel = QLabel(self.yesterframe)
        self.yesterlabel.setObjectName(u"yesterlabel")
        self.yesterlabel.setGeometry(QRect(680, 10, 271, 51))
        font8 = QFont()
        font8.setPointSize(35)
        font8.setBold(True)
        self.yesterlabel.setFont(font8)
        self.yesterlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.motor4 = QSlider(self.yesterframe)
        self.motor4.setObjectName(u"motor4")
        self.motor4.setGeometry(QRect(270, 420, 31, 160))
        self.motor4.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border: 1px solid #b5d4f4;\n"
"    border-radius: 2px;\n"
"    width: 4px;\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background-color: #378add;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #378add;\n"
"    border-radius: 12px;\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    margin: 0 -10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #e6f1fb;\n"
"    border-color: #185fa5;\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #378add;\n"
"}")
        self.motor4.setMinimum(1200)
        self.motor4.setMaximum(1800)
        self.motor4.setValue(1500)
        self.motor4.setOrientation(Qt.Orientation.Vertical)
        self.motor3 = QSlider(self.yesterframe)
        self.motor3.setObjectName(u"motor3")
        self.motor3.setGeometry(QRect(220, 420, 31, 160))
        self.motor3.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border: 1px solid #b5d4f4;\n"
"    border-radius: 2px;\n"
"    width: 4px;\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background-color: #378add;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #378add;\n"
"    border-radius: 12px;\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    margin: 0 -10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #e6f1fb;\n"
"    border-color: #185fa5;\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #378add;\n"
"}")
        self.motor3.setMinimum(1200)
        self.motor3.setMaximum(1800)
        self.motor3.setValue(1500)
        self.motor3.setOrientation(Qt.Orientation.Vertical)
        self.motor5 = QSlider(self.yesterframe)
        self.motor5.setObjectName(u"motor5")
        self.motor5.setGeometry(QRect(320, 420, 31, 160))
        self.motor5.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border: 1px solid #b5d4f4;\n"
"    border-radius: 2px;\n"
"    width: 4px;\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background-color: #378add;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #378add;\n"
"    border-radius: 12px;\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    margin: 0 -10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #e6f1fb;\n"
"    border-color: #185fa5;\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #378add;\n"
"}")
        self.motor5.setMinimum(1200)
        self.motor5.setMaximum(1800)
        self.motor5.setValue(1500)
        self.motor5.setOrientation(Qt.Orientation.Vertical)
        self.motor6 = QSlider(self.yesterframe)
        self.motor6.setObjectName(u"motor6")
        self.motor6.setGeometry(QRect(370, 420, 31, 160))
        self.motor6.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border: 1px solid #b5d4f4;\n"
"    border-radius: 2px;\n"
"    width: 4px;\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background-color: #378add;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #378add;\n"
"    border-radius: 12px;\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    margin: 0 -10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #e6f1fb;\n"
"    border-color: #185fa5;\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #378add;\n"
"}")
        self.motor6.setMinimum(1200)
        self.motor6.setMaximum(1800)
        self.motor6.setValue(1500)
        self.motor6.setOrientation(Qt.Orientation.Vertical)
        self.motor1 = QSlider(self.yesterframe)
        self.motor1.setObjectName(u"motor1")
        self.motor1.setGeometry(QRect(120, 420, 31, 160))
        self.motor1.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border: 1px solid #b5d4f4;\n"
"    border-radius: 2px;\n"
"    width: 4px;\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background-color: #378add;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #378add;\n"
"    border-radius: 12px;\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    margin: 0 -10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #e6f1fb;\n"
"    border-color: #185fa5;\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #378add;\n"
"}")
        self.motor1.setMinimum(1200)
        self.motor1.setMaximum(1800)
        self.motor1.setValue(1500)
        self.motor1.setTracking(True)
        self.motor1.setOrientation(Qt.Orientation.Vertical)
        self.motor1.setTickPosition(QSlider.TickPosition.NoTicks)
        self.motor2 = QSlider(self.yesterframe)
        self.motor2.setObjectName(u"motor2")
        self.motor2.setGeometry(QRect(170, 420, 31, 161))
        self.motor2.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border: 1px solid #b5d4f4;\n"
"    border-radius: 2px;\n"
"    width: 4px;\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #e6f1fb;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background-color: #378add;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #378add;\n"
"    border-radius: 12px;\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    margin: 0 -10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #e6f1fb;\n"
"    border-color: #185fa5;\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #378add;\n"
"}")
        self.motor2.setMinimum(1200)
        self.motor2.setMaximum(1800)
        self.motor2.setValue(1500)
        self.motor2.setSliderPosition(1500)
        self.motor2.setOrientation(Qt.Orientation.Vertical)
        self.rovframe = QLabel(self.yesterframe)
        self.rovframe.setObjectName(u"rovframe")
        self.rovframe.setGeometry(QRect(20, 40, 481, 361))
        self.rovframe.setPixmap(QPixmap(u":/Icons/iCONS/yester rov.png"))
        self.rovframe.setScaledContents(True)
        self.rovframe.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.yhawk = QLabel(self.yesterframe)
        self.yhawk.setObjectName(u"yhawk")
        self.yhawk.setGeometry(QRect(900, 6, 71, 61))
        self.yhawk.setPixmap(QPixmap(u":/Icons/iCONS/YHawk.png"))
        self.yhawk.setScaledContents(True)
        self.yhawk.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.motor1number = QLabel(self.yesterframe)
        self.motor1number.setObjectName(u"motor1number")
        self.motor1number.setGeometry(QRect(130, 590, 16, 21))
        self.motor1number.setFont(font)
        self.motor2number = QLabel(self.yesterframe)
        self.motor2number.setObjectName(u"motor2number")
        self.motor2number.setGeometry(QRect(180, 590, 16, 21))
        self.motor2number.setFont(font)
        self.motor3number = QLabel(self.yesterframe)
        self.motor3number.setObjectName(u"motor3number")
        self.motor3number.setGeometry(QRect(230, 590, 16, 21))
        self.motor3number.setFont(font)
        self.motor4number = QLabel(self.yesterframe)
        self.motor4number.setObjectName(u"motor4number")
        self.motor4number.setGeometry(QRect(280, 590, 16, 21))
        self.motor4number.setFont(font)
        self.motor5number = QLabel(self.yesterframe)
        self.motor5number.setObjectName(u"motor5number")
        self.motor5number.setGeometry(QRect(330, 590, 16, 21))
        self.motor5number.setFont(font)
        self.motor6number = QLabel(self.yesterframe)
        self.motor6number.setObjectName(u"motor6number")
        self.motor6number.setGeometry(QRect(380, 590, 16, 21))
        self.motor6number.setFont(font)
        self.frame = QFrame(self.yesterframe)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(817, 60, 3, 955))
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(30, 55, 100);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.maxspeedlabel = QLabel(self.yesterframe)
        self.maxspeedlabel.setObjectName(u"maxspeedlabel")
        self.maxspeedlabel.setGeometry(QRect(840, 80, 121, 31))
        font9 = QFont()
        font9.setPointSize(13)
        font9.setBold(True)
        self.maxspeedlabel.setFont(font9)
        self.maxspeedlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minspeedlabel = QLabel(self.yesterframe)
        self.minspeedlabel.setObjectName(u"minspeedlabel")
        self.minspeedlabel.setGeometry(QRect(840, 125, 121, 31))
        self.minspeedlabel.setFont(font9)
        self.minspeedlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minspeed = QSpinBox(self.yesterframe)
        self.minspeed.setObjectName(u"minspeed")
        self.minspeed.setGeometry(QRect(990, 125, 91, 31))
        self.minspeed.setStyleSheet(u"QSpinBox {\n"
"    background-color: #0f172a;\n"
"    color: #e2e8f0;\n"
"    border: 2px solid #1e3a8a;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 2px solid #3b82f6;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #60a5fa;\n"
"    background-color: #020617;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button {\n"
"    background-color: #1e293b;\n"
"    border: none;\n"
"    width: 20px;\n"
"}\n"
"\n"
"/* Hover */\n"
"QSpinBox::up-button:hover,\n"
"QSpinBox::down-button:hover {\n"
"    background-color: #3b82f6;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QSpinBox::up-button:pressed,\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"/* \ud83d\udd25 ARROWS (THIS WAS MISSING) */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/Icons/iCONS/two-arrow (1).png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/Icons/iCONS/two-"
                        "arrow down.png);\n"
"\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")
        self.minspeed.setMaximum(2100)
        self.minspeed.setSingleStep(50)
        self.minspeed.setValue(1200)
        self.maxspeed = QSpinBox(self.yesterframe)
        self.maxspeed.setObjectName(u"maxspeed")
        self.maxspeed.setGeometry(QRect(990, 80, 91, 31))
        self.maxspeed.setStyleSheet(u"QSpinBox {\n"
"    background-color: #0f172a;\n"
"    color: #e2e8f0;\n"
"    border: 2px solid #1e3a8a;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 2px solid #3b82f6;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #60a5fa;\n"
"    background-color: #020617;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button {\n"
"    background-color: #1e293b;\n"
"    border: none;\n"
"    width: 20px;\n"
"}\n"
"\n"
"/* Hover */\n"
"QSpinBox::up-button:hover,\n"
"QSpinBox::down-button:hover {\n"
"    background-color: #3b82f6;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QSpinBox::up-button:pressed,\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"/* \ud83d\udd25 ARROWS (THIS WAS MISSING) */\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/Icons/iCONS/two-arrow (1).png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/Icons/iCONS/two-"
                        "arrow down.png);\n"
"\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")
        self.maxspeed.setMaximum(2100)
        self.maxspeed.setSingleStep(50)
        self.maxspeed.setValue(1900)
        self.label_4 = QLabel(self.yesterframe)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(850, 200, 141, 51))
        self.label_4.setFont(font9)
        self.Servo1function = QComboBox(self.yesterframe)
        self.Servo1function.addItem("")
        self.Servo1function.setObjectName(u"Servo1function")
        self.Servo1function.setGeometry(QRect(1000, 210, 171, 36))
        self.Servo1function.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_5 = QLabel(self.yesterframe)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1190, 200, 141, 51))
        self.label_5.setFont(font9)
        self.Servo1reverse = QComboBox(self.yesterframe)
        self.Servo1reverse.addItem("")
        self.Servo1reverse.setObjectName(u"Servo1reverse")
        self.Servo1reverse.setGeometry(QRect(1270, 210, 171, 31))
        self.Servo1reverse.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.Servo2function = QComboBox(self.yesterframe)
        self.Servo2function.addItem("")
        self.Servo2function.setObjectName(u"Servo2function")
        self.Servo2function.setGeometry(QRect(1000, 270, 171, 36))
        self.Servo2function.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_6 = QLabel(self.yesterframe)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(850, 260, 141, 51))
        self.label_6.setFont(font9)
        self.Servo2reverse = QComboBox(self.yesterframe)
        self.Servo2reverse.addItem("")
        self.Servo2reverse.setObjectName(u"Servo2reverse")
        self.Servo2reverse.setGeometry(QRect(1270, 270, 171, 31))
        self.Servo2reverse.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_7 = QLabel(self.yesterframe)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1190, 260, 141, 51))
        self.label_7.setFont(font9)
        self.Servo3reverse = QComboBox(self.yesterframe)
        self.Servo3reverse.addItem("")
        self.Servo3reverse.setObjectName(u"Servo3reverse")
        self.Servo3reverse.setGeometry(QRect(1270, 330, 171, 31))
        self.Servo3reverse.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.Servo3function = QComboBox(self.yesterframe)
        self.Servo3function.addItem("")
        self.Servo3function.setObjectName(u"Servo3function")
        self.Servo3function.setGeometry(QRect(1000, 330, 171, 36))
        self.Servo3function.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_8 = QLabel(self.yesterframe)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1190, 320, 141, 51))
        self.label_8.setFont(font9)
        self.label_9 = QLabel(self.yesterframe)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(850, 320, 141, 51))
        self.label_9.setFont(font9)
        self.label_10 = QLabel(self.yesterframe)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(850, 380, 141, 51))
        self.label_10.setFont(font9)
        self.Servo4function = QComboBox(self.yesterframe)
        self.Servo4function.addItem("")
        self.Servo4function.setObjectName(u"Servo4function")
        self.Servo4function.setGeometry(QRect(1000, 390, 171, 36))
        self.Servo4function.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_11 = QLabel(self.yesterframe)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(1190, 380, 141, 51))
        self.label_11.setFont(font9)
        self.Servo4reverse = QComboBox(self.yesterframe)
        self.Servo4reverse.addItem("")
        self.Servo4reverse.setObjectName(u"Servo4reverse")
        self.Servo4reverse.setGeometry(QRect(1270, 390, 171, 31))
        self.Servo4reverse.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.Servo5function = QComboBox(self.yesterframe)
        self.Servo5function.addItem("")
        self.Servo5function.setObjectName(u"Servo5function")
        self.Servo5function.setGeometry(QRect(1000, 450, 171, 36))
        self.Servo5function.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_12 = QLabel(self.yesterframe)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(850, 440, 141, 51))
        self.label_12.setFont(font9)
        self.Servo5reverse = QComboBox(self.yesterframe)
        self.Servo5reverse.addItem("")
        self.Servo5reverse.setObjectName(u"Servo5reverse")
        self.Servo5reverse.setGeometry(QRect(1270, 450, 171, 31))
        self.Servo5reverse.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_13 = QLabel(self.yesterframe)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1190, 440, 141, 51))
        self.label_13.setFont(font9)
        self.Servo6function = QComboBox(self.yesterframe)
        self.Servo6function.addItem("")
        self.Servo6function.setObjectName(u"Servo6function")
        self.Servo6function.setGeometry(QRect(1000, 510, 171, 36))
        self.Servo6function.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.Servo6reverse = QComboBox(self.yesterframe)
        self.Servo6reverse.addItem("")
        self.Servo6reverse.setObjectName(u"Servo6reverse")
        self.Servo6reverse.setGeometry(QRect(1270, 510, 171, 31))
        self.Servo6reverse.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_14 = QLabel(self.yesterframe)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(850, 500, 141, 51))
        self.label_14.setFont(font9)
        self.label_15 = QLabel(self.yesterframe)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1190, 500, 141, 51))
        self.label_15.setFont(font9)
        self.label_16 = QLabel(self.yesterframe)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(850, 560, 141, 51))
        self.label_16.setFont(font9)
        self.Servo7function = QComboBox(self.yesterframe)
        self.Servo7function.addItem("")
        self.Servo7function.setObjectName(u"Servo7function")
        self.Servo7function.setGeometry(QRect(1000, 570, 171, 36))
        self.Servo7function.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_17 = QLabel(self.yesterframe)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(1190, 560, 141, 51))
        self.label_17.setFont(font9)
        self.Servo7reverse = QComboBox(self.yesterframe)
        self.Servo7reverse.addItem("")
        self.Servo7reverse.setObjectName(u"Servo7reverse")
        self.Servo7reverse.setGeometry(QRect(1270, 570, 171, 31))
        self.Servo7reverse.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.Servo8reverse = QComboBox(self.yesterframe)
        self.Servo8reverse.addItem("")
        self.Servo8reverse.setObjectName(u"Servo8reverse")
        self.Servo8reverse.setGeometry(QRect(1270, 630, 171, 31))
        self.Servo8reverse.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.Servo8function = QComboBox(self.yesterframe)
        self.Servo8function.addItem("")
        self.Servo8function.setObjectName(u"Servo8function")
        self.Servo8function.setGeometry(QRect(1000, 630, 171, 36))
        self.Servo8function.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_18 = QLabel(self.yesterframe)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(1190, 620, 141, 51))
        self.label_18.setFont(font9)
        self.label_19 = QLabel(self.yesterframe)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(850, 620, 141, 51))
        self.label_19.setFont(font9)
        self.stackedWidget.addWidget(self.yesterpanel)
        self.zedwidget = QWidget()
        self.zedwidget.setObjectName(u"zedwidget")
        self.camerasettings = QFrame(self.zedwidget)
        self.camerasettings.setObjectName(u"camerasettings")
        self.camerasettings.setGeometry(QRect(0, -1, 1760, 1017))
        self.camerasettings.setStyleSheet(u"QFrame#camerasettings {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.75,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0.0  rgb(8, 20, 58),\n"
"        stop:0.4  rgb(7, 18, 52),\n"
"        stop:0.749 rgb(5, 16, 46),\n"
"        stop:1.0  rgb(5, 18, 50)\n"
"    );\n"
"\n"
"    border: 2px solid rgb(201, 169, 97);\n"
"    border-top: none;\n"
"    border-left: none;\n"
"\n"
"    padding: 10px 15px;\n"
"    min-height: 60px;\n"
"\n"
"    color: #C9A84C;\n"
"}")
        self.camerasettings.setFrameShape(QFrame.Shape.StyledPanel)
        self.camerasettings.setFrameShadow(QFrame.Shadow.Raised)
        self.label_24 = QLabel(self.camerasettings)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(700, 10, 231, 61))
        font10 = QFont()
        font10.setPointSize(21)
        font10.setBold(True)
        self.label_24.setFont(font10)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_25 = QLabel(self.camerasettings)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 130, 181, 31))
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(True)
        self.label_25.setFont(font11)
        self.Servo4function_2 = QComboBox(self.camerasettings)
        self.Servo4function_2.addItem("")
        self.Servo4function_2.setObjectName(u"Servo4function_2")
        self.Servo4function_2.setGeometry(QRect(200, 130, 171, 36))
        self.Servo4function_2.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_28 = QLabel(self.camerasettings)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(420, 130, 181, 31))
        self.label_28.setFont(font11)
        self.Servo4function_4 = QComboBox(self.camerasettings)
        self.Servo4function_4.addItem("")
        self.Servo4function_4.setObjectName(u"Servo4function_4")
        self.Servo4function_4.setGeometry(QRect(540, 130, 171, 36))
        self.Servo4function_4.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_29 = QLabel(self.camerasettings)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 300, 221, 31))
        self.label_29.setFont(font11)
        self.Servo4function_5 = QComboBox(self.camerasettings)
        self.Servo4function_5.addItem("")
        self.Servo4function_5.setObjectName(u"Servo4function_5")
        self.Servo4function_5.setGeometry(QRect(240, 300, 171, 36))
        self.Servo4function_5.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.Servo4function_6 = QComboBox(self.camerasettings)
        self.Servo4function_6.addItem("")
        self.Servo4function_6.setObjectName(u"Servo4function_6")
        self.Servo4function_6.setGeometry(QRect(580, 300, 171, 36))
        self.Servo4function_6.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_30 = QLabel(self.camerasettings)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(460, 300, 181, 31))
        self.label_30.setFont(font11)
        self.label_31 = QLabel(self.camerasettings)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 430, 181, 31))
        self.label_31.setFont(font11)
        self.Servo4function_7 = QComboBox(self.camerasettings)
        self.Servo4function_7.addItem("")
        self.Servo4function_7.setObjectName(u"Servo4function_7")
        self.Servo4function_7.setGeometry(QRect(200, 430, 171, 36))
        self.Servo4function_7.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.Servo4function_8 = QComboBox(self.camerasettings)
        self.Servo4function_8.addItem("")
        self.Servo4function_8.setObjectName(u"Servo4function_8")
        self.Servo4function_8.setGeometry(QRect(540, 430, 171, 36))
        self.Servo4function_8.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_32 = QLabel(self.camerasettings)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(420, 430, 181, 31))
        self.label_32.setFont(font11)
        self.label_33 = QLabel(self.camerasettings)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 540, 201, 31))
        self.label_33.setFont(font11)
        self.Servo4function_9 = QComboBox(self.camerasettings)
        self.Servo4function_9.addItem("")
        self.Servo4function_9.setObjectName(u"Servo4function_9")
        self.Servo4function_9.setGeometry(QRect(220, 540, 171, 36))
        self.Servo4function_9.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.Servo4function_10 = QComboBox(self.camerasettings)
        self.Servo4function_10.addItem("")
        self.Servo4function_10.setObjectName(u"Servo4function_10")
        self.Servo4function_10.setGeometry(QRect(560, 540, 171, 36))
        self.Servo4function_10.setStyleSheet(u"QComboBox {\n"
"    background-color: #1a1a2e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    border-radius: 8px;\n"
"    padding: 8px 32px 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover { border-color: #7c7cf8; }\n"
"QComboBox:focus { border-color: #7c7cf8; }\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 28px;\n"
"    border-left: 1px solid #3d3d7a;\n"
"    border-radius: 0 8px 8px 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 8px; height: 8px;\n"
"    border-left: 2px solid #7c7cf8;\n"
"    border-bottom: 2px solid #7c7cf8;\n"
"    margin-right: 6px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #16213e;\n"
"    color: #e0e0ff;\n"
"    border: 1px solid #3d3d7a;\n"
"    selection-background-color: #3d3d7a;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.label_34 = QLabel(self.camerasettings)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(440, 540, 181, 31))
        self.label_34.setFont(font11)
        self.stackedWidget.addWidget(self.zedwidget)
        self.leftPanel = QFrame(self.settingspage)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setGeometry(QRect(0, 62, 160, 1017))
        self.leftPanel.setStyleSheet(u"QFrame {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius:0.75,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0.0  rgb(8, 20, 58),\n"
"        stop:0.4  rgb(7, 18, 52),\n"
"        stop:0.749 rgb(5, 16, 46),\n"
"        stop:1.0  rgb(5, 18, 50)\n"
"    );\n"
"\n"
"    border-top: none;\n"
"    border-left: 2px solid rgb(201, 169, 97);\n"
"    border-bottom: 2px solid rgb(201, 169, 97);\n"
"    border-right: 1px solid rgb(30, 55, 100);\n"
"\n"
"    padding: 10px 15px;\n"
"    min-height: 60px;\n"
"\n"
"    color: #C9A84C;\n"
"}\n"
"")
        self.leftPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.controllericon = QPushButton(self.leftPanel)
        self.controllericon.setObjectName(u"controllericon")
        self.controllericon.setMinimumSize(QSize(128, 112))
        self.controllericon.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 50px;\n"
"    padding: 6px 14px;\n"
"    min-width: 100px;\n"
"    min-height: 100px;\n"
"    max-width: 100px;\n"
"    max-height: 100px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(120, 40, 180, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(75, 20, 120);\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(75, 20, 120);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/iCONS/controllersettings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.controllericon.setIcon(icon7)
        self.controllericon.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.controllericon)

        self.zed2iicon = QPushButton(self.leftPanel)
        self.zed2iicon.setObjectName(u"zed2iicon")
        self.zed2iicon.setMinimumSize(QSize(128, 112))
        self.zed2iicon.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 50px;\n"
"    padding: 6px 14px;\n"
"    min-width: 100px;\n"
"    min-height: 100px;\n"
"    max-width: 100px;\n"
"    max-height: 100px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 180, 160, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 110, 100);\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(0, 110, 100);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/iCONS/zed2i.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zed2iicon.setIcon(icon8)
        self.zed2iicon.setIconSize(QSize(160, 160))

        self.verticalLayout_3.addWidget(self.zed2iicon)

        self.yground = QPushButton(self.leftPanel)
        self.yground.setObjectName(u"yground")
        self.yground.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 50px;\n"
"    padding: 6px 14px;\n"
"    min-width: 100px;\n"
"    min-height: 100px;\n"
"    max-width: 100px;\n"
"    max-height: 100px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(220, 80, 120, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(150, 40, 70);\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(150, 40, 70);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/iCONS/YGROUND.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.yground.setIcon(icon9)
        self.yground.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.yground)

        self.MainWidget.addWidget(self.settingspage)
        self.stackedWidget.raise_()
        self.leftPanel.raise_()
        self.topBar_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MainWidget.setCurrentIndex(1)
        self.TopWidget.setCurrentIndex(0)
        self.middlewidget.setCurrentIndex(0)
        self.bottomwidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Menubutton.setText("")
        self.Teambutton.setText("")
        self.camerasbutton.setText("")
        self.label.setText("")
        self.Minimizebutton.setText("")
        self.MaximizeButton.setText("")
        self.Exitbutton.setText("")
        self.zedleftlabel.setText("")
        self.rightrear.setText("")
        self.leftrear.setText("")
        self.downcameralabel.setText("")
        self.leftrearcamera.setText("")
        self.rightrearcamera.setText("")
        self.downcamera_2.setText("")
        self.leftzed.setText("")
        self.downcameralabel_2.setText("")
        self.leftone.setText("")
        self.rightone.setText("")
        self.downcamera_4.setText("")
        self.forward.setText("")
        self.backward.setText("")
        self.right.setText("")
        self.left.setText("")
        self.up.setText("")
        self.down.setText("")
        self.yawing.setText("")
        self.rovmodes.setText("")
        self.firstgripper.setText("")
        self.secondgripper.setText("")
        self.thirdgripper.setText("")
        self.fourthgripper.setText("")
        self.Servolabel.setText(QCoreApplication.translate("MainWindow", u"Servo ", None))
        self.labelPercentage.setText(QCoreApplication.translate("MainWindow", u"0\u00b0", None))
        self.Servolabel_2.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.labelPercentage_2.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.timerlabel.setText(QCoreApplication.translate("MainWindow", u"15:00", None))
        self.startButton_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.restartButton.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.logoLabel.setText("")
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"DIVE IN", None))
        self.quoteLabel.setText(QCoreApplication.translate("MainWindow", u"Forged in Gold, Tempered by Depth \u2014 Champions Rise from the Abyss", None))
        self.Minimizebutton_2.setText("")
        self.Exitbutton_2.setText("")
        self.MaximizeButton_2.setText("")
        self.Copyrights.setText(QCoreApplication.translate("MainWindow", u"TITANS V2.0\n"
"   \u00a9 2026 Youssef Efat", None))
        self.tocontrolframe.setText("")
        self.label_2.setText("")
        self.Minimizebutton_3.setText("")
        self.MaximizeButton_3.setText("")
        self.Exitbutton_3.setText("")
        self.controllernormal.setText("")
        self.controllerlateral.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Controller Settings", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Youssef Emara", None))

        self.PilotName.setText(QCoreApplication.translate("MainWindow", u"Pilot", None))
        self.yesterlabel.setText(QCoreApplication.translate("MainWindow", u"YESTER", None))
        self.rovframe.setText("")
        self.yhawk.setText("")
        self.motor1number.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.motor2number.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.motor3number.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.motor4number.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.motor5number.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.motor6number.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.maxspeedlabel.setText(QCoreApplication.translate("MainWindow", u"Max Speed", None))
        self.minspeedlabel.setText(QCoreApplication.translate("MainWindow", u"Min Speed", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Servo1 Function", None))
        self.Servo1function.setItemText(0, QCoreApplication.translate("MainWindow", u"Motor1", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.Servo1reverse.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))

        self.Servo2function.setItemText(0, QCoreApplication.translate("MainWindow", u"Motor2", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Servo2 Function", None))
        self.Servo2reverse.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.Servo3reverse.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))

        self.Servo3function.setItemText(0, QCoreApplication.translate("MainWindow", u"Motor3", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Servo3 Function", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Servo4 Function", None))
        self.Servo4function.setItemText(0, QCoreApplication.translate("MainWindow", u"Motor4", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.Servo4reverse.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))

        self.Servo5function.setItemText(0, QCoreApplication.translate("MainWindow", u"Motor5", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Servo5 Function", None))
        self.Servo5reverse.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.Servo6function.setItemText(0, QCoreApplication.translate("MainWindow", u"Motor6", None))

        self.Servo6reverse.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Servo6 Function", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Servo7 Function", None))
        self.Servo7function.setItemText(0, QCoreApplication.translate("MainWindow", u"unassigned", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.Servo7reverse.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))

        self.Servo8reverse.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))

        self.Servo8function.setItemText(0, QCoreApplication.translate("MainWindow", u"unassigned", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Servo8 Function", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Camera Settings", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Zed Camera Quality:", None))
        self.Servo4function_2.setItemText(0, QCoreApplication.translate("MainWindow", u"720p", None))

        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Frame rate:", None))
        self.Servo4function_4.setItemText(0, QCoreApplication.translate("MainWindow", u"30FPS", None))

        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Bottom Camera Quality:", None))
        self.Servo4function_5.setItemText(0, QCoreApplication.translate("MainWindow", u"1080p", None))

        self.Servo4function_6.setItemText(0, QCoreApplication.translate("MainWindow", u"30FPS", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Frame rate:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Rear Camera Quality:", None))
        self.Servo4function_7.setItemText(0, QCoreApplication.translate("MainWindow", u"720p", None))

        self.Servo4function_8.setItemText(0, QCoreApplication.translate("MainWindow", u"30FPS", None))

        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Frame rate:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Grippers Camera Quality:", None))
        self.Servo4function_9.setItemText(0, QCoreApplication.translate("MainWindow", u"720p", None))

        self.Servo4function_10.setItemText(0, QCoreApplication.translate("MainWindow", u"30FPS", None))

        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Frame rate:", None))
        self.controllericon.setText("")
        self.zed2iicon.setText("")
        self.yground.setText("")
    # retranslateUi

