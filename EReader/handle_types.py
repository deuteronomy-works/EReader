import os

class HandleTypes:

    @staticmethod
    def save_bytes_content(filename, content):
        folder, name = os.path.split(filename)
        if folder:
            os.makedirs(folder)
        with open(filename, mode='wb') as raw_file:
            raw_file.write(content)
    
    @staticmethod
    def save_content(filename, content):
        folder, name = os.path.split(filename)
        if folder:
            os.makedirs(folder)
        with open(filename, mode='wb') as write_file:
            write_file.write(content)

    @staticmethod
    def ITEM_UNKNOWN(item):
        print(item.get_name())
        content = item.get_content()
        return content

    @staticmethod
    def ITEM_IMAGE(item):
        print(item.get_name())
        content = item.get_content()
        return content

    @staticmethod
    def ITEM_STYLE(item) :
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_SCRIPT(item):
        print(item.get_name())
        content = item.get_content()
        return content

    @staticmethod
    def ITEM_NAVIGATION(item):
        print(item.get_name())
        content = item.get_content()
        return content

    @staticmethod
    def ITEM_VECTOR(item):
        print(item.get_name())
        content = item.get_content()
        return content

    @staticmethod
    def ITEM_FONT(item):
        print(item.get_name())
        content = item.get_content()
        return content

    @staticmethod
    def ITEM_VIDEO(item):
        print(item.get_name())
        content = item.get_content()
        return content

    @staticmethod
    def ITEM_AUDIO(item):
        print(item.get_name())
        content = item.get_content()
        return content

    @staticmethod
    def ITEM_DOCUMENT(item):
        print(item.get_name())
        content = item.get_body_content()
        return content

    @staticmethod
    def ITEM_COVER(item):
        print(item.get_name())
        content = item.get_content()
        return content

    @staticmethod
    def ITEM_SMIL(item):
        print(item.get_name())
        content = item.get_content()
        return content
