import s2sphere as s2


class Object:
    def __init__(self):
        pass

    def extra_pixel_bounds(self):
        return 0, 0, 0, 0

    def bounds(self):
        return s2.LatLngRect()

    def render(self, transformer, cairo_context):
        print('render object')
