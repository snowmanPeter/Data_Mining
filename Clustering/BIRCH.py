#encoding:utf-8

"""
    BIRCH模型的核心是CF模型，下面将主要构建CF模型
"""

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

