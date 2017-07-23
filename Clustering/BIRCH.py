#encoding:utf-8

"""
    BIRCH模型的核心是CF模型，下面将主要构建CF树
"""

import numpy as np

class BTNode():

    def __init__(self,cfNum,cfNode):
        self.cfNum= cfNum
        self.cfNode = cfNode

class CFNode():

    def __init__(self,n,LS,SS,btNode):
        self.n = n
        self.SL = LS
        self.SS = SS
        self.btNOde = btNode

class CFTree():

    def __init__(self ,data ,B ,L ,T ,metric):
        """
        初始化CF Tree的参数
        :param B: 表示内部节点的平衡因子
        :param L: 表示叶子节点的平衡因子
        :param T: 表示簇半径阈值
        """
        self.data = data
        self.B = B
        self.L = L
        self.T = T
        self.metric = metric

    def dist_compute(self):
        if self.metric == "Euclidean":



    def addNode(self, value):
        if type(value) != np.ndarray:
            value = np.array(value)
        if self.root is None:
            self.root.cfNum = 1
            self.root.cfNode = [CFNode(1,value,value*value),]
        else:



