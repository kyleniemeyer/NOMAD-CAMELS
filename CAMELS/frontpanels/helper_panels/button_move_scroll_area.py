from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QScrollArea, QMainWindow
from PyQt5.QtGui import QDrag
from PyQt5.QtCore import Qt, QMimeData

class DragButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            mimeData = QMimeData()
            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.exec_(Qt.MoveAction)

class BidirectionalDict:
    def __init__(self):
        self._forward = {}
        self._reverse = {}

    def __getitem__(self, key):
        return self._forward[key]

    def __setitem__(self, key, value):
        self._forward[key] = value
        self._reverse[value] = key

    def __delitem__(self, key):
        value = self._forward.pop(key)
        del self._reverse[value]

    def __len__(self):
        return len(self._forward)

    def __iter__(self):
        return iter(self._forward)

    def items(self):
        return self._forward.items()

    def keys(self):
        return self._forward.keys()

    def values(self):
        return self._forward.values()

    def get_key(self, value):
        return self._reverse[value]

    def get_value(self, key):
        return self._forward[key]

    def __repr__(self):
        return f"BidirectionalDict({self._forward})"




class DropArea(QWidget):
    def __init__(self, button_wdith:int):
        super().__init__()
        # self.initUI()
        self.buttons = BidirectionalDict()
        self.button_order = []
        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.setAcceptDrops(True)
        self.columnCount = 0
        self.rowCount = 0

        self.min_column_width = button_wdith + 1


    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        event.setDropAction(Qt.MoveAction)
        event.accept()

        source_widget = event.source()

        drag_pos = self.buttons.get_key(source_widget)
        drop_row, drop_col = self.get_drop_position(event.pos())
        if drop_row * self.columnCount + drop_col >= len(self.buttons):
            drop_col = int(len(self.buttons) - drop_row * self.columnCount - 1)
        child_at = self.layout().itemAtPosition(drop_row, drop_col).widget()
        drop_pos = self.buttons.get_key(child_at)

        adding = 0
        if self.button_order.index(drag_pos) < self.button_order.index(drop_pos):
            adding = 1
        self.button_order.remove(drag_pos)
        insert_pos = self.button_order.index(drop_pos)
        self.button_order.insert(insert_pos + adding, drag_pos)
        self.updateLayout()
        return

    def get_drop_position(self, pos):
        rect = self.rect()
        center = rect.center()
        width = self.width()
        height = self.height()
        x_dist = (pos - center).x() + width/2
        y_dist = (pos - center).y() + height/2
        column_width = width / self.columnCount
        row_height = height / self.rowCount
        return int(y_dist // row_height), int(x_dist // column_width)



    def updateLayout(self):
        width = self.width()

        # calculate number of columns based on current width
        columns = max(1, width // self.min_column_width)

        # calculate new positions of buttons based on columns
        positions = [(i // columns, i % columns) for i in range(len(self.buttons))]
        self.columnCount = columns
        self.rowCount = len(positions) // columns + (1 if len(positions) % columns else 0)
        for button, position in zip(self.button_order, positions):
            self.layout().addWidget(self.buttons[button], *position)


class Drop_Scroll_Area(QScrollArea):
    def __init__(self, button_width=100, button_height=100, parent=None):
        super().__init__(parent=parent)
        self.drop_area = DropArea(button_width)
        self.setWidget(self.drop_area)
        self.setWidgetResizable(True)
        self.drop_area.updateLayout()
        self.button_width = button_width
        self.button_height = button_height

    def resizeEvent(self, a0):
        super().resizeEvent(a0)
        self.drop_area.updateLayout()

    def updateLayout(self):
        self.drop_area.updateLayout()

    def add_button(self, button, name):
        button.setFixedSize(self.button_width, self.button_height)
        self.drop_area.buttons[name] = button
        self.drop_area.button_order.append(name)
        self.drop_area.updateLayout()

    def get_button_order(self):
        return self.drop_area.button_order



if __name__ == '__main__':
    app = QApplication([])
    main_window = QMainWindow()
    area = Drop_Scroll_Area()
    main_window.setCentralWidget(area)
    for i in range(15):
        area.add_button(DragButton(f'Button {i}'), str(i))
    main_window.show()
    app.exec_()