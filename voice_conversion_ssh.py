from ssh import SSH
import sys
from voice_conversion_ssh_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QPushButton, QMainWindow


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pb_upload.clicked.connect(self.upload_click)
        self.ui.pb_convert.clicked.connect(self.convert_click)
        self.ui.pb_download.clicked.connect(self.download_click)

    def upload_click(self):
        message = SSH.upload_wav_to_server()
        QMessageBox.information(self,
                                '>_<',
                                message,
                                QMessageBox.Yes)

    def convert_click(self):
        message = SSH.convert_wav()
        QMessageBox.information(self,
                                '>_<',
                                message,
                                QMessageBox.Yes)

    def download_click(self):
        message = SSH.download_wav_from_server()
        QMessageBox.information(self,
                                '>_<',
                                message,
                                QMessageBox.Yes)


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())

# SSH.upload_wav_to_server()
# SSH.convert_wav()
# SSH.download_wav_from_server()