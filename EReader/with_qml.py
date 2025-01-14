import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWebEngineQuick import QtWebEngineQuick

import misc
from connector import Connector

misc.reader_html_replacer('ex1/index.xhtml', 'ex1/nav.xhtml')

app = QGuiApplication(sys.argv)
QtWebEngineQuick.initialize()

engine = QQmlApplicationEngine()
engine.load('main.qml')
engine.quit.connect(app.quit)

sys.exit(app.exec())
