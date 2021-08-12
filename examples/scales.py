from charming import map


def scale_band(domain, range, padding=0):
    band_width = (range[1] - range[0]) / len(domain)

    def scale(value):
        i = domain.index(value)
        return range[0] + band_width * i + padding
    scale.band_width = lambda: band_width - padding
    scale.domain = lambda: domain
    scale.range = lambda: range
    return scale


def scale_linear(domain, range):
    def scale(value):
        return map(value, domain[0], domain[1], range[0], range[1])
    scale.domain = lambda: domain
    scale.range = lambda: range
    return scale


def scale_ordinal(domain, range):
    return lambda value: range[domain.index(value)]
