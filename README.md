# SingleLine otf-svgMaker

## Robofont

`SingleLine_otf-svgMaker_Robofont` is a Python script for [Robofont](https://robofont.com/) by [Frederik Berlaen](https://typemytype.com/) that permits to export any skeletal / monoline UFO-based font project towards a single-line OpenType-SVG font with open paths running in the Adobe environment (CC 2019 and above) with kerning and opentype features full support. `SingleLine_otf-svgMaker-Robofont` uses [roundingPen](https://github.com/typemytype/outlinerRoboFontExtension/blob/master/Outliner.roboFontExt/lib/outlinePen.py) script by Frederik Berlaen. Make sure that [Outliner](https://github.com/typemytype/outlinerRoboFontExtension) extension is installed before running `SingleLine_otf-svgMaker-Robofont` export script in Robofont. 

## Glyphs

`SingleLine_oft-svgMaker-Glyphs` is a Python script for [Glyphs](https://glyphsapp.com/) by [Simon Thiefes](https://simonthiefes.de) that implements the same functionality as the Robofont script but for Glyphs. It is tested on Glyphs 3 and duplictes the drawing layer with open contours to an svg color layer. After running the script you can proceed to exporting the font through the Glyphs export window.

`SingleLine otf-svgMaker` script opens new perspectives for any typedesigner with monoline projects and fab labs users by largely simplifying typographical practices oriented towards CNC (Computer Numerical Control) engraving or printing.

This script was developed and first applied in the *Relief SingleLine* typeface distributed under the [Open Font License](https://scripts.sil.org/ofl) and available for download at isdaT-type [Relief SingleLine Github repository](https://github.com/isdat-type/Relief-SingleLine). 

The resulting open paths OpenType-SVG fonts comprise two layers: a single-line layer based on SVG and a second layer with a classic outlined OTF. By default, if an application can’t use the open paths SVG layer it should switch automatically to the outlined OTF layer also embedded in this OpenType-SVG fonts.

In Illustrator or Indesign (CC 2019 and above), compose your typographic layout, then choose the function */Text /Vectorize* to achieve titles or paragraphs as single-line shapes to send to your favorite CNC machine or to print. With such open paths fonts you can apply for example an equal stroke thickness to your typographic composition no matter the type size.

## Contributors

[Frederik Berlaen](https://typemytype.com/) / Instagram [@typemytype](https://www.instagram.com/typemytype/) / Twitter [@typemytype](https://twitter.com/typemytype)

[François Chastanet](http://francoischastanet.com/) / Instagram [@francois_chastanet](https://www.instagram.com/francois_chastanet/) / Twitter [@f_chastanet](https://twitter.com/f_chastanet)

[Simon Thiefes](https://simonthiefes.de) / Mastodon [@simonthiefes](https://typo.social/@simonthiefes)



