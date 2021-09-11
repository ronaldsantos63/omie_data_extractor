import sys
from PyQt5.QtWidgets import QApplication

from view.main_application import MainApplication


def main():
    app = QApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(False)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
