# Summing series

def m_series(i):
    result = 0
    for j in range(1,i+1):
        result = result + j/(j+1)
    return result

print("i".ljust(5),"m(i)".ljust(5))
for j in range(1,21):
    print(repr(j).ljust(5),"{0:.4f}".format(m_series(j)))
