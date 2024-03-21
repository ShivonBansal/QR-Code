import qrcode

def generate_qr(link):
    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    return img

if __name__ == "__main__":
    # Get user input for the link
    link = input("Enter the link to encode in QR code: ")
    
    # Generate QR code
    qr_code = generate_qr(link)
    
    # Save the image or display it
    file_name = input("Enter the file name to save the QR code (including extension, e.g., qr_code.png): ")
    qr_code.save(file_name)
    print(f"QR code saved as {file_name}")
