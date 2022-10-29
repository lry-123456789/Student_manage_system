import os.path, os
import sqlite3
import sys
import time
from shutil import copyfile

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5 import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
except:
    print('we can not found moudle pyqt5 or this moudle run failed , reinstall ?(Y/N)')
    a = input()
    if a == 'Y' or 'y':
        os.system("python -m pip install pyqt5 --upgrade --user")
        """create the environment"""
        try:
            from PyQt5 import QtCore, QtGui, QtWidgets
            from PyQt5.QtWidgets import QApplication, QMainWindow
            from PyQt5 import *
            from PyQt5.QtWidgets import *
            from PyQt5.QtCore import *
        except:
            print("can not install moudle pyqt5,so this program can not start.")
    else:
        print('can not start the moudle,exit the program...\nplease wait')
        exit(-1)

indexwindows = 0

__author__name__ = 'lry'
__author__email__ = '76830986+lry-123456789@user.noreply.github.com'
__maintainer__name__ = 'lry'
__maintainer__email__ = '1224137702@qq.com'
__version__ = 'v1.0.0'


def copyright():
    """
this file is edited by lry (c) 2020~2022
"""


def database(type: str):
    if type == 'login':
        return "login.db"
    if type == 'stu_info':
        return "info.db"


Login_ui = 0
Register_ui = 0
main_ui = 0


class show_license(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 0, 781, 501))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 510, 181, 41))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 509, 161, 41))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 510, 151, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.setEnabled(False)
        self.radioButton.clicked.connect(self.license_ok)
        self.radioButton_2.clicked.connect(self.license_no)
        self.radioButton_2.click()
        try:
            self.pushButton.clicked.connect(self.show_next)
        except Exception as e:
            print(e)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "第一次使用前须知"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">学生信息管理系统1.0.0安装使用协议</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请务必认真阅读和理解本《学生管理系统安装许可使用协议》（以下简称“《协议》”）中规定的所有权利和限制。除非您接受本《协议》条款，否则您无权下载、安装或使用随附本《协议》的学生管理系统软件（以下简称“本软件”）及其相关服务。您一旦安装、复制、下载、访问或以其它方式使用本软件产品，将视为对本《协议》的接受，即表示您同意接受本《协议》各项条款的约束。如果您不同意本《协议》中的条款，请不要安装、复制或使用本软件。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本《协议》是用户与LRY之间关于用户下载、安装、使用、复制本软件的法律协议。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.权利声明</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本软件的一切知识产权，以及与本软件相关的所有信息内容，包括但不限于：文字表述及其组合、图标、图饰、图像、图表、色彩、界面设计、版面框架、有关数据、附加程序、印刷材料或电子文档等均为LRY所有，受著作权法和国际著作权条约以及其他知识产权法律法规的保护。</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.许可范围</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.1 下载、安装和使用：本软件为免费软件，用户可以非商业性、无限制数量地下载、安装及使用本软件。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.2 复制、分发和传播：用户可以非商业性、无限制数量地复制、分发和传播本软件产品。但必须保证每一份复制、分发和传播都是完整和真实的,包括所有有关本软件产品的软件、电子文档,版权和商标，亦包括本协议。</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.权利限制</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.1 禁止反向工程、反向编译和反向汇编：用户不得对本软件产品进行反向工程（ReverseEngineer）、反向编译（Decompile）或反向汇编（Disassemble），同时不得改动编译在程序文件内部的任何资源。除法律、法规明文规定允许上述活动外，用户必须遵守此协议限制。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.2 组件分割:本软件产品是作为一个单一产品而被授予许可使用,用户不得将各个部分分开用于任何目的。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.3 个别授权:如需进行商业性的销售、复制、分发，包括但不限于软件销售、预装、捆绑等，必须获得LRY的书面授权和许可。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.4 保留权利：本协议未明示授权的其他一切权利仍归LRY所有，用户使用其他权利时必须获得LRY的书面同意。</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.用户使用须知</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本程序只能用于非商业用途，如果用于商业用途，请向发布者获取商业授权许可。</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5．免责与责任限制</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.1 用户确认，其知悉本软件所有功能及LRY为实现本软件各功能所进行的必要操作，其根据自身需求自愿选择使用本软件及相关服务，因使用本软件及相关服务所存在的风险和一切后果将完全由其自己承担，LRY不承担任何责任。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.2 本软件经过详细的测试，但不能保证与所有的软硬件系统完全兼容，不能保证本软件完全没有错误。如果出现不兼容及软件错误的情况，用户可发送邮件至1224137702@qq.com将情况报告LRY，获得技术支持。如果无法解决兼容性问题，用户可以删除本软件。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.3 在适用法律允许的最大范围内，对因使用或不能使用本软件所产生的损害及风险，包括但不限于直接或间接的个人损害、商业赢利的丧失、贸易中断、商业信息的丢失或任何其它经济损失，LRY不承担任何责任。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.4 对于因电信系统或互联网网络故障、计算机故障或病毒、信息损坏或丢失、计算机系统问题或其它任何不可抗力原因而产生损失，LRY不承担任何责任。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.5 用户违反本协议规定，LRY有权采取包括但不限于中断使用许可、停止提供服务、限制使用、法律追究等措施。</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.法律及争议解决</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.1 本协议适用中华人民共和国法律。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.2 因本协议引起的或与本协议有关的任何争议，各方应友好协商解决；协商不成的，任何一方均可将有关争议提交至被告住所地有管辖权的法院诉讼解决。</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.其他条款</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.1 如果本协议中的任何条款无论因何种原因完全或部分无效或不具有执行力，或违反任何适用的法律，则该条款被视为删除，但本协议的其余条款仍应有效并且有约束力。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.2 LRY有权随时根据有关法律、法规的变化以及公司经营状况和经营策略的调整等修改本协议。修改后的协议会在github网站https://github.com/lry-123456789/Student_manage_system上公布，并随附于新版本软件。当发生有关争议时，以最新的协议文本为准。如果不同意改动的内容，用户可以自行删除本软件。如果用户继续使用本软件，则视为您接受本协议的变动。</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.3 LRY在法律允许最大范围内对本协议拥有解释权与修改权。</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8.如果您确定使用本软件，则自动视为同意本软件的所有条款。</p></body></html>"))
        self.radioButton.setText(_translate("MainWindow", "I Agree"))
        self.radioButton_2.setText(_translate("MainWindow", "I do not agree"))
        self.pushButton.setText(_translate("MainWindow", "next step"))

    def license_ok(self):
        self.pushButton.setEnabled(True)

    def license_no(self):
        self.pushButton.setEnabled(False)

    def show_next(self):
        try:
            # print("1")
            # global indexwindows
            # print("1")
            # indexwindows = QMainWindow()
            # print("1")
            # index_ui = login()
            # print("1")
            # index_ui.setupUi(indexwindows)
            # print("1")
            # indexwindows.show()
            # print("1")
            # self.MainWindow.hide()
            # #del self
            global Login_ui
            Login_ui.show()
            self.close()
        except Exception as e:
            print(e)


class login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 236)
        MainWindow.setMinimumSize(QtCore.QSize(800, 236))
        MainWindow.setMaximumSize(QtCore.QSize(800, 236))
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 711, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 70, 711, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 130, 181, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 130, 181, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.pushButton_2.pyqtConfigure(objectName='pushButton_2',clicked=self.goto_new_window)
        self.pushButton.clicked.connect(self.goto_new_window)
        self.pushButton_3.clicked.connect(self.goto_exit)
        self.pushButton_2.clicked.connect(self.goto_register_window)

        # print("11")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow0", "登录到学生信息管理系统"))
        self.label.setText(_translate("MainWindow0", "Account:"))
        self.label_2.setText(_translate("MainWindow0", "Password:"))
        self.pushButton.setText(_translate("MainWindow0", "login"))
        self.pushButton_2.setText(_translate("MainWindow0", "register"))
        self.pushButton_3.setText(_translate("MainWindow0", "exit"))

    def goto_new_window(self):
        if os.path.exists("known.ini"):
            print("not first use")
        else:
            f = open("known.ini", "a+")
            print("[status]\nlogin.ini created\n[end]", file=f)
            f.close()
        conn = sqlite3.connect(database('login'))
        cursor = conn.cursor()
        try:
            sql = "CREATE TABLE LOGIN(ACCOUNT PRIMARY KRY TEXT NOT NULL, PASSWORD TEXT NOT NULL)"
            cursor.execute(sql)
            result = cursor.fetchall()
            conn.commit()
        except sqlite3.OperationalError as E:
            print(E)
        cursor.close()
        conn.close()
        # 此处表头创建完成<避免在无数据库文件时报错>
        # 登录验证操作
        conn = sqlite3.connect(database('login'))
        cursor = conn.cursor()
        # 获取用户名和密码
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()
        sql = "SELECT * from LOGIN WHERE ACCOUNT = '%s' AND PASSWORD = '%s'" % (account, password)
        print(cursor.execute(sql))
        result = cursor.fetchall()
        conn.commit()
        # print(result)
        cursor.close()
        conn.close()
        if result == []:
            QMessageBox.warning(self, '密码错误', '密码错误', QMessageBox.Yes)
        else:
            # 此处可以连接下一个登录界面
            global main_ui
            main_ui.show()
            self.close()

    def goto_register_window(self):
        try:
            # print("1")
            # global indexwindows0
            # indexwindows0 = QMainWindow()
            # index_ui = Register()
            # index_ui.setupUi(indexwindows0)
            # indexwindows0.show()
            # self.MainWindow.close()
            # --------------------------#
            # app0 = QApplication(sys.argv)
            # mainwindow = QMainWindow()
            # output = login()
            # # output1 = login()
            # ui = output
            # ui.setupUi(mainwindow)
            # mainwindow.show()
            # sys.exit(app0.exec())
            global Register_ui
            Register_ui.show()
            self.close()
        except Exception as e:
            print(e)

    def goto_exit(self):
        exit(0)


class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 218)
        MainWindow.setMinimumSize(QtCore.QSize(800, 218))
        MainWindow.setMaximumSize(QtCore.QSize(800, 218))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 141, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 10, 661, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 50, 661, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 90, 661, 31))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 130, 281, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.pull_info_to_database)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "注册到学生信息管理系统"))
        self.label.setText(_translate("MainWindow", "Account:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.label_3.setText(_translate("MainWindow", "Confirm password:"))
        self.pushButton.setText(_translate("MainWindow", "Create Account"))

    def pull_info_to_database(self):
        # 连接数据库
        user_account = self.lineEdit.text()
        user_password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()
        if user_account == '':
            a = QMessageBox.warning(self, '用户名不能为空', '用户名不能为空', QMessageBox.Yes)
            return
        if user_password == '':
            a = QMessageBox.warning(self, '密码不能为空', '密码不能为空', QMessageBox.Yes)
            return
        if user_password == user_account:
            a = QMessageBox.warning(self, '用户名不能与密码相同', '用户名不能与密码相同', QMessageBox.Yes)
            return
        if user_password != confirm_password:
            a = QMessageBox.warning(self, '两次密码不一致，请重新输入', '两次密码不一致，请重新输入', QMessageBox.Yes)
            return
        # 检查通过，连接数据库
        conn = sqlite3.connect(database('login'))
        cursor = conn.cursor()
        try:
            sql = "CREATE TABLE LOGIN(ACCOUNT PRIMARY KEY NOT NULL, PASSWORD TEXT NOT NULL)"
            cursor.execute(sql)
            result = cursor.fetchall()
            conn.commit()
        except sqlite3.OperationalError as E:
            print(E)
        cursor.close()
        conn.close()
        conn = sqlite3.connect(database('login'))
        cursor = conn.cursor()
        try:
            sql = "insert into LOGIN values('%s', '%s')" % (user_account, user_password)
            print(cursor.execute(sql))
            result = cursor.fetchall()
            conn.commit()
            # print(result)
            cursor.close()
            conn.close()
            QMessageBox.information(self, '注册完成', '注册完成')
            Login_ui.show()
            self.close()
        except:
            QMessageBox.warning(self, '提示', '用户名已存在')


class Operation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        conn = sqlite3.connect(database("stu_info"))
        cursor = conn.cursor()
        try:
            sql = "select count(*) from INFO"
            cursor.execute(sql)
            conn.commit()
            id = cursor.fetchall()
        except sqlite3.OperationalError as E:
            # print(E)
            sql = "create table INFO(stu_id primary key not null, name text not null, age text not null, gender text not null)"
            cursor.execute(sql)
            conn.commit()
            id = 0
        finally:
            cursor.close()
            conn.close()
        self.lines = id
        self.filename = 0
        f = open(database("stu_info"), "rb")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 90, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(105, 10, 90, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 10, 90, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(295, 10, 110, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 781, 491))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 761, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 180)
        self.tableWidget.setColumnWidth(1, 180)
        self.tableWidget.setColumnWidth(2, 180)
        self.tableWidget.setColumnWidth(3, 180)
        self.tableWidget.setHorizontalHeaderLabels(('学号', '姓名', '年龄', '性别'))
        self.tableWidget.setRowCount(0)  # 列
        # 在此处显示所有信息
        try:
            conn = sqlite3.connect(database("stu_info"))
            cursor = conn.cursor()
            sql = "select * from INFO"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
        except:
            result = []
            # print("0")
        finally:
            cursor.close()
            conn.close()
        self.tableWidget.setRowCount(len(result))
        # self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(4):
                # print(type(result[i][j]))
                self.tableWidget.setItem(i, j, QTableWidgetItem(result[i][j]))
        self.tableWidget.viewport().update()
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 0, 371, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(12, 20, 351, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.insert_stu_info)
        self.pushButton_2.clicked.connect(self.del_stu_info)
        self.pushButton_3.clicked.connect(self.change_stu_info)
        self.pushButton_4.clicked.connect(self.insert_or_export)
        self.timer = QTimer()
        self.timer.timeout.connect(self.protect_thread)
        self.timer.start(100)
        # self.timer0 = QTimer()
        # self.timer0.timeout.connect(self.runtime_protect_Database)
        # self.timer0.start(10)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生信息管理系统 v1.0.0 powered by lry (c) 2020~2022"))
        self.pushButton.setText(_translate("MainWindow", "添加学生信息"))
        self.pushButton_2.setText(_translate("MainWindow", "删除学生信息"))
        self.pushButton_3.setText(_translate("MainWindow", "修改学生信息"))
        self.pushButton_4.setText(_translate("MainWindow", "导入/导出"))
        self.groupBox.setTitle(_translate("MainWindow", "所有学生信息"))
        self.groupBox_2.setTitle(_translate("MainWindow", "status"))
        self.label.setText(_translate("MainWindow", "can not attach to the database, please check the connection"))
        if os.path.exists(database("stu_info")):
            self.label.setText("successfully connect to the database")
        else:
            self.label.setText("can not connect to the database")

    def insert_stu_info(self):
        self.Qt_UI_protect()
        stu_id = 0
        stu_name = 0
        stu_age = 0
        stu_gender = 0
        temp, is_OK = QInputDialog.getInt(self, "请输入学号", '请输入学号', min=0)
        # print(temp,is_OK)            0,True
        if is_OK == False:
            return
        stu_id = temp
        temp, is_OK = QInputDialog.getText(self, '请输入学生姓名', '请输入学生姓名')
        # print(temp,is_OK)           None ,False
        if is_OK == False:
            return
        stu_name = temp
        temp, is_Ok = QInputDialog.getInt(self, '请输入年龄', '请输入年龄', min=1, max=100)
        # print(temp,is_Ok)             0,True
        if is_OK == False:
            return
        stu_age = temp
        list_str = ('男', '女')
        temp, is_OK = QInputDialog.getItem(self, '请输入性别', '请输入性别', list_str)
        if is_OK == False:
            return
        if temp not in list_str:
            return
        stu_gender = temp
        # 避免错误，在数据库中审查唯一标识符是否被占用
        conn = sqlite3.connect(database('stu_info'))
        cursor = conn.cursor()
        try:
            sql = "SELECT * FROM INFO WHERE stu_id = '%s'" % (str(stu_id))
            cursor.execute(sql)
            result = cursor.fetchall()
            conn.commit()
            if result != []:
                QMessageBox.critical(self, "学号<唯一标识符>被占用", "学号<唯一标识符>被占用", QMessageBox.Yes)
                return
        except sqlite3.OperationalError as E:
            # print(E)
            return
        finally:
            cursor.close()
            conn.close()
        # 此时数据获取完成
        conn = sqlite3.connect(database('stu_info'))
        cursor = conn.cursor()
        try:
            sql = "insert into INFO values('%s','%s','%s','%s')" % (str(stu_id), stu_name, str(stu_age), stu_gender)
            cursor.execute(sql)
            result = cursor.fetchall()
            conn.commit()
        except sqlite3.OperationalError as E:
            print(E)
        cursor.close()
        conn.close()
        # 在主界面上显示
        try:
            conn = sqlite3.connect(database("stu_info"))
            cursor = conn.cursor()
            sql = "select * from INFO"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
            # print(result[0][0])
        except:
            print("0")
        finally:
            cursor.close()
            conn.close()
        # print(len(result))
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(4):
                # print(type(result[i][j]))
                self.tableWidget.setItem(i, j, QTableWidgetItem(result[i][j]))

    def del_stu_info(self):
        self.Qt_UI_protect()
        # 此处删除某个学生的信息
        stu_id, is_OK = QInputDialog.getInt(self, "请输入待删除的学生学号", "请输入待删除的学生学号", min=0)
        if is_OK == False:
            return
        try:
            conn = sqlite3.connect(database("stu_info"))
            cursor = conn.cursor()
            # print(stu_id)
            sql = "delete from INFO where stu_id = '%s'" % (str(stu_id))
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as E:
            print(E)
        try:
            conn = sqlite3.connect(database("stu_info"))
            cursor = conn.cursor()
            sql = "select * from INFO"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
            # print(result[0][0])
        except:
            print("0")
        finally:
            cursor.close()
            conn.close()
        # print(len(result))
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(4):
                # print(type(result[i][j]))
                self.tableWidget.setItem(i, j, QTableWidgetItem(result[i][j]))

    def change_stu_info(self):
        self.Qt_UI_protect()
        # 此处为修改某个学生的信息
        temp, is_OK = QInputDialog.getInt(self, "请输入待修改的学生ID", '请输入待修改的学生ID', min=0)
        if is_OK == False:
            return
        stu_id_before = temp
        list_str = ('id', '姓名', '年龄', '性别')
        change, is_OK = QInputDialog.getItem(self, '请选择待修改的信息项目', '请选择待修改的项目', list_str)
        if is_OK == False:
            return
        if change not in list_str:
            return
        if change == 'id':
            temp, is_OK = QInputDialog.getInt(self, "请输入修改后的ID", "请输入修改后的ID", min=0)
            if is_OK == False:
                return
            conn = sqlite3.connect(database("stu_info"))
            cursor = conn.cursor()
            sql = "UPDATE INFO SET stu_id = '%s' WHERE stu_id = '%s'" % (temp, stu_id_before)
            cursor.execute(sql)
            QMessageBox.information(self, "修改完成", '修改完成', QMessageBox.Yes)
            conn.commit()
            cursor.close()
            conn.close()
            # 主界面组件更新
            try:
                conn = sqlite3.connect(database("stu_info"))
                cursor = conn.cursor()
                sql = "select * from INFO"
                cursor.execute(sql)
                result = cursor.fetchall()
                # print(result)
                # print(result[0][0])
            except:
                print("0")
            finally:
                cursor.close()
                conn.close()
            # print(len(result))
            self.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for j in range(4):
                    # print(type(result[i][j]))
                    self.tableWidget.setItem(i, j, QTableWidgetItem(result[i][j]))
            return
        if change == '姓名':
            temp, is_OK = QInputDialog.getText(self, "请输入修改后的姓名", "请输入修改后的姓名")
            if is_OK == False:
                return
            conn = sqlite3.connect(database("stu_info"))
            cursor = conn.cursor()
            sql = "UPDATE INFO SET name = '%s' WHERE stu_id = '%s'" % (temp, stu_id_before)
            cursor.execute(sql)
            QMessageBox.information(self, "修改完成", '修改完成', QMessageBox.Yes)
            conn.commit()
            cursor.close()
            conn.close()
            # 主界面组件更新
            try:
                conn = sqlite3.connect(database("stu_info"))
                cursor = conn.cursor()
                sql = "select * from INFO"
                cursor.execute(sql)
                result = cursor.fetchall()
                # print(result)
                # print(result[0][0])
            except:
                print("0")
            finally:
                cursor.close()
                conn.close()
            # print(len(result))
            self.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for j in range(4):
                    # print(type(result[i][j]))
                    self.tableWidget.setItem(i, j, QTableWidgetItem(result[i][j]))
            return
        if change == '年龄':
            temp, is_OK = QInputDialog.getInt(self, "请输入修改后的年龄", "请输入修改后的年龄", min=0, max=100)
            if is_OK == False:
                return
            conn = sqlite3.connect(database("stu_info"))
            cursor = conn.cursor()
            sql = "UPDATE INFO SET age = '%s' WHERE stu_id = '%s'" % (temp, stu_id_before)
            cursor.execute(sql)
            QMessageBox.information(self, "修改完成", '修改完成', QMessageBox.Yes)
            conn.commit()
            cursor.close()
            conn.close()
            # 主界面组件更新
            try:
                conn = sqlite3.connect(database("stu_info"))
                cursor = conn.cursor()
                sql = "select * from INFO"
                cursor.execute(sql)
                result = cursor.fetchall()
                # print(result)
                # print(result[0][0])
            except:
                print("0")
            finally:
                cursor.close()
                conn.close()
            # print(len(result))
            self.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for j in range(4):
                    # print(type(result[i][j]))
                    self.tableWidget.setItem(i, j, QTableWidgetItem(result[i][j]))
            return
        if change == '性别':
            list_gender = ('男', '女')
            temp, is_OK = QInputDialog.getItem(self, "请输入修改后的性别", "请输入修改后的性别", list_gender)
            if is_OK == False:
                return
            if temp not in list_gender:
                return
            conn = sqlite3.connect(database("stu_info"))
            cursor = conn.cursor()
            sql = "UPDATE INFO SET gender ='%s' WHERE stu_id = '%s'" % (temp, stu_id_before)
            cursor.execute(sql)
            QMessageBox.information(self, "修改完成", '修改完成', QMessageBox.Yes)
            conn.commit()
            cursor.close()
            conn.close()
            # 主界面组件更新
            try:
                conn = sqlite3.connect(database("stu_info"))
                cursor = conn.cursor()
                sql = "select * from INFO"
                cursor.execute(sql)
                result = cursor.fetchall()
                # print(result)
                # print(result[0][0])
            except:
                print("0")
            finally:
                cursor.close()
                conn.close()
            # print(len(result))
            self.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for j in range(4):
                    # print(type(result[i][j]))
                    self.tableWidget.setItem(i, j, QTableWidgetItem(result[i][j]))
            return
        QMessageBox.critical(self, "RuntimeError", "StackOverFlow", QMessageBox.Yes)
        exit(-1)

    def protect_thread(self):
        time_str = time.asctime(time.localtime(time.time()))
        if os.path.exists(database("stu_info")):
            self.label.setText(time_str + "\tconnected to database")
        else:
            self.label.setText(time_str + "\tfailed connect to database")
            QMessageBox.critical(self, "严重错误",
                                 "请勿在运行时删除数据库文件(RuntimeError:database disconnected <info.db>\nPress Yes to create database again)",
                                 QMessageBox.Yes)
            self.Qt_UI_protect()
        try:
            conn = sqlite3.connect(database("stu_info"))
            cursor = conn.cursor()
            sql = "select * from INFO"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
            # print(result[0][0])
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)
            result = []
        # print(len(result))
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(4):
                # print(type(result[i][j]))
                self.tableWidget.setItem(i, j, QTableWidgetItem(result[i][j]))

    def Qt_UI_protect(self):
        conn = sqlite3.connect(database("stu_info"))
        cursor = conn.cursor()
        try:
            sql = "select count(*) from INFO"
            cursor.execute(sql)
            conn.commit()
            id = cursor.fetchall()
        except sqlite3.OperationalError as E:
            # print(E)
            sql = "create table INFO(stu_id primary key not null, name text not null, age text not null, gender text not null)"
            cursor.execute(sql)
            conn.commit()
            id = 0
        finally:
            cursor.close()
            conn.close()

    def insert_or_export(self):
        list_choose = ('导入', '导出')
        temp, is_OK = QInputDialog.getItem(self, "请选择类别", "请选择类别", list_choose)
        if is_OK == False:
            return
        if temp not in list_choose:
            return
        if temp == '导入':
            try:
                self.insert_into_database()
            except Exception as e:
                QMessageBox.critical(self,"严重错误",e)
        if temp == '导出':
            QMessageBox.information(self,"系统暂不支持此操作","系统暂不支持此操作，请期待后续版本")

    def insert_into_database(self):
        # filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "请选择文件", os.getcwd(),
        #                                                            "TXT(*.txt);;XLSX(*.xlsx);;XLS(*.xls);;CSV(*.csv)")
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "请选择文件", os.getcwd(),
                                                                   "XLSX(*.xlsx);;XLS(*.xls)")
        print(filename)
        print(filetype)
        # filetype  :   txt             xlsx            xls             csv
        # type      :   TXT(*.txt)      XLSX(*xlsx)     XLS(*xls)       CSV(*csv)
        type_list = ['TXT(*.txt)', 'XLSX(*.xlsx)', 'XLS(*.xls)', 'CSV(*.csv)']
        if filetype == type_list[0]:
            self.filename = filename
            self.insert_from_txt()
            return
        if filetype == type_list[1]:
            self.filename = filename
            self.insert_from_xlsx()
            return
        if filetype == type_list[2]:
            self.filename = filename
            self.insert_from_xls()
            return
        if filetype == type_list[3]:
            self.filename = filename
            self.insert_from_csv()
            return
        return

    def insert_from_txt(self):
        QMessageBox.information(self,"暂不支持","暂不支持")

    def insert_from_xlsx(self):
        QMessageBox.information(self,"注意","本程序使用的是单线程，运行时可能会出现无响应情况，请等待即可")
        time0 = time.time()
        print("1")
        try:
            import xlrd3
        except:
            QMessageBox.critical(self, "严重错误",
                                 "无法启动组件导出到xlsx\n可能是因为没有安装运行库xlrd3\n<run this command in your terminal: pip install xlrd3 --user>")
            return
        filename = self.filename
        try:
            workbook = xlrd3.open_workbook(filename)
        except Exception as e:
            QMessageBox.critical(self, "未知错误", e + "\n本组件无法继续执行")
            return
        names = workbook.sheet_names()
        # print(names)
        worksheet = workbook.sheet_by_name(names[0])
        cols = worksheet.ncols
        # print("cols = ", cols)
        if cols < 4:
            QMessageBox.critical(self, "严重错误", "AssertError:\n<assert cols >= 4>")
            return
        list_ok = [0, 0, 0, 0]
        ok = False
        for col in range(cols):
            value = worksheet.cell_value(0, col)
            if value == '学号':
                ok = True
                list_ok[0] = col
                break
        if ok == False:
            QMessageBox.critical(self, "无法查找到学号信息", "无法查找到学号信息")
            return
        ok = False
        for col in range(cols):
            value = worksheet.cell_value(0, col)
            if value == '姓名':
                ok = True
                list_ok[1] = col
                break
        if ok == False:
            QMessageBox.critical(self, "无法查找姓名信息", "无法查找姓名信息")
            return
        ok = False
        for col in range(cols):
            value = worksheet.cell_value(0, col)
            if value == '年龄':
                ok = True
                list_ok[2] = col
                break
        if ok == False:
            QMessageBox.critical(self, "无法查找年龄信息", "无法查找年龄信息")
            return
        ok = False
        for col in range(cols):
            value = worksheet.cell_value(0, col)
            if value == '性别':
                ok = True
                list_ok[3] = col
                break
        if ok == False:
            QMessageBox.critical(self, "无法查找性别信息", "无法查找性别信息")
            return
        # xlrd read ended
        # get rows
        # print("1")
        nrows = worksheet.nrows
        lines = nrows - 1
        # get some information
        # commit this information to database
        # print("1")
        conn = sqlite3.connect(database("stu_info"))
        cursor = conn.cursor()
        # 如果没有表头，则创建表头
        try:
            sql = "create table INFO(stu_id primary key not null, name text not null, age text not null, gender text not null)"
            cursor.execute(sql)
            conn.commit()
        except sqlite3.OperationalError as E:
            print(E)
        finally:
            cursor.close()
            conn.close()
        # print("1")
        # 表头已经创建：
        # 可以插入数据：
        name_list = []
        age_list = []
        stu_id_list = []
        gender_list = []
        for i in range(lines):
            # stu_id, name, age, gender = worksheet.cell_value(i + 1, list_ok[0]), worksheet.cell_value(i + 1, list_ok[
            #     1]), worksheet.cell_value(i + 1, list[2]), worksheet.cell_value(i + 1, list_ok[3])
            # print(list_ok,lines,i)
            output_str = "progress="+str(i)+"/"+str(lines)+"stage1/2"
            self.label.setText(output_str)
            stu_id = worksheet.cell_value(i+1,list_ok[0])
            name = worksheet.cell_value(i+1,list_ok[1])
            age = worksheet.cell_value(i+1,list_ok[2])
            gender = worksheet.cell_value(i+1,list_ok[3])
            # print(stu_id,name,age,gender)
            if stu_id == '':
                QMessageBox.critical(self,"严重错误","无法查找学号信息"+str(i+1)+"行")
                return
            if name == "":
                QMessageBox.critical(self,"严重错误","无法查找姓名信息"+str(i+1)+"行")
                return
            if age == "":
                QMessageBox.critical(self,"严重错误","无法找到年龄信息"+str(i+1)+"行")
                return
            if gender == "":
                QMessageBox.critical(self,"严重错误","w货找到性别信息"+str(i+1)+"行")
                return
            list_gender = ['男','女']
            if gender not in list_gender:
                QMessageBox.critical(self,"严重错误","性别无法识别")
            if type(stu_id) != int:
                stu_id = int(stu_id)
            if type(age) != int:
                age = int(age)
            if type(stu_id) != str:
                stu_id = str(stu_id)
            if type(name) != str:
                name = str(name)
            if type(age) != str:
                age = str(age)
            if type(gender) != str:
                gender = str(gender)
            stu_id_list.append(stu_id)
            name_list.append(name)
            age_list.append(age)
            gender_list.append(gender)
        conn = sqlite3.connect(database("stu_info"))
        cursor = conn.cursor()
        for i in range(len(name_list)):
            try :
                output_str = "progress="+str(i)+"/"+str(len(name_list))+"stage2/2"
                self.label.setText(output_str)
                sql = "insert into INFO values('%s','%s','%s','%s')"%(stu_id_list[i],name_list[i],age_list[i],gender_list[i])
                # print(sql)
                cursor.execute(sql)
                # print("1")
                conn.commit()
                # print("1")
            except sqlite3.OperationalError as e:
                # print(e)
                QMessageBox.warning(self,"警告","学号数据信息已被占用，无法写入信息")
            except Exception as e:
                # print(e)
                QMessageBox.warning(self,"未知错误",str(e))
                return
        cursor.close()
        conn.close()

        # commit 完成
        # 更新主界面
        try:
            conn = sqlite3.connect(database("stu_info"))
            cursor = conn.cursor()
            sql = "select * from INFO"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
            # print(result[0][0])
        except:
            print("0")
        finally:
            cursor.close()
            conn.close()
        # print(len(result))
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(4):
                # print(type(result[i][j]))
                self.tableWidget.setItem(i, j, QTableWidgetItem(result[i][j]))
        time1 = time.time()
        used = time1 - time0
        cols = len(result)
        output_str = "操作完成,一共成功完成"+str(cols)+"条数据\n用时"+str(used)+"s"
        QMessageBox.information(self,"操作完成",output_str)

    def insert_from_xls(self):
        self.insert_from_xlsx()

    def insert_from_csv(self):
        QMessageBox.information(self,"暂时不支持","暂不支持")



def check_system():
    print('sys info:', sys.platform)
    if sys.platform == 'linux':
        print('this program run on Linux platform may have some errors')
    if sys.platform == 'win32':
        print('detect windows platform')


def start():
    print('checking system info please wait...')
    check_system()
    print('Load UI subsystem,please wait')
    app = QApplication(sys.argv)
    global Login_ui, Register_ui, main_ui
    Login_ui = login()
    Register_ui = Register()
    License_ui = show_license()
    print('Runtime protect<database> mode : open')
    main_ui = Operation()
    print('check UI information,please wait')
    if os.path.exists("known.ini"):
        Login_ui.show()
    else:
        License_ui.show()
    sys.exit(app.exec())
    # app = QApplication(sys.argv)
    # mainwindow = show_license(parent=None)
    # mainwindow.show()
    # sys.exit(app.exec())


if __name__ == '__main__':
    start()
