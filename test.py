f = open("hz_vehicle.txt", "r")
f2 = open('test.txt', "w")
while True:
    line = f.readline()
    if line:
        l = line.split(',')
        f2.write('INSERT INTO HZ_VEHICLE(XH,HPZL,HPHM) VALUES (%s,%s,%s);' %
                 (l[0], l[1], l[2]))
        f2.write('\n')
    else:
        break

f.close()
f2.close()

##f    = open('test.txt', "a")
###line = f.readline()
# f.write('abc')
# f.close()
