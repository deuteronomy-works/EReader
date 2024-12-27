import os

import ebooklib
from ebooklib import epub

from handle_types import HandleTypes

fileIn = "./ex1.epub"

def save_book_details():
    _, filename = os.path.split(fileIn)
    name, _ = os.path.splitext(filename)
    if not os.path.exists(name):
        os.makedirs(name)

    os.chdir(name)


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

save_book_details()



for item in book.get_items():
    content = tags[item.get_type()](item)

