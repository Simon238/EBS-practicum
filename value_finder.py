import math

C_one = [1, 3.3, 4.7, 6.8, 10, 22, 33, 47, 68, 100, 220, 330, 470]
C_one = [10**(-6)*x for x in C_one]
C_two = [1, 1.5, 2.2, 2.7, 3.3, 4.7, 6.8, 10, 22, 100]
C_two = [10**(-9)*x for x in C_two]
R_p = [50, 100, 200, 220, 500]
R = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
R_one = R
c = 10
# construct E12 series values.
while R_one[len(R_one)-1] < 150000:
    for x in R:
        if x*c <= 150000:
            R_one.append(x*c)
        else:
            break
    c *= 10
R_two = R_one

for x in C_one:
    for y in C_two:
        for z in R_p:
            for u in R_one:
                for v in R_two:
                    # omega values (in Hertz) for alpha = 0
                    omeg_one = 1 / (math.pi * 2 * (z + v) * x)
                    omeg_two = 1 / (math.pi * 2 * x * u)
                    omeg_three = 1/(math.pi * 2 * (z+v)*y)
                    # gain value for alpha = 1
                    gain = v/(z+u)
                    # set restrictions.
                    if (1 < omeg_one) and (1.98 < gain < 2.01) and (omeg_two < 20) and (20000 < omeg_three):
                        print('gain: ' + str(gain))
                        print('omega 1: ' + str(omeg_one))
                        print('omega 2: ' + str(omeg_two))
                        print('omega 3: ' + str(omeg_three))
                        print('C1: ' + str(x) + ', C2: ' + str(y) + ', Rp: ' + str(z) + ', R1: ' + str(u) + ', R2: ' + str(v))
