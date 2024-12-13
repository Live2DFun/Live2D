﻿from core.io.iserializable import ISerializable
from core.type import Array
from core.param import ParamDefSet


class ModelImpl(ISerializable):
    INSTANCE_COUNT = 0

    def __init__(self):
        self.paramDefSet = None
        self.partsDataList = None
        self.canvasWidth = 400
        self.canvasHeight = 400
        ModelImpl.INSTANCE_COUNT += 1

    def initDirect(self):
        if self.paramDefSet is None:
            self.paramDefSet = ParamDefSet()

        if self.partsDataList is None:
            self.partsDataList = Array()

    def getCanvasWidth(self):
        return self.canvasWidth

    def getCanvasHeight(self):
        return self.canvasHeight

    def read(self, br):
        self.paramDefSet = br.readObject()
        self.partsDataList = br.readObject()
        self.canvasWidth = br.readInt32()
        self.canvasHeight = br.readInt32()

    def _6S(self, aH):
        self.partsDataList.append(aH)

    def getPartsDataList(self):
        return self.partsDataList

    def E2_(self):
        return self.paramDefSet