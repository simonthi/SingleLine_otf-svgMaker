# SingleLine_otf-svgMaker_Glyphs, Glyphs single-line OpenType SVG export preparation script
# by Simon Thiefes for haw-type-design, 2024 
# HAW Hamburg
# haw-type-design https://github.com/haw-type-design

from AppKit import NSColor
import copy

#specifiy stroke weight for export
strokeWeight = 40

#load font
font = Glyphs.font

#check for existant svg instance
instanceNames = [instance.name for instance in font.instances]
if ("SVG" in instanceNames):
    print("SVG Instance already exists. Rename instance and run script again to proceed.")

#else: append SVG instance to font
else:
    # generate new SVG Instance of the fon
    SVGinstance = GSInstance()
    SVGinstance.name = "SVG"
    # set tables in created instance
    SVGinstance.customParameters['Color Layers to SVG'] = True
    SVGinstance.customParameters['Export SVG Table'] = True
    font.instances.append(SVGinstance)
    #loop over glyphs
    for glyph in Glyphs.font.glyphs:
        #make changes non destructive
        glyph.beginUndo()
        #get content of bottommost layer 
        layer = glyph.layers[0]
        #create new svg layer
        newLayer = GSLayer()
        newLayer.name = 'svg'
        newLayer.attributes["color"] = True
        glyph.layers.append(newLayer)
        #copy shapes and metrics
        newLayerID = glyph.layers[newLayer.layerId]
        newLayerID.shapes = copy.copy(layer.shapes)
        newLayerID.LSB = layer.LSB
        newLayerID.RSB = layer.RSB
        #set paths to specified stroke weight
        for path in newLayerID.paths:
            #set stroke width/height
            path.attributes['strokeWidth'] = strokeWeight
            path.attributes['strokeHeight'] = strokeWeight
            #set strokes to black color
            path.attributes['strokeColor'] = NSColor.blackColor()
        for path in layer.paths:
            #set stroke width/height
            path.attributes['strokeWidth'] = strokeWeight
            path.attributes['strokeHeight'] = strokeWeight
            #this should set the linecaps to rounded. however, it is ignored as of now. consider this a stub for future updates of glyphs
            path.attributes['lineCapEnd'] = 3
            path.attributes['lineCapStart'] = 3
        #end undo cycles
        glyph.endUndo()
        Glyphs.redraw()