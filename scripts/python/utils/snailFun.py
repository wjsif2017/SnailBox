import threading
import hou


SNAIL_DBUG = False


def display_status(message, severity_level=1):  # 显示状态栏消息
    if SNAIL_DBUG:
        print(message)
        return
    severity_dict = {
        0: hou.severityType.Message,
        1: hou.severityType.ImportantMessage,
        2: hou.severityType.Warning,
        3: hou.severityType.Error,
        4: hou.severityType.Fatal,
    }
    # message = "*" * 10 + message + "*" * 10
    severity = severity_dict[severity_level]
    hou.ui.setStatusMessage(message, severity=severity)

    def clear_status_message():
        hou.ui.setStatusMessage("")

    threading.Timer(10, clear_status_message).start()
