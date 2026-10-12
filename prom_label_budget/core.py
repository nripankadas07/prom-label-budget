import re

def run(data):
    series, drop = data.get("series"), data.get("drop", [])
    if not isinstance(series,list) or len(series)>10000 or not isinstance(drop,list) or any(not isinstance(x,str) for x in drop) or len(set(drop))!=len(drop) or "__name__" in drop:
        raise ValueError("bounded series and unique drop labels required; keep __name__")
    unique = set()
    if any(not re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", x) for x in drop):
        raise ValueError("invalid drop label")
    for labels in series:
        if not isinstance(labels,dict) or not labels.get("__name__") or len(labels)>64:
            raise ValueError("each series requires __name__ and at most 64 labels")
        if any(not isinstance(k,str) or not re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*",k) or not isinstance(v,str) or len(v)>4096 for k,v in labels.items()):
            raise ValueError("ASCII label names and bounded string values required")
        if not re.fullmatch(r"[a-zA-Z_:][a-zA-Z0-9_:]*",labels["__name__"]):
            raise ValueError("legacy ASCII metric name required")
        unique.add(tuple(sorted(labels.items())))
    metrics, values, projected = {}, {}, {}
    for ident in unique:
        labels=dict(ident)
        metric=labels["__name__"]
        metrics[metric]=metrics.get(metric,0)+1
        for k,v in ident:
            values.setdefault(k,set()).add(v)
        key=tuple((k,v) for k,v in ident if k not in drop)
        projected[key]=projected.get(key,0)+1
    collisions=sorted(n for n in projected.values() if n>1)
    return {"input_rows":len(series),"unique_series":len(unique),"duplicates":len(series)-len(unique),"metrics":dict(sorted(metrics.items())),"label_cardinality":{k:len(v) for k,v in sorted(values.items())},"projected_series":len(projected),"collision_group_sizes":collisions,"lost_identity_count":len(unique)-len(projected)}
