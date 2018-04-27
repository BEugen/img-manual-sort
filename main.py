import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import design  # Это наш конвертированный файл дизайна
import os
import random
import cv2


options = {'sr': '', 'ds': '', 'img': '', 'l': 0, 't': 0}


class ImagerSortApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.source.clicked.connect(self.source_browse)
        self.destination.clicked.connect(self.destination_browse)

    def source_browse(self):
        sr_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if sr_directory:
            options['sr'] = sr_directory
            self.count.setText(str(len(os.listdir(sr_directory))))
            self.load_image()

    def destination_browse(self):
        ds_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if ds_directory:
            options['ds'] = ds_directory

    def load_image(self):
        if options['l'] == 2 and options['t'] == 2:
            img = random.choice(os.listdir(options['sr']))
            options['img'] = img
            pixmap = QPixmap(options['sr'] + '/' + img)
            self.img.setPixmap(pixmap)
        else:
            pass

    def img_empty(self):
        pass

    def img_dust(self):
        pass

    def img_broken(self):
        pass

    def img_briket(self):
        pass



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ImagerSortApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()