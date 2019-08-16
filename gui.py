import sys

from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QApplication, QMainWindow

from client import Client
from ui_mainwindow import Ui_mainWindow

c = Client()

# command to compile GUI
# pyside2-uic mainwindow.ui > ui_mainwindow.py


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.fill_list_view()
        self.ui.insert.clicked.connect(self.insert_line)
        self.ui.delete_2.clicked.connect(self.delete_selected)
        self.ui.update.clicked.connect(self.show_update_form)
        self.ui.update_button.clicked.connect(self.update_selected)

        # hide form for updating on start
        self.hide_update_form()

    def fill_list_view(self):
        values = c.get_all()
        model = QStandardItemModel()
        self.ui.listView.setModel(model)

        for i, number, text in values:
            line = "{}: {}, {}".format(i, number, text)
            item = QStandardItem(line)
            model.appendRow(item)

    def insert_line(self):
        number = self.ui.number.value()
        text = self.ui.text.text()
        if not text:
            return
        c.transaction('create', number, text)
        self.ui.number.setValue(1)
        self.ui.text.setText('')
        self.fill_list_view()

    def delete_selected(self):
        selected = self.ui.listView.selectedIndexes()
        for s in selected:
            id, _ = s.data().split(': ')
            c.transaction('deleted', int(id))
            self.fill_list_view()

    def hide_update_form(self):
        self.ui.update_form_label.hide()
        self.ui.update_id.hide()
        self.ui.update_button.hide()
        self.ui.update_number.hide()
        self.ui.update_text.hide()

    def show_update_form(self):
        selected = self.ui.listView.selectedIndexes()
        for s in selected:
            id, number_text = s.data().split(': ')
            number, text = number_text.split(', ')

            self.ui.update_form_label.show()
            self.ui.update_id.setText(id)
            self.ui.update_id.show()
            self.ui.update_number.setValue(int(number))
            self.ui.update_number.show()
            self.ui.update_text.setText(text)
            self.ui.update_text.show()
            self.ui.update_button.show()

    def update_selected(self):
        id = int(self.ui.update_id.text())
        number = self.ui.update_number.value()
        text = self.ui.update_text.text()

        c.transaction('set_number', id, number)
        c.transaction('set_text', id, text)

        self.hide_update_form()
        self.fill_list_view()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
