def overlay_serializer(overlay):
    return {
        "id": str(overlay["_id"]),
        "x": overlay["x"],
        "y": overlay["y"],
        "width": overlay["width"],
        "height": overlay["height"],
        "content": overlay["content"],
        "type": overlay["type"]  # text or image
    }
