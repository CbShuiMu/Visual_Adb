import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建 TableWidget
        self.table_widget = QTableWidget(self)
        self.setCentralWidget(self.table_widget)

        # 设置表格的行数和列数
        self.table_widget.setRowCount(4)  # 设置表格有4行
        self.table_widget.setColumnCount(2)  # 设置表格有2列

        # 添加按钮控件到每个单元格
        for row in range(self.table_widget.rowCount()):  # 遍历每一行
            for col in range(self.table_widget.columnCount()):  # 遍历每一列
                # 创建按钮控件，设置文本并连接槽函数
                button = QPushButton("按钮", self.table_widget)
                button.clicked.connect(self.button_clicked)  # 按钮点击事件处理函数
                # 将按钮控件添加到单元格中
                self.table_widget.setCellWidget(row, col, button)

                # 设置单元格的其他内容
                # item = QTableWidgetItem(f"行{row + 1}, 列{col + 1}")  # 创建一个表格项，并设置文本
                # self.table_widget.setItem(row, col, item)  # 将表格项添加到单元格中

    def button_clicked(self):
        # 按钮点击事件处理函数
        button = self.sender()  # 获取发送信号的按钮
        cell_widget = self.table_widget.indexAt(button.pos())  # 获取按钮所在的单元格
        row = cell_widget.row()  # 获取单元格的行号
        col = cell_widget.column()  # 获取单元格的列号
        print(f"按钮位于第 {row + 1} 行，第 {col + 1} 列被点击")  # 打印按钮被点击的位置信息


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
