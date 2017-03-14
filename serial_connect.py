import serial
import logging

ser = serial.Serial('COM1', 9600)


def fan_on():
    logging.info('turning fan on ...')
    try:
        ser.write('on')
        return True
    except Exception as e:
        logging.error('failed to turn fan on')
        logging.error(e)
        return False


def fan_off():
    logging.info('turning fan off ...')
    try:
        ser.write('off')
        return True
    except Exception as e:
        logging.error('failed to turn fan off')
        logging.error(e)
        return False


if __name__ == '__main__':
    # while ser.inWaiting() == 0:
    #    print 'waiting'
    # fan_on()
    # time.sleep(10)
    # fan_off()
    pass
