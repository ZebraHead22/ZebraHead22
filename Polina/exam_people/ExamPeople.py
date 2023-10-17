import os
import sys
import pandas as pd
import Ui_infogypsies_time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class MainApplication(QtWidgets.QMainWindow, Ui_infogypsies_time.Ui_ExamPeople):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.data = None
        self.browse_btn.clicked.connect(self.browse)
        self.process_btn.clicked.connect(self.process)
        self.export_btn.clicked.connect(self.export)
        self.exit_btn.clicked.connect(self.exit)
        self.const_time.setChecked(True) 

    def browse(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.lineEdit.setText(self.file)
        self.filename, self.file_extension = os.path.splitext(self.file)

    def process(self):
        self.df = pd.DataFrame()
        if self.file_extension == '.csv':
            self.df = pd.read_csv(self.file, delimiter=',', index_col=None)
            self.df['Время на занятии'] = (pd.to_datetime(self.df['Время выхода'], format='%d.%m.%Y %H:%M:%S')
                                    - pd.to_datetime(self.df['Время входа'], format='%d.%m.%Y %H:%M:%S'))
        elif self.file_extension == '.xlsx':
            self.df1 = pd.read_excel(self.file, index_col=None)
            self.df = self.df1.iloc[:, 0].str.split(',', expand=True)
            self.df.columns = [n.replace('"', '') for n in self.df1.columns.str.split(',')[0]]
            self.df['Время на занятии'] = (pd.to_datetime(self.df['Время выхода'], format='%d.%m.%Y %H:%M:%S %p')
                                    - pd.to_datetime(self.df['Время входа'], format='%d.%m.%Y %H:%M:%S %p'))

        self.df = self.df.rename(columns={'Имя (настоящее имя)': 'Name'})
        self.df = self.df.set_index('Name')
        self.df = self.df.sort_index()
        self.df = self.df.reset_index()
        names = self.df['Name'].to_list()
        #Если человек заходит с разных устройств
        def rename(lst):
            for i in range(len(lst)-1):
                if lst[i] != 'iPhone':
                    if str(lst[i+1]).count(lst[i]) >= 1:
                        lst[i+1] = lst[i]
            return lst
        rename(names)
        
        self.df['Name'] = names
        self.df = self.df.set_index('Name')
        self.df = self.df.groupby(level='Name').sum(numeric_only=False)
        self.df = self.df.reset_index()
        self.df['Минуты присутствия'] = self.df['Время на занятии'].dt.total_seconds().div(
            60).astype(int)
        #Время занятия и минимальное время присутствия для зачета
        if self.const_time.isChecked():
            self.compare_time = 90
        else:
            self.compare_time = self.lesson_time.value() * (self.persent.value() * 0.01)
        #Делаем сравнение
        def normalise_row(row):
            if row['Минуты присутствия'] >= self.compare_time:
                result = 'Зачет'
            else:
                result = 'Не зачет'
            return result
        self.df['Оценка присутствия'] = self.df.apply(
            lambda row: normalise_row(row), axis=1)
        #Удаляем лишние столбцы
        self.df = self.df.drop(['Электронная почта пользователя', 'Время входа', 'Время выхода', 'Продолжительность (минуты)',
                      'Гость', 'Согласие на запись', 'В зале ожидания', 'Время на занятии'], axis=1)
        #Настраиваем таблицу
        self.people_table.clear()
        self.people_table.setRowCount(0)
        headers = self.df.columns.values.tolist()
        self.people_table.setColumnCount(len(headers))
        self.people_table.setHorizontalHeaderLabels(headers)
        header = self.people_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        #Заполняем таблицу
        for i, row in self.df.iterrows():
            self.people_table.setRowCount(self.people_table.rowCount() + 1)
            for j in range(self.people_table.columnCount()):
                self.people_table.setItem(i, j, QTableWidgetItem(str(row[j])))
        self.people_table.show()

    def export(self):
        with pd.ExcelWriter(self.filename + '_result.xlsx') as writer:
            self.df.to_excel(writer, sheet_name='Lesson',
                        index=None, index_label=None)

    def exit(self):
        exit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
