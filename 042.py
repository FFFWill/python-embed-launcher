import sys
import os
import subprocess
import ctypes
import platform
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QFrame, QTextEdit, QDesktopWidget,
                             QMenu, QAction, QAbstractItemView, QFileDialog, QTabWidget,
                             QTabBar, QTreeWidget, QTreeWidgetItem, QMessageBox,
                             QSplitter)
from PyQt5.QtCore import Qt, QPoint, QSize, QRect, QProcess, QEvent
from PyQt5.QtGui import (QColor, QFont, QPainter, QLinearGradient, QIcon, QTextCursor, QPixmap,
                         QPainterPath)


class AppStyles:
    """集中管理应用程序的所有样式和颜色"""

    # ===== 窗口样式 =====
    WINDOW_MIN_SIZE = (1000, 700)
    WINDOW_INIT_SIZE = (1000, 700)
    WINDOW_BG_GRADIENT = [
        QColor(0, 129, 129),  # 渐变起始颜色 (深青色)
        QColor(135, 206, 250)  # 渐变结束颜色 (天蓝色)
    ]
    WINDOW_CORNER_RADIUS = 0  # 窗口圆角半径

    # ===== 标题栏样式 =====
    TITLE_BAR_HEIGHT = 40
    TITLE_BAR_BG = "rgba(0, 211, 211, 0)"  # 标题栏背景
    TITLE_FONT = ("微软雅黑", 10, QFont.Bold)
    TITLE_COLOR = "#2C3E50"  # 标题文字颜色

    # ===== 按钮样式 =====
    BUTTON_SIZE = QSize(30, 30)
    BUTTON_RADIUS = 0  # 按钮圆角半径
    BUTTON_BG = "rgba(255, 255, 255, 0)"  # 按钮背景
    BUTTON_HOVER_BG = "rgba(255, 255, 255, 0.8)"  # 按钮悬停背景
    CLOSE_BUTTON_HOVER_BG = "#FF6B6B"  # 关闭按钮悬停背景
    CLOSE_BUTTON_HOVER_COLOR = "white"  # 关闭按钮悬停文字颜色
    RUN_BUTTON_COLOR = "#4CAF50"  # 运行按钮颜色
    RUN_BUTTON_HOVER = "#81C784"  # 运行按钮悬停颜色
    TERMINAL_BUTTON_COLOR = "#2196F3"  # 终端按钮颜色
    TERMINAL_BUTTON_HOVER = "#64B5F6"  # 终端按钮悬停颜色
    STOP_BUTTON_COLOR = "#FF5252"  # 停止按钮颜色
    STOP_BUTTON_HOVER = "#FF8A80"  # 停止按钮悬停颜色
    SIDEBAR_BUTTON_BG = "rgba(0, 211, 211, 0)"  # 侧边栏按钮背景###########################
    SIDEBAR_BUTTON_HOVER_BG = "rgba(255, 255, 255, 0.5)"  # 侧边栏按钮悬停背景
    SIDEBAR_BUTTON_COLOR = "#FFFFFF"  # 侧边栏按钮文字颜色
    SIDEBAR_BUTTON_RADIUS = 0  # 侧边栏按钮圆角半径
    SIDEBAR_BUTTON_SIZE = QSize(35, 35)  # 侧边栏按钮大小

    # ===== 内容区域样式 =====
    CONTENT_BG = "rgba(0, 162, 162, 0)"  # 内容区背景

    # ===== 侧边栏样式 =====
    SIDEBAR_WIDTH = 200
    SIDEBAR_BG = "rgba(0, 211, 211, 0)"  # 深蓝色半透明背景
    SIDEBAR_BORDER = "1px solid rgba(100, 150, 200, 0)"  # 侧边栏边框
    SIDEBAR_TITLE_FONT = ("微软雅黑", 12, QFont.Bold)
    SIDEBAR_TITLE_COLOR = "#E0F7FA"  # 侧边栏标题颜色
    SIDEBAR_TITLE_PADDING = "padding-bottom: 10px;"  # 侧边栏标题下边距

    # ===== 文件列表样式 =====
    FILE_LIST_PADDING = "8px 10px"  # 减少左右内边距，使内容更靠左
    FILE_LIST_BORDER = "none"  # 移除文件项下边框
    FILE_LIST_BG = "rgba(255, 255, 255, 0)"  # 文件项背景
    FILE_LIST_HOVER_BG = "rgba(255, 255, 255, 0.3)"  # 悬停背景
    FILE_LIST_SELECTED_BG = "rgba(100, 200, 255, 0.4)"  # 选中背景
    FILE_LIST_RADIUS = "0px"  # 文件项圆角
    FILE_LIST_FONT = ("微软雅黑", 10)
    FILE_LIST_HEIGHT = 35  # 文件项高度
    FOLDER_COLOR = "#E1F5FE"  # 文件夹文字颜色（浅蓝色）
    FILE_COLOR = "#FFFFFF"  # 文件文字颜色（白色）
    ICON_SIZE = 20  # 图标大小

    # ===== 标签页样式 =====
    TAB_BG = "rgba(255, 255, 255, 0.2)"  # 标签页背景
    TAB_ACTIVE_BG = "rgba(255, 255, 255, 0.7)"  # 活动标签页背景
    TAB_FONT = ("微软雅黑", 9)
    TAB_COLOR = "#2C3E50"  # 标签页文字颜色
    TAB_ACTIVE_COLOR = "#2980B9"  # 活动标签页文字颜色
    TAB_CLOSE_SIZE = 15  # 关闭按钮大小
    TAB_HEIGHT = 30  # 标签页高度
    TAB_PADDING = "0px 10px"  # 标签页内边距

    # ===== 编辑器样式 =====
    EDITOR_BG = "rgba(0, 0, 0, 0.7)"  # 编辑器背景
    EDITOR_COLOR = "#FFFFFF"  # 编辑器文字颜色
    EDITOR_FONT = "Consolas, monospace"  # 编辑器字体
    EDITOR_FONT_SIZE = "10pt"  # 编辑器字体大小

    # ===== 输出区域样式 =====
    OUTPUT_BG = "rgba(0, 0, 0, 0.9)"  # 输出区域背景
    OUTPUT_COLOR = "#00FF00"  # 输出区域文字颜色
    OUTPUT_FONT = "Consolas, monospace"  # 输出区域字体
    OUTPUT_FONT_SIZE = "10pt"  # 输出区域字体大小
    OUTPUT_HEIGHT = 150  # 输出区域初始高度

    # ===== 滚动条样式 =====
    SCROLLBAR_WIDTH = 12  # 滚动条宽度
    SCROLLBAR_BG = "rgba(100, 100, 100, 0.2)"  # 滚动条背景
    SCROLLBAR_HANDLE_BG = "rgba(200, 200, 200, 0.5)"  # 滚动条手柄背景
    SCROLLBAR_HANDLE_HOVER_BG = "rgba(230, 230, 230, 0.7)"  # 悬停时手柄背景
    SCROLLBAR_RADIUS = 6  # 滚动条圆角

    @classmethod
    def global_stylesheet(cls):
        """返回应用程序的全局样式表"""
        return f"""
            #titleBar {{
                background-color: {cls.TITLE_BAR_BG};
            }}
            #contentFrame {{
                background-color: {cls.CONTENT_BG};
            }}
            #sidebar {{
                background-color: {cls.SIDEBAR_BG};
                border-left: {cls.SIDEBAR_BORDER};
                border-radius: 0px 8px 8px 0px;
            }}
            #fileList {{
                background: transparent;
                border: none;
                outline: none;
                font-family: "{cls.FILE_LIST_FONT[0]}";
                font-size: {cls.FILE_LIST_FONT[1]}px;
                color: {cls.FILE_COLOR};
                border-radius: 8px;
                /* 添加左内边距使内容更靠左 */
                padding-left: 5px;
            }}
            #fileList::item {{
                height: {cls.FILE_LIST_HEIGHT}px;
                padding: {cls.FILE_LIST_PADDING};
                background-color: {cls.FILE_LIST_BG};
                border-radius: {cls.FILE_LIST_RADIUS};
                margin-bottom: 3px;
                /* 移除右内边距，使内容更靠左 */
                padding-right: 5px;
            }}
            #fileList::item:hover {{
                background-color: {cls.FILE_LIST_HOVER_BG};
            }}
            #fileList::item:selected {{
                background-color: {cls.FILE_LIST_SELECTED_BG};
            }}
            QTextEdit {{
                line-height: 1.5;
            }}
            QPushButton {{
                border: none;
                border-radius: {cls.BUTTON_RADIUS}px;
                font-weight: bold;
                background-color: {cls.BUTTON_BG};
            }}
            QPushButton:hover {{
                background-color: {cls.BUTTON_HOVER_BG};
            }}
            #closeBtn:hover {{
                background-color: {cls.CLOSE_BUTTON_HOVER_BG};
                color: {cls.CLOSE_BUTTON_HOVER_COLOR};
            }}
            #runBtn {{
                background-color: {cls.RUN_BUTTON_COLOR};
                color: white;
            }}
            #runBtn:hover {{
                background-color: {cls.RUN_BUTTON_HOVER};
            }}
            #runBtn:disabled {{
                background-color: rgba(0, 0, 0, 0.1);
                color: gray;
            }}
            #terminalBtn {{
                background-color: {cls.TERMINAL_BUTTON_COLOR};
                color: white;
            }}
            #terminalBtn:hover {{
                background-color: {cls.TERMINAL_BUTTON_HOVER};
            }}
            #stopBtn {{
                background-color: {cls.STOP_BUTTON_COLOR};
                color: white;
            }}
            #stopBtn:hover {{
                background-color: {cls.STOP_BUTTON_HOVER};
            }}
            #stopBtn:disabled {{
                background-color: rgba(0, 0, 0, 0.1);
                color: gray;
            }}
            .sidebarButton {{
                background-color: {cls.SIDEBAR_BUTTON_BG};
                color: {cls.SIDEBAR_BUTTON_COLOR};
                border: none;
                border-radius: {cls.SIDEBAR_BUTTON_RADIUS}px;
                font-weight: bold;
                font-size: 14px;
                min-width: {cls.SIDEBAR_BUTTON_SIZE.width()}px;
                min-height: {cls.SIDEBAR_BUTTON_SIZE.height()}px;
            }}
            .sidebarButton:hover {{
                background-color: {cls.SIDEBAR_BUTTON_HOVER_BG};
            }}
            QTabWidget::pane {{
                border: none;
                background: transparent;
            }}
            QTabBar::tab {{
                background-color: {cls.TAB_BG};
                color: {cls.TAB_COLOR};
                font-family: "{cls.TAB_FONT[0]}";
                font-size: {cls.TAB_FONT[1]}px;
                padding: {cls.TAB_PADDING};
                height: {cls.TAB_HEIGHT}px;
                /*border-top-left-radius: 5px;*/
                /*border-top-right-radius: 5px;*/
                margin-right: 0px;
                border: 1px solid rgba(200, 200, 200, 0.3);
                border-bottom: none;
            }}
            QTabBar::tab:selected {{
                background-color: {cls.TAB_ACTIVE_BG};
                color: {cls.TAB_ACTIVE_COLOR};
                font-weight: bold;
            }}
            QTabBar::close-button {{
                subcontrol-position: right;
                subcontrol-origin: margin;
                padding: 2px;
                image: url(:/close.png);
            }}
            QTabBar::close-button:hover {{
                background-color: rgba(255, 0, 0, 0.3);
                border-radius: 7px;
            }}
            #outputArea {{
                background-color: {cls.OUTPUT_BG};
                color: {cls.OUTPUT_COLOR};
                font-family: {cls.OUTPUT_FONT};
                font-size: {cls.OUTPUT_FONT_SIZE};
                padding: 5px;
                border: none;
                border-top: 1px solid rgba(100, 100, 100, 0.5);
            }}
            #editorArea {{
                background-color: {cls.EDITOR_BG};
                color: {cls.EDITOR_COLOR};
                font-family: {cls.EDITOR_FONT};
                font-size: {cls.EDITOR_FONT_SIZE};
                padding: 5px;
                border: none;
            }}

           
            QTabBar::scroller {{
                width: 0;
                height: 0;
            }}
            QTabBar QToolButton {{
                width: 0;
                height: 0;
            }}

            /* ===== 滚动条样式 ===== */
            QScrollBar:vertical {{
                background: {cls.SCROLLBAR_BG};
                width: {cls.SCROLLBAR_WIDTH}px;
                border-radius: {cls.SCROLLBAR_RADIUS}px;
                margin: 7px;
                /* 添加右边距，使滚动条与内容分开 */
                margin-right: 3px;
            }}

            QScrollBar::handle:vertical {{
                background: {cls.SCROLLBAR_HANDLE_BG};
                min-height: 30px;
                border-radius: {cls.SCROLLBAR_RADIUS}px;
            }}

            QScrollBar::handle:vertical:hover {{
                background: {cls.SCROLLBAR_HANDLE_HOVER_BG};
            }}

            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                background: none;
                height: 0px;
            }}

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                background: none;
            }}

            /* 水平滚动条 - 隐藏 */
            QScrollBar:horizontal {{
                height: 0px;
            }}
        """


class FileListWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("fileList")
        self.setHeaderHidden(True)  # 隐藏表头
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        self.itemDoubleClicked.connect(self.handle_double_click)

        # 设置统一的图标大小
        self.setIconSize(QSize(AppStyles.ICON_SIZE, AppStyles.ICON_SIZE))

        # 设置缩进为0，使内容更靠左
        self.setIndentation(0)

        # 设置文件夹和文件图标
        self.folder_icon = self.create_folder_icon()
        self.file_icon = self.create_file_icon()

        # 设置滚动条策略
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def create_folder_icon(self):
        """创建精美的文件夹图标"""
        pixmap = QPixmap(24, 24)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制文件夹主体
        painter.setBrush(QColor(64, 128, 255))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(2, 6, 20, 16, 4, 4)

        # 绘制文件夹顶部
        painter.setBrush(QColor(80, 160, 255))
        painter.drawRoundedRect(2, 4, 16, 4, 2, 2)

        painter.end()
        return QIcon(pixmap)

    def create_file_icon(self):
        """创建精美的文件图标"""
        pixmap = QPixmap(24, 24)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制文件主体
        painter.setBrush(QColor(220, 220, 255))
        painter.setPen(QColor(180, 180, 220))
        painter.drawRect(4, 2, 16, 20)

        # 绘制文件折叠角
        path = QPainterPath()
        path.moveTo(16, 2)
        path.lineTo(20, 6)
        path.lineTo(20, 22)
        path.lineTo(4, 22)
        path.lineTo(4, 2)
        path.lineTo(16, 2)
        path.lineTo(20, 6)

        painter.setBrush(QColor(240, 240, 255))
        painter.drawPath(path)

        painter.end()
        return QIcon(pixmap)

    def show_context_menu(self, position):
        item = self.itemAt(position)
        if not item:
            return

        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: rgba(50, 50, 70, 0.9);
                border: 1px solid rgba(100, 150, 200, 0.5);
                border-radius: 5px;
                padding: 5px;
            }

            QMenu::item {
                color: #FFFFFF;
                padding: 5px 20px 5px 10px;
            }
            QMenu::item:selected {
                background-color: rgba(100, 150, 200, 0.7);
                border-radius: 3px;
            }
        """)

        # 根据项目类型显示不同的菜单项
        if item.data(0, Qt.UserRole) == "folder":
            open_action = QAction("打开文件夹", self)
            open_action.triggered.connect(lambda: self.open_folder(item))
            menu.addAction(open_action)
        elif item.data(0, Qt.UserRole) == "file":
            # 添加编辑选项
            edit_action = QAction("编辑", self)
            edit_action.triggered.connect(lambda: self.edit_selected_file(item))
            menu.addAction(edit_action)

            # 添加运行选项（直接打开编辑页面并运行）
            run_action = QAction("运行", self)
            run_action.triggered.connect(lambda: self.run_and_edit_file(item))
            menu.addAction(run_action)
        elif item.data(0, Qt.UserRole) == "parent":
            open_action = QAction("返回上级目录", self)
            open_action.triggered.connect(self.navigate_up)
            menu.addAction(open_action)

        # 添加返回上级目录选项
        if self.parent().parent().parent().folder_path != os.path.expanduser("~"):
            up_action = QAction("返回上级目录", self)
            up_action.triggered.connect(self.navigate_up)
            menu.addAction(up_action)

        menu.exec_(self.viewport().mapToGlobal(position))

    def run_and_edit_file(self, item):
        """运行并编辑选中的文件"""
        if item:
            file_name = item.text(0)
            parent = self.parent().parent().parent()  # 获取主窗口引用
            if parent:
                # 编辑文件（打开或切换到编辑标签页）
                parent.edit_file(file_name)

                # 查找Python解释器
                python_exe_path = parent.find_python_exe()
                if not python_exe_path:
                    QMessageBox.critical(parent, "运行错误", "找不到Python解释器")
                    return

                # 运行文件（在编辑标签页中）
                if file_name in parent.editor_tabs:
                    editor_tab = parent.editor_tabs[file_name]
                    editor_tab.run_file(python_exe_path)


    def handle_double_click(self, item, column):
        """处理双击事件"""
        if item.data(0, Qt.UserRole) == "folder":
            self.open_folder(item)
        elif item.data(0, Qt.UserRole) == "parent":
            self.navigate_up()
        elif item.data(0, Qt.UserRole) == "file":
            # 双击文件时编辑
            self.edit_selected_file(item)

    def open_folder(self, item):
        """打开选中的文件夹"""
        folder_name = item.text(0)
        parent = self.parent().parent().parent()  # 获取主窗口引用
        if parent:
            parent.enter_folder(folder_name)

    def navigate_up(self):
        """返回上级目录"""
        parent = self.parent().parent().parent()  # 获取主窗口引用
        if parent:
            parent.navigate_up()

    def run_selected_file(self, item):
        """运行选中的文件"""
        if item:
            file_name = item.text(0)
            parent = self.parent().parent().parent()  # 获取主窗口引用
            if parent:
                # 获取完整文件路径
                file_path = os.path.join(parent.folder_path, file_name)

                # 查找Python解释器
                python_exe_path = parent.find_python_exe()
                if not python_exe_path:
                    QMessageBox.critical(parent, "运行错误", "找不到Python解释器")
                    return

                # 创建输出标签页
                output_tab = OutputTab(file_name, main_window=parent)
                parent.output_tabs[file_name] = output_tab
                tab_index = parent.tab_widget.addTab(output_tab, file_name)
                parent.tab_widget.setCurrentIndex(tab_index)

                # 运行文件
                if not output_tab.run_file(file_path, python_exe_path):
                    parent.close_output_tab_by_name(file_name)

    def edit_selected_file(self, item):
        """编辑选中的文件"""
        if item:
            file_name = item.text(0)
            parent = self.parent().parent().parent()  # 获取主窗口引用
            if parent:
                parent.edit_file(file_name)


class OutputTab(QWidget):
    """用于显示命令行输出的标签页"""

    def __init__(self, file_name, main_window=None, is_terminal=False):
        super().__init__()
        self.file_name = file_name
        self.is_terminal = is_terminal
        self.main_window = main_window  # 保存主窗口引用

        self.process = QProcess(self)  # 使用QProcess代替subprocess
        self.process.setProcessChannelMode(QProcess.MergedChannels)  # 合并输出和错误
        self.process.readyReadStandardOutput.connect(self.handle_output)
        self.process.readyReadStandardError.connect(self.handle_error)
        self.process.finished.connect(self.process_finished)
        self.process.started.connect(self.process_started)
        self.process.stateChanged.connect(self.process_state_changed)

        # 命令起始位置（用于终端输入）
        self.command_start_position = 0
        self.pending_input = False  # 新增：标记是否等待输入

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # 创建输出显示区域
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(False)  # 终端可编辑
        self.output_area.setObjectName("outputArea")
        self.output_area.setFocusPolicy(Qt.StrongFocus)
        self.layout.addWidget(self.output_area)

        # 安装事件过滤器
        self.output_area.installEventFilter(self)

    def eventFilter(self, obj, event):
        """事件过滤器处理终端输入"""
        if obj == self.output_area and event.type() == QEvent.KeyPress:
            return self.handle_key_event(event)
        return super().eventFilter(obj, event)

    def handle_key_event(self, event):
        """处理键盘事件"""
        # 处理回车键
        if event.key() == Qt.Key_Return and not event.modifiers() & Qt.ShiftModifier:
            # 获取当前光标位置
            cursor = self.output_area.textCursor()

            # 获取当前行文本
            cursor.select(QTextCursor.LineUnderCursor)
            full_line = cursor.selectedText()

            # 如果是终端或等待输入
            if self.is_terminal or self.pending_input:
                # 只提取用户输入的命令部分
                if '>' in full_line:
                    # 找到最后一个'>'的位置
                    last_gt_index = full_line.rfind('>')
                    command = full_line[last_gt_index + 1:].strip()
                else:
                    command = full_line.strip()

                if command:
                    # 执行命令或发送输入
                    if self.is_terminal:
                        self.execute_command(command)
                    else:
                        self.write_input(command)

                    # 重置输入等待状态
                    self.pending_input = False

                    # 在命令后添加换行符
                    cursor.movePosition(QTextCursor.EndOfLine)
                    cursor.insertText("\n")
                    self.output_area.setTextCursor(cursor)
                    self.command_start_position = self.output_area.textCursor().position()

            # 阻止默认行为（插入换行符）
            return True

        # 处理退格键 - 防止删除历史输出
        elif event.key() == Qt.Key_Backspace:
            cursor = self.output_area.textCursor()
            if cursor.position() < self.command_start_position:
                return True

        return False

    def append_output(self, text):
        """追加输出文本"""
        self.output_area.moveCursor(QTextCursor.End)
        self.output_area.insertPlainText(text)
        self.output_area.moveCursor(QTextCursor.End)
        # 确保UI更新
        QApplication.processEvents()

    def handle_output(self):
        """实时处理标准输出"""
        # 使用正确的编码读取输出（解决乱码问题）
        output = self.process.readAllStandardOutput().data()
        try:
            # 尝试GBK解码（Windows中文环境常用）
            decoded_output = output.decode('gbk')
        except UnicodeDecodeError:
            try:
                # 尝试UTF-8解码
                decoded_output = output.decode('utf-8')
            except:
                # 如果都不行，使用错误提示
                decoded_output = "[无法解码的输出]\n"

        # 检查是否有输入请求
        if "input(" in decoded_output or "input (" in decoded_output:
            self.pending_input = True

        self.append_output(decoded_output)

    def handle_error(self):
        """实时处理错误输出"""
        # 使用正确的编码读取错误输出
        error = self.process.readAllStandardError().data()
        try:
            # 尝试GBK解码（Windows中文环境常用）
            decoded_error = error.decode('gbk')
        except UnicodeDecodeError:
            try:
                # 尝试UTF-8解码
                decoded_error = error.decode('utf-8')
            except:
                # 如果都不行，使用错误提示
                decoded_error = "[无法解码的错误输出]\n"

        self.append_output(decoded_error)

    def process_started(self):
        """进程启动时的处理"""
        # 修复：不再添加额外的提示符
        pass

    def process_finished(self, exit_code, exit_status):
        """进程结束"""
        self.append_output(f"\n进程已退出，返回代码: {exit_code}\n")
        # 通知主窗口更新输入框状态
        if self.main_window:
            self.main_window.update_run_button_state()

    def process_state_changed(self, new_state):
        """进程状态变化时更新输入框状态"""
        if self.main_window:
            self.main_window.update_run_button_state()

    def run_file(self, file_path, python_exe_path):
        """运行指定的文件"""
        try:
            # 设置工作目录
            self.process.setWorkingDirectory(os.path.dirname(file_path))

            # 启动进程（使用无缓冲模式）
            self.process.start(python_exe_path, ['-u', file_path])
            return True
        except Exception as e:
            self.append_output(f"运行失败: {str(e)}\n")
            return False

    def run_command(self, command):
        """运行指定的命令"""
        try:
            # 启动进程
            self.process.start(command)
            return True
        except Exception as e:
            self.append_output(f"运行失败: {str(e)}\n")
            return False

    def execute_command(self, command):
        """执行终端输入的命令"""
        if not self.is_terminal or not command:
            return

        # 规范化命令：将 "cd.." 转换为 "cd .."
        if command.startswith("cd.."):
            command = "cd " + command[2:]  # 将 "cd.." 转换为 "cd .."

        # 修复：不再添加命令到输出区域
        # 因为终端会回显用户的输入

        if self.process and self.process.state() == QProcess.Running:
            try:
                # 尝试使用GBK编码（Windows中文环境）
                command_bytes = command.encode('gbk') + b'\r\n'
            except UnicodeEncodeError:
                # 如果GBK失败，使用UTF-8
                command_bytes = command.encode('utf-8') + b'\r\n'

            self.process.write(command_bytes)
            # 强制刷新缓冲区
            self.process.waitForBytesWritten()

            # 更新命令起始位置
            self.command_start_position = self.output_area.textCursor().position()

    def write_input(self, text):
        """向进程写入输入内容"""
        if self.process and self.process.state() == QProcess.Running:
            try:
                # 添加换行符表示输入结束
                input_text = text + "\n"

                # 尝试使用GBK编码（Windows中文环境）
                input_bytes = input_text.encode('gbk')
            except UnicodeEncodeError:
                # 如果GBK失败，使用UTF-8
                input_bytes = input_text.encode('utf-8')

            self.process.write(input_bytes)
            # 强制刷新缓冲区
            self.process.waitForBytesWritten()
            return True
        return False

    def terminate_process(self):
        """强制终止正在运行的进程"""
        if self.process.state() == QProcess.Running:
            # Windows系统使用任务树终止命令
            if platform.system() == 'Windows':
                subprocess.call(f"taskkill /F /T /PID {self.process.processId()}",
                                shell=True)
            else:  # Linux/macOS
                self.process.terminate()
                self.process.waitForFinished(1000)
            self.append_output("\n进程已被强制终止\n")

    def is_process_running(self):
        """检查进程是否正在运行"""
        return self.process.state() == QProcess.Running


class EditorTab(QWidget):
    """用于编辑文件的标签页"""

    def __init__(self, file_path, main_window=None):
        super().__init__()
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.main_window = main_window
        self.is_modified = False
        self.process = None
        self.output_visible = False

        # 主布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # 创建分割器
        self.splitter = QSplitter(Qt.Vertical)
        self.layout.addWidget(self.splitter)

        # 创建编辑器区域
        self.editor_area = QTextEdit()
        self.editor_area.setObjectName("editorArea")
        self.editor_area.setFont(QFont("Consolas", 10))
        self.editor_area.textChanged.connect(self.mark_modified)
        self.splitter.addWidget(self.editor_area)

        # 创建输出区域
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(False)  # 设置为可编辑以便输入
        self.output_area.setObjectName("outputArea")
        self.output_area.setMinimumHeight(50)
        self.output_area.setMaximumHeight(1000)
        self.output_area.hide()  # 初始隐藏输出区域
        self.output_area.installEventFilter(self)  # 安装事件过滤器
        self.splitter.addWidget(self.output_area)

        # 设置分割器比例
        self.splitter.setSizes([400, 150])

        # 加载文件内容
        self.load_file()

    def eventFilter(self, obj, event):
        """事件过滤器，用于处理输出区域的输入"""
        if obj == self.output_area and event.type() == QEvent.KeyPress:
            # 当在输出区域按下回车键时（不带Shift）
            if event.key() == Qt.Key_Return and not event.modifiers() & Qt.ShiftModifier:
                cursor = self.output_area.textCursor()
                cursor.movePosition(QTextCursor.End)
                cursor.select(QTextCursor.LineUnderCursor)
                input_line = cursor.selectedText()
                if input_line.strip():
                    # 发送输入
                    self.write_input(input_line.strip())
                    # 在输出区域追加换行，模拟终端
                    self.output_area.append("")
                return True  # 事件已处理
        return super().eventFilter(obj, event)

    def write_input(self, text):
        """向进程写入输入内容"""
        if self.process and self.process.state() == QProcess.Running:
            try:
                # 添加换行符表示输入结束
                input_text = text + "\n"

                # 尝试使用GBK编码（Windows中文环境）
                input_bytes = input_text.encode('gbk')
            except UnicodeEncodeError:
                # 如果GBK失败，使用UTF-8
                input_bytes = input_text.encode('utf-8')

            self.process.write(input_bytes)
            # 强制刷新缓冲区
            self.process.waitForBytesWritten()
            return True
        return False

    def mark_modified(self):
        """标记文件已修改"""
        self.is_modified = True
        if self.main_window:
            # 在标签页标题前添加星号表示修改
            tab_index = self.main_window.tab_widget.indexOf(self)
            if tab_index != -1:
                tab_text = self.main_window.tab_widget.tabText(tab_index)
                if not tab_text.startswith("*"):
                    self.main_window.tab_widget.setTabText(tab_index, f"*{tab_text}")

    def load_file(self):
        """加载文件内容到编辑器"""
        try:
            # 检测文件编码
            with open(self.file_path, 'rb') as f:
                raw_data = f.read()
                result = self.detect_encoding(raw_data)

            # 使用检测到的编码打开文件
            with open(self.file_path, 'r', encoding=result['encoding'], errors='replace') as f:
                content = f.read()
                self.editor_area.setPlainText(content)
                self.is_modified = False
                return True
        except Exception as e:
            self.editor_area.setPlainText(f"无法加载文件: {str(e)}")
            return False

    def detect_encoding(self, data):
        """检测文件编码"""
        # 尝试常见编码
        encodings = ['utf-8', 'gbk', 'gb2312', 'gb18030', 'big5', 'shift_jis', 'iso-8859-1']

        for enc in encodings:
            try:
                data.decode(enc)
                return {'encoding': enc, 'confidence': 1.0}
            except UnicodeDecodeError:
                continue

        # 如果常见编码都不行，使用chardet（如果可用）
        try:
            import chardet
            result = chardet.detect(data)
            return result
        except ImportError:
            return {'encoding': 'utf-8', 'confidence': 0.5}

    def save_file(self):
        """保存文件内容"""
        try:
            # 获取当前编辑器内容
            content = self.editor_area.toPlainText()

            # 保存文件
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            self.is_modified = False
            if self.main_window:
                # 移除标签页标题前的星号
                tab_index = self.main_window.tab_widget.indexOf(self)
                if tab_index != -1:
                    tab_text = self.main_window.tab_widget.tabText(tab_index)
                    if tab_text.startswith("*"):
                        self.main_window.tab_widget.setTabText(tab_index, tab_text[1:])
            return True
        except Exception as e:
            QMessageBox.critical(self, "保存错误", f"无法保存文件: {str(e)}")
            return False

    def run_file(self, python_exe_path):
        """运行当前文件"""
        # 如果已有进程在运行，先终止
        if self.process and self.process.state() == QProcess.Running:
            self.process.terminate()
            self.process.waitForFinished(1000)

        # 显示输出区域
        if not self.output_visible:
            self.output_area.show()
            self.output_visible = True

        # 清空输出
        self.output_area.clear()

        # 保存文件
        if not self.save_file():
            return

        # 创建进程
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.handle_output)
        self.process.readyReadStandardError.connect(self.handle_error)
        self.process.finished.connect(self.process_finished)
        self.process.started.connect(self.process_started)

        # 设置工作目录
        self.process.setWorkingDirectory(os.path.dirname(self.file_path))

        # 启动进程
        try:
            self.process.start(python_exe_path, ['-u', self.file_path])
            self.append_output(f"运行: {self.file_name}\n")
        except Exception as e:
            self.append_output(f"运行失败: {str(e)}\n")

        # 通知主窗口更新按钮状态
        if self.main_window:
            self.main_window.update_run_button_state()

    def process_started(self):
        """进程启动时的处理"""
        # 通知主窗口更新按钮状态
        if self.main_window:
            self.main_window.update_run_button_state()

    def append_output(self, text):
        """追加输出文本"""
        self.output_area.moveCursor(QTextCursor.End)
        self.output_area.insertPlainText(text)
        self.output_area.moveCursor(QTextCursor.End)

    def handle_output(self):
        """处理标准输出"""
        output = self.process.readAllStandardOutput().data()
        try:
            decoded_output = output.decode('gbk')
        except UnicodeDecodeError:
            try:
                decoded_output = output.decode('utf-8')
            except:
                decoded_output = "[无法解码的输出]\n"
        self.append_output(decoded_output)

    def handle_error(self):
        """处理错误输出"""
        error = self.process.readAllStandardError().data()
        try:
            decoded_error = error.decode('gbk')
        except UnicodeDecodeError:
            try:
                decoded_error = error.decode('utf-8')
            except:
                decoded_error = "[无法解码的错误输出]\n"
        self.append_output(decoded_error)

    def process_finished(self, exit_code, exit_status):
        """进程结束"""
        self.append_output(f"\n进程已退出，返回代码: {exit_code}\n")
        # 通知主窗口更新按钮状态
        if self.main_window:
            self.main_window.update_run_button_state()

    def terminate_process(self):
        """强制终止正在运行的进程及其子进程"""
        if self.process and self.process.state() == QProcess.Running:
            # 获取进程ID
            pid = self.process.processId()

            if platform.system() == 'Windows':
                try:
                    # 使用更可靠的进程树终止命令
                    subprocess.run(
                        f"taskkill /F /T /PID {pid}",
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        timeout=2
                    )
                except:
                    # 如果taskkill失败，使用更底层的API
                    try:
                        import ctypes
                        PROCESS_TERMINATE = 1
                        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)
                        ctypes.windll.kernel32.TerminateProcess(handle, -1)
                        ctypes.windll.kernel32.CloseHandle(handle)
                    except:
                        pass
            else:  # Linux/macOS
                # 使用进程组ID终止整个进程树
                try:
                    import os
                    import signal
                    os.killpg(os.getpgid(pid), signal.SIGKILL)
                except:
                    self.process.terminate()

            # 确保进程终止
            self.process.waitForFinished(1000)
            self.append_output("\n进程已被强制终止\n")

            # 通知主窗口更新按钮状态
            if self.main_window:
                self.main_window.update_run_button_state()

    def keyPressEvent(self, event):
        # 使用Ctrl+S保存文件
        if event.key() == Qt.Key_S and event.modifiers() & Qt.ControlModifier:
            self.save_file()
            event.accept()
        # 使用Ctrl+R运行文件
        elif event.key() == Qt.Key_R and event.modifiers() & Qt.ControlModifier:
            self.main_window.run_current_file()
            event.accept()
        else:
            super().keyPressEvent(event)


class TabBarWithClose(QTabBar):
    """带关闭按钮的标签栏"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setExpanding(False)
        self.setElideMode(Qt.ElideRight)

    def tabSizeHint(self, index):
        """调整标签大小以适应关闭按钮"""
        size = super().tabSizeHint(index)
        size.setWidth(size.width() + 25)  # 为关闭按钮留出空间
        return size


class FramelessWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 检查并设置窗口图标
        icon_path = "exe.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"警告: 找不到图标文件 {icon_path}")

        # 设置窗口无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置窗口背景透明以实现圆角效果
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 窗口大小
        self.setMinimumSize(*AppStyles.WINDOW_MIN_SIZE)
        self.resize(*AppStyles.WINDOW_INIT_SIZE)

        # 设置窗口居中显示
        self.center_window()

        # 初始化变量
        self.draggable = False
        self.drag_position = QPoint()
        self.is_resizing = False
        self.resize_direction = None
        self.start_geometry = None
        self.edge_width = 8  # 边缘宽度用于拉伸检测

        # 默认文件夹路径（可修改）
        self.folder_path = os.getcwd()  # os.path.expanduser("~")  # 用户主目录
        self.allowed_extensions = ['.txt', '.py', '.png', '.pdf', '.ppt', '.html']

        # 添加标签页管理字典
        self.output_tabs = {}  # file_name: OutputTab
        self.editor_tabs = {}  # file_name: EditorTab
        self.terminal_counter = 1  # 终端标签页计数器

        # 初始化UI
        self.initUI()

        # 启用鼠标跟踪
        self.setMouseTracking(True)

    def center_window(self):
        """将窗口居中显示在屏幕上"""
        # 获取屏幕尺寸
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口尺寸
        window_size = self.geometry()
        # 计算居中位置
        x = (screen.width() - window_size.width()) // 2
        y = (screen.height() - window_size.height()) // 2
        # 移动窗口到居中位置
        self.move(x, y)

    def initUI(self):
        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(0)

        # 标题栏 - 设置为透明
        self.title_bar = QWidget()
        self.title_bar.setFixedHeight(AppStyles.TITLE_BAR_HEIGHT)
        self.title_bar.setObjectName("titleBar")

        title_layout = QHBoxLayout(self.title_bar)
        title_layout.setContentsMargins(15, 0, 15, 0)

        # 标题
        self.title_label = QLabel("阿炜的管理器")
        self.title_label.setFont(QFont(*AppStyles.TITLE_FONT))
        self.title_label.setStyleSheet(f"color: {AppStyles.TITLE_COLOR};")

        # 新建终端按钮
        self.terminal_btn = QPushButton("+T")
        self.terminal_btn.setFixedSize(AppStyles.BUTTON_SIZE)
        self.terminal_btn.setObjectName("terminalBtn")
        self.terminal_btn.setToolTip("新建终端标签页")
        self.terminal_btn.clicked.connect(self.add_terminal_tab)

        # 运行按钮
        self.run_btn = QPushButton("▶")
        self.run_btn.setFixedSize(AppStyles.BUTTON_SIZE)
        self.run_btn.setObjectName("runBtn")
        self.run_btn.setToolTip("运行当前程序 (Ctrl+R)")
        self.run_btn.clicked.connect(self.run_current_file)
        self.run_btn.setEnabled(False)  # 初始禁用

        # 停止按钮
        self.stop_btn = QPushButton("■")
        self.stop_btn.setFixedSize(AppStyles.BUTTON_SIZE)
        self.stop_btn.setObjectName("stopBtn")
        self.stop_btn.setToolTip("停止当前运行的程序")
        self.stop_btn.clicked.connect(self.stop_current_process)
        self.stop_btn.setEnabled(False)  # 初始禁用

        # 窗口控制按钮
        self.min_btn = QPushButton("—")
        self.min_btn.setFixedSize(AppStyles.BUTTON_SIZE)
        self.min_btn.setObjectName("minBtn")

        self.max_btn = QPushButton("□")
        self.max_btn.setFixedSize(AppStyles.BUTTON_SIZE)
        self.max_btn.setObjectName("maxBtn")

        self.close_btn = QPushButton("×")
        self.close_btn.setFixedSize(AppStyles.BUTTON_SIZE)
        self.close_btn.setObjectName("closeBtn")

        # 添加控件到标题栏
        title_layout.addWidget(self.title_label)
        title_layout.addStretch()
        title_layout.addWidget(self.terminal_btn)
        title_layout.addWidget(self.run_btn)
        title_layout.addWidget(self.stop_btn)
        title_layout.addStretch(1)
        title_layout.addWidget(self.min_btn)
        title_layout.addWidget(self.max_btn)
        title_layout.addWidget(self.close_btn)

        # 主内容区域
        content_frame = QFrame()
        content_frame.setObjectName("contentFrame")
        content_layout = QHBoxLayout(content_frame)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # 左侧区域
        main_widget = QWidget()
        main_layout_inner = QVBoxLayout(main_widget)
        main_layout_inner.setContentsMargins(0, 0, 0, 0)
        main_layout_inner.setSpacing(0)

        # ==== 创建标签页组件 ====
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabBar(TabBarWithClose())  # 使用自定义标签栏
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_output_tab)
        self.tab_widget.currentChanged.connect(self.tab_changed)  # 添加标签页切换事件

        # 创建初始终端标签页
        self.add_terminal_tab()

        # 添加标签页
        main_layout_inner.addWidget(self.tab_widget, 1)  # 标签页占剩余空间

        # 右侧侧边栏
        self.sidebar = QWidget()
        self.sidebar.setFixedWidth(AppStyles.SIDEBAR_WIDTH)
        self.sidebar.setObjectName("sidebar")  # 添加对象名以便在样式表中引用

        # 侧边栏内容
        sidebar_layout = QVBoxLayout(self.sidebar)
        # 调整侧边栏边距，使内容更靠左
        sidebar_layout.setContentsMargins(10, 20, 5, 20)  # 右边距减少为5px
        sidebar_layout.setSpacing(10)  # 增加间距

        # 顶部工具栏
        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(0, 0, 0, 10)
        toolbar_layout.setSpacing(8)  # 设置按钮间距

        # 返回上级目录按钮 - 使用新样式
        self.up_btn = QPushButton("⤴")
        self.up_btn.setProperty("class", "sidebarButton")
        self.up_btn.setToolTip("返回上级目录")
        self.up_btn.setFixedSize(AppStyles.SIDEBAR_BUTTON_SIZE)
        self.up_btn.clicked.connect(self.navigate_up)
        self.up_btn.setEnabled(False)  # 初始禁用

        # 文件夹选择按钮 - 使用新样式
        self.folder_btn = QPushButton("📁")
        self.folder_btn.setProperty("class", "sidebarButton")
        self.folder_btn.setToolTip("选择文件夹")
        self.folder_btn.setFixedSize(AppStyles.SIDEBAR_BUTTON_SIZE)
        self.folder_btn.clicked.connect(self.select_folder)

        # 刷新按钮 - 使用新样式
        self.refresh_btn = QPushButton("🔄")
        self.refresh_btn.setProperty("class", "sidebarButton")
        self.refresh_btn.setToolTip("刷新文件列表")
        self.refresh_btn.setFixedSize(AppStyles.SIDEBAR_BUTTON_SIZE)
        self.refresh_btn.clicked.connect(self.load_file_list)

        toolbar_layout.addWidget(self.up_btn)
        toolbar_layout.addWidget(self.folder_btn)
        toolbar_layout.addWidget(self.refresh_btn)

        # 当前路径标签
        self.path_label = QLabel("当前文件夹:")
        self.path_label.setFont(QFont("微软雅黑", 9))
        self.path_label.setStyleSheet("color: #E0F7FA; margin-bottom: 5px;")

        # 创建文件列表
        self.file_list = FileListWidget()
        # 设置文件列表内容对齐方式为靠左
        self.file_list.setIndentation(0)

        sidebar_layout.addLayout(toolbar_layout)
        sidebar_layout.addWidget(self.path_label)
        sidebar_layout.addWidget(self.file_list, 1)  # 文件列表占据剩余空间

        # 添加主区域和侧边栏到主内容区
        content_layout.addWidget(main_widget, 1)  # 主区域占剩余空间
        content_layout.addWidget(self.sidebar)  # 侧边栏固定宽度

        # 添加标题栏和内容到主布局
        main_layout.addWidget(self.title_bar)
        main_layout.addWidget(content_frame, 1)

        # 连接按钮信号
        self.min_btn.clicked.connect(self.showMinimized)
        self.max_btn.clicked.connect(self.toggle_maximize)
        self.close_btn.clicked.connect(self.close)

        # 初始加载文件列表
        self.load_file_list()

    def select_folder(self):
        """打开文件夹选择对话框"""
        folder = QFileDialog.getExistingDirectory(self, "选择文件夹", self.folder_path)
        if folder:
            self.folder_path = folder
            self.load_file_list()

    def navigate_up(self):
        """返回上级目录"""
        parent_dir = os.path.dirname(self.folder_path)
        if os.path.isdir(parent_dir) and parent_dir != self.folder_path:
            self.folder_path = parent_dir
            self.load_file_list()

    def enter_folder(self, folder_name):
        """进入子文件夹"""
        new_path = os.path.join(self.folder_path, folder_name)
        if os.path.isdir(new_path):
            self.folder_path = new_path
            self.load_file_list()

    def load_file_list(self):
        """加载指定文件夹的文件和文件夹列表"""
        # 清空文件列表
        self.file_list.clear()

        # 更新返回上级按钮状态
        self.up_btn.setEnabled(self.folder_path != os.path.expanduser("~") and
                               os.path.dirname(self.folder_path) != self.folder_path)

        # 更新路径标签
        self.path_label.setText(f"当前文件夹:\n{self.folder_path}")

        # 检查文件夹是否存在
        if not os.path.isdir(self.folder_path):
            return

        try:
            # 添加返回上级目录项
            if self.folder_path != os.path.expanduser("~") and os.path.dirname(self.folder_path) != self.folder_path:
                parent_item = QTreeWidgetItem(self.file_list)
                parent_item.setText(0, "..")
                parent_item.setIcon(0, self.file_list.folder_icon)
                parent_item.setData(0, Qt.UserRole, "parent")
                # 设置特殊颜色
                parent_item.setForeground(0, QColor("#FFCC80"))  # 橙色

            # 获取文件夹中的所有条目
            entries = os.listdir(self.folder_path)
            # 先添加文件夹，再添加文件
            folders = []
            files = []

            for entry in entries:
                entry_path = os.path.join(self.folder_path, entry)
                if os.path.isdir(entry_path):
                    folders.append(entry)
                else:
                    # 检查文件扩展名
                    _, ext = os.path.splitext(entry)
                    if ext.lower() in self.allowed_extensions:
                        files.append(entry)

            # 按名称排序
            folders.sort()
            files.sort()

            # 添加文件夹
            for folder in folders:
                item = QTreeWidgetItem(self.file_list)
                item.setText(0, folder)
                item.setIcon(0, self.file_list.folder_icon)
                item.setData(0, Qt.UserRole, "folder")
                # 设置文件夹颜色
                item.setForeground(0, QColor(AppStyles.FOLDER_COLOR))

            # 添加文件
            for file in files:
                item = QTreeWidgetItem(self.file_list)
                item.setText(0, file)
                item.setIcon(0, self.file_list.file_icon)
                item.setData(0, Qt.UserRole, "file")
                # 设置文件颜色
                item.setForeground(0, QColor(AppStyles.FILE_COLOR))

            # 显示条目计数
            self.file_list.setToolTip(f"找到 {len(folders)} 个文件夹, {len(files)} 个文件")

        except Exception as e:
            print(f"无法读取文件夹: {e}")
            self.file_list.setToolTip(f"错误: {str(e)}")

    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.max_btn.setText("□")
        else:
            self.showMaximized()
            self.max_btn.setText("❐")

    def find_python_exe(self):
        """查找内置Python解释器路径"""
        # 获取当前执行文件的目录（此程序.exe所在目录）
        current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

        # 方案1：在当前目录下查找python/python.exe
        python_dir = os.path.join(current_dir, "python")
        python_exe = os.path.join(python_dir, "python.exe")
        if os.path.exists(python_exe):
            return python_exe

        # 方案2：在上一级目录查找（如果程序在子目录中）
        parent_dir = os.path.dirname(current_dir)
        python_dir = os.path.join(parent_dir, "python")
        python_exe = os.path.join(python_dir, "python.exe")
        if os.path.exists(python_exe):
            return python_exe

        # 方案3：在系统环境变量中查找
        try:
            if platform.system() == 'Windows':
                # 在Windows上使用where命令
                result = subprocess.check_output("where python", shell=True, text=True)
                if result:
                    # 取第一个找到的Python解释器
                    return result.splitlines()[0].strip()
            else:
                # 在Linux/macOS上使用which命令
                result = subprocess.check_output("which python", shell=True, text=True)
                if result:
                    return result.strip()
        except:
            pass

        return None

    def edit_file(self, file_name):
        """编辑指定文件"""
        # 获取完整文件路径
        file_path = os.path.join(self.folder_path, file_name)

        # 检查文件是否存在
        if not os.path.exists(file_path):
            return

        # 如果已有该文件的编辑标签页，直接激活
        if file_name in self.editor_tabs:
            tab_index = self.tab_widget.indexOf(self.editor_tabs[file_name])
            if tab_index != -1:
                self.tab_widget.setCurrentIndex(tab_index)
                return

        # 创建新的编辑标签页
        editor_tab = EditorTab(file_path, main_window=self)
        self.editor_tabs[file_name] = editor_tab

        # 添加标签页
        tab_index = self.tab_widget.addTab(editor_tab, file_name)
        self.tab_widget.setCurrentIndex(tab_index)

        # 更新运行按钮状态
        self.update_run_button_state()

        return editor_tab  # 返回编辑标签页引用

    def run_current_file(self):
        """运行当前标签页的文件"""
        current_index = self.tab_widget.currentIndex()
        if current_index < 0:
            return

        current_tab = self.tab_widget.widget(current_index)

        # 如果当前标签页是编辑器
        if isinstance(current_tab, EditorTab):
            # 查找Python解释器
            python_exe_path = self.find_python_exe()
            if not python_exe_path:
                QMessageBox.critical(self, "运行错误", "找不到Python解释器")
                return

            current_tab.run_file(python_exe_path)
        # 如果当前标签页是终端
        elif current_tab in self.output_tabs.values() and current_tab.is_terminal:
            # 终端标签页不需要运行操作
            pass

    def stop_current_process(self):
        """停止当前运行的进程（仅对编辑器标签页有效）"""
        current_index = self.tab_widget.currentIndex()
        if current_index < 0:
            return

        current_tab = self.tab_widget.widget(current_index)

        # 如果当前标签页是编辑器，并且有进程在运行
        if isinstance(current_tab, EditorTab):
            if current_tab.process and current_tab.process.state() == QProcess.Running:
                current_tab.terminate_process()
                # 立即禁用停止按钮，避免重复点击
                self.stop_btn.setEnabled(False)
        # 对于终端标签页，我们不执行任何操作

    def close_output_tab(self, index):
        """关闭指定索引的标签页并终止关联进程"""
        # 获取标签页组件
        tab_widget = self.tab_widget.widget(index)
        tab_name = self.tab_widget.tabText(index)

        # 检查是否是编辑标签页
        if tab_name in self.editor_tabs:
            # 检查是否有未保存的修改
            editor_tab = self.editor_tabs[tab_name]
            if editor_tab.is_modified:
                reply = QMessageBox.question(self, "保存修改",
                                             f"文件 {tab_name} 有未保存的修改。是否保存?",
                                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
                if reply == QMessageBox.Cancel:
                    return
                elif reply == QMessageBox.Yes:
                    if not editor_tab.save_file():
                        return  # 如果保存失败，不关闭标签页

            # 终止编辑器标签页的进程
            if editor_tab.process and editor_tab.process.state() == QProcess.Running:
                editor_tab.terminate_process()

            # 从字典中移除
            del self.editor_tabs[tab_name]

        # 如果是输出标签页，终止进程
        if tab_name in self.output_tabs:
            output_tab = self.output_tabs[tab_name]
            output_tab.terminate_process()  # 确保终止进程
            del self.output_tabs[tab_name]

        # 移除标签页
        self.tab_widget.removeTab(index)

        # 更新按钮状态
        self.update_run_button_state()

    def close_output_tab_by_name(self, file_name):
        """按文件名关闭标签页"""
        if file_name in self.output_tabs:
            # 查找标签页索引
            for i in range(self.tab_widget.count()):
                if self.tab_widget.tabText(i) == file_name:
                    self.close_output_tab(i)
                    break

    def add_terminal_tab(self):
        """添加新的终端标签页"""
        # 生成唯一的终端名称
        tab_name = f"终端{self.terminal_counter}"
        self.terminal_counter += 1

        # 创建终端标签页
        terminal_tab = OutputTab(tab_name, main_window=self, is_terminal=True)
        self.output_tabs[tab_name] = terminal_tab
        tab_index = self.tab_widget.addTab(terminal_tab, tab_name)
        self.tab_widget.setCurrentIndex(tab_index)

        # 启动终端
        if sys.platform == 'win32':
            # Windows使用cmd - 修复：使用正确的启动方式
            terminal_tab.run_command("cmd.exe")
        else:
            # Linux/macOS使用bash
            terminal_tab.run_command("bash")

        # 修复：设置初始工作目录
        terminal_tab.process.setWorkingDirectory(os.getcwd())

        # 更新按钮状态
        self.update_run_button_state()

    def tab_changed(self, index):
        """标签页切换事件处理"""
        self.update_run_button_state()

    def update_run_button_state(self):
        """更新运行和停止按钮状态（根据当前标签页）"""
        current_index = self.tab_widget.currentIndex()
        if current_index < 0:
            self.run_btn.setEnabled(False)
            self.stop_btn.setEnabled(False)
            return

        current_tab = self.tab_widget.widget(current_index)
        is_running = False

        # 检查是否有进程在运行
        if isinstance(current_tab, EditorTab):
            self.run_btn.setEnabled(True)
            if current_tab.process and current_tab.process.state() == QProcess.Running:
                is_running = True

        elif current_tab in self.output_tabs.values() and current_tab.is_terminal:
            self.run_btn.setEnabled(False)
            if current_tab.is_process_running():
                # 终端标签页有进程运行，但我们不启用停止按钮
                is_running = False
        else:
            self.run_btn.setEnabled(False)
            self.stop_btn.setEnabled(False)

        # 更新停止按钮状态 - 只对编辑器标签页有效
        self.stop_btn.setEnabled(is_running)

    # 重写绘制事件以实现圆角和背景色
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 创建渐变背景
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, AppStyles.WINDOW_BG_GRADIENT[0])
        gradient.setColorAt(1, AppStyles.WINDOW_BG_GRADIENT[1])

        # 绘制圆角矩形背景
        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), AppStyles.WINDOW_CORNER_RADIUS, AppStyles.WINDOW_CORNER_RADIUS)

    # 确定拉伸方向
    def get_resize_direction(self, pos):
        rect = self.rect()
        top_edge = pos.y() < self.edge_width
        bottom_edge = pos.y() > rect.height() - self.edge_width
        left_edge = pos.x() < self.edge_width
        right_edge = pos.x() > rect.width() - self.edge_width

        if top_edge and left_edge:
            return "top-left"
        elif top_edge and right_edge:
            return "top-right"
        elif bottom_edge and left_edge:
            return "bottom-left"
        elif bottom_edge and right_edge:
            return "bottom-right"
        elif top_edge:
            return "top"
        elif bottom_edge:
            return "bottom"
        elif left_edge:
            return "left"
        elif right_edge:
            return "right"
        return None

    # 设置光标形状
    def set_cursor_shape(self, direction):
        if direction == "top" or direction == "bottom":
            self.setCursor(Qt.SizeVerCursor)
        elif direction == "left" or direction == "right":
            self.setCursor(Qt.SizeHorCursor)
        elif direction == "top-left" or direction == "bottom-right":
            self.setCursor(Qt.SizeFDiagCursor)
        elif direction == "top-right" or direction == "bottom-left":
            self.setCursor(Qt.SizeBDiagCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

    # 鼠标事件处理 - 用于窗口拖动和拉伸
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.pos()
            self.resize_direction = self.get_resize_direction(pos)

            if self.resize_direction:
                # 开始拉伸
                self.is_resizing = True
                self.start_geometry = self.geometry()
                self.start_pos = event.globalPos()
            else:
                # 开始拖动
                self.draggable = True
                self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        pos = event.pos()

        # 设置光标形状 - 即使没有按下鼠标也更新
        direction = self.get_resize_direction(pos)
        self.set_cursor_shape(direction)

        # 处理窗口拉伸
        if self.is_resizing and self.resize_direction and self.start_geometry:
            current_pos = event.globalPos()
            diff = current_pos - self.start_pos

            new_geometry = QRect(self.start_geometry)

            if "top" in self.resize_direction:
                new_geometry.setTop(new_geometry.top() + diff.y())
                # 防止窗口高度过小
                if new_geometry.height() < self.minimumHeight():
                    new_geometry.setTop(new_geometry.bottom() - self.minimumHeight())

            if "bottom" in self.resize_direction:
                new_geometry.setBottom(new_geometry.bottom() + diff.y())
                # 防止窗口高度过小
                if new_geometry.height() < self.minimumHeight():
                    new_geometry.setBottom(new_geometry.top() + self.minimumHeight())

            if "left" in self.resize_direction:
                new_geometry.setLeft(new_geometry.left() + diff.x())
                # 防止窗口宽度过小
                if new_geometry.width() < self.minimumWidth():
                    new_geometry.setLeft(new_geometry.right() - self.minimumWidth())

            if "right" in self.resize_direction:
                new_geometry.setRight(new_geometry.right() + diff.x())
                # 防止窗口宽度过小
                if new_geometry.width() < self.minimumWidth():
                    new_geometry.setRight(new_geometry.left() + self.minimumWidth())

            self.setGeometry(new_geometry)

        # 处理窗口拖动
        elif event.buttons() == Qt.LeftButton and self.draggable:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.draggable = False
        self.is_resizing = False
        self.resize_direction = None
        self.start_geometry = None
        # 释放后恢复默认光标
        self.setCursor(Qt.ArrowCursor)

    def closeEvent(self, event):
        """窗口关闭时终止所有进程"""
        # 检查所有编辑标签页是否有未保存的修改
        unsaved_files = []
        for file_name, editor_tab in self.editor_tabs.items():
            if editor_tab.is_modified:
                unsaved_files.append(file_name)

        if unsaved_files:
            file_list = "\n".join(unsaved_files)
            reply = QMessageBox.question(self, "未保存的修改",
                                         f"以下文件有未保存的修改:\n{file_list}\n\n确定要退出吗?",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.No:
                event.ignore()
                return

        # 关闭所有标签页（包括终端标签页）
        for i in range(self.tab_widget.count() - 1, -1, -1):
            self.close_output_tab(i)

        # 确保所有进程都被终止
        for tab_name, output_tab in list(self.output_tabs.items()):
            output_tab.terminate_process()

        event.accept()


def is_admin():
    """检查当前进程是否以管理员权限运行"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()  # 非零为True
    except:
        return False  # 异常时默认非管理员


def request_admin_privileges():
    """请求提升管理员权限(重新启动程序并获取管理员身份)"""
    if not is_admin():  # 如果当前非管理员
        print("正在请求管理员权限...")
        # ShellExecuteW 是Windows API，用于启动新进程
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1
        )
        sys.exit()  # 退出当前非管理员进程,等待新进程启动


if __name__ == "__main__":
    # 请求管理员权限
    if platform.system() == 'Windows':
        request_admin_privileges()

    app = QApplication(sys.argv)

    # 设置应用样式
    app.setStyleSheet(AppStyles.global_stylesheet())

    window = FramelessWindow()
    window.setWindowTitle("阿炜的管理器")
    window.show()
    sys.exit(app.exec_())

