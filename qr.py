import qrcode

image = qrcode.make("https://127.0.01:8000")
image.save('qr.png')