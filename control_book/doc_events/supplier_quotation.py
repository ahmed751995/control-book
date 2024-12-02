def before_save(doc, method=None):
    for item in doc.items:
        if item.image:
            item.custom_picture = f"<img src='{item.image}' width=32 style='margin-top: -6px; height: 32px !important; ' />"
        else:
            item.custom_picture = ""
