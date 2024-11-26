def before_save(doc, method=None):
    for item in doc.bill_of_quantity_id:
        if item.attach_image_wjpb:
            item.custom_picture = f"<img src='{item.attach_image_wjpb}' width=32 style='margin-top: -6px; height: 32px !important; ' />"
        else:
            item.custom_picture = ""
