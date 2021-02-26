import qrcode, os

def makeQRcode(qr_string):
    file_name = "picture.png"

    # QRコード画像データ生成
    img = qrcode.make(qr_string)

    # 画像ファイルとして保存
    img.save(file_name)
