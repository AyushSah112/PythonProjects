import qrcode

data = input("Enter your URL\n ")
qr = qrcode.make(data)
file_name = input("Enter your file name ") + ".png"
qr.save(file_name)

print(f"QRcode saved as {file_name} ")