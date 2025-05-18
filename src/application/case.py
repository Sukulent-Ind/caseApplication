from PyQt5 import QtWidgets, QtGui
from src.resources.MainWindow import Ui_MainWindow
from src.resources.AddNewWorker import Ui_NewWorkerForm
from src.resources.InfoAboutWorker import Ui_WorkerInformation
from src.resources.AddNewDepartment import Ui_NewDepartment
from src.resources.Turniket import Ui_RFID
from src.resources.ValidErr import Ui_Dialog
import sys
import requests



apiurl = "http://127.0.0.1:8000/"


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.find.clicked.connect(self.find_worker)
        self.ui.find_attendance.clicked.connect(self.show_attendance)
        self.ui.new_worker.clicked.connect(self.new_worker)
        self.ui.new_department.clicked.connect(self.new_department)

        self.worker_info_window = InfoWorkerWindow()
        self.new_worker_window = NewWorkerWindow()
        self.new_department_window = NewDepWindow()
        self.turniket_window = TurniketWindow()

    def find_worker(self):
        if(self.ui.FIO_find.text() in ["", "Введите ФИО!"]):
            self.ui.FIO_find.setText("Введите ФИО!")
            return

        response = requests.get(apiurl + "worker/{fio}?name=" + self.ui.FIO_find.text())

        if response.status_code == 200 and response.json() != []:
            self.worker_info_window.set_data(response)
            self.worker_info_window.show()

        else:
            self.ui.FIO_find.setText("Не найден")
        return

    def show_all_names(self):
        pass

    def show_attendance(self):
        pass

    def new_worker(self):
        self.new_worker_window.set_data()
        self.new_worker_window.show()

    def new_department(self):
        pass

    def check_worker_count(self):
        pass


class NewWorkerWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(NewWorkerWindow, self).__init__()
        self.ui = Ui_NewWorkerForm()
        self.ui.setupUi(self)

        self.departments = self.get_departments()

        self.ui.cancel_add_worker.clicked.connect(self.cancel_clk)
        self.ui.add_worker.clicked.connect(self.create_worker)

        self.valid_err_window = ValidErrWindow()

    def hideEvent(self, a0):
        self.ui.department_number.currentTextChanged.disconnect()

    def dep_num_chg(self):
        self.ui.department_name.setText(self.departments[self.ui.department_number.currentText()]["name"])
        self.ui.department_adress.setText(self.departments[self.ui.department_number.currentText()]["adress"])

    def cancel_clk(self):
        self.hide()

    def create_worker(self):
        new_data = {}
        new_data["name"] = " ".join([self.ui.surename.text(), self.ui.name.text(), self.ui.father_name.text()]).strip()
        new_data["adress"] = self.ui.adress.text()
        new_data["phone_number"] = self.ui.phone.text()

        try:
            new_data["passport_series"] = int(self.ui.passport_series.text())
            new_data["passport_number"] = int(self.ui.passport_number.text())
            new_data["department_id"] = int(self.ui.department_number.currentText())
        except:
            self.valid_err_window.show()
            return

        response = requests.post(apiurl + f"worker", json=new_data)

        if response.status_code == 200:
            self.hide()
        else:
            self.valid_err_window.show()
            return

    def set_data(self):
        self.departments = self.get_departments()

        self.ui.surename.clear()
        self.ui.name.clear()
        self.ui.father_name.clear()
        self.ui.adress.clear()
        self.ui.passport_series.clear()
        self.ui.passport_number.clear()
        self.ui.phone.clear()
        self.ui.department_number.setCurrentText(list(self.departments.keys())[0])
        self.ui.department_name.setText(self.departments[self.ui.department_number.currentText()]["name"])
        self.ui.department_adress.setText(self.departments[self.ui.department_number.currentText()]["adress"])

        self.ui.department_number.currentTextChanged.connect(self.dep_num_chg)

    def get_departments(self):
        self.ui.department_number.clear()
        response = requests.get(apiurl + "departments/all")
        if response.status_code != 200 or response.json() == []:
            self.ui.department_number.addItem("0")
            return {"0": {"name": "0", "adress": "0"}}

        new_dep = {}

        for resp in response.json():
            self.ui.department_number.addItem(str(resp["id"]))
            new_dep[str(resp["id"])] = {"adress": resp["adress"], "name": resp["name"]}
        return new_dep


class InfoWorkerWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(InfoWorkerWindow, self).__init__()
        self.ui = Ui_WorkerInformation()
        self.ui.setupUi(self)
        self.departments = {}
        self.id = 0

        self.ui.ok.clicked.connect(self.ok_clk)
        self.ui.save_changes.clicked.connect(self.save_clk)

        self.valid_err_window = ValidErrWindow()

    def hideEvent(self, a0):
        self.ui.department_number.currentTextChanged.disconnect()

    def ok_clk(self):
        self.hide()

    def dele_clk(self):
        pass

    def save_clk(self):
        new_data = {}
        new_data["name"] = " ".join([self.ui.surename.text(), self.ui.name.text(), self.ui.father_name.text()]).strip()
        new_data["adress"] = self.ui.adress.text()
        new_data["phone_number"] = self.ui.phone.text()

        try:
            new_data["passport_series"] = int(self.ui.passport_series.text())
            new_data["passport_number"] = int(self.ui.passport_number.text())
            new_data["department_id"] = int(self.ui.department_number.currentText())
        except:
            self.valid_err_window.show()
            return

        response = requests.put(apiurl + f"worker/{self.id}", json=new_data)

        if response.status_code == 200:
            self.hide()
        else:
            self.valid_err_window.show()
            return

    def dep_num_chg(self):
        self.ui.department_name.setText(self.departments[self.ui.department_number.currentText()]["name"])
        self.ui.department_adress.setText(self.departments[self.ui.department_number.currentText()]["adress"])

    def set_data(self, data: requests.Response):
        data = data.json()[0]
        self.departments = self.get_departments()
        self.id = data["id"]

        fio = data["name"].split()
        if len(fio) < 2:
            fio.append("")
            fio.append("")
        elif len(fio) < 3:
            fio.append("")

        self.ui.surename.setText(str(fio[0]))
        self.ui.name.setText(str(fio[1]))
        self.ui.father_name.setText(str(fio[2]))
        self.ui.adress.setText(data["adress"])
        self.ui.passport_series.setText(str(data["passport_series"]))
        self.ui.passport_number.setText(str(data["passport_number"]))
        self.ui.phone.setText(data["phone_number"][4:])
        self.ui.department_number.setCurrentText(str(data["department_id"]))
        self.ui.department_name.setText(self.departments[self.ui.department_number.currentText()]["name"])
        self.ui.department_adress.setText(self.departments[self.ui.department_number.currentText()]["adress"])

        self.ui.department_number.currentTextChanged.connect(self.dep_num_chg)

    def get_departments(self):
        response = requests.get(apiurl + "departments/all")
        if response.status_code != 200 or response.json() == []:
            return {"0": {"name": "0", "adress": "0"}}

        new_dep = {}
        self.ui.department_number.clear()
        for resp in response.json():
            self.ui.department_number.addItem(str(resp["id"]))
            new_dep[str(resp["id"])] = {"adress": resp["adress"], "name": resp["name"]}
        return new_dep


class NewDepWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(NewDepWindow, self).__init__()
        self.ui = Ui_NewDepartment()
        self.ui.setupUi(self)


class TurniketWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(TurniketWindow, self).__init__()
        self.ui = Ui_RFID()
        self.ui.setupUi(self)


class ValidErrWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ValidErrWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.ok_btn.clicked.connect(self.ok_clk)

    def ok_clk(self):
        self.hide()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())