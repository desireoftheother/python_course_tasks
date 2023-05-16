def custom_compress(iterable, selectors):
    zipped = zip(iterable, selectors)
    filtered = filter(lambda pair: pair[1], zipped)
    mapped = map(lambda pair: pair[0], filtered)
    return mapped
