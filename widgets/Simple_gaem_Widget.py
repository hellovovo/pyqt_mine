from PyQt5 import QtGui
from PyQt5.QtCore import QEvent, QRect, QTimer
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
        self.lab_time = None
        self.lab_cnt = None
        self.time_cnt = 0
        self.start_tag = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.init_data()


    def bind_view(self,lab_time,lab_cnt):
        self.lab_time = lab_time
        self.lab_cnt = lab_cnt

    def update_cnt(self):
        if not self.lab_cnt:
            return
        cnt = 10 - len(self.tags)
        self.lab_cnt.setText(str(cnt))

    def update_time(self):
        if self.failed or self.wintag:
            return
        if not self.lab_time:
            return
        if not self.start_tag:
            return
        self.lab_time.setText(str(self.time_cnt))
        self.time_cnt += 1


    def init_data(self):
        self.flag = QImage('imgs/img_flag.jpg')
        self.flag = self.flag.scaledToWidth(18)
        self.lei = QImage('imgs/lei.jpg')
        self.lei = self.lei.scaledToWidth(18)

        self.mine.clear()
        self.tags.clear()
        self.safe_pos.clear()
        self.start_tag = False
        self.time_cnt = 0

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
        self.update_cnt()
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


        for pos in self.tags:
            p.drawImage(11+pos[0]*20,11+pos[1]*20,self.flag,0,0,18,18)

        for pos in self.safe_pos.keys():
            p.setPen(QColor(150, 150, 150))
            p.setBrush(QBrush(QColor(150, 150, 150)))
            p.drawRect(11 + pos[0] * 20, 11 + pos[1] * 20, 18, 18)
            if self.safe_pos[pos] != 0:
                p.setPen(QColor(15, 230, 60))
                p.setFont(QFont('宋体', 18, 18))
                p.drawText(10 + pos[0] * 20, 10 + pos[1] * 20 + 20, str(self.safe_pos[pos]))

        if self.failed:
            for item in self.mine:
                # p.drawEllipse(item[0] * 20 + 12, item[1] * 20 + 12, 16, 16)
                p.drawImage(11 + item[0] * 20, 11 + item[1] * 20, self.lei, 0, 0, 18, 18)

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
            self.start_tag = True
        else:
            if pos in self.tags:
                self.tags.remove(pos)
            else:
                if pos not in self.safe_pos:
                    self.tags.add(pos)
            self.update_cnt()
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
