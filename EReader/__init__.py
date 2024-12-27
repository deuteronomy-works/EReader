import ebooklib
from ebooklib import epub
from handle_types import HandleTypes

fileIn = "./ex2.epub"
fileOut = "tags_view.txt"


book = epub.read_epub(fileIn)
content = ""
tags = {
      ebooklib.ITEM_UNKNOWN : HandleTypes.ITEM_UNKNOWN,
ebooklib.ITEM_IMAGE : HandleTypes.ITEM_IMAGE,
ebooklib.ITEM_STYLE : HandleTypes.ITEM_STYLE,
ebooklib.ITEM_SCRIPT: HandleTypes.ITEM_SCRIPT,
ebooklib.ITEM_NAVIGATION: HandleTypes.ITEM_NAVIGATION,
ebooklib.ITEM_VECTOR: HandleTypes.ITEM_VECTOR,
ebooklib.ITEM_FONT: HandleTypes.ITEM_FONT,
ebooklib.ITEM_VIDEO: HandleTypes.ITEM_VIDEO,
ebooklib.ITEM_AUDIO: HandleTypes.ITEM_AUDIO,
ebooklib.ITEM_DOCUMENT: HandleTypes.ITEM_DOCUMENT,
ebooklib.ITEM_COVER: HandleTypes.ITEM_COVER,
ebooklib.ITEM_SMIL: HandleTypes.ITEM_SMIL
}

ind = 0
for item in book.get_items():
    ind += 1
    if ind < 5:
          continue
    content = tags[item.get_type()](item)
    """ if item.get_type() == ebooklib.ITEM_DOCUMENT:
        bodyContent = item.get_body_content().decode()
        content += bodyContent """
    break

with open(fileOut, 'wb') as fout:
        fout.write(content)
