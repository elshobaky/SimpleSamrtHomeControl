import os
import sys
import time
import socket
import logging
from bottle import (route, run,
                    template, static_file,
                    redirect)

from settings import (config_logging, MAIN_DIR,
                      STATIC_DIR, TEMPLATES_DIR)

from serial_connect import fan_on, fan_off


# serve static files , folders
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=STATIC_DIR)


# URL routing and request handlers

# function to render templates
def render(filename, **kwargs):
    filepath = os.path.join(TEMPLATES_DIR, filename)
    return template(filepath, **kwargs)


# main page ,search page
@route('/')
def home():
    """returns html template of Home page.
    provide site navigation options.
    """
    global fan_status
    return render('index.html', fan_status=fan_status)


@route('/fan/on')
def turn_fan_on():
    global fan_status
    if fan_on():
        fan_status = True
    redirect('/')


@route('/fan/off')
def turn_fan_off():
    global fan_status
    if fan_off():
        fan_status = False
    redirect('/')


def reset_fan():
    global fan_status
    logging.info("turnning off fan")
    if fan_off():
        logging.info('fan is turned off')
        fan_status = False
    else:
        logging.error('cannot turn off the fan')
        logging.info('retrying after 5 seconds')
        time.sleep(5)
        logging.info('retrying....')
        if fan_off():
            logging.info('fan is turned off')
            fan_status = False
        else:
            logging.error('cannot turn off the fan')
            sys.exit()


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    ip = s.getsockname()[0]
    s.close()
    if not ip:
        logging.error('cannot get ip automatically. make sure of your network access')
        return user_ip_input()
    return ip


def user_ip_input():
    print """
    please enter the number of one of the following options:
        1- retry to get IP automatically.
        2- run server on the localhost.
        3- enter IP manually.
    """
    choice = raw_input("enter the number of your choice:   ")
    if choice == '1':
        logging.info("retyring to get ip automatically ... ")
        return get_local_ip()
    if choice == '2':
        return 'localhost'
    if choice == '3':
        return raw_input("please enter IP address: ")
    else:
        logging.error('wrong choice')
        return user_ip_input()


if __name__ == '__main__':
    config_logging()
    fan_status = False
    logging.info("getting local IP address ...")
    IP = get_local_ip()
    PORT = 80
    logging.info("IP obtained {}".format(IP))
    logging.info("running server at {}:8080".format(IP))
    logging.info("Initiating server ....")
    logging.info("Setting up wrok directories .. ")
    logging.info("MAIN_DIR = {}".format(MAIN_DIR))
    logging.info("STATIC_DIR = {}".format(STATIC_DIR))

    reset_fan()

    run(host=IP, port=PORT,
        debug=True, server='paste')
