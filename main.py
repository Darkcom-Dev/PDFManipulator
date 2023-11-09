import PyPDF2 as pdf
import os
import argparse

def get_info(file):
    with open(file, 'rb') as f:
        pdfile = pdf.PdfReader(f)
        info = pdfile.metadata
        number_of_pages = len(pdfile.pages)
        print(info)
        print(f'title: {info.title}')
        print(f'author: {info.author}')
        print(f'subject: {info.subject}')
        print(f'creator: {info.creator}')
        print(f'producer: {info.producer}')
        print(number_of_pages)


def version():
    print(f'argparse version: {argparse.__version__}')
    print(f'PyPDF2 version: {pdf.__version__}')

parser = argparse.ArgumentParser(description="Split or Join PDF")

def split(file, page, *output):
    print("Splitting PDF")
    print(f'file: {file}, page: {page}')
    print(f'output: {output}')

    with open(file, "rb") as f:
        pdfile = pdf.PdfReader(f)
        pages = pdfile.pages
        # print(pages[page].extract_text())

        pdf_writer = pdf.PdfWriter()

        for i in range(0, page):
            pdf_writer.add_page(pages[i])

        pdf_writer_2 = pdf.PdfWriter()

        for j in range(page, len(pages)):
            pdf_writer_2.add_page(pages[j])

        with open(output[0], "wb") as f:
            pdf_writer.write(f)

        with open(output[1], "wb") as f:
            pdf_writer_2.write(f)
        # page_data = pdfile.reader.pages(list(page))
        # print(page_data.extract_text())



def join(output, *files):
    print("Joining PDF")
    print(f'files: {files}')
    print(f'output: {output}')

    merger = pdf.PdfMerger()
    for file in files:
        pdffile = pdf.PdfReader(open(file,'rb'))
        merger.append(pdffile)

    with open(output, 'wb') as f:
        merger.write(f)

    merger.close()

def main():
    #split("Scrum.pdf", 2 ,"SCR1.pdf", "SCR2.pdf")
    pass


if __name__ == "__main__":
    parser.add_argument(
        "-i", "--input", nargs="+", help="Input PDF file(s)", required=True
    )
    parser.add_argument(
        "-o", "--output", nargs="+", help="Output PDF file(s)", required=True
    )
    parser.add_argument(
        "-s", "--split", help="Split PDF", action="store_true"
    )
    parser.add_argument(
        "-j", "--join", help="Join PDF", action="store_true"
    )
    parser.add_argument(
        "-n", "--number", help="Number of pages to split", type=int
    )
    parser.add_argument(
        "-l", "--length", help="Length of each page", type=int
    )
    parser.add_argument(
        "-p", "--page", help="Page to split", type=int
    )
    parser.add_argument(
        "-v", "--version", action="version", version=version
    )
    parser.add_argument(
        "-g", "--get_info", action="store_true", help="Get info from PDF"
    )
    args = parser.parse_args()

    if args.split:
        if not args.output:
            print("Please specify an output file")
            main()
        if type(args.output) != list:
            print("Please specify an output file")
            main()
        if type(args.page) != int:
            print("Please specify a page integer")
            main()
        else:
            split(args.input[0], args.page, *args.output)
    elif args.join:
        if not args.output:
            print("Please specify an output file")
            main()
        if type(args.output) != list:
            print("Please specify an output file")
            main()
        else:
            join(args.output[0], *args.input)
    elif args.get_info:
        get_info(args.input[0])
    
if __name__ == "__maini__":
    """
    parser.add_argument(
        "-i", "--input", nargs="+", help="Input PDF file(s)", required=True
    )
    parser.add_argument(
        "-o", "--output", nargs="+", help="Output PDF file(s)", required=True
    )
    args = parser.parse_args()
    #join(args.output[0], *args.input)
    """
    main()
