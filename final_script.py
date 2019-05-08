#! /usr/bin/env python3

import numpy as np
from scipy.optimize import curve_fit
from sdtfile import SdtFile
import matplotlib.pyplot as plt
import math

###########################################a                                    
def model_func(x, a, k,b, kk):
    """The model function"""
    # bi-exponential or mono-exponetial fit
    return a*np.exp(-k/x) + b*np.exp(-kk/x)

###########################################a                                    
def main():


    # load in the file and define x and y data
    sdt = SdtFile('1_1.sdt')
    d = sdt.data[0]
    aa = d.sum(axis=0)
    x= aa + 2
    y= np.linspace(11.,244., 244)

    # define values with greater than 0 counts
    N = x
    #print('N', x)
    N = [i for i in N if i>=10000]
    #print ('Nlog', N)
    maxval=N.index(max(N))
    #print('max',maxval)
    N2= N[maxval:len(N)]
    #print('N2: ',N2)
    tt=np.linspace(int(maxval),int(len(N)), int(len(N) - maxval))
    t=tt
    
    # new N value
    N = N2
    
    #sig = np.zeros(nobs) + stdev
    #sig = np.zeros(len(N)) + stdev
    sig= np.sqrt(np.array(N))
    print('sig',sig)
    print('sum',np.sum(sig))
    
    # preset variables
    stdev = 64000

    # x and y
    y=np.array(N)
    x=np.array(tt)

    # Fit the curve, give a guess p0
    p0=(8, 1000, 8, 1000)
    opt, pcov = curve_fit(model_func, x, y, p0)
    a, k , b, kk= opt

    # Compute chi square
    Nexp = model_func(x, *opt)
    r = N - Nexp
    chisq = np.sum((r/stdev)**2)
    #df = nobs - 2
    print('chisq =',chisq)


    # test result
    x2=np.linspace(50,255,50,255)
    y2=model_func(x2,a,k,b,kk)
    fig, ax = plt.subplots()
    ax.plot(x2, y2, color='r', label ='Fit. func: $f(x) = %.3f e^{%.3f x} %.3f e^{%.3f x}' % (a,k,b,kk))
    ax.plot(x,y,'bo', label='data')
    ax.legend(loc='best')
    plt.yscale('log')
    plt.show()


###########################################a                                    
main()
