import sys                                 # 导入sys模块，用于退出程序时指定退出码
from .untitled2 import Ui_Dialog           # 从Qt Designer自动生成的UI模块中导入对话框界面类
from PySide2.QtWidgets import QApplication, QDialog, QMessageBox  # 导入Qt应用程序类、对话框基类、消息框

class MyDialog(QDialog):                   # 自定义对话框类，继承自QDialog（Qt的对话框基类）
    def __init__(self, parent=None):       # 构造函数，parent参数指定父窗口，默认为None
        super(MyDialog, self).__init__(parent)  # 调用父类QDialog的构造函数，完成Qt底层初始化
        self.ui = Ui_Dialog()              # 创建Ui_Dialog实例，加载Qt Designer设计的对话框界面
        self.ui.setupUi(self)              # 将设计的界面布局应用到当前对话框

        # 连接按钮信号："确定"→先校验再关闭，"取消"→直接关闭
        self.ui.pushButton.clicked.connect(self._on_accept)  # 将"确定"按钮的点击信号连接到自定义校验方法
        self.ui.pushButton_2.clicked.connect(self.reject)    # 将"取消"按钮的点击信号连接到QDialog内置的reject()方法

    def _on_accept(self):                  # 自定义的"确定"处理函数，在校验通过后才关闭对话框
        """校验用户是否做了选择，未选择时弹出警告并阻止关闭"""
        # 检查两个单选按钮是否都未被选中，isChecked()返回True(选中)或False(未选中)
        if not self.ui.radioButton.isChecked() and not self.ui.radioButton_2.isChecked():
            QMessageBox.warning(self, "提示", "请先选择一个选项！")  # 弹出警告对话框，标题为"提示"，内容为"请先选择一个选项！"
            return                         # 提前返回，不执行后面的accept()，对话框保持打开状态
        self.accept()                      # 校验通过，调用QDialog内置的accept()方法关闭对话框并返回Accepted结果码

if __name__ == '__main__':                 # 判断是否以主程序运行（而非被导入）
    app = QApplication(sys.argv)           # 创建Qt应用程序实例，sys.argv传入命令行参数
    dialog = MyDialog()                    # 创建自定义对话框实例
    dialog.show()                          # 显示对话框（默认新建窗口是隐藏的）
    sys.exit(app.exec_())                  # app.exec_()进入Qt事件循环，等待用户操作；sys.exit()退出程序并返回状态码