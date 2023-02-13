#*************** Basic QRCode #***************#
# import qrcode as qr
'''
############# QRCode of URL #############
img = qr.make("https://www.google.co.in/")
img.save("MyQR.png")
'''

'''
############# QRCode of Text #############
img = qr.make("Chatrapati Shivaji Maharaj")
img.save("Swarajya Sansthapan.png")
'''

#*************** Advance QRCode #***************#
import qrcode 
from PIL import Image  # PIL means Pillow

'''
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
    )
qr.add_data("https://www.google.co.in/")
qr.make(fit=True)
img = qr.make_image(fill_color="gold",back_color="black")
img.save("Advance_QRCode_googlelink2.png")
'''


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=10,
    )
qr.add_data("https://www.google.co.in/")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="white")
img.save("Advance_QRCode_googlelink2.png")



