import sys                                 # 导入sys模块，用于获取命令行参数和退出程序

from .untitld import Ui_Form            # 从Qt Designer自动生成的UI模块中导入界面类
from PySide2.QtWidgets import QWidget, QApplication  # 导入PySide2的Qt组件：窗口、应用程序


class MyForm(QWidget):                  # 自定义窗口类，继承自QWidget（兼容Qt Designer设计的Form）
    def __init__(self,parent=None):     # 构造函数，parent参数指定父窗口，默认为None
        super().__init__(parent)        # 调用父类QWidget的构造函数，完成Qt底层初始化
        self.ui = Ui_Form()             # 创建Ui_Form实例，加载Qt Designer设计的界面
        self.ui.setupUi(self)           # 将设计的界面布局应用到当前窗口

if __name__ == '__main__':              # 判断是否以主程序运行（而非被导入）
    app = QApplication(sys.argv)        # 创建Qt应用程序实例，sys.argv传入命令行参数
    window = MyForm()                   # 创建主窗口实例
    window.show()                       # 显示窗口（默认新建窗口是隐藏的）
    sys.exit(app.exec_())              # app.exec进入Qt事件循环，程序等待用户操作，sys.exit退出时返回状态码


