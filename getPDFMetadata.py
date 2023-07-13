import PyPDF2
import optparse

def printMetadata(fileName):
    pdfFile = open(fileName, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    pdfInfo = pdfReader.metadata
    print("[*] Metadata of the PDF: ", str(fileName))
    for metaItem in pdfInfo:
        print("[+]" + metaItem + ":" + pdfInfo[metaItem])

def run():
    parser = optparse.OptionParser()
    parser.add_option("-f", dest='fileName', type='string', help="give the PDF file name")
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print("Usage: getPDFMetadata.py -f <PDF file name>")
        exit(0)
    else:
        printMetadata(fileName)

if __name__ == "__main__":
    run()