from control_book.utils import add_preview_image

def before_save(doc, method=None):
    add_preview_image(doc)
