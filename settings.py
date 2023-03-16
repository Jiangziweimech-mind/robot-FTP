# !/usr/bin/python
# -*- coding: utf-8 -*-

from ftplib import FTP


class LinkFTP:
    """
    连接 FTP 服务器
    """

    def __init__(self, host: str, port: int, username: str, password: str):
        ftp_ = FTP()
        # 连接
        ftp_.connect(host, port)
        # 登录
        ftp_.login(username, password)
        print(f"{host} {port} {username} {password} 连接成功")
        self.ftp = ftp_
        self.buffer_size = 2048

    def download_file(self, remote_path: str, local_path: str) -> None:
        """
        从 ftp 下载文件
        :param remote_path: 远程服务器的目录绝对路径
        :param local_path:
        :return:
        """
        with open(local_path, 'wb') as fp:
            self.ftp.retrbinary('RETR ' + remote_path, fp.write, self.buffer_size)
            self.ftp.set_debuglevel(0)

    def upload_file(self, remote_path: str, local_path: str) -> None:
        """
        从本地上传文件到 ftp
        :param remote_path: 远程服务器的目录绝对路径
        :param local_path:
        :return:
        """
        with open(local_path, 'rb') as fp:
            self.ftp.storbinary('STOR ' + remote_path, fp, self.buffer_size)
            self.ftp.set_debuglevel(0)

    def path_list(self, path: str) -> list:
        """
        获取路径信息
        :param path: 路径
        :return:
        """
        # 获取 ftp
        ftp = self.ftp
        # 切换路径
        ftp.cwd(path)
        # 显示目录下所有目录信息
        ftp.dir()
        # 获取目录下的文件夹
        dir_list: list = ftp.nlst()
        # 排序
        dir_list.sort()
        return dir_list

    def current_path(self):
        ftp = self.ftp
        return ftp.pwd()





