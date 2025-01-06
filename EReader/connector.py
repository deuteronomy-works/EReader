from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot


class Connector(QObject):

    def __init__(self, parent=None):
        super().__init__(self)
