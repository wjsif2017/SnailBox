from hutil.Qt.QtCore import QUrl, QEventLoop
from hutil.Qt.QtNetwork import QNetworkAccessManager, QNetworkRequest

# 共享的全局 QNetworkAccessManager 实例
NET_MANAGER = QNetworkAccessManager()
ACTIVE_DOWNLOADS = set()  # 存储所有的下载任务


class S_Network:
    def __init__(self):
        self.manager = NET_MANAGER
        self.fun = None
        self.reply = None  # 存储 reply，防止 GC 回收
        self.event_loop = None  # 存储同步请求的事件循环（仅同步请求用）

    def start_workA(self, url, fun=None):
        """异步请求：回调函数处理数据"""
        self.fun = fun
        request = QNetworkRequest(QUrl(url))
        self.reply = self.manager.get(request)  # 发送 GET 请求
        self.reply.finished.connect(self.handle_response)  # 绑定回调
        ACTIVE_DOWNLOADS.add(self)  # 记录任务

    def start_workB(self, url):
        """同步请求：使用 QEventLoop 阻塞等待"""
        request = QNetworkRequest(QUrl(url))
        self.reply = self.manager.get(request)  # 发送 GET 请求

        # 创建 QEventLoop 并阻塞等待请求完成
        self.event_loop = QEventLoop()
        self.reply.finished.connect(self.event_loop.quit)  # 绑定退出事件
        ACTIVE_DOWNLOADS.add(self)  # 记录任务
        self.event_loop.exec_()  # 进入事件循环，阻塞直到请求完成

        return self.handle_response()  # 返回请求结果

    def handle_response(self):
        """处理 HTTP 响应"""
        try:
            if self.reply is None:
                print("Error: No active reply")
                return None

            if self.reply.error():
                print(f"下载失败: {self.reply.errorString()}")
                return None  # 返回 None 表示请求失败

            data = self.reply.readAll().data()  # 读取数据
            if self.fun:
                self.fun(data)  # 异步请求回调
            else:
                return data  # 同步请求返回数据

        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            if self in ACTIVE_DOWNLOADS:
                ACTIVE_DOWNLOADS.discard(self)  # 确保只移除一次
            if self.reply:
                self.reply.deleteLater()  # 释放资源
                self.reply = None  # 防止后续访问已删除的 reply

    def cancel(self):
        """取消当前下载"""
        if self.reply:
            self.reply.finished.disconnect()  # 先断开 finished 绑定，防止触发 handle_response
            self.reply.abort()  # 终止下载
            print("下载已取消")
        if self in ACTIVE_DOWNLOADS:
            ACTIVE_DOWNLOADS.discard(self)  # 确保只移除一次
        if self.reply:
            self.reply.deleteLater()  # 释放资源
            self.reply = None  # 防止后续访问已删除的 reply


def cancel_all_downloads():
    """取消所有进行中的下载"""
    global ACTIVE_DOWNLOADS
    for network in list(ACTIVE_DOWNLOADS):  # 遍历所有活跃的下载实例
        network.cancel()
    ACTIVE_DOWNLOADS.clear()  # 确保所有任务都被移除
    print("所有下载已取消")
