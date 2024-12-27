import ebooklib
from ebooklib import epub

fileIn = "./ex1.epub"
fileOut = "out01.html"

book = epub.read_epub(fileIn)
content = ""

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        bodyContent = item.get_body_content().decode()
        content += bodyContent

with open(fileOut, 'w', encoding='utf-8') as fout:
        fout.write(content)
