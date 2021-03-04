# 使い方
#    引数でディレクトリを指定．引数がないときは，
#   このプログラムが置かれているディレクトリ（「os.path.abspath(os.path.dirname(__file__))」で取得）を使用
#    プログラムを止めるには CTRL + C （同時押し）
# 参考Webページ
#    https://pythonhosted.org/watchdog/quickstart.html#a-simple-example

import hashlib
import os
import pathlib
import pprint
import sys
import time

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# from makeQRcode import makeQRcode

# 認証情報を生成
gauth = GoogleAuth()

# Creates local webserver and auto handles authentication.
gauth.LocalWebserverAuth() 

# 認証情報をもとにGoogleDriveFileオブジェクトを生成
drive = GoogleDrive(gauth)

class ChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        """
        ファイル作成検知
        :param event:
        :return:
        """
        # ファイル名取得
        src_name = os.path.basename(event.src_path)
        print(f'src_name: {src_name}')
        src_name = src_name.replace(".crdownload", "")
        print(f'src_name replaced: {src_name}')
        
        # makeQRcode(src_name)
        f = drive.CreateFile({'title' : 'picture.jpg',
            'mimeType' : 'image/jpeg'})
        f.SetContentFile(src_name)
        f.Upload()
        print(f'{src_name}をアップ完了')

        # パスの確認のため取得　最終的に削除する部分
        print('upload: ',f)

    
if __name__ == '__main__':
    # ディレクトリの取得と，カレントディレクトリの変更
    path = os.path.abspath(os.path.dirname(__file__))
    print("dirname: ",path)

    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
