# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Type Network, www.typenetwork.com, www.pagebot.io
#     Licensed under MIT conditions
#     Made for usage in DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     oval.py
#
from __future__ import division # Make integer division result in float.
from drawBot import oval

from pagebot import setStrokeColor, setFillColor
from pagebot.style import NO_COLOR
from pagebot.elements.element import Element
from pagebot.toolbox.transformer import pointOffset

class Oval(Element):
    def __init__(self, point=None, parent=None, style=None, name=None, eId=None, **kwargs):
        Element.__init__(self, point=point, parent=parent, style=style, name=name, eId=eId, **kwargs)
        # Initialize the default Element behavior tags.
        self.isContainer = False
        self.isText = False
        self.isFlow = False

    def draw(self, origin):
        p = pointOffset(self.point, origin)
        p = self._applyOrigin(p)    
        p = self._applyScale(p)    
        px, py, _ = self._applyAlignment(p) # Ignore z-axis for now.
        
        setFillColor(self.css('fill', NO_COLOR))
        setStrokeColor(self.css('stroke', NO_COLOR), self.css('strokeWidth'))
        oval(px, py, self.w, self.h)

        self._restoreScale()
        self._drawElementInfo(origin) # Depends on css flag 'showElementInfo'
