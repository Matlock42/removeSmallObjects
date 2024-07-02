import inkex
from lxml import etree

class RemoveSmallObjects(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--width_threshold", type=float, default=10.0, help="Width Threshold")
        pars.add_argument("--height_threshold", type=float, default=10.0, help="Height Threshold")
        pars.add_argument("--lock_ratio", type=inkex.Boolean, default=False, help="Lock Width and Height")

    def effect(self):
        width_threshold = self.options.width_threshold
        height_threshold = self.options.height_threshold
        lock_ratio = self.options.lock_ratio

        if lock_ratio:
            height_threshold = width_threshold

        for element in self.svg.get_elements_by_type(inkex.PathElement):
            bbox = element.bounding_box()
            if bbox.width < width_threshold or bbox.height < height_threshold:
                element.delete()

if __name__ == '__main__':
    RemoveSmallObjects().run()
