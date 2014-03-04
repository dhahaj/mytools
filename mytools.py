import csv,json,subprocess,time
from time import gmtime,asctime
from pprint import *

def cls():
    subprocess.call('CMD /C "CLS"')

def space():
    subprocess.call('CMD /C "ECHO."')

def call(cmd, shell=True, lst=True):
    return subprocess.call(cmd, shell=shell)

def append2file(filename, path, data):
    f = open(filename,'w')
    try:
        f.write(data)
    except IOError as e:
        print e
    finally:
        f.close()

def get_time(sec=0,str=None):
    if sec > 0:
        t = time.gmtime(sec)
        return time.asctime(t)

def pp(what):
	space()
	pprint(what)
	space()

print "mytools!"
