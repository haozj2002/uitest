import sys                                 # 导入sys模块，用于获取命令行参数和退出程序
from datetime import datetime              # 导入datetime模块，用于获取当前时间

from .untitld import Ui_Form              # 从Qt Designer自动生成的UI模块中导入界面类
from PySide2.QtWidgets import QWidget, QApplication  # 导入PySide2的Qt组件：窗口、应用程序
import logger                              # 导入日志模块


class MyForm(QWidget):                  # 自定义窗口类，继承自QWidget（兼容Qt Designer设计的Form）
    def __init__(self, parent=None):    # 构造函数，parent参数指定父窗口，默认为None
        super().__init__(parent)        # 调用父类QWidget的构造函数，完成Qt底层初始化
        self.ui = Ui_Form()             # 创建Ui_Form实例，加载Qt Designer设计的界面
        self.ui.setupUi(self)           # 将设计的界面布局应用到当前窗口

        # 将日志模块绑定到界面底部的文本框，之后 logger.instance.log() 会自动显示到界面
        logger.instance.set_text_edit(self.ui.textEdit_3)

        # 连接所有控件的信号到日志记录
        self._connect_signals()

        logger.instance.info("主窗口已创建")  # 记录主窗口创建

    def _connect_signals(self):         # 连接界面控件信号到日志记录方法
        """将所有交互控件的信号连接到日志记录"""

        # 下拉框：选项改变时记录
        self.ui.comboBox.currentTextChanged.connect(
            lambda text: logger.instance.info(f"下拉框1 选择: {text}"))
        self.ui.comboBox_2.currentTextChanged.connect(
            lambda text: logger.instance.info(f"下拉框2 选择: {text}"))
        self.ui.comboBox_3.currentTextChanged.connect(
            lambda text: logger.instance.info(f"下拉框3 选择: {text}"))
        self.ui.comboBox_4.currentTextChanged.connect(
            lambda text: logger.instance.info(f"下拉框4 选择: {text}"))
        self.ui.comboBox_5.currentTextChanged.connect(
            lambda text: logger.instance.info(f"下拉框5 选择: {text}"))

        # 按钮：点击时记录
        self.ui.pushButton.clicked.connect(
            lambda: logger.instance.info("点击按钮: PushButton"))
        self.ui.pushButton_2.clicked.connect(
            lambda: logger.instance.info("点击按钮: PushButton_2"))
        self.ui.pushButton_3.clicked.connect(
            lambda: logger.instance.info("点击按钮: PushButton_3"))
        self.ui.pushButton_4.clicked.connect(
            lambda: logger.instance.info("点击按钮: PushButton_4"))
        self.ui.pushButton_5.clicked.connect(
            lambda: logger.instance.info("点击按钮: PushButton_5"))

        # 复选框：状态改变时记录
        self.ui.checkBox.stateChanged.connect(
            lambda s: logger.instance.info(f"复选框1: {'选中' if s else '取消'}"))
        self.ui.checkBox_2.stateChanged.connect(
            lambda s: logger.instance.info(f"复选框2: {'选中' if s else '取消'}"))
        self.ui.checkBox_3.stateChanged.connect(
            lambda s: logger.instance.info(f"复选框3: {'选中' if s else '取消'}"))
        self.ui.checkBox_4.stateChanged.connect(
            lambda s: logger.instance.info(f"复选框4: {'选中' if s else '取消'}"))
        self.ui.checkBox_5.stateChanged.connect(
            lambda s: logger.instance.info(f"复选框5: {'选中' if s else '取消'}"))
        self.ui.checkBox_6.stateChanged.connect(
            lambda s: logger.instance.info(f"复选框6: {'选中' if s else '取消'}"))
        self.ui.checkBox_7.stateChanged.connect(
            lambda s: logger.instance.info(f"复选框7: {'选中' if s else '取消'}"))
        self.ui.checkBox_8.stateChanged.connect(
            lambda s: logger.instance.info(f"复选框8: {'选中' if s else '取消'}"))

        # 文本框：内容改变时记录（截取前50字符防刷屏）
        # self.ui.textEdit.textChanged.connect(
        #     lambda: logger.instance.info(f"文本框1 内容变更: {self.ui.textEdit.toPlainText()[:50]}"))
        # self.ui.textEdit_2.textChanged.connect(
        #     lambda: logger.instance.info(f"文本框2 内容变更: {self.ui.textEdit_2.toPlainText()[:50]}"))

        # 单行输入框：按回车时记录
        self.ui.lineEdit.returnPressed.connect(
            lambda: logger.instance.info(f"输入框 输入: {self.ui.lineEdit.text()}"))

    def showEvent(self, event):         # 窗口显示事件，重写Qt内置方法
        """窗口显示时记录日志"""
        logger.instance.info("主窗口已显示")  # 记录主窗口显示
        super().showEvent(event)        # 调用父类的showEvent，确保Qt内部逻辑正常执行

    def closeEvent(self, event):        # 窗口关闭事件，重写Qt内置方法
        """窗口关闭时记录日志"""
        logger.instance.info("主窗口已关闭")  # 记录主窗口关闭
        super().closeEvent(event)       # 调用父类的closeEvent，确保Qt内部逻辑正常执行

if __name__ == '__main__':              # 判断是否以主程序运行（而非被导入）
    app = QApplication(sys.argv)        # 创建Qt应用程序实例，sys.argv传入命令行参数
    window = MyForm()                   # 创建主窗口实例
    window.show()                       # 显示窗口（默认新建窗口是隐藏的）
    sys.exit(app.exec_())               # app.exec进入Qt事件循环，程序等待用户操作，sys.exit退出时返回状态码
