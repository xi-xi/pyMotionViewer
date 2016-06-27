import os
import csv
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
    SEP = ','
    m = df.Motion()
    with open(filename, "r") as f:
        prop_names = f.readline().split(SEP)
        prop_values = f.readline().split(SEP)
        if len(prop_names) != len(prop_values):
            return None
        props = dict(zip(prop_names, prop_values))
        m.set_max_frame(int(props["NumFrames"]))
        m.set_fps(float(props["DataRate"]))
        m.set_markers(f.readline().split(SEP))
        for row in csv.reader(f):
            frame, posture = build_posture_from_csv(row, m.get_markers())
            m[frame] = posture
    return m


def build_posture_from_csv(row, markers):
    p = df.Posture()
    frame = int(row[0])
    for name, x, y, z in zip(markers[2::3], row[2::3], row[3::3], row[4::3]):
        p[name] = np.array([float(x), float(y), float(z)])
    return frame, p


def load_trc(filename):
    pass


def load_ts(filename):
    pass


def load_xlsx(filename):
    pass
