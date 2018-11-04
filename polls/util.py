def dictGet(hashMap, key):
    try:
        return hashMap[key]
    except KeyError:
        return ""
