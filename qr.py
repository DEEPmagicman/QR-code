import PyPDF2
import qrcode


def main():
    pdffile = "medical.pdf"
    pdfRead = PyPDF2.PdfFileReader(pdffile)
    page = pdfRead.getPage(0)
    pageContent = page.extractText()
    print(pageContent)

    #QR code
    qr = qrcode.QRCode( version=1, box_size=10,border=5)
    data = pageContent
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black",back_color="white")
    img.save("scan.png")
    print("QR Code Generated")


if __name__ == "__main__":
    main()
