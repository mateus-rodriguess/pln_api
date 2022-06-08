from slugify import slugify

def validation(username: str):
    """
    ....
    """
    return slugify(username,lowercase=False)
  