from string import Template


class TileProvider:
    def __init__(self, name=None, url_pattern=None, shards=None, api_key=None, attribution=None, max_zoom=None):
        self._name = name
        self._url_pattern = Template(url_pattern)
        self._shards = shards
        self._api_key = api_key
        self._attribution = attribution
        self._max_zoom = max_zoom if ((max_zoom is not None) and (max_zoom <= 20)) else 20

    def set_api_key(self, key):
        self._api_key = key

    def name(self):
        return self._name

    def attribution(self):
        return self._attribution

    def tile_size(self):
        return 256

    def max_zoom(self):
        return self._max_zoom

    def url(self, zoom, x, y):
        if (zoom < 0) or (zoom > self._max_zoom):
            return None
        shard = None
        if self._shards is not None and len(self._shards) > 0:
            shard = self._shards[(x + y) % len(self._shards)]
        return self._url_pattern.substitute(s=shard, z=zoom, x=x, y=y, k=self._api_key)


tile_provider_OSM = TileProvider(
    'osm',
    url_pattern='https://$s.tile.openstreetmap.org/$z/$x/$y.png',
    shards=['a', 'b', 'c'],
    attribution='Maps & Data © OpenStreetMap.org contributors',
    max_zoom=19)

tile_provider_StamenTerrain = TileProvider(
    'stamen-terrain',
    url_pattern='http://$s.tile.stamen.com/terrain/$z/$x/$y.png',
    shards=['a', 'b', 'c', 'd'],
    attribution='Maps © Stamen, Data © OpenStreetMap.org contributors',
    max_zoom=18)

tile_provider_StamenToner = TileProvider(
    'stamen-toner',
    url_pattern='http://$s.tile.stamen.com/toner/$z/$x/$y.png',
    shards=['a', 'b', 'c', 'd'],
    attribution='Maps © Stamen, Data © OpenStreetMap.org contributors',
    max_zoom=20)

default_tile_providers = {
    tile_provider_OSM.name(): tile_provider_OSM,
    tile_provider_StamenTerrain.name(): tile_provider_StamenTerrain,
    tile_provider_StamenToner.name(): tile_provider_StamenToner,
}
