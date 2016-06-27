"""Core data structure module

このモジュールでは中枢を構成するデータ構造を定義します(多分)
"""


class Motion:
    def __init__(self):
        self._postures = {}
        self._markers = []
        self._fps = 0.0
        self._max_frame = 0

    def __getitem__(self, key):
        return self._postures[key]

    def __setitem__(self, key, value):
        self._postures[key] = value

    def get_fps(self):
        return self._fps

    def set_fps(self, value):
        self._fps = value

    def get_max_frame(self):
        return self._max_frame

    def set_max_frame(self, value):
        self._max_frame = value

    def get_markers(self):
        return self._markers

    def set_markers(self, value):
        self._markers = value


class Posture:
    def __init__(self):
        self._joint_positions = {}

    def __len__(self):
        return len(self._joint_positions)

    def __getitem(self, key):
        return self._joint_positions[key]

    def __setitem(self, key, value):
        self._joint_positions[key] = value

    def __iter__(self):
        return self._joint_positions.__iter__()

    def __reversed__(self):
        return self._joint_positions.__reversed__()

    def __contains__(self, item):
        return self._joint_positions.__contains__(item)

    def get_joints_name(self):
        return [k for k in self._joint_positions.keys()]

    def contains(self, key):
        return key in self._joint_positions
