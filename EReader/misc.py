

READER_CSS_PATH = "./css/reader.css"
USER_CONTENT_FOLDER= "../user_contents/"


def reader_html_replacer(index_file: str, nav_file: str) -> None:

    with open("./reader.html", 'r') as reader_file:
        replaced = reader_file.read()

    index_file = USER_CONTENT_FOLDER + index_file
    nav_file = USER_CONTENT_FOLDER + nav_file

    # replace css
    replaced = replaced.replace("{{CSS_FILE}}", READER_CSS_PATH)

    # replace index
    replaced = replaced.replace("{{INDEX_FILE}}", index_file)

    # replace nav
    replaced = replaced.replace("{{NAV_FILE}}", nav_file)

    with open("./reader_files/reader.html", 'w') as reader_file:
        reader_file.write(replaced)
