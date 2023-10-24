# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:30:11 2023

@author: u07391
"""

import numpy as np
import ith

if __name__=='__main__':
    temperaturas=np.loadtxt('./datos/temperaturas.txt')
    humedad=np.loadtxt('./datos/humedad.txt')
    THI=ith.ith(temperature=temperaturas,humidity=humedad)
    stress=ith.isStress(THI)
