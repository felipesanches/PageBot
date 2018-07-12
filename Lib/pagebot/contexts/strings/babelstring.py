# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     babelstring.py
#

class BabelString(object):
    """BabelString is the base class of various types of (formatted) string representations 
    needed for different builder classes."""

    def __init__(self, s, context, style=None):
        self.s = s # Enclose the Flat/Drawbot/html string in this wrapper.
        self.style = style # Optional style to set the context parameters.
        self.context = context

    def __repr__(self):
        return u'%s' % self.s

    def __add__(self, s):
        self.append(s)
        return self

    def __mul__(self, d):
        s = self.s
        for n in range(d-1):
            s += self.s
        self.s = s
        # Something to do with the html? 
        return self

    def __len__(self):
        return len(self.s)

    def append(self, s):
        """Append string or FlatString to self."""
        try:
            self.s += s.s
        except (TypeError, AttributeError):
            self.s += s # Convert to babel string, whatever it is.

    def type(self):
        """Answer the id of the class, in case a caller wants to know what kind of 
        BabelString this is."""
        return self.BABEL_STRING_TYPE

    def _get_w(self):
        return self.size()[0]
    w = property(_get_w)

    def _get_h(self):
        return self.size()[1]
    h = property(_get_h)

    def size(self):
        """Answer the size tuple (w, h) of the string."""
        return self.context.textSize(self)


if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
