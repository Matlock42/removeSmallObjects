#!/usr/bin/env python3
import inkex
from lxml import etree

class RemoveSmallObjects(inkex.EffectExtension):
    """Deletes small objects that may exist in your Inkscape document."""
    def add_arguments(self, pars):
        pars.add_argument(
            "--width_threshold",
            type=float,
            default=0.50,
            help="Width Threshold",
        )
        pars.add_argument(
            "--height_threshold",
            type=float,
            default=0.50,
            help="Height Threshold",
        )

    def effect(self):
        width_threshold = self.options.width_threshold
        height_threshold = self.options.height_threshold

        for element in self.svg.descendants().filter(inkex.PathElement):
            if element.is_visible():
                bbox = element.shape_box()
                if bbox.width < width_threshold and bbox.height < height_threshold:
                    element.delete()

if __name__ == '__main__':
    RemoveSmallObjects().run()
