# Typographic Poster
The **TypographicPoster.md** file contains all Markdown content, including various functions to create this Typographic Poster.

## Embedded Python
The connection between Markdown content and Python can be made from 2 different directions. 

* PageBot application scripts that create a **Document** instance, with templates, element and typesetters parsing Markdown text.
* MarkDown text files that include all Python code to create documents. It only needs a small bootstrap script to create the **Typesetter** and parse this file.

~~~Python
cid = 'Poster'
# Import the size, Poster class and layout template.

from pagebot.style import A2
from pagebot.publications import Poster
from pagebot.templates import StackedTypography

W, H = A2 
title = 'When fonts started a new world'

# Poster instance stored as “doc”, typsetter can find it.
# Set the size of the poster as derived from "A2"
# Use the predefined dynamic template for content layout.

doc = Poster(w=W, h=H, originTop=False, 	
	title=title, 
	defaultTemplate=StackedTypography())

# Views define the way documents are exported.
# Add space for cropmarks and registrations marks
view = doc.getView()
view.padding = 40
view.showPageCropMarks = True
view.showPageRegistrationMarks = True
view.showPageFrame = True
~~~	

~~~
reference
~~~
The content of this poster is an example summary of the the file pagebot/resources/content/TypeNetwork/WhenFontsStartedANewWorld.md. It is published on the TN website.


~~~
headline
~~~

### When fonts started a new world
A lot has been written and said about OpenType Variations. There are Operating Systems developers, application developers, font developers, content-developing users, and just plain old users. “As you were,” “Just a taste,” and “Whole hog!” are three of many possible attitudes these folks may, or may not, adopt towards OpenType Variations. As you can imagine, I’m going to write more on the topic.

~~~
topic
~~~

As described in the introduction, variations technology superficially changes nothing about the “workings” of older fonts or applications. Users still begin their work by selecting the keyboard and input method associated with their script and language, or just by clicking an icon of their national flag. From there, the OS maps the characters it’ll show on the screen to match those on the keyboard, and turns on any required OpenType features for that script and language. All the individual font files are sorted for presentation by family name, with a hyphen somewhere separating the family name from the style, treatment, and/or effect name.

So, when the user opens an application for authoring a new document, applications present a font family, style, and size, ready for the user’s input of their own script, in the form of whatever characters they want to type; defaults for all of the selections, from script to character, must exist. This is also true of web documents: the workings cannot exist without the full satisfaction of the “mantra” — from script to font family, to style, to size — in order to function at the simplest level, with fonts today.

A script is a collection of characters that may be used to compose one or more languages. A design class relates to the basic characteristics of font families like serif, sans serif, or script. A font family is a collection of font variants with common details in the terminations, shapes, internal contrasts, and angles. A font style is a variation of the family, or a combination of variations like weight and width, that do not fundamentally alter the comment characteristics of the font family, just the proportions of white and black. Font treatments include stroking the contour, filling it, drop shadows, and possible variants that change neither font family nor style, just how it is positioned, or how the contour is interpreted or augmented. Lastly, a user may choose effects, like simulated scratches and scuffs to the output type, or modification of one or multiple treatments over time, as in animation.

~~~
description
~~~

From there the document specifications are commonly available to fonts in the form of size selection, justification, line spacing, and column width, as well as web techniques like fitting text to boxes on the fly. As things are, that mantra takes the user up to character input, a blinking cursor…or they can change font families, or style within the font family, or they can change from standard characters to an OpenType feature. Then they can either accept or change the default composition parameters, and finally set type.

That of course depends on their application taking advantage of what the operating system and/or HTML offer today. And each operating system, and the web, offers slightly different mantras. But as things are, nothing about any of this changes for users of non-variable fonts, in operating systems or applications that are compliant with the new variations in OpenType 1.8. What users continue to be faced with is large aggregate font file sizes that get larger for every specialized use required of the font family, and often inscrutable font names like FamilySansDisplay-SemiboldItalicPro. Type developers, of course, can just keep doing things as they were.

~~~
chapter1
~~~

### Just a taste

Stepping out for “just a taste” of OpenType Variations, for both a font developer and a web developer, means that an existing font family of 24 individual styles can be reduced to a single variable-font file. The type developer defines a master style, creates a width axis to contain the four widths of the font family, makes a weight axis to contain the six weights of the family, adds each of the existing 24 styles as intermediate instances of width and weight, and via variations-compliant browsers, serves the same documents with no apparent difference to the typography. In fact, the same styles in use would be served to non-compliant browsers and they would obviously look the same.

The major difference in a variable-font approach is that all the styles are contained in a single font file. My mom? She thinks every page of the web is shown somewhere; and via an image and camera system, her computer points at it so she can see it. No offense, but most people think a font is an Illustrator file of each letter that can be scaled and otherwise manipulated before the computer takes a picture of it for use. I wish it was all like that, but fonts today are conglomerates of different data, dedicated to a span of functions from the presentation of the font name in menus, to a kerning-pair adjustment of four pixels in the last character I typed.

In the midst of the conglomerate parts is a font table establishing the units per em of the font, the family name, etc. Another conglomerate part is a glyph table, which has a directory, and then each glyph is stored as a list of points with three attributes: it’s either on or off the contour, and it has an X and a Y location in the em units of the font, relative to zero zero of the em, i.e., where the blinking cursor of the user intersects the baseline at any point size, in any application.

As the user selects a point or pixel size in an application, the whole em of the font and each list of points for each glyph is “sized” to the pixels needed for the user’s choice of size and device, then the font is “scaled” on that ppm if there are any hints, and then a Bézier is calculated in the OS of that sized and scaled font, and finally the result of this is rendered and displayed to the screen as characters are typed.

The OS is usually fast enough to make the entire font at the size the user is about to type, in advance, so there is no lag. But all this is also happening on the web, where a horde of font assets can suddenly appear over the cascading horizon for mass download, sizing, scaling, and rendering. Sites that either employ large numbers of font styles or use fonts with large contingents of glyphs per style, slow things down. And as we know from Gutenberg to Mergenthaler, and from Warnock to Webtype, when type slows things down, technology seeks to speed it up.

Compressing and speeding things up in variable fonts comes in three forms. In the example of a 24-style Latin font family, most of the tables of the 24 files involved are redundant. Other than the particular style name, the location of the Bézier points, and the style-specific kerning pairs, everything else just repeats. So adding new conglomerate parts to the font format that store all the redundant family data in a single file, as variable fonts do, saves a certain amount of file space.

But the storage of variable glyphs themselves greatly compresses and speeds things up. By converting the description of all the contours of the font family into a single master, with a set of changes, or deltas, the master can morph to the shape of each glyph at one of the stylistic variable extremes, like weight maximum, to define the boldest font style of the weight axis. These extremes together create the design space in which an existing 24-style family can be stored. But if each point of each contour of each glyph needed to be stored as a delta, it would not save very much space, which is the third of the things that make variable fonts very clever.

In the process of hinting a font, the hinter does not need to hint every single point of the contour; only the key points that need to be at consistent character heights, or the stem weights, are hinted, and then, right before rendering of a font, the TrueType instruction language contains the instruction “interpolate untouched points.” What this instruction does is locate all of the points that haven’t been hinted, relative to those that have, straightening out the contour as close as possible to its original shape for the user’s point size or pixel-per-em request.

This hinting of course has to be done very carefully for complex scripts or for fonts of most scripts being used at small sizes, as the input font may have 2048 units per em, and the pixels or units per em the user requests may be 20. With every single point in the contour needing a location in the user’s requested font, a lot of untouched point interpolation is already going on in the font software of every operating system today.

Using interpolation like this, operating system font software is able to compress all the ppm sizes of a font style down to TrueType instructions, and one set of contours. Variations technology uses the same thing to compress the entire font family, in addition to all the ppm sizes already being compressed.

In our example 24-style family, the uppercase O may well have 24 points in each of the 24 styles, or a total of 576 contour points to store all the uppercase O‘s.

Variable fonts store 24 points for the default font and a total of 20 deltas for all the 24 existing uppercase O‘s, and for all the weights and widths of all the O’s in between. To add an optical size axis, or any other set of stylistic options, like grade or contrast, eight or so additional deltas brings hundreds of new possible shapes to our O. This style compression, and its effects on the storage of complex scripts, like some of those found in Asia, combined with the additional functionality of all the intermediate styles (a true rarity in software development), is what re-attracted Google, Microsoft, and Adobe back to variations, 20 years after their invention.

As a result of their attraction to the rarity of compression-with-additional-functionality, “just a taste” is what most users are likely to get from variable fonts, as OS fonts like Microsoft’s Segoe, Google’s Roboto, and Adobe’s Source Sans follow Apple’s San Francisco, an Apple GX Variations font, into somewhat secret service. That is to say, unlike the font industry or the typographic press, the majority of users will be working with variable fonts before they know it. By the end of 2018 all the major operating systems and the web will have attained what I call Variations World, which is implementation of the OpenType 1.8 specification.

The wider world it enters this time, though, includes the combination of variable fonts, much wider adoption of Unicode, OpenType layout, TrueType hinting, higher resolution devices, HTML, broadband, and an exceptionally strong type industry, both creatively and technically. For foundries and users adopting a taste of variations, they will be able to remake and use, respectively, the same font families they made before as individual styles, bringing any user who wishes, up to the same level of typographic font software and font functionality as the OS font users will already be experiencing.

~~~
chapter2
~~~

### Whole hog!

As I write this today, in June of 2017, major browser manufacturers are developing variations-aware upgrades, and it appears highly likely that variable font technology will take off on the web first. This is, I think, a really good thing for variable fonts, as the web presents the opportunity for type developers and web programmers, with no application “interference,” to really exercise and shape the common uses of the combined technologies listed above in a relatively free and open environment.

Starting with only my own experience as a guide, I’ve had one round of development with variations two decades ago. So I already know what it’s like to be “as you were,” as well as having “just a taste” of variations in Skia and our demo GX fonts like Zycon, Buffalo Gal, Jam, and Chunk. So two weeks before the August 2016 announcement of variable fonts, when the alliance supporting their advancement asked for our support at Font Bureau, I was ready to go “whole hog.”

By December of 2016, we had developed several prototype variable fonts with Google that contained over 20 axes, only a few of them “registered,” and as of today, we’ve got over 50 axes specified for inclusion in one or another kind of variable-font product. This is not to imply that “whole hog” for a whole-hog user of the future means fathoming a 50-axis variable font. Our prototype fonts were intended to demonstrate variable-font technology as far as possible in two designs, with three months to do so, which was then extended for another three months a little later.

That extension included an obligation to demonstrate the use of variable fonts, which eventually became honed down to the use of variable fonts in compliant browsers. (If you are using one right now, you are looking at variable fonts in use. If not, you are seeing the default variations font.) This demonstration was not so much aimed at users, though I am entirely delighted to have as many as possible reading along. It is intended to explore variations in public, for the benefit of application, OS, and web-standards developers.

The underlying reason for this is that the specification of variable fonts has remained fairly close to that of the early 90s, and in my opinion, and the opinion of others, it needs an update for the years of global typographic and technical progress in between. Part of that update obviously is to make it interoperable with Microsoft, Adobe, Google, and web-font technologies, and those companies have done a great job with the difficult task of getting from “as they were,” if you will, to “just a taste” — as they are, if you will. When I was asked specifically to go beyond the “registered axes,” which I will get to in a minute, I immediately thought “I’ve been hired to go ‘whole hog’!”

Registered axes are the ones that the specification’s owners, Microsoft and Adobe, feel are important enough to include, by reserving their ID tag, documenting definitions for them, and standardizing their values, to enable operating systems and applications to programmatically connect what an axis does, with an action and a user interface. There are currently five such axes, including two that have to do with a font’s “posture,” i.e., whether it is upright, oblique, or italic, and are not particularly applicable to most variation requirements.

Width and weight, two of the other registered axes, are understood to change the style, which I define as not changing the script, class, or family, just the appearance of the width and weight, respectively, relative to a “regular” style. And the fifth registered axis is optical size, a treatment, because it changes neither the script, class, family, nor style, just the appearance of a style at a particular size, or range of sizes. So that’s the three registered axes I was asked to go beyond.

In developing just the two fonts we did with Google, Decovar and Amstelvar, and with the revival and updating of Zycon, a demo font we made for Apple in the ’90s, we created 34 variation axes, with 30 of them being unregistered, so far. That was not as many as Google wanted, which took a while to figure out as we went along, because it was new to them and a long time ago for us.

In the end, we made axes that work alone, and together, to enable the user to make interactive or programmatic changes to their typography: from the alignments of the script or scripts they are using (demonstrated in Amstelvar) to the treatments of particular styles, such as the exact thickness of an open counter within an outline version of a particular weight of a font (demonstrated in Decovar).

This rather belated presentation of detailed examples of variable fonts in potential use, somewhat perplexed the developers of the specification. The alliance, while clearly devoted to one interoperable effort to get variable fonts done, does not have one market to do it for. Apple integrates all, Adobe is concentrated in the creative suite, Microsoft in the office, and Google is diversified but more of a web-based open app developer than the other three combined.

In the year-and-a-half the alliance worked on the specification in secret, they never made the connection between all the axes people have been requesting for years, and the way to actually make them. They also never made the connection between the mantra, all their software uses, and this new technology with the ability to manipulate typography all along the mantra; e.g., not a single axis we have encountered so far, crosses the mantra’s bounds. All of the axes we’ve developed, that we plan to present to users, affect one part of the mantra at a time.

So, this is an exciting time, as the give-and-take between alliance members seeking solutions for their markets, application and font developers seeking differentiation, and a lot of users seeking help, all ramping up over a 20-year period of relative stagnation in this area, means a lot of font software of various kinds, from type-design tools to font families, from applications to web code, will be coming out in the next year or two.

~~~
conclusion
~~~

So, hold on to your háčeks, it should be an interesting year for typography.

~~~
navigation
~~~
Chapter i: When lines roamed the earth
Chapter ii: When line-to curve-to ruled the world
About Type Network Subscribe to the Newsletter Help and Support © Copyright Type Network 2016. All Rights Reserved.