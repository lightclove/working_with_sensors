import os
import smbus


def find_I2C_BusNUM(self):
    try:
        # -2 - предпоследний символ в выражении /dev/i2c-* с учетом пробела в конце.
        print('Найден номер шины I2C устройства в системе: ' + str(os.popen('ls /dev/i2c-*').read()[-2]))

        return os.popen('ls /dev/i2c-*').read()[-2].split('\n')
    except Exception as be:
        print("\033[31m {}".format('Возникла ошибка в программе:' + "\033[31m {}".format(be.with_traceback())))
        print("\033[30m {}".format(""))
        return -1


########################################################################################################################
"""
    Метод чтения байта данных. Открыть шину I2C «0» и прочитать один байт по адресу 0x39, со смещением 0x0C (адрес регистра).
"""


def i2cReadByteData(self, busNum=0, addess2read=0x39, offset=0x0C):
    bus = smbus.SMBus(busNum)
    try:
        data2read = bus.read_byte_data(addess2read, offset)
        print(data2read)
        bus.close()
    except BaseException as be:
        print("\033[31m {}".format('Возникла ошибка в программе:' + "\033[31m {}".format(be.with_traceback())))
        print("\033[30m {}".format(""))
        return -1


"""
    Метод чтения массива данных. Открыть шину I2C «0» и записать один байт по адресу 0x39, со смещением 0x0C (адрес регистра).
"""


# @ToDo UNDER CONSTRUCTION TEST IT !  запись байта
def i2cwrite(self, busNum=0, data2write=45, addess2write=0x39, offset=0x0C):
    try:
        bus = smbus.SMBus(busNum)
        bus.write_byte_data(addess2write, offset, data2write)
        bus.close()
    except Exception as be:
        print("\033[31m {}".format('Возникла ошибка в программе:' + "\033[31m {}".format(be.with_traceback())))
        print("\033[30m {}".format(""))
        return -1

    """
    @param bus_num = 0..N Номер шины
    """

    def I2C_scan(self, bus_num, start=0x03, end=0x78):
        from smbus2 import SMBus
        import sys
        try:

            bus = SMBus(bus_num)

            print(' ИНФОРМАЦИЯ по I2C:')
            print("Номер I2C шины: " + str(bus_num))
            print("Начальный адрес шины: " + hex(start))
            print("Конечный адрес шины: " + hex(end) + "\n")

            for i in range(start, end):
                val = 1
                try:
                    bus.read_byte(i)
                except OSError as e:
                    val = e.args[0]
                finally:
                    if val != 5:  # No device
                        if val == 1:
                            res = "Устройство доступно на шине I2C по адресу "
                            print(res + " -> " + hex(i))
                        elif val == 16:
                            res = "Устройство занято на шине I2C по адресу"
                            print(res + " -> " + hex(i))
                        elif val == 110:
                            res = "Таймаут опроса на шине I2C"
                            print(res)
                        else:
                            res = "на шине I2C код ошибки " + str(val) + " по адресу"
                            # print(res + " -> " + hex(i))
        except Exception as be:
            print("\033[31m {}".format('Возникла ошибка в программе:' + "\033[31m {}".format(be.with_traceback())))
            print("\033[30m {}".format(""))
            return -1

    """
        Метод чтения байта данных. Открыть шину I2C «0» и прочитать один байт по адресу 0x39, со смещением 0x0C (адрес регистра).
    """

    def i2cReadByteData(self, busNum=0, addess2read=0x39, offset=0x0C):
        bus = smbus.SMBus(busNum)
        try:
            data2read = bus.read_byte_data(addess2read, offset)
            print(data2read)
            bus.close()
        except BaseException as be:
            print("\033[31m {}".format('Возникла ошибка в программе:' + "\033[31m {}".format(be.with_traceback())))
            print("\033[30m {}".format(""))
            return -1

    """
        Метод чтения массива данных. Открыть шину I2C «0» и записать один байт по адресу 0x39, со смещением 0x0C (адрес регистра).
    """

    # @ToDo UNDER CONSTRUCTION TEST IT !  запись байта
    def i2cwrite(self, busNum=0, data2write=45, addess2write=0x39, offset=0x0C):
        try:
            bus = smbus.SMBus(busNum)
            bus.write_byte_data(addess2write, offset, data2write)
            bus.close()
        except Exception as be:
            print("\033[31m {}".format('Возникла ошибка в программе:' + "\033[31m {}".format(be.with_traceback())))
            print("\033[30m {}".format(""))
            return -1


#######################


I2C_scan(1)
