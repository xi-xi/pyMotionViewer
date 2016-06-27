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


def get_dafault_trc_markers():
    return [
        "Frame#",
        "Time",
        "Top.head", "", "",
        "Back.Head", "", "",
        "Front.Head", "", "",
        "L.Head_Offset", "", "",
        "R.Shoulder", "", "",
        "L.Shoulder", "", "",
        "Neck", "", "",
        "L.BackOffset", "", "",
        "R.Bicep", "", "",
        "R.Elbow", "", "",
        "R.ForeArm", "", "",
        "R.Radius", "", "",
        "R.Ulna", "", "",
        "R.Thumb", "", "",
        "R.Pinky", "", "",
        "L.Bicep", "", "",
        "L.Elbow", "", "",
        "L.Forearm", "", "",
        "L.Radius", "", "",
        "L.Ulna", "", "",
        "L.Thumb", "", "",
        "L.Pinky", "", "",
        "R.ASIS", "", "",
        "L.ASIS", "", "",
        "R.PSIS", "", "",
        "L.PSIS", "", "",
        "V.Sacral", "", "",
        "R.Thigh", "", "",
        "R.Knee", "", "",
        "R.Shank", "", "",
        "R.Ankle", "", "",
        "R.Heel", "", "",
        "R.Toe", "", "",
        "R.Foot", "", "",
        "L.Thigh", "", "",
        "L.Knee", "", "",
        "L.Shank", "", "",
        "L.Ankle", "", "",
        "L.Toe", "", "",
        "L.Heel", "", "",
        "L.Foot", "", ""
    ]


def load_trc(filename):
    SEP = "\t"
    m = df.Motion()
    with open(filename, "r") as f:
        f.readline()
        prop_names = f.readline().split(SEP)
        prop_values = f.readline().split(SEP)
        props = dict(zip(prop_names, prop_values))
        m.set_max_frame(int(props["NumFrames"]))
        m.set_fps(float(props["DataRate"]))
        markers = f.readline().split(SEP)
        if len(markers) <= 3:
            markers = get_dafault_trc_markers()
        m.set_markers(markers)
        f.readline()
        f.readline()
        for row in csv.reader(f, delimiter=SEP):
            frame, posture = build_posture_from_trc(row, m.get_markers())
            m[frame] = posture
    return m


def build_posture_from_trc(row, markers):
    p = df.Posture()
    frame = int(row[0])
    for name, x, y, z in zip(markers[2::3], row[2::3], row[3::3], row[4::3]):
        p[name] = np.array([float(x), float(y), float(z)])
    return frame, p


def load_ts(filename):
    pass


def load_xlsx(filename):
    pass
