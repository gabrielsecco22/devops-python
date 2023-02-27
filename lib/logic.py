import wikipedia


def wiki(name="War Goddess", lenght=1):
    """This fetches wikipedia content"""

    return wikipedia.summary(name, lenght)
