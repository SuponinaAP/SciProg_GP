import numpy as np
L = int(input())
v1 = int(input())
v2 = int(input())
vm = int(input())
#v2_vm = v2+vm #скорость сближения второго поезда и мухи
#v1_vm = v1+vm #скорость сближения первого поезда и мухи
v_crush = v1+v2 #скорость сблиэения 2 поездов
t = L/v_crush
#v_comb = v_crush+vm
num = t*vm
#t_fin = L/v_comb
print(int(num)) 