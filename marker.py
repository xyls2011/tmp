from object import Object
import math
import s2sphere as s2


class Marker(Object):
    def __init__(self, latlng=None):
        Object.__init__(self)
        if latlng is None:
            raise ValueError('Trying to create marker with empty coordinates')
        self.latlng = latlng
        self.color = (1, 0, 0)
        self.size = 10

    def bounds(self):
        return s2.LatLngRect.from_point(self.latlng)

    def extra_pixel_bounds(self):
        return -1 * self.size, -3 * self.size, self.size, 0

    def render(self, transformer, cairo_context):
        x, y = transformer.ll2pixel(self.latlng)
        r = self.size
        dx = r * math.sin(math.pi / 3.0)
        dy = r * math.cos(math.pi / 3.0)
        cairo_context.save()
        cairo_context.set_source_rgb(*self.color)
        x_count = math.ceil(transformer.image_width() / (2 * transformer.world_width()))
        for p in range(-x_count, x_count + 1):
            cairo_context.save()
            cairo_context.translate(p * transformer.world_width(), 0)
            cairo_context.arc(x, y - 2 * r, r, 0, 2 * math.pi)
            cairo_context.fill()
            cairo_context.new_path()
            cairo_context.line_to(x, y)
            cairo_context.line_to(x - dx, y - 2 * r + dy)
            cairo_context.line_to(x + dx, y - 2 * r + dy)
            cairo_context.close_path()
            cairo_context.fill()
            cairo_context.restore()
        cairo_context.restore()
