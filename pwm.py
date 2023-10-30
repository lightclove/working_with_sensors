# Еhe PWM is basically achieved by calculating the voltage at a given time.
# Варианты реализации аналогового сигнала ШИМ для датчика C02
# Справочная информация:
# Инверторы — это устройства, которые принимают постоянный ток и превращают его в переменный.
# Они делают это с помощью H-моста, который меняет направление тока, и они меняют его периодически импульсами,
# так что общее изменение выглядит как синусоида.
# Это называется широтно-импульсной модуляцией или ШИМ.
# Простейшей формой ШИМ является модифицированная прямоугольная волна,
# которая в основном представляет собой прямоугольную волну с дополнительными шагами.
# Однако истинная синусоида может быть получена с помощью SPWM или синусоидальной широтно-импульсной модуляции

# from math import trunc
#
# import matplotlib
# import numpy as np
# import matplotlib.pyplot as plt

# def PWM(t, frequency, dutyCycle):
#     #period = 1 / frequency
#     #pt = tt / period
#     pt = t * frequency # "period" time, where 1 unit is 1 period on the "real" time stamp.
#     tc = pt - trunc(pt) # cycle time within 1 period. 0..1.
#     return 1 if tc < dutyCycle else 0 # where 1 means on and 0 means off
########################################################################################################################
# A vectorized solution :
# percent=30.0
# TimePeriod=1.0
# Cycles=10
# dt=0.01
#
# t=np.arange(0,Cycles*TimePeriod,dt);
# pwm= t%TimePeriod<TimePeriod*percent/100
# plt.plot(t, pwm)


########################################################################################################################
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# percent=float(input('on percentage:'))
# TimePeriod=float(input('time period:'))
# Cycles=int(input('number of cycles:'))
# dt=0.01  # 0.01 appears to be your time resolution
#
# x=np.arange(0,Cycles*TimePeriod,dt);  #linspace's third argument is number of samples, not step
#
# y=np.zeros_like(x)   # makes array of zeros of the same length as x
# npts=TimePeriod/dt
#
# i=0
# while i*dt< Cycles*TimePeriod:
#     if (i % npts)/npts < percent/100.0:
#         y[i]=1
#     i=i+1
#
# plt.plot(x,y,'.-')
# plt.ylim([-.1,1.1])
########################################################################################################################
from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

out_width = 100
out_height = 1000

frequency = 50
divisions = 500
amplitude = 200

scope_out = []
delay = 1


def square_wave(d, f):
    # создать квадратную волну, учитывая частоту и рабочий цикл
    return lambda x: int(10 ** 15 * (sin(2 * pi * x * f) + abs(sin(2 * pi * x * f) + 2 * d - 1) + 2 * d - 1) > 0.1)


def sin_tables(acc, f):
    return [sin(2 * pi * f * (i / acc)) for i in range(acc)]


lookup = sin_tables(divisions, frequency)


def data_gen(i):
    current = i % len(lookup)
    duty_cycle = lookup[current] / max(lookup)
    new_wave = square_wave(duty_cycle, frequency)

    if ((i - current) / len(lookup)) % 2 == 0:
        return new_wave(i) * amplitude + out_height / 2
    else:
        return -new_wave(i) * amplitude + out_height / 2


def animate(i):
    if len(scope_out) == out_width:
        scope_out.pop(0)
    scope_out.append(data_gen(i))

    ax.clear()
    ax.plot(scope_out)

    ax.set_ylim([0, out_height])
    ax.set_xlim([0, out_width])


fig, ax = plt.subplots()
ani = animation.FuncAnimation(
    fig, animate, interval=delay
)
plt.show()
