import qrcode

# Platform-aware download page: sends iOS visitors to the App Store,
# Android visitors to Google Play, everyone else to the landing page.
# Trailing slash is deliberate -- it avoids a 301 hop on scan.
url = 'https://ghefman.github.io/SimplePdfUtils/get/'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
img.save('qrcode.png')

print('QR code saved as qrcode.png')
