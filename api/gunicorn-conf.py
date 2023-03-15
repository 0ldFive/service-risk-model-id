from gevent import monkey
monkey.patch_all()
import multiprocessing
debug = False
loglevel = 'info'
bind = '127.0.0.1:6800'
pidfile = '/var/gunicron/gunicorn.pid'
logfile = '/var/gunicron/gunicorn.log'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
