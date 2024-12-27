import os

class HandleTypes:

    @staticmethod
    def save_bytes_content(filename, content):
        folder, name = os.path.split(filename)
        if folder and  not os.path.exists(folder):
            os.makedirs(folder)

        with open(filename, mode='wb') as raw_file:
            raw_file.write(content)
    
    @staticmethod
    def save_content(filename, content):
        folder, name = os.path.split(filename)
        if folder and  not os.path.exists(folder):
            os.makedirs(folder)
        
        with open(filename, mode='wb') as write_file:
            write_file.write(content)

    @staticmethod
    def ITEM_UNKNOWN(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_IMAGE(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_STYLE(item) :
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_SCRIPT(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_NAVIGATION(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_VECTOR(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_FONT(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_VIDEO(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_AUDIO(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_DOCUMENT(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_COVER(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content

    @staticmethod
    def ITEM_SMIL(item):
        HandleTypes.save_content(item.get_name(),item.get_content())
        content = ""
        return content
