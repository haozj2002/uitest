"""
日志模块：将日志实时输出到控制台、文件、界面文本框
"""
from datetime import datetime


# 日志级别常量
INFO = "INFO"
WARNING = "WARNING"
ERROR = "ERROR"


class Logger:
    """日志记录器，支持控制台、文件、界面文本框三个输出目标"""

    def __init__(self, log_file="app.log"):
        self.log_file = log_file              # 日志文件路径
        self.text_edit = None                 # 界面文本框引用（后续通过 set_text_edit 绑定）

    def log(self, msg, level=INFO):
        """记录一条日志，同时输出到控制台、文件、界面文本框"""
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name = 'main'
        line = f"[{time_str}] {name} [{level}] {msg}"

        # 1. 输出到控制台（带颜色）
        color_map = {INFO: "\033[97m", WARNING: "\033[93m", ERROR: "\033[91m"}
        color = color_map.get(level, "\033[97m")
        print(f"{color}{line}\033[0m")

        # 2. 写入日志文件（追加模式）
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(line + "\n")

        # 3. 输出到界面文本框（如果已绑定）
        if self.text_edit is not None:
            time_short = datetime.now().strftime("%H:%M:%S")
            name = 'main'
            self.text_edit.append(f"[{time_short}] {name} [{level}] {msg}")

    def set_text_edit(self, text_edit):
        """绑定界面文本框，绑定后 log() 会自动显示到界面"""
        self.text_edit = text_edit

    def info(self, msg):
        """快捷记录 INFO 级别日志"""
        self.log(msg, INFO)

    def warning(self, msg):
        """快捷记录 WARNING 级别日志"""
        self.log(msg, WARNING)

    def error(self, msg):
        """快捷记录 ERROR 级别日志"""
        self.log(msg, ERROR)


# 全局单例，任意文件中 import logger; logger.instance.info() 即可使用
instance = Logger()
