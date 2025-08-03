import argparse
import os
import markdown
from weasyprint import HTML
from weasyprint import CSS

css_path = os.path.join(os.path.dirname(__file__), "style.css")

def md_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_content = markdown.markdown(md_content)
    HTML(string=html_content).write_pdf(pdf_path, stylesheets=["style.css"])

    print(f"✅ PDF generated: {pdf_path}")

def main():
    parser = argparse.ArgumentParser(
        description="📄 Convert a Markdown (.md) file to a styled PDF",
        epilog="""
Example usage:
  python md2pdf.py --mdfile proposal.md
  python md2pdf.py --mdfile notes.md --pdffile D:\\Docs\\notes.pdf

If --pdffile is not provided, the output will be saved to:
  C:\\temp\\<mdfilename>.pdf
""",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '--mdfile',
        required=True,
        help="Path to the input Markdown (.md) file"
    )

    parser.add_argument(
        '--pdffile',
        help="Optional path to save the output PDF file"
    )

    args = parser.parse_args()

    md_path = args.mdfile
    if not os.path.isfile(md_path):
        print(f"❌ Markdown file not found: {md_path}")
        return

    if args.pdffile:
        pdf_path = args.pdffile
    else:
        filename = os.path.splitext(os.path.basename(md_path))[0]
        pdf_path = f"C:\\temp\\{filename}.pdf"

    md_to_pdf(md_path, pdf_path)

if __name__ == "__main__":
    main()
