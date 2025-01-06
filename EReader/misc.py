

READER_CSS_PATH = "./reader_files/css/reader.css"


def reader_html_replacer(index_file: str, nav_file: str) -> str:

    with open("./reader.html", 'w') as reader_file:
        replaced = reader_file.read()

    # replace css
    replaced = replaced.replace("{{CSS_FILE}}", READER_CSS_PATH)

    # replace index
    replaced = replaced.replace("{{INDEX_FILE}}", index_file)

    # replace nav
    replaced = replaced.replace("{{NAV_FILE}}", nav_file)

    return replaced
