#import the qrcode module

import qrcode

#customize the qrcode

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )

#add data here

qr.add_data("https://drive.google.com/file/d/15IYi0eOUoLyLg6M7NeHx7rSx2B9kRGME/view?usp=sharing")

#make the qr code

qr.make(fit = True)

img=qr.make_image(fill_color="black", back_color="white")

img.save("qrcode.png")

