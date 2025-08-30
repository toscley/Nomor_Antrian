from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
import sys, os, webbrowser
from datetime import datetime

App = QApplication([])
nomor = QWidget()
nomor.setWindowTitle('Nomor Antrian RS')
nomor.resize(200,200)
text1 = QLabel('RUMAH SAKIT MEDAN')
text2 = QLabel('Ambil Nomor Antrian')
button1 = QPushButton('ambil nomor')
global no_antri 
no_antri = 0

line = QVBoxLayout()
line.addWidget(text1, alignment = Qt.AlignCenter)
line.addWidget(text2, alignment = Qt.AlignCenter)
line.addWidget(button1, alignment = Qt.AlignCenter)
nomor.setLayout(line)

def NA() :
    global no_antri 
    no_antri += 1
    return no_antri

def Message() :
    global no_antri
    today = datetime.now()
    formatted_date = today.strftime("%d-%b-%Y %H:%M:%S")
    No_anda = QMessageBox()
    No_anda.setWindowTitle('Nomor Anda')
    No_anda.resize(200,200)
    No_anda.setText("<div align = 'center'> Nomor Antrian Anda <br><b> " + str(NA()) + " </b></div>")
    No_anda.setStandardButtons(QMessageBox.Ok | QMessageBox.Yes) # Ok & Yes
    No_anda.button(QMessageBox.Ok).setText('Tutup')
    No_anda.button(QMessageBox.Yes).setText('Print')
    choice = No_anda.exec()
    if choice == QMessageBox.Yes :
        filename = "antrian_template.html"
        html_content = """<!DOCTYPE html>
        <html>
            <head>
                <title>Antrian</title>
                <style>
                    .myDiv {
                        border : 2px outset grey;
                        background-color : white;
                        text-align : center;
                    }
                </style>
                <script>
                    window.onload = function() {{
                    window.print();                }}
                </script>
            </head>
            <body>\
                <div class="myDiv">
                    <center>
                        <h1>RUMAH SAKIT MEDAN</h1>
                        <h2>Jl. M. H. Thamrin, Kota Medan</h2><br>
                        <h3>Bunga Citra</h3>
                        <h3>"""+formatted_date+"""</h3>
                        <br>
                        <br>
                        <font size="10">
                            Umum<br>
                            """+str(no_antri)+"""
                        </font>
                        <br>
                        <br>
                        <h2>Terima Kasih</h2>
                        <h3>By Medicaboo</h3>
                    </center>
                </div>
            </body>
        </html>
        """

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        webbrowser.open_new_tab(os.path.abspath(filename))

button1.clicked.connect(Message)

nomor.show()
App.exec_()
