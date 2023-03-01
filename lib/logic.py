import wikipedia


def wiki(name="War Goddess", lenght=1):
    """This fetches wikipedia content"""

    return wikipedia.summary(name, lenght)

def search_wiki(name):
    """Search wikipedia for names"""

    return wikipedia.search(name)
