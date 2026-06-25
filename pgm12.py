import qrcode
def generate_qr(data,filename="qrcode.png"):
    qr=qrcode.make(data)
    qr.save(filename)
    print("QR Code saved as",filename)
generate_qr("D:\AGV\agv")
