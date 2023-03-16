from settings import LinkFTP

host = "192.168.125.129"
port = 21
username = ""
password = ""
local_path = r"./text.txt"
remote_path = r"./text.txt"
link_ftp = LinkFTP(host, port, username, password)
link_ftp.upload_file(remote_path, local_path)


