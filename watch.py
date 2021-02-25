# 使い方
#    引数でディレクトリを指定．引数がないときは，
#   このプログラムが置かれているディレクトリ（「os.path.abspath(os.path.dirname(__file__))」で取得）を使用
#    プログラムを止めるには CTRL + C （同時押し）
# 参考Webページ
#    https://pythonhosted.org/watchdog/quickstart.html#a-simple-example

import sys
import time
import os
import hashlib
import pathlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ChangeHandler(FileSystemEventHandler):
    # def __init__(self):
    #     with open(FILENAME, 'rb') as f:
    #         # 最後のイベント時でのファイルの md5 ハッシュ値を入れておく
    #         self.oldmd5 = hashlib.md5(f.read()).hexdigest()
    #         # 最後のイベント時でのファイルの pos 値を入れておく
    #         self.pos = f.tell()
    def on_deleted(self, event):
        """
        ファイル削除検知
        :param event:
        :return:
        """
        src_name = os.path.basename(event.src_path)
        print(f'{src_name}を削除しました')

    def on_created(self, event):
        """
        ファイル作成検知
        :param event:
        :return:
        """
        # ファイル名取得
        src_name = os.path.basename(event.src_path)
        print(f'{src_name}ができました')

if __name__ == '__main__':
    # ディレクトリの取得と，カレントディレクトリの変更
    if len(sys.argv) > 1:
        path = sys.argv[1]
        os.chdir(path)
    else:
        path = os.path.abspath(os.path.dirname(__file__))

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