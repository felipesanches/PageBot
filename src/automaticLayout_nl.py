import os
import weakref
import fontTools
import copy
import xml.etree.ElementTree as ET

import document 
reload(document)
from document import Document, Page, Composer, Template, Galley, getRootStyle

FILENAME = 'automaticLayout_nl.md' # 'automaticLayout_nl.md'
TITLE = 'Automatic Layout'

# ELement id of the text box on pages the hold the main text flow.
MAIN_FLOW = 'main' 

# Tracking presets for tag styles.
H1_TRACK = H2_TRACK = 0.015
H3_TRACK = 0.030 # Tracking as relative factor to font size.
P_TRACK = 0.030

if 1:
    BOOK = 'Productus-Book'
    BOOK_ITALIC = 'Productus-BookItalic'
    BOLD = 'Productus-Bold'
    SEMIBOLD = 'Productus-Semibold'
    MEDIUM = 'Productus-Medium'
else:
    BOOK = MEDIUM = 'Georgia'
    BOOK_ITALIC = 'Georgia-Italic'
    BOLD = SEMIBOLD = 'Georgia-Bold'

rs = getRootStyle()

# Alter basic layout measures 
rs.u = U = 7
rs.pw = 595 # Page width 210mm, international generic fit.
rs.ph = 11 * 72 # Page height 11", international generic fit.
rs.ml = 7*U # Margin left
rs.mt = 7*U # Margin top
rs.baselineGrid = 2*U
rs.cw = 11*U # Column width. 
rs.g = U # Generic gutter.
rs.ch = rs.baselineGrid - rs.g # Approx. square. Fit with baseline.
rs.listTabs = [(U*0.8, 'left')] # Default indent for bullet lists
# Display option
rs.gridStroke = 0.8
rs.showGrid = True
rs.showBaselineGrid = True
# Text measures
rs.leading = rs.baselineGrid
rs.fontSize = 10
rs.font = BOOK
# Language settings
rs.language = 'nl-be'

BOX_COLOR = rs.noColor # Optonal fill color to mark columns.

# -----------------------------------------------------------------         
def makeDocument():
    u"""Demo page composer."""

    # Set some values of the default template (as already generated by the document).
    # Make squential unique names for the flow boxes inside the templates
    flowId0 = MAIN_FLOW+'0' 
    flowId1 = MAIN_FLOW+'1'
    flowId2 = MAIN_FLOW+'2'
    
    # Template 1
    template1 = Template(rs.w, rs.h, rs) # Create template of main size. Front page only.
    if rs.showGrid: # Enable to show grid columns and margins.
        template1.grid() 
    if rs.showBaselineGrid: # Enable to show baseline grid.
        template1.baselineGrid()
    # Create empty image place holders. To be filled by running content on the page.
    # Since there is no style yet, templates cannot use cImage, etc.
    template1.cImage(None, 4, 0, 2, 4) 
    template1.cImage(None, 0, 5, 2, 3)
    # Create linked text boxes. Note the "nextPage" to keep on the same page or to next.
    template1.cTextBox('', 0, 0, 2, 5, flowId0, nextBox=flowId1, nextPage=0, fill=BOX_COLOR)
    template1.cTextBox('', 2, 0, 2, 8, flowId1, nextBox=flowId2, nextPage=0, fill=BOX_COLOR)
    template1.cTextBox('', 4, 4, 2, 4, flowId2, nextBox=flowId0, nextPage=1, fill=BOX_COLOR)
    # Create page number box. Pattern PAGENUMBER is replaced by actual page number.
    template1.cText(rs.pageNumberMarker, 6, 0, font=rs.font, fontSize=12, fill=BOX_COLOR)

    # Template 2
    template2 = Template(rs.w, rs.h, rs) # Create second template. This is for the main pages.
    if rs.showGrid: # Enable to show grid columns and margins.
        template2.grid() 
    if rs.showBaselineGrid: # Enable to show baseline grid.
        template2.baselineGrid()
    template2.cImage(None, 4, 0, 2, 3)
    template2.cImage(None, 0, 5, 2, 3)
    template2.cImage(None, 2, 2, 2, 2)
    template2.cImage(None, 2, 0, 2, 2)
    template2.cImage(None, 4, 6, 2, 2)
    template2.cTextBox('', 0, 0, 2, 5, flowId0, nextBox=flowId1, nextPage=0, fill=BOX_COLOR)
    template2.cTextBox('', 2, 4, 2, 4, flowId1, nextBox=flowId2, nextPage=0, fill=BOX_COLOR)
    template2.cTextBox('', 4, 3, 2, 3, flowId2, nextBox=flowId0, nextPage=1, fill=BOX_COLOR)
    # Create page number box. Pattern PAGENUMBER is replaced by actual page number.
    template2.cText(rs.pageNumberMarker, 6, 0, font=rs.font, fontSize=12, fill=BOX_COLOR)
   
    # Create new document with (w,h) and fixed amount of pages.
    # Make number of pages with default document size.
    # Initially make all pages default with template2
    doc = Document(rs, TITLE, template=template2, pages=2) 
     
    # Add styles for whole document and text flows.  
    doc.newStyle(name='document')
    doc.newStyle(name='page')             
    doc.newStyle(name='chapter', font=BOOK)    
    doc.newStyle(name='title', fontSize=rs.fontSize*3, font=BOLD)
    doc.newStyle(name='subtitle', fontSize=rs.fontSize*1.5, font=BOOK_ITALIC)
    doc.newStyle(name='author', fontSize=rs.fontSize*1.5, font=BOOK, fill=(1, 0, 0))
    doc.newStyle(name='h1', fontSize=rs.fontSize*2, font=SEMIBOLD, fill=0.1, stroke=None,
        leading=20, rLeading=0, tracking=H1_TRACK, needsBelow=rs.needsBelow)
    doc.newStyle(name='h2', fontSize=rs.fontSize*1.5, font=SEMIBOLD, fill=0.2, stroke=None, 
        leading=20, rLeading=0, tracking=H2_TRACK, needsBelow=rs.needsBelow)
    doc.newStyle(name='h3', fontSize=rs.fontSize*1.2, font=MEDIUM, fill=0, 
        leading=15, rLeading=0, needsBelow=rs.needsBelow,
        tracking=H3_TRACK, paragraphTopSpacing=rs.u, paragraphBottomSpacing=rs.u/2)
    
    # Spaced paragraphs.
    doc.newStyle(name='p', fontSize=rs.fontSize, font=BOOK, fill=0.1, 
        stroke=None, tracking=P_TRACK, language=rs.language, align=rs.align,
        leading=rs.leading, rLeading=rs.rLeading, hyphenation=rs.hyphenation, 
        stripWhiteSpace=' ')
    doc.newStyle(name='b', font=SEMIBOLD, stripWhiteSpace=' ')
    doc.newStyle(name='em', font=BOOK_ITALIC, stripWhiteSpace=' ')
    doc.newStyle(name='img', leading=rs.leading, rLeading=rs.rLeading,
        fontSize=rs.fontSize, font=BOOK,)
    
    # Footnote reference index.
    doc.newStyle(name='sup', font=MEDIUM, 
         rBaselineShift=0.6, fontSize=14*0.65, stripWhiteSpace=' ')
    doc.newStyle(name='li', fontSize=rs.fontSize, font=BOOK, 
        tracking=P_TRACK, leading=rs.leading, rLeading=rs.rLeading,
        hyphenation=True, indent=rs.listIndent, firstLineIndent=1, 
        #tailIndent=U, 
        stripWhiteSpace=' ')
    doc.newStyle(name='ul', stripWhiteSpace=' ',)
    doc.newStyle(name='literatureref', stripWhiteSpace=False,
        fill=0.5, rBaselineShift=0.2, fontSize=14*0.8)
    doc.newStyle(name='footnote', stripWhiteSpace=False,
        fill=(1, 0, 0), fontSize=0.8*U, font=BOOK)
    doc.newStyle(name='caption', stripWhiteSpace=False, tracking=P_TRACK, 
        language=rs.language, 
        fill=0.2, leading=rs.leading*0.8, fontSize=rs.fontSize*0.8,
        font=BOOK_ITALIC, indent=rs.u/2, tailIndent=-rs.u/2, 
        hyphenation=rs.hyphenation)

    # Create main Galley for this page, for pasting the sequence of elements.    
    g = Galley() 

    # Change template of page 1
    doc[0].setTemplate(template1)
    
    # Fill the main flow of text boxes with the ML-->XHTML formatted text. 
    c = Composer(doc)
    c.typesetFile(FILENAME, doc[0], flowId0)
     
    return doc
        
d = makeDocument()
d.export('export/AutomaticLayout.pdf') 

    