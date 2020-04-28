from PyQt5 import QtGui
from PyQt5.QtCore import QEvent, QRect, QTimer
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont, QMouseEvent, QBitmap, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QStyleOption, QStyle, QDialog, QMessageBox

import random

color = {1: QColor(20, 50, 255), 2: QColor(20, 232, 25), 3: QColor(252, 200, 10), 4: QColor(255, 100, 15),
         5: QColor(200, 20, 25), 6: QColor(220, 30, 5), 7: QColor(230, 30, 0), 8: QColor(255, 0, 0)}


class SimpleWidget(QWidget):
    def __init__(self, parent, *args):
        super(SimpleWidget, self).__init__(parent=parent)
        self.mine = set()
        self.tags = set()
        self.safe_pos = {}
        self.failed = False
        self.checked = set()
        self.wintag = False
        self.game_safe_pos = set()
        self.flag = None
        self.lab_time = None
        self.lab_cnt = None
        self.time_cnt = 0
        self.start_tag = False

        self.row = args[0]['row']
        self.col = args[0]['col']
        self.mine_cnt = args[0]['mine']

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.init_data()

    def bind_view(self, lab_time, lab_cnt):
        self.lab_time = lab_time
        self.lab_cnt = lab_cnt
        self.update_cnt()

    def update_cnt(self):
        if not self.lab_cnt:
            return
        cnt = self.mine_cnt - len(self.tags)
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

        self.lei = QImage('imgs/lei.jpg')

        self.mine.clear()
        self.tags.clear()
        self.safe_pos.clear()
        self.start_tag = False
        self.time_cnt = 0

        self.failed = False
        self.wintag = False
        self.checked = set()
        self.game_safe_pos = set([(i, j) for j in range(self.row) for i in range(self.col)])

        rc = self.row * self.col
        li = list(range(rc))
        for i in range(self.mine_cnt):
            idx = random.randint(0, rc - 1 - i)
            tmp = li[idx]
            li[idx] = li[rc - 1 - i]
            li[rc - 1 - i] = tmp

        random_li = li[rc - self.mine_cnt:].copy()
        for num in random_li:
            r, c = divmod(num, self.row)
            self.mine.add((r, c))
            self.game_safe_pos.remove((r, c))
        self.update_cnt()
        self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, QPainter(self), self)

        width, height = self.width() - 4, self.height() - 4
        cell_row, cell_col = width // self.col, height // self.row
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        line_height = cell_row * self.col
        line_width = cell_col * self.row
        for i in range(self.row + 1):
            p.drawLine(2 + i * cell_row, 2, 2 + i * cell_row, line_height)
        for i in range(self.col + 1):
            p.drawLine(2, 2 + i * cell_col, line_width, 2 + i * cell_col)
        # print('paintEvent')

        p.setPen(QColor(100, 10, 255))
        p.setBrush(QBrush(QColor(212, 100, 123)))
        # for item in self.clicked_pos:
        #     p.drawEllipse(item[0]*20+12,item[1]*20+12,16,16)

        for pos in self.tags:
            p.drawImage(3 + pos[0] * cell_row, 3 + pos[1] * cell_col, self.flag, 0, 0, cell_row - 2, cell_col - 2)

        for pos in self.safe_pos.keys():
            p.setPen(QColor(150, 150, 150))
            p.setBrush(QBrush(QColor(150, 150, 150)))
            p.drawRect(3 + pos[0] * cell_row, 3 + pos[1] * cell_col, cell_row - 2, cell_col - 2)
            if self.safe_pos[pos] != 0:
                p.setPen(color[self.safe_pos[pos]])
                p.setFont(QFont('宋体', cell_row - 2, cell_row - 2))
                p.drawText(3 + pos[0] * cell_row, cell_row - 5 + pos[1] * cell_col, str(self.safe_pos[pos]))

        if self.failed:
            for item in self.mine:
                # p.drawEllipse(item[0] * 20 + 12, item[1] * 20 + 12, 16, 16)
                p.drawImage(3 + item[0] * cell_row, 3 + item[1] * cell_col, self.lei, 0, 0, cell_row - 2, cell_col - 2)

    # 处理双击事件
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.failed or self.wintag:
            return
        pos = self.getPos(a0)
        if not pos:
            return
        if pos not in self.safe_pos:
            self.processPos(pos)
            return
        self.inferPos(pos)
        if self.wintag:
            QMessageBox.information(self, '胜利', '您赢了，好厉害哟！', QMessageBox.Ok)

    def inferPos(self,pos):
        x,y = pos
        cnt =  0
        checkPoses = []
        for i in range(-1, 2):
            ix = x + i
            for j in range(-1, 2):
                iy = j + y
                if ix == x and iy == y:
                    continue
                if (ix, iy) in self.tags:
                    cnt += 1
                else:
                    checkPoses.append((ix,iy))
        if self.safe_pos[pos] == cnt:
            for checkPos in checkPoses:
                self.processPos(checkPos)




    def getPos(self,a0):
        x, y = a0.x(), a0.y()

        width, height = self.width() - 4, self.height() - 4
        cell_row, cell_col = width // self.col, height // self.row

        self.flag = self.flag.scaledToHeight(cell_row)
        self.lei = self.lei.scaledToHeight(cell_col)
        posX, posY = x // cell_col, y // cell_row
        if posY >= self.row or posX >= self.col:
            return
        pos = (posX, posY)
        return pos

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.failed or self.wintag:
            return

        pos = self.getPos(a0)
        if not pos:
            return
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

        if pos[0] >= self.row or pos[1] >= self.col:
            return
        if pos in self.mine:
            self.failed = True
            self.update()
            QMessageBox.information(self, '游戏结束', '您挂了，请再接再厉', QMessageBox.Ok)
            return
        self.check(pos)

    def check(self, pos):
        x, y = pos
        if x >= self.row or y >= self.col:
            return
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
                    if ix < 0 or iy < 0 or ix > self.row or iy > self.col:
                        continue
                    if (ix, iy) in self.mine:
                        cnt += 1
                    self.check((ix, iy))
