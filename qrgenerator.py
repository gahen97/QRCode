import image
import qrcode

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 10
)

website = "https://www.google.ca/"

qr.add_data(website)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color="white")
img.save("qr_code.png")