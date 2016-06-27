import os
import pandas as pd
import numpy as np
import dataframe as df


def load(filename, datatype=None):
    if datatype is None:
        datatype = os.path.splitext(filename)[1][1:].lower()
    loader = get_loader(datatype)
    if loader is None:
        raise ValueError("datatype{} is invalid".format(datatype))
    return loader(filename)


def get_loader(datatype):
    if datatype == "csv":
        return load_csv
    elif datatype == "trc":
        return load_trc
    elif datatype == "ts":
        return load_ts
    elif datatype == "xlsx":
        return load_xlsx
    return None


def load_csv(filename):
    pass


def load_trc(filename):
    pass


def load_ts(filename):
    pass


def load_xlsx(filename):
    pass
