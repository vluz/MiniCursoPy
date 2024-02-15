import pyqrcode


qr = pyqrcode.create("https://www.startupbarreiro.pt/")
qr.png("codigoQR.png", scale=10)