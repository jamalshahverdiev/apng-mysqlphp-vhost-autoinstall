#!/bin/env python2.7

import cmd
import time
import sys
import os

def ap():
    print('\nScript Domain adi teleb edir.')
    arg1 = raw_input('Xahis olunur domain adini daxil edesiniz: ')
    os.system('yum -y install epel-release')
    os.system('yum -y install httpd mod_ssl openssl')
    os.system('mkdir -p /usr/local/domen/')
    os.system('mkdir /var/log/httpd/')
    os.system('/bin/cp -f `pwd`/httpd.conf /etc/httpd/conf/')
    os.system('echo \"Include /usr/local/domen/*\" >> /etc/httpd/conf/httpd.conf')
    os.system('mkdir -p /var/www/'+arg1+'/public_html')
    os.system('chown -R apache:apache /var/www/'+arg1+'/public_html')
    os.system('chown -R apache:apache /usr/local/domen/')
    os.system('chmod 755 /var/www')
    os.system('touch /var/www/'+arg1+'/public_html/index.html')

    reps = {'www.domain.lan':arg1}
    with open('/var/www/'+arg1+'/public_html/index.html', 'w') as outfile:
        with open(os.getcwd()+'/tempindex.html', 'r') as infile:
            for line in infile:
                for src, target in reps.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)

    vhf = {'domain':arg1}
    with open('/usr/local/domen/'+arg1, 'w') as outfile:
        with open(os.getcwd()+'/domain', 'r') as infile:
            for line in infile:
                for src, target in vhf.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)

    os.system('touch /var/log/httpd/'+arg1+'_error.log')
    os.system('touch /var/log/httpd/'+arg1+'_access.log')
    os.system('chkconfig httpd on')
    os.system('/etc/init.d/httpd start')
    time.sleep(3)
    apidfile = '/var/run/httpd/httpd.pid'
    if os.path.isfile(apidfile):
        print('\nArtiq apache web server yuklenmis ve VirtualHost yaradilmisdir.')
    else:
        print('Web server Apache-in ishe dushmesinde problem bas vermishdir')
        sys.exit()
    print('\n\n################################################################')
    print('1. PHP ve MySQL yukleyib qurmaq ucun 1 daxil edib ENTER sixin.')
    print('2. Scriptden cixmaq ucun, 2 daxil edib ENTER sixin.')
    arg2 = raw_input('Xahis olunur seciminizi edesiniz: ')

    if arg2 == str or len(arg2) != 1:
        print("\nYalniz 1 ve ya 2 reqemini birlikde olmamaqla daxil etmek mumkundur.")
        sys.exit()
    elif len(arg2) == 1 and (arg2 == 1 or arg2 == 2):
        print(arg2, "daxil etdiniz...")
        pass

    if int(arg2) == 1:
        os.system('yum -y install mysql-server.x86_64 php php-mysql')
        os.system('/etc/init.d/mysqld start')
        os.system('chkconfig mysqld on')
        os.system('service httpd restart')
        print('\n\n')
        mpidfile = '/var/run/mysqld/mysqld.pid'
        if os.path.isfile(mpidfile):
            print('MySQL-in tehlukesizlik qurashdirmalarini edin.....')
            time.sleep(3)
            os.system('mysql_secure_installation')
        else:
            print('MySQL islemir')
            sys.exit()
        time.sleep(3)
        print('Artiq MySQL qurulmushdur..........')
        sqlroot = raw_input('MySQL root istifadeci sifresini daxil edin: ')
        newdb = raw_input('Yeni yaradilacaq baza adini daxil edin: ')
        newdbuser = raw_input('Yeni yaradilacaq MySQL istifadeci adini daxil edin: ')
        newdbpass = raw_input(newdbuser+' istifadecinin sifresini daxil edin: ')
        os.system('mysql -u root -p%s -e "CREATE DATABASE %s;"' %(sqlroot, newdb))
        os.system('mysql -u root -p%s -e "GRANT ALL PRIVILEGES ON %s.* TO %s@localhost IDENTIFIED BY \'%s\';"' %(sqlroot, newdb,newdbuser, newdbpass))
        os.system('mysql -u root -p%s -e "FLUSH PRIVILEGES;"' %(sqlroot))

        replacements = {'saytdb':newdb, 'saytuser':newdbuser, 'freebsd':newdbpass}
        with open('/var/www/'+arg1+'/public_html/index.php', 'w') as outfile:
            with open(os.getcwd()+'/tempindex.php', 'r') as infile:
                for line in infile:
                    for src, target in replacements.iteritems():
                        line = line.replace(src, target)
                    outfile.write(line)

        os.system('/etc/init.d/httpd restart')
        print('\nApache web server yuklenmis ve ishlek veziyyetdedir\n\n')
    else:
        sys.exit()

def ng():
    print('\nScript Domain adi teleb edir.')
    arg1 = raw_input('Xahis olunur domain adini daxil edesiniz: ')

    os.system('yum -y install epel-release')
    os.system('yum -y install nginx')
    os.system('mkdir -p /var/www/'+arg1+'/public_html')
    os.system('chown -R nginx:nginx /var/www/'+arg1+'/public_html')
    os.system('chmod 755 /var/www')
    os.system('touch /var/www/'+arg1+'/public_html/index.html')

    nghtreps = {'ngsec.lan':arg1}
    with open('/var/www/'+arg1+'/public_html/index.html', 'w') as outfile:
        with open(os.getcwd()+'/ngindex.html', 'r') as infile:
            for line in infile:
                for src, target in nghtreps.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)

    os.system('touch /etc/nginx/conf.d/'+arg1+'.conf')

    ngvhcnfreps = {'ngsec.lan':arg1}
    with open('/etc/nginx/conf.d/'+arg1+'.conf', 'w') as outfile:
        with open(os.getcwd()+'/ngsec.conf', 'r') as infile:
            for line in infile:
                for src, target in ngvhcnfreps.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)

    os.system('chkconfig nginx on')
    os.system('/etc/init.d/nginx restart')
    time.sleep(3)
    os.system('/bin/cp -f `pwd`/nginx.conf /etc/nginx/')

    ngpfile = '/var/run/nginx.pid'
    if os.path.isfile(ngpfile):
        print('\nArtiq nginx web server yuklenmis ve virtual host yaradilmisdir.\n\n')
    else:
        print('Web serverin ise dusmesi prosesinde her hansisa sehv bas vermisdir.')
        sys.exit()

    print('################################################################')
    print('1. PHP-FPM ve MySQL yukleyib qurmaq ucun 1 daxil edib ENTER sixin.')
    print('2. Scriptden cixmaq ucun, 2 daxil edib ENTER sixin.')
    arg2 = raw_input('Xahis olunur seciminizi edesiniz: ')

    if arg2 == str or len(arg2) != 1:
        print("\nYalniz 1 ya da 2 reqemini tek olmaqla daxil ede bilersiniz.")
        sys.exit()
    elif len(arg2) == 1 and (arg2 == 1 or arg2 == 2):
        print(arg2, "daxil etdiniz...")
        pass

    if int(arg2) == 1:
        os.system('yum -y install mysql-server.x86_64 php-fpm php-mysql')
        os.system('/etc/init.d/mysqld start')
        os.system('chkconfig mysqld on')
        os.system('service nginx restart')
        print('\n\n')
        mpidfile = '/var/run/mysqld/mysqld.pid'
        if os.path.isfile(mpidfile):
            print('MySQL-in tehlukesizlik qurashdirmalarini edin.....')
            time.sleep(3)
            os.system('mysql_secure_installation')
        else:
            print('MySQL islemir')
            sys.exit()	
        time.sleep(3)
        print('Artiq MySQL qurulmushdur..........')
        sqlroot = raw_input('MySQL root istifadeci sifresini daxil edin: ')
        newdb = raw_input('Yeni yaradilacaq baza adini daxil edin: ')
        newdbuser = raw_input('Yeni yaradilacaq MySQL istifadeci adini daxil edin: ')
        newdbpass = raw_input(newdbuser+' istifadecinin sifresini daxil edin: ')
        os.system('mysql -u root -p%s -e "CREATE DATABASE %s;"' %(sqlroot, newdb))
        os.system('mysql -u root -p%s -e "GRANT ALL PRIVILEGES ON %s.* TO %s@localhost IDENTIFIED BY \'%s\';"' %(sqlroot, newdb,newdbuser, newdbpass))
        os.system('mysql -u root -p%s -e "FLUSH PRIVILEGES;"' %(sqlroot))
        os.system('/bin/cp -f `pwd`/php.ini /etc/')
        os.system('/bin/cp -f `pwd`/nginx.conf /etc/nginx/')

        dbreps = {'saytdb':newdb, 'saytuser':newdbuser, 'freebsd':newdbpass}
        with open('/var/www/'+arg1+'/public_html/index.php', 'w') as outfile:
            with open(os.getcwd()+'/tempindex.php', 'r') as infile:
                for line in infile:
                    for src, target in dbreps.iteritems():
                        line = line.replace(src, target)
                    outfile.write(line)

        rplace = {'ngphp.lan':arg1}
        with open('/etc/nginx/conf.d/'+arg1+'.conf', 'w') as outfile:
            with open(os.getcwd()+'/ngphp.conf', 'r') as infile:
                for line in infile:
                    for src, target in rplace.iteritems():
                        line = line.replace(src, target)
                    outfile.write(line)

        os.system('rm -rf /var/www/'+arg1+'/public_html/index.html')
        os.system('/bin/cp -f `pwd`/www.conf /etc/php-fpm.d/')
        os.system('/etc/init.d/php-fpm start')
        os.system('/etc/init.d/nginx restart')
        print('\nnGinx web server yuklenmis ve ishlek veziyyetdedir\n\n')
    else:
	print('Scriptden istifade elediyiniz ucun tesekkur edirik...')
	sys.exit()

while True:
    print('Secimleriniz: ')
    print('1. LAMP yukleyib vhost qurmaq ucun, 1 reqemi daxil edib Enter sixin.')
    print('2. Nginx PHP-FPM MySQL yukeyib vhost qurmaq ucun, 2 reqemi daxil edib Enter sixin.')
    print('3. Scriptden cixmaq ucun 3 reqemini daxil edib ENTER sixin.')
    ent = raw_input('Xahis olunur seciminizi edesiniz: ')

    if len(ent) > 1 and (ent != 1 or ent !=2 or ent != 3):
        print("\nYalniz 1, 2 ve 3 reqemini ayri olmaqla daxil etmek olar.")
        sys.exit()
    elif int(ent) == 1 or int(ent) == 2:
#        print(ent, "secmisiniz")
        pass

    if int(ent) == 1:
        ap()
    elif int(ent) == 2:
        ng()
    else:
        break
