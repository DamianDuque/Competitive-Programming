a = -1.85718386
b = -1.85718389
c = -1.85748754

errn = abs(c-b)
errn1 = abs(b-a)
print(errn)
print(errn1)

k = errn1/errn**1.62
print(k)
