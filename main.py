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
        self.pb0.clicked.connect(self.img_empty)
        self.pb1.clicked.connect(self.img_lowmaterial)
        self.pb2.clicked.connect(self.img_dust)
        self.pb3.clicked.connect(self.img_broken)
        self.pb4.clicked.connect(self.img_briket)
        self.img_parts = None
        self.s_path = ''
        self.d_path = ''
        self.im_index = -1
        self.im_name = ''
        self.dust_path = ''
        self.lowmat_path = ''
        self.empty_path = ''
        self.broken_path = ''
        self.briket_path = ''
        self.img_code = 0
        self.img_class = ''

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
            self.empty_path = ds_directory + '/0'
            self.lowmat_path = ds_directory + '/1'
            self.dust_path = ds_directory + '/2'
            self.broken_path = ds_directory + '/3'
            self.briket_path = ds_directory + '/4'
            if not os.path.exists(self.lowmat_path):
                os.makedirs(self.lowmat_path)
            if not os.path.exists(self.empty_path):
                os.makedirs(self.empty_path)
            if not os.path.exists(self.dust_path):
                os.makedirs(self.dust_path)
            if not os.path.exists(self.broken_path):
                os.makedirs(self.broken_path)
            if not os.path.exists(self.briket_path):
                os.makedirs(self.briket_path)

    def load_image(self):
        if self.im_index > 3 or self.im_index == -1:
            self.im_index = 0
            img = random.choice(os.listdir(self.s_path))
            self.count.setText(str(len(os.listdir(self.s_path))))
            self.im_name = img
            self.img_code = random.randint(0, 20000)
            imp = self.s_path.split('/')
            self.img_class = imp[len(imp) - 1]
            im = cv2.resize(cv2.imread(self.s_path + '/' + img), (224, 224))
            self.im_show_preview(im)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            (h, w) = im.shape[:2]
            centr = (w / 3, h / 2)
            M = cv2.getRotationMatrix2D(centr, -15, 1.3)
            im = cv2.warpAffine(im, M, (w, h))
            im = im[0:h, 30:190]
            self.img_parts = np.zeros((224 * 4, 224), np.uint8)
            for x in range(0, 4):
                y1, y2, x1, x2 = self.img_section(x)
                self.img_parts[x * 224:x * 224 + 224, 0:224] = cv2.resize(im[y1:y2, x1:x2], (224, 224))
            os.remove(self.s_path + '/' + self.im_name)
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

    def im_show_preview(self, im):
        h, w, ch = im.shape
        bpl = 3 * w
        qim = QImage(im, w, h, bpl, QImage.Format_RGB888)
        pixmap = QPixmap(qim)
        self.img_full.setPixmap(pixmap)

    def img_section(self, index):
        if index == 0:
            # |x| |
            # | | |
            return 0, 112, 0, 112
        elif index == 1:
            # | |x|
            # | | |
            return 0, 112, 112, 224
        elif index == 2:
            # | | |
            # |x| |
            return 112, 224, 0, 112
        else:
            # | | |
            # | |x|
            return 112, 224, 112, 224

    def img_empty(self):
        self.img_write(self.empty_path + '/' + self.gen_file_name(self.empty_path))

    def img_lowmaterial(self):
        self.img_write(self.lowmat_path + '/' + self.gen_file_name(self.lowmat_path))

    def img_dust(self):
        self.img_write(self.dust_path + '/' + self.gen_file_name(self.dust_path))

    def img_broken(self):
        self.img_write(self.broken_path + '/' + self.gen_file_name(self.broken_path))

    def img_briket(self):
        self.img_write(self.briket_path + '/' + self.gen_file_name(self.briket_path))

    def img_write(self, path):
        i = self.im_index - 1
        cv2.imwrite(path, self.img_parts[i * 224:i * 224 + 224, 0:224], [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        self.load_image()

    def gen_file_name(self, path):
        path = path.split('/')
        im_class = path[len(path) - 1]
        return self.img_class + '_IM-K2-UB_' + str(self.img_code) + '_' + \
               str(self.im_index - 1) + '_' + im_class + ".jpg"


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ImagerSortApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
