import qrcode, os

# def makeQRcode():
file_name = "qr_code.png"
print("QRコードに変換したい文字列を入力してください: ", end="")

# キーボードから変換したい文字列を入力させる
qr_string = input()

# QRコード画像データ生成
img = qrcode.make(qr_string)

# 画像ファイルとして保存
img.save(file_name)

# 現在のディレクトリ位置を取得
current_dir = os.getcwd()

print("「{0}\\{1}」にQRコード画像を保存しました".format(current_dir, file_name))
