from pathlib import Path
import sys
from pdf2image import convert_from_path


def pdf_to_jpg(pdf_path):
    pdf_path = Path(pdf_path)

    # extract PDF name (without extension) to use as folder name
    output_dir = pdf_path.stem
    output_dir_path = pdf_path.parent / output_dir
    output_dir_path.mkdir(exist_ok=True)

    pages = convert_from_path(pdf_path)

    # save each page as a JPEG
    for i, page in enumerate(pages, start=1):
        output_path = output_dir_path / f"page_{i}.jpg"
        page.save(output_path, "JPEG")

    print(f"Saved all pages to folder: {output_dir}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_jpg.py <path_to_pdf>")
        sys.exit(1)

    pdf_file_path = sys.argv[1]
    pdf_to_jpg(pdf_file_path)
