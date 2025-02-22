import sys
sys.path.append("/Users/zny/Desktop/Git/zny/BondPrice_Z_File.py") 


import BondPrice_Z_File 

def test_getBondPrice_Z():
    yc = [.010,.015,.020,.025,.030]
    times=[1,1.5,3,4,7]
    face = 2000000
    couponRate = .04

    x = BondPrice_Z_File.getBondPrice_Z(face, couponRate, times, yc)
    return x




print(test_getBondPrice_Z())


