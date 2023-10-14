import os
import sys
import pandas as pd
from PyQt5 import QtWidgets

class MainApplication(QtWidgets.QMainWindow, Ui_designX.Ui_MDFourier):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = False
        self.data = None
        self.times = []
        self.energies = []
        self.uploadbtn.clicked.connect(self.upload)
        self.showBtn.clicked.connect(self.goProcess)
        self.saveBtn.clicked.connect(self.saveData)
        self.extBtn.clicked.connect(self.exitMode)
        self.openCSVBtn.clicked.connect(self.fastCsv)
        self.miscBtn.clicked.connect(self.misc)
# -----------------------------------------------------------------------------------------------------------------------
    def browse(self):
            self.file = QtWidgets.QFileDialog.getOpenFileName()[0]
            self.lineEdit.setText(self.file)
    def fastCsv(self):
        self.graphicsView_fourier.clear()
        self.graphicsView_energy.clear()
        self.newTimes = []
        self.newEnergies = []
        self.srLabel.setText("----------------------------")
        self.mlLabel.setText("----------------------------")
        self.tsLabel.setText("----------------------------")
        self.csvfile = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[
            0]
        self.datLabel_2.setText(os.path.basename(self.csvfile))
# -----------------------------------------------------------------------------------------------------------------------

    def upload(self):
        try:
            self.newTimes = []
            self.newEnergies = []
            self.atoms = float(self.atomNumValue.value())
            self.df = pd.read_csv(self.csvfile)
            self.newTimes = self.df['TS']
            self.newEnergies = self.df['ENERGY']
            self.newTimes = np.array(Series.tolist(self.newTimes))*(10**(-15))
            self.newEnergies = np.array(Series.tolist(self.newEnergies))
            try:
                self.newEnergies = self.newEnergies / self.atoms * 0.0434
            except RuntimeWarning:
                pass
            self.cutTime = float(self.newTimes[1] - self.newTimes[0])
            self.sampleRate = float(round(float(1 / float(self.cutTime))))
            self.tsLabel.setText(str(self.cutTime) + " s")
            self.srLabel.setText(str(float(self.sampleRate)/(10**12))+" THz")
            self.mlLabel.setText(str(len(self.newTimes)))
            self.graphicsView_energy.setBackground('w')
            self.graphicsView_energy.setLabel('bottom', 'time', units='s')
            self.graphicsView_energy.setLabel('left', 'Energy', units='eV')
            self.graphicsView_energy.plot(
                self.newTimes, self.newEnergies, pen='b')
            self.directory = os.path.dirname(self.csvfile)
        except ValueError:
            pass
# ----------------------------------------------------------------------------------------------------------------------

    def goProcess(self):
        self.graphicsView_fourier.clear()
        self.xSamp = []
        self.ySamp = []
        self.xSamp = np.array(self.newTimes)
        self.ySamp = np.array(self.newEnergies)
        self.window = np.hanning(int(round(len(self.xSamp))))
        self.y_res = self.ySamp * self.window
        energies_fft = sp.fftpack.fft(np.array(self.y_res))
        self.energies_psd = np.abs(energies_fft)
        self.fftFreq = sp.fftpack.fftfreq(
            len(energies_fft), 1 / float(self.sampleRate))
        self.i = self.fftFreq > 0
        self.reverseCm = 1/((3*(10**10))/(self.fftFreq[self.i]))
        self.graphicsView_fourier.setBackground('w')
        self.graphicsView_fourier.setLabel('bottom', 'k', units='cm^-1')
        self.graphicsView_fourier.setLabel('left', 'Amplitude', units=None)
        if self.naturalBox.isChecked():
            self.graphicsView_fourier.plot(
                self.reverseCm, self.energies_psd[self.i], pen='r')
        if self.logBox.isChecked():
            self.graphicsView_fourier.plot(
                self.reverseCm, np.log10(self.energies_psd[self.i]), pen='b')
        if self.tenLogsBox.isChecked():
            self.graphicsView_fourier.plot(
                self.reverseCm, 10 * np.log10(self.energies_psd[self.i]), pen='r')
# ----------------------------------------------------------------------------------------------------------------------

    def misc(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory()
        print(self.directory)
 # ----------------------------------------------------------------------------------------------------------------------

    def saveData(self):
        df = pandas.DataFrame()
        df['f (cm-1)'] = self.reverseCm

        df['AmplitudePure'] = self.energies_psd[self.i]
        df['AmplitudeLog10'] = np.log10(self.energies_psd[self.i])
        df['Amplitude10Log10'] = 10 * np.log10(self.energies_psd[self.i])

        te = pandas.DataFrame()
        te['t (ps)'] = np.array(self.newTimes)*(10**12)
        te['E (meV)'] = np.array(self.newEnergies)*1000
        with pd.ExcelWriter(str(self.directory)+"/"+'result.xlsx') as writer:
            df.to_excel(writer, sheet_name='fft', index=None, index_label=None)
            te.to_excel(writer, sheet_name='energy',
                        index=None, index_label=None)
        self.graphicsView_fourier.clear()
        self.graphicsView_energy.clear()
        self.newTimes = []
        self.newEnergies = []
        self.srLabel.setText("----------------------------")
        self.mlLabel.setText("----------------------------")
        self.tsLabel.setText("----------------------------")
        self.directory = None
# ----------------------------------------------------------------------------------------------------------------------

    def exitMode(self):
        exit()
# ----------------------------------------------------------------------------------------------------------------------


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()