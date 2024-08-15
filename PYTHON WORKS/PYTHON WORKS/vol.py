def vol_holcy(R,r,h):
    vol=22/7*(R*R-r*r)*h
    return vol
R=int(input())
r=int(input())
h=int(input())
print(vol_holcy(R,r,h))

def vol_sph(r):
    vol=4/3*22/7*(r*r*r)
    return vol
r=int(input())
print(vol_sph(r))

def vol_hemsph(r):
    vol=2/3*22/7*(r*r*r)
    return vol
r=int(input())
print(vol_sph(r))