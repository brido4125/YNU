import math


def sphereVolume(pa_radius):
    vol = 4 / 3 * math.pi * pow(pa_radius, 3);
    print(vol)


radius = int(input("반지름을 입력하세요 : "))
sphereVolume(radius)
