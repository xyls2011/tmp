import s2sphere as s2


def latlng(lat, lng):
    return s2.LatLng.from_degrees(lat, lng)


def parse_latlng(s):
    print(s)
    a = s.split(',')
    print(a)
    if len(a) != 2:
        raise ValueError('Cannot parse coordinates string "{}" (not a comma-separated lat/lng pair)'.format(s))

    try:
        lat = float(a[0].strip())
        lng = float(a[1].strip())
        print(lat)
        print(lng)
    except ValueError:
        raise ValueError('Cannot parse coordinates string "{}" (non-numeric lat/lng values)'.format(s))

    if lat < -90 or lat > 90 or lng < -180 or lng > 180:
        raise ValueError('Cannot parse coordinates string "{}" (out of bounds lat/lng values)'.format(s))

    return latlng(lat, lng)


def parse_latlngs(s):
    res = []
    for c in s.split():
        c = c.strip()
        if len(c) > 0:
            res.append(parse_latlng(c))
    return res
