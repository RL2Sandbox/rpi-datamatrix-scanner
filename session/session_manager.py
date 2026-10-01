
# Session management
# Session management

session = {
    "barcode": None,
    "damage_image": None
}


def update_barcode(barcode):
    session["barcode"] = barcode


def update_damage(image_path):
    session["damage_image"] = image_path


def ready():
    return (
        session["barcode"] is not None
        and session["damage_image"] is not None
    )


def get_session():
    return session


def reset():
    session["barcode"] = None
    session["damage_image"] = None
