
c4=[5, 8]
c6=[3, 7]

def adunarea_fractiilor(x, y):
    numit=x[1]*y[1]
    x[0]=x[0]*numit/x[1]
    y[0]=y[0]*numit/y[1]
    numarator=x[0]+y[0]
    return (numarator, numit)

print(adunarea_fractiilor(x, y))