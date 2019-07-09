# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     book.py
#
from pagebot.conditions import *
from pagebot.publications.publication import Publication
from pagebot.elements import *
from pagebot.constants import *

class BaseCalendar(Publication):
    """Create a default calendar for the indicated year. 
    Add cover and monthly pages.

    >>> from pagebot.toolbox.dating import now
    >>> calendar = BaseCalendar(now().year, size=A4)
    >>> calendar.year == now().year
    True
    >>> calendar.size
    (210mm, 297mm)
    """

    # Default paper sizes that are likely to be used for 
    # books in portrait ratio.
    PAGE_SIZES = {
        'A2': A2,
        'B2': B2,
        'A3': A3,
        'B3': B3,
        'A4': A4,
        'B4': B4,
        'A5': A5,
        'B5': B5,
        'A2Square': A2Square,
        'A3Square': A3Square,
        'A4Square': A4Square,
        'HalfLetter': HalfLetter,
        'Letter': Letter,
        'Legal': Legal,
        'JuniorLegal': JuniorLegal,
        'Tabloid': Tabloid,
        'Ledger': Ledger,
        'Statement': Statement,
        'Executive': Executive,
        'Folio': Folio,
        'Quarto': Quarto,
        'Size10x14': Size10x14,
        'A4Letter': A4Letter,
        'A4Oversized': A4Oversized,
    }
    DEFAULT_PAGE_SIZE_NAME = 'A3Square'
    DEFAULT_PAGE_SIZE = PAGE_SIZES[DEFAULT_PAGE_SIZE_NAME]

    def __init__(self, year, **kwargs):
        Publication.__init__(self, **kwargs)
        self.year = year


if __name__ == "__main__":
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
