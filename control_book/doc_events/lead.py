def before_save(doc, method=None):
    for item in doc.custom_bill_of_quantity:
        if item.attach_image_wjpb:
            item.preview_image = f"<img src='{item.attach_image_wjpb}' width=32 style='margin-top: -6px; height: 32px !important; ' />"
        else:
            item.preview_image = ""
