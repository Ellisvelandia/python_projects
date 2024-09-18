import qrcode

data = input("Enter text or URL: ").strip()
file_name = input("Enter name of file: ").strip()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)

image = qr.make_image(fill_color="black", back_color="white")

image.save(file_name)

print(f"QR code generated successfully! {file_name}")