import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QAction,qApp,QMainWindow
class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazialani = QTextEdit()
        self.temizle = QPushButton("Temizle")
        self.dosyaac = QPushButton("Aç")
        self.kaydet=QPushButton("Kaydet")

        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.dosyaac)
        h_box.addWidget(self.kaydet)
        v_box = QVBoxLayout()
        self.temizle.clicked.connect(self.temiz)
        self.dosyaac.clicked.connect(self.acik)
        self.kaydet.clicked.connect(self.kayit)
        v_box.addWidget(self.yazialani)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setGeometry(500,100,1000,800)
        self.setWindowTitle("Notebook")

    def temiz(self):
        self.yazialani.clear()
    def acik(self):
        try:
            dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("Desktop"))
            with open(dosya_ismi[0],"r") as file:
                self.yazialani.setText(file.read())
        except:
            pass
    def kayit(self):
        try:
            dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("Desktop"))
            with open(dosya_ismi[0],"w") as file:
                file.write(self.yazialani.toPlainText())
        except:
            pass
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Notepad()

        self.setCentralWidget(self.pencere)
        self.menuleri_olustur()
    def menuleri_olustur(self):

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        temizleme = QAction("Temizle",self)
        temizleme.setShortcut("Ctrl+D")
        çıkış = QAction("Çıkış",self)
        çıkış.setShortcut("Ctrl+L")
        self.setWindowTitle("Metin Editörü")
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizleme)
        dosya.addAction(çıkış)
        dosya.triggered.connect(self.response)
        self.show()
    def response(self,action):
        if action.text() == "Dosya Aç":
            self.pencere.acik()
        elif action.text() == "Dosya Kaydet":
            self.pencere.kayit()
        elif action.text() == "Çıkış":
            qApp.quit()
        elif action.text() == "Temizle":
            self.pencere.temiz()




app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
