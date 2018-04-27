import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import design  # Это наш конвертированный файл дизайна
import os
import random
import cv2
import numpy as np


options = {'sr': '', 'ds': '', 'img': None, 'i': 0}

class ImagerSortApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.source.clicked.connect(self.source_browse)
        self.destination.clicked.connect(self.destination_browse)
        self.img_parts = None
        self.s_path = ''
        self.d_path = ''
        self.im_index = 0
        self.im_name = ''

    def source_browse(self):
        sr_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if sr_directory:
            self.s_path = sr_directory
            self.count.setText(str(len(os.listdir(sr_directory))))
            self.load_image()

    def destination_browse(self):
        ds_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if ds_directory:
            self.d_path = ds_directory

    def load_image(self):
        if self.im_index > 3 or not self.img_parts:
            img = random.choice(os.listdir(self.s_path))
            self.im_name = img
            im = cv2.resize(cv2.imread(self.s_path + '/' + img), (224, 224))
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            (h, w) = im.shape[:2]
            centr = (w / 3, h / 2)
            M = cv2.getRotationMatrix2D(centr, -15, 1.3)
            im = cv2.warpAffine(im, M, (w, h))
            im = im[0:h, 30:190]
            self.img_parts = np.zeros((224*4, 224), np.uint8)
            for x in range(0, 4):
                y1, y2, x1, x2 = self.img_section(x)
                self.img_parts[x*224:x*224 + 224, 0:224] = cv2.resize(im[y1:y2, x1:x2], (224, 224))
        self.im_show()

    def im_show(self):
        im = self.img_parts[self.im_index * 224:self.im_index * 224 + 224, 0:224]
        im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
        h, w, ch = im.shape
        bpl = 3 * w
        qim = QImage(im, w, h, bpl, QImage.Format_RGB888)
        pixmap = QPixmap(qim)
        self.img.setPixmap(pixmap)
        self.im_index = self.im_index + 1

    def img_section(self, index):
        if index == 0:
            # |x| |
            # | | |
            return 0, 112, 0, 112
        elif index == 1:
            #| |x|
            #| | |
            return 0, 112, 112, 224
        elif index == 2:
            #| | |
            #|x| |
            return 112, 224, 0, 112
        else:
            #| | |
            #| |x|
            return 112, 224, 112, 224

    def img_empty(self):
        if not os.path.exists(self.d_path + '/0'):
            os.makedirs(self.d_path + '/0')

    def img_dust(self):
        if not os.path.exists(self.d_path + '/1'):
            os.makedirs(self.d_path + '/1')

    def img_broken(self):
        if not os.path.exists(self.d_path + '/2'):
            os.makedirs(self.d_path + '/2')

    def img_briket(self):
        if not os.path.exists(self.d_path + '/3'):
            os.makedirs(self.d_path + '/3')

    def img_write(self, path):
        i = self.im_index - 1
        cv2.imwrite(self.img_parts[i*224:i*224 + 224, 0:224], path)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ImagerSortApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()