def add_preview_image(doctype):
    for item in doctype.items:
        if item.image:
            item.custom_picture = f"<img src='{item.image}' width=32 style='margin-top: -6px; height: 32px !important; ' />"
        else:
            item.custom_picture = ""
