#encoding:utf-8

import numpy as np

class distance():

    def _Euclidean_Distance(self,a,b):
        return np.sum((a-b)*(a-b))

    def _Manhattan_Distance(self,a,b):
        return np.sum(np.abs(a-b))

    def _Cluster_Average_Distance(self,a,b):
        return np.sum()