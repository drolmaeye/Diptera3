from epics import Motor

m = Motor('16test:m2')

# a = m.show_info()

b = m.move(0, relative=False, wait=True)

# print(m.within_limits(10))

print(b)
print(m.readback)

