#!/usr/bin/env python
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting usage of DrawBot, www.drawbot.com
#     Supporting usage of Flat, https://github.com/xxyxyz/flat
# -----------------------------------------------------------------------------
#
#     AlignElements.py
#
#     This script generates a page with aligned square, showing how conditional placement works.
#     Interactive Variable() only works in DrawBot context.
#
import pagebot # Import to know the path of non-Python resources.

# Creation of the RootStyle (dictionary) with all available default style parameters filled.
from pagebot.style import getRootStyle, CENTER, NO_COLOR, TOP, BOTTOM
# Document is the main instance holding all information about
# the document togethers (pages, styles, etc.)
from pagebot.document import Document
from pagebot.elements import *
# Import all layout condition classes
from pagebot.conditions import *

# Variables used as interactive globals in DrawBot context.
ShowOrigins = False
ShowElementInfo = False
ShowDimensions = False
PageSize = 500

W = H = PageSize

G = 8 # Distance between the squares.
SQ = 8 * G # Size of the squares

# Export in _export folder that does not commit in Git. Force to export PDF.
EXPORT_PATH = '_export/AlignElements.png'


def makeDocument():
    u"""Make a new document."""

    doc = Document(w=W, h=H, originTop=False, autoPages=1)

    page = doc[0] # Get the single page from te document.

    # Hard coded padding, just for simple demo, instead of filling padding an 
    # columns in the root style.
    page.padding = SQ

    # Position square in the 4 corners of the page area.
    # Notice that their alignment (left) does not matter for the conditions.
    newRect(w=SQ, h=SQ, parent=page,
            conditions=(Right2Right(),Top2Top()), fill=0.7)
    newRect(w=SQ, h=SQ, parent=page,
            conditions=(Left2Left(),Bottom2Bottom()), fill=0.7)
    newRect(w=SQ, h=SQ, parent=page,
            conditions=(Left2Left(),Top2Top()), fill=0.7)
    newRect(w=SQ, h=SQ, parent=page,
            conditions=(Right2Right(),Bottom2Bottom()), fill=0.7)

    # Make new container for adding elements inside with alignment.
    cnt = newRect(w=W-2*SQ, h=H-2*SQ,
                  fill=(0.8, 0.8, 0.8, 0.4),
                  parent=page, margin=SQ, yAlign=BOTTOM, 
                  xAlign=CENTER, stroke=None,
                  conditions=(Center2Center(), Middle2Middle()))

    # Add rectangles to the page,
    # using alignment conditions to position rules.
    newRect(w=SQ, h=SQ, stroke=None, parent=page, xAlign=CENTER,
            conditions=(Center2Center(), Middle2Middle()), fill=(1, 0, 0))
 
    conditions = [
         (Center2Center(),Top2Top()),
         (Center2Center(),Bottom2Bottom()),
         (Left2Left(),Middle2Middle()),
         (Right2Right(),Middle2Middle())
    ]
    for condition in conditions:
        newRect(w=SQ, h=SQ, stroke=None, parent=page, xAlign=CENTER,
                conditions=condition, fill=(1, 1, 0))

    sideConditions = [
         (Center2Center(),Top2TopSide()),
         (Center2Center(),Bottom2BottomSide()),
         (Left2LeftSide(),Middle2Middle()),
         (Right2RightSide(),Middle2Middle())
    ]
    for condition in sideConditions:
        newRect(w=SQ, h=SQ, stroke=None, parent=page, xAlign=CENTER,
                conditions=condition, fill=(0.5, 1, 0))

    cornerConditions = [
         (Left2LeftSide(),Top2TopSide()),
         (Right2RightSide(),Top2TopSide()),
         (Left2LeftSide(),Bottom2BottomSide()),
         (Right2RightSide(),Bottom2BottomSide())
    ]
    for condition in cornerConditions:
        newRect(w=SQ, h=SQ, stroke=None, parent=page, xAlign=CENTER,
                conditions=condition, fill=(0, 0, 1))
    # Solve the layout placement conditions on the page by moving the
    # elements that are not on the right positions (which is all of them,
    # because we did not add point attributes when creating them.

    score = page.solve()
    if score.fails:
        print('Failed to solve %d conditions:' % len(score.fails))
    for condition, e in score.fails:
        print(e.bottom2BottomSide())
        print(condition, e, e.bottom,
              Bottom2BottomSide().test(e),
              e.isBottomOnBottomSide(), e.bottom)

    # Get the current view of the document. This allows setting of
    # parameters how the document is represented on output.
    view = doc.view
    view.w, view.h = W, H
    # Set view options. Full list is in elements/views/baseviews.py
    view.padding = 30 # Showing cropmarks and registration marks
                      # need >= 20 padding of the view.
    view.showPageRegistrationMarks = True
    view.showPageCropMarks = True
    view.showPageFrame = True
    view.showPagePadding = True
    view.showPageNameInfo = True

    # These values can be changed in the Variable window,
    # when in DrawBot context.
    view.showElementOrigin = ShowOrigins # Show origin alignment
                                         # markers on each element.
    view.showElementDimensions = ShowDimensions
    view.showElementInfo = ShowElementInfo # Show boxes with element info

    return doc # Answer the doc for further doing.
  
if __name__ == '__main__':

    d = makeDocument()
    # Make interactive global controls. Only works in DrawBot context. Otherwise ignored.
    d.context.Variable([
        dict(name='ShowMeasures', ui='CheckBox', args=dict(value=True)),
        dict(name='ShowDimensions', ui='CheckBox', args=dict(value=False)),
        dict(name='ShowElementInfo', ui='CheckBox', args=dict(value=False)),
        dict(name='PageSize', ui='Slider', args=dict(minValue=100, value=400, maxValue=800)),
    ], globals())

    d.export(EXPORT_PATH) 

