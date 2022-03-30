from PyPDF2 import PdfFileReader, PdfFileWriter


def encrypt_file(file_in: str, file_out: str, pw: str):
    pdf_in = PdfFileReader(file_in)
    pdf_out = PdfFileWriter()

    for i in range(pdf_in.numPages):
        pdf_out.addPage(pdf_in.getPage(i))

    with open(file_out, "wb") as f:
        pdf_out.encrypt(pw)
        pdf_out.write(f)


if __name__ == '__main__':
    encrypt_file('cv.pdf', 'cve.pdf', '123456')
