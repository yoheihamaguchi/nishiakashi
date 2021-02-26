from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
import pprint

# 認証情報を生成
gauth = GoogleAuth()

# Creates local webserver and auto handles authentication.
gauth.LocalWebserverAuth() 

# 認証情報をもとにGoogleDriveFileオブジェクトを生成
drive = GoogleDrive(gauth)
f = drive.CreateFile()
print('before',f)

# アップロードするfileを設定
f.SetContentFile('./images/onepiece01_luffy.png')
p = os.path.basename('./images/onepiece01_luffy.png')
f['title'] = p
print('after',f)

id = drive.ListFile({'q':'title= "onepiece01_luffy.png"'}).GetList()[0]['id']
f = drive.CreateFile({'id':id})
print('id: ',f['id'])
print('title: ',f['title'])
permissions = f.GetPermissions()
print(permissions)