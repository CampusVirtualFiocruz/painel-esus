def get_cids(cids):
    return f"""select unnest (array[
      {cids}]) as codigo"""
