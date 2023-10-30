""" Метод тестирования на работоспособность устройств по spi
    https://www.raspbe.with_traceback()rrypi.org/documentation/hardware/raspbe.with_traceback()rrypi/spi/README.md
    Приведенное выше записывает 3 байта, содержащихся в data_out, и копирует полученные данные в data_in.
    Обратите внимание, что data_in всегда будет кортежем той же длины, что и data_out, и будет просто отражать состояние вывода MISO на протяжении транзакции.
    Пользователь должен понять поведение устройства, подключенного к выводам SPI.
"""
import os


def cspidev_test(self, deviceNum):
    try:
        print(' Тестирование по SPI устройства /dev/spidev0.' + str(deviceNum))
        tested = os.popen('./spidev_test -D ' + str(deviceNum)).read()
        print(tested)
        return tested
    except Exception as be:
        print("\033[31m {}".format('Возникла ошибка в программе:' + "\033[31m {}".format(be.with_traceback())))
        print("\033[30m {}".format(""))
        return -1


def spi_test(self, deviceNum):
    try:
        import spi
        # Откройте дескриптор файла на устройстве SPI с помощью одного из двух чипов:
        # device_0 = spi.openSPI(device="/dev/spidev0.1", mode=0, speed=500000, bits=8, delay=0)
        # Ключевое слово устройства может быть "/dev/spidev0.0" или "/dev/spidev0.1".
        # Разница относится к тому, какой вывод выбора микросхемы используется драйвером устройства SPI.
        # Ключевое слово mode может быть 0,1,2 или 3, и многие устройства SPI могут работать на частоте до 8000000 Гц,
        # Используйте возвращенный дескриптор устройства для проведения транзакции SPI

        # Открыть дескриптор файла для
        # spi device 0, использующий вывод CE0 для выбора чипа
        device = spi.openSPI(device=deviceNum,
                             mode=0,
                             speed=1000000)

        # Это не обязательно, а не просто демонстрировать обратную петлю
        # data_in = (0x00, 0x00, 0x00)
        # Транзактные данные
        data_out = (0xFF, 0x00, 0xFF)
        print("Отправлен запрос c числовой последовательностью: " + str(data_out) + " на устройство: " + str(deviceNum))
        # This is not necessary, not just demonstrate loop-back
        # data_in = (0x00, 0x00, 0x00)
        data_in = spi.transfer(device, data_out)
        print("Получен ответ от устройства " + str(deviceNum) + " c числовой последовательностью:" + str(data_in))
        print('------------------------------------------------------------')
        print('ПАРАМЕТРЫ SPI устройства {} :'.format(deviceNum))
        print('------------------------------------------------------------')
        # print(device)
        print('Ключевое слово mode: ' + str(device[b'mode']))
        print('Бит за слово (bits per word): ' + str(device[b'bits']))
        print('Скорость транзакции : ' + str(device[b'speed']) + ' Гц')
        print('Задержка : ' + str(device[b'delay']) + ' мс')

        # Close file descriptors
        spi.closeSPI(device)


    except Exception as be:
        print("\033[31m {}".format('Возникла ошибка в программе:' + "\033[31m {}".format(be.with_traceback())))
        print("\033[30m {}".format(""))
        return -1


# @ ToDo UNDER CONSTRUCTION TEST IT !
def spi_test_(self, CHIP_SELECT_0_OR_1, value_8bit=[191, 192, 193]):
    try:
        import spidev
        spi = spidev.SpiDev()
        spi.open(0, CHIP_SELECT_0_OR_1)
        spi.max_speed_hz = 1000000

        resp = spi.xfer(value_8bit)
        print(' ОБРАЩЕНИЕ К АКСЕЛЕРОМЕТРУ MPU92/65 ПО SPI ')
        print('-----------------------------------------')
        print(' Ответ по SPI от устройства в виде числовой последовательности: ' + str(resp))
        zAccel = (value_8bit[1] << 8) + value_8bit[2]
        print(' Акселлерация по оси Z: ' + str(zAccel))
        return zAccel
    except Exception as be:
        print("\033[31m {}".format('Возникла ошибка в программе:' + "\033[31m {}".format(be.with_traceback())))
        print("\033[30m {}".format(""))
        return -1







