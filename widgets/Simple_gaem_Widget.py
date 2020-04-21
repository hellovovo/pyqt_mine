from PyQt5 import QtGui
from PyQt5.QtCore import QEvent, QRect
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont, QMouseEvent, QBitmap, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QStyleOption, QStyle, QDialog, QMessageBox

import random

from wx._core import MouseButton


class SimpleWidget(QWidget):
    def __init__(self, parent):
        super(SimpleWidget, self).__init__(parent=parent)
        self.mine = set()
        self.tags = set()
        self.safe_pos = {}
        self.failed = False
        self.checked = set()
        self.wintag = False
        self.game_safe_pos = set()
        self.flag = None
        # self.lei=  None

        self.init_data()

    def init_data(self):
        self.flag = QImage('../imgs/img_flag.jpg')
        # self.flag = self.flag.scaledToHeight(50)
        self.lei = QImage('../imgs/lei.jpg')
        # self.lei = self.lei.scaledToHeight(50)

        self.mine = set()
        self.tags = set()
        self.safe_pos = {}
        self.failed = False
        self.wintag = False
        self.checked = set()
        self.game_safe_pos = set([(i, j) for j in range(9) for i in range(9)])
        #     9*9 格子 10个雷
        li = list(range(81))
        for i in range(10):
            idx = random.randint(0, 80 - i)
            tmp = li[idx]
            li[idx] = li[80 - i]
            li[80 - i] = tmp

        random_li = li[71:].copy()
        for num in random_li:
            r, c = divmod(num, 9)
            self.mine.add((r, c))
            self.game_safe_pos.remove((r, c))
        self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, QPainter(self), self)

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        # p.setPen(QColor(0,0,0))
        # p.setPen(QPen())
        for i in range(11):
            p.drawLine(10 + i * 20, 10, 10 + i * 20, 190)
        for i in range(11):
            p.drawLine(10, 10 + i * 20, 190, 10 + i * 20)
        print('paintEvent')

        p.setPen(QColor(100, 10, 255))
        p.setBrush(QBrush(QColor(212, 100, 123)))
        # for item in self.clicked_pos:
        #     p.drawEllipse(item[0]*20+12,item[1]*20+12,16,16)
        if self.failed:
            for item in self.mine:
                p.drawEllipse(item[0] * 20 + 12, item[1] * 20 + 12, 16, 16)

        for pos in self.tags:
            # p.setBrush(QBrush(QColor(230, 70, 70)))
            # p.drawRect(15 + pos[0] * 20, 15 + pos[1] * 20, 10, 10)
            # p.drawImage(0,0,self.flag,0,0,20,20)
            p.drawImage(QRect(pos[0],pos[1],400,400),self.lei)

        for pos in self.safe_pos.keys():
            p.setPen(QColor(150, 150, 150))
            p.setBrush(QBrush(QColor(150, 150, 150)))
            p.drawRect(10 + pos[0] * 20, 10 + pos[1] * 20, 20, 20)
            if self.safe_pos[pos] != 0:
                p.setPen(QColor(100, 230, 120))
                p.setFont(QFont('宋体', 18, 18))
                p.drawText(10 + pos[0] * 20, 10 + pos[1] * 20 + 20, str(self.safe_pos[pos]))
        p.drawImage(0,0,self.lei,0,0,100,100)
        p.end()

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.failed or self.wintag:
            return
        x, y = a0.x() - 10, a0.y() - 10
        posX, posY = x // 20, y // 20
        pos = (posX, posY)
        print(a0.button())
        print(a0.type())
        if a0.button() == 1:
            self.processPos(pos)
        else:
            if pos in self.tags:
                self.tags.remove(pos)
            else:
                self.tags.add(pos)
        self.update()
        if self.wintag:
            QMessageBox.information(self, '胜利', '您赢了，好厉害哟！', QMessageBox.Ok)

    def processPos(self, pos):
        if pos in self.mine:
            self.failed = True
            self.update()
            QMessageBox.information(self, '游戏结束', '您挂了，请再接再厉', QMessageBox.Ok)
            return
        self.check(pos)

    def check(self, pos):
        x, y = pos
        cnt = 0
        for i in range(-1, 2):
            ix = x + i
            for j in range(-1, 2):
                iy = j + y
                if ix == x and iy == y:
                    continue
                if (ix, iy) in self.mine:
                    cnt += 1
        self.checked.add(pos)
        if pos in self.game_safe_pos:
            self.game_safe_pos.remove(pos)
            if len(self.game_safe_pos) == 0:
                self.wintag = True
        self.safe_pos[pos] = cnt
        if cnt == 0:
            x, y = pos
            for i in range(-1, 2):
                ix = x + i
                for j in range(-1, 2):
                    iy = j + y
                    if ix == x and iy == y:
                        continue
                    if (ix, iy) in self.checked:
                        continue
                    if ix < 0 or iy < 0 or ix > 8 or iy > 8:
                        continue
                    if (ix, iy) in self.mine:
                        cnt += 1
                    self.check((ix, iy))
