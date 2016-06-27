"""Core data structure module

このモジュールでは中枢を構成するデータ構造を定義します(多分)
"""


class Motion:
    def __init__(self):
        pass


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
