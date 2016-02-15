#!/bin/env python

import sys

def phpmysql():
        print('###########################################################')
        print('Artiq apache web server yuklenmis ve VirtualHost yaradilmisdir.')
        print('1. PHP ve MySQL yukleyib qurmaq ucun 1 daxil edib ENTER sixin.')
        print('2. Scriptden cixmaq ucun, 2 daxil edib ENTER sixin.')
        arg2 = input('Xahish olunur seciminizi edesiniz: ')
        if arg2 == 1:
                os.system('yum -y install mysql-server.x86_64 php php-mysql')
                os.system('/etc/init.d/mysqld start')
                os.system('chkconfig mysqld on')
        else:
                sys.exit()

phpmysql()
