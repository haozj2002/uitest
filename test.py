import sys     # 导入sys模块，用于退出程序时指定退出码
from PySide2.QtWidgets import QApplication  # 导入Qt应用程序类，每个Qt程序必须有一个实例
from ui.jiemian1 import MyDialog               # 导入自定义的登录对话框类
from ui.jiemian2 import MyForm                 # 导入自定义的主窗口类

def main():                                 # 主函数，封装程序入口逻辑
    app = QApplication(sys.argv)            # 创建Qt应用程序实例，接收命令行参数

    entry = MyDialog()                      # 创建登录对话框实例
    result = entry.exec_()                  # 模态运行对话框，阻塞等待用户操作，返回结果码

    if result != MyDialog.Accepted:         # 如果用户没有点击"确定"（即取消或关闭）
        sys.exit(1)                         # 以退出码1退出程序，表示非正常退出

    main_window = MyForm()                  # 用户确认后，创建主窗口实例
    main_window.show()                      # 显示主窗口（默认是隐藏的）

    sys.exit(app.exec_())                   # 进入Qt事件循环，程序等待用户交互，退出时传递退出码

if __name__ == '__main__':                  # 判断是否以主程序运行（而非被导入）
    main()                                  # 调用主函数，启动程序

