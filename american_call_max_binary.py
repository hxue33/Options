import numpy as np
import pandas as pd


class Option:
    def __init__(self,s1,s2,st,num1,num2,q1,q2,sig1,sig2,rho,expT,r,K,type,call_put):
        self.s1 = s1   #
        self.s2 = s2
        self.st = st
        self.num1 = num1
        self.num2 = num2
        self.q1 = q1
        self.q2 = q2
        self.sig1 = sig1
        self.sig2 = sig2
        self.t = expT
        self.r = r
        self.rho = rho
        self.K = K
        self.type = type
        self.call_put = call_put

    def call_put_flag(self):
        if self.call_put == "call":
            return 1
        else:
            return -1

    def payoff(self):
        z = self.call_put_flag
        if self.type == 1:
            return max(0,z*(self.q1*self.s1-self.q2-self.s2)-z*
