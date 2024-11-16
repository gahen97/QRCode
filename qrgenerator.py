import image
import qrcode

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 10
)


satisfy = "No"

while (satisfy == "No"):
    website = input("Please enter the URL link to generate the QR code for: ")
    print("The URL is:" + str(website))
    satisfy = input("Are you satisfied with this URL? (Yes/No)")
    
    while (satisfy != "Yes" and satisfy != "No"):
        satisfy = input("Invalid response. Please only type in Yes or No.")
    


qr.add_data(website)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color="white")
img.save("qr_code.png")