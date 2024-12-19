def my_zip(names, ids, points, strct=True):
    if strct:
        if len(names) == len(ids) == len(points):
            return list(zip(names, ids, points))
        else:
            raise ValueError("All lists must have the same length.")
    else:
        min_len = min(len(names), len(ids), len(points))
        return list(zip(names[:min_len], ids[:min_len], points[:min_len]))
