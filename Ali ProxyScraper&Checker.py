import requests
import os
import subprocess
import random
import re
import threading
import urllib.request
import argparse
import sys
from time import sleep
from colorama import Fore, Back, Style, init
from time import time
from sys import stdout
init(autoreset=True)
from rich import pretty
from rich.text import Text as tekz
import random
zombie = '\033[2;32m'  'Ali  Proxy Checker & Generator'

for char in zombie:
    stdout.write(char)
    stdout.flush()
    sleep(0.05)
zombie = '\x1b[1;33m[\x1b[1;36m Have a Nice Day\x1b[1;33m]\x1b[1;32m\n'
for char in zombie:
    stdout.write(char)
    stdout.flush()
    sleep(0.10)
output_file = 'Ali Proxy.txt'
os.system('cls' if os.name == 'nt' else 'clear')

if os.path.isfile(output_file):
    os.remove(output_file)

proxy_urls = [
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt',
            'https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
            'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
            'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
            'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
            'https://rootjazz.com/proxies/proxies.txt',
            'https://spys.me/proxy.txt',
            'https://proxyspace.pro/http.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt',
            'https://www.proxy-list.download/api/v1/get?type=socks5',
            'https://api.openproxylist.xyz/socks5.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
            'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
            'https://api.openproxylist.xyz/socks4.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
            'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
            'https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all',
            'https://api.openproxylist.xyz/http.txt',
            'https://alexa.lr2b.com/proxylist.txt',
            'https://multiproxy.org/txt_all/proxy.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
            'https://api.openproxylist.xyz/http.txt',
            'https://alexa.lr2b.com/proxylist.txt',
            'https://multiproxy.org/txt_all/proxy.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt',
            'https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
            'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
            'https://sunny9577.github.io/proxy-scraper/proxies.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
            'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt',
            'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
            'https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt',
            'https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt',
            'https://spys.me/socks.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
            'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks4.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt',
            'https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
            'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
            'https://sunny9577.github.io/proxy-scraper/proxies.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
            'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt',
            'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
            'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4',
            'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all',
            'https://api.openproxylist.xyz/socks4.txt',
            'https://proxyspace.pro/socks4.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
            'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks4.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt',
            'https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
            'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt',
            'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
            'https://api.openproxylist.xyz/socks5.txt',
            'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5',
            'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5',
            'https://proxyspace.pro/socks5.txt',
            'https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt',
            'https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt',
            'https://spys.me/socks.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt'
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
            'https://proxyspace.pro/https.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt',
            'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
            'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
            'https://rootjazz.com/proxies/proxies.txt',
            'https://spys.me/proxy.txt',
            'https://proxyspace.pro/http.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt'
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
            'https://openproxy.space/list/socks5',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
            'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
            'https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
            'https://proxyspace.pro/https.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
            'https://api.openproxylist.xyz/socks4.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
            'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4',
            'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all',
            'https://api.openproxylist.xyz/socks4.txt',
            'https://proxyspace.pro/socks4.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt',
            'https://openproxy.space/list/socks5',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt',
'https://www.proxy-list.download/api/v1/get?type=socks5',
'https://api.openproxylist.xyz/socks5.txt',
'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
'https://api.openproxylist.xyz/socks5.txt',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5',
'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5',
'https://proxyspace.pro/socks5.txt',
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
'https://api.openproxylist.xyz/http.txt',
'https://api.proxyscrape.com/v2/?request=displayproxies',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
'http://worm.rip/http.txt',
'https://proxyspace.pro/http.txt',
'https://multiproxy.org/txt_all/proxy.txt',
'https://proxy-spider.com/api/proxies.example.txt',
'https://proxylist.geonode.com/api/proxy-list?limit=350&page=1&sort_by=lastChecked&sort_type=desc',
'http://globalproxies.blogspot.com/',
'http://www.cybersyndrome.net/plz.html',
'http://www.cybersyndrome.net/plr5.html',
'http://biskutliat.blogspot.com/',
'http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html',
'http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html',
'http://www.cybersyndrome.net/pla5.html',
'http://vipprox.blogspot.com/2013_06_01_archive.html',
'http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html',
'http://vipprox.blogspot.com/p/blog-page_7.html',
'http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html',
'http://vipprox.blogspot.com/2013_02_01_archive.html',
'http://alexa.lr2b.com/proxylist.txt',
'http://vipprox.blogspot.com/2013_03_01_archive.html',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196260',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196258',
'http://sock5us.blogspot.com/2013/06/01-07-13-free-proxy-server-list.html',#comment-form
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196251',
'http://free-ssh.blogspot.com/feeds/posts/default',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196259',
'http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html',
'http://proxyfirenet.blogspot.com/',
'https://www.javatpoint.com/proxy-server-list',
'https://openproxy.space/list/http',
'http://proxydb.net/',
'http://olaf4snow.com/public/proxy.txt',
'http://westdollar.narod.ru/proxy.htm',
'https://openproxy.space/list/socks4',
'https://openproxy.space/list/socks5',
'http://tomoney.narod.ru/help/proxi.htm',
'http://sergei-m.narod.ru/proxy.htm',
'http://rammstein.narod.ru/proxy.html',
'http://greenrain.bos.ru/R_Stuff/Proxy.htm',
'http://inav.chat.ru/ftp/proxy.txt',
'http://johnstudio0.tripod.com/index1.htm',
'http://atomintersoft.com/transparent_proxy_list',
'http://atomintersoft.com/anonymous_proxy_list',
'http://atomintersoft.com/high_anonymity_elite_proxy_list',
'http://atomintersoft.com/products/alive-proxy/proxy-list/3128',
'http://atomintersoft.com/products/alive-proxy/proxy-list/com',
'http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/',
'http://atomintersoft.com/products/alive-proxy/socks5-list',
'http://atomintersoft.com/proxy_list_domain_com',
'http://atomintersoft.com/proxy_list_domain_edu',
'http://atomintersoft.com/proxy_list_domain_net',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
'http://atomintersoft.com/proxy_list_domain_org',
'http://atomintersoft.com/proxy_list_port_3128',
'http://atomintersoft.com/proxy_list_port_80',
'http://atomintersoft.com/proxy_list_port_8000',
'http://atomintersoft.com/proxy_list_port_81',
'http://hack-hack.chat.ru/proxy/allproxy.txt',
'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
'http://hack-hack.chat.ru/proxy/anon.txt',
'http://hack-hack.chat.ru/proxy/p1.txt',
'http://hack-hack.chat.ru/proxy/p2.txt',
'http://hack-hack.chat.ru/proxy/p3.txt',
'http://hack-hack.chat.ru/proxy/p4.txt',
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://free-proxy-list.net/',
'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt',
'https://www.us-proxy.org/',
'https://free-proxy-list.com/',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5',
'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true',
'https://www.proxyscan.io/download?type=http',
'https://proxyspace.pro/socks5.txt',
'https://proxyspace.pro/http.txt',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://www.proxy-list.download/api/v1/get?type=http',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html',
'http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html',
'http://vipprox.blogspot.com/2013_06_01_archive.html',
'http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html',
'http://vipprox.blogspot.com/p/blog-page_7.html',
'http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html',
'http://vipprox.blogspot.com/2013_02_01_archive.html',
'http://alexa.lr2b.com/proxylist.txt',
'http://vipprox.blogspot.com/2013_03_01_archive.html',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196251',
'http://free-ssh.blogspot.com/feeds/posts/default',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196259',
'http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html',
'http://proxyfirenet.blogspot.com/',
'https://www.javatpoint.com/proxy-server-list',
'https://openproxy.space/list/http',
'http://proxydb.net/',
'http://olaf4snow.com/public/proxy.txt',
'https://openproxy.space/list/socks4',
'https://openproxy.space/list/socks5',
'http://rammstein.narod.ru/proxy.html',
'http://greenrain.bos.ru/R_Stuff/Proxy.htm',
'http://inav.chat.ru/ftp/proxy.txt',
'http://johnstudio0.tripod.com/index1.htm',
'http://atomintersoft.com/transparent_proxy_list',
'http://atomintersoft.com/anonymous_proxy_list',
'http://atomintersoft.com/high_anonymity_elite_proxy_list',
'http://atomintersoft.com/products/alive-proxy/proxy-list/3128',
'http://atomintersoft.com/products/alive-proxy/proxy-list/com',
'http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/',
'http://atomintersoft.com/products/alive-proxy/socks5-list',
'http://atomintersoft.com/proxy_list_domain_com',
'http://atomintersoft.com/proxy_list_domain_edu',
'http://atomintersoft.com/proxy_list_domain_net',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
'http://atomintersoft.com/proxy_list_domain_org',
'http://atomintersoft.com/proxy_list_port_3128',
'http://atomintersoft.com/proxy_list_port_80',
'http://atomintersoft.com/proxy_list_port_8000',
'http://atomintersoft.com/proxy_list_port_81',
'http://hack-hack.chat.ru/proxy/allproxy.txt',
'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
'http://hack-hack.chat.ru/proxy/anon.tx',
'http://hack-hack.chat.ru/proxy/p1.txt',
'http://hack-hack.chat.ru/proxy/p2.txt',
'http://hack-hack.chat.ru/proxy/p3.txt',
'http://hack-hack.chat.ru/proxy/p4.txt',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
]

def download_and_save_proxies(url, output_file):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_file, 'a') as file:
                file.write(response.text)
                print(f"{Fore.WHITE}Successfully Collecting Proxy On {url} ({Fore.GREEN}Scraper By Root{Fore.GREEN})")
        else:
            print(f"{Fore.RED}Failed to Collecting Proxy On{url}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Falid {url}{Fore.RESET}")

open(output_file, 'w').close()

class Proxy:
    def __init__(self, method, proxy):
        if method.lower() not in ["http", "https"]:
            raise NotImplementedError("Only HTTP and HTTPS are supported")
        self.method = method.lower()
        self.proxy = proxy

    def is_valid(self):
        return re.match(r"\d{1,3}(?:\.\d{1,3}){3}(?::\d{1,5})?$", self.proxy)

    def check(self, site, timeout, user_agent):
        url = self.method + "://" + self.proxy
        proxy_support = urllib.request.ProxyHandler({self.method: url})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        req = urllib.request.Request(self.method + "://" + site)
        req.add_header("User-Agent", user_agent)
        try:
            start_time = time()
            urllib.request.urlopen(req, timeout=timeout)
            end_time = time()
            time_taken = end_time - start_time
            return True, time_taken, None
        except Exception as e:
            return False, 0, e

    def __str__(self):
        return self.proxy

def verbose_print(verbose, message):
    if verbose:
        print(message)

def check(file, timeout, method, site, verbose, random_user_agent):
    proxies = []
    with open(file, "r") as f:
        for line in f:
            proxies.append(Proxy(method, line.replace("\n", "")))

    print(f"{Fore.GREEN}Checking {Fore.YELLOW}{len(proxies)} {Fore.GREEN}Proxy")
    proxies = filter(lambda x: x.is_valid(), proxies)
    valid_proxies = []
    user_agent = random.choice(user_agents)

    def check_proxy(proxy, user_agent):
        new_user_agent = user_agent
        if random_user_agent:
            new_user_agent = random.choice(user_agents)
        valid, time_taken, error = proxy.check(site, timeout, new_user_agent)
        message = {
            True: f"{proxy} is valid, took {time_taken} seconds",
            False: f"{proxy} is invalid: {repr(error)}",
        }[valid]
        verbose_print(verbose, message)
        valid_proxies.extend([proxy] if valid else [])

    threads = []
    for proxy in proxies:
        t = threading.Thread(target=check_proxy, args=(proxy, user_agent))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    with open(file, "w") as f:
        for proxy in valid_proxies:
            f.write(str(proxy) + "\n")

    print(f"{Fore.GREEN}Found {Fore.YELLOW}{len(valid_proxies)} {Fore.GREEN}valid proxies")


def verbose_print(verbose, message):
    if verbose:
        print(message)

for url in proxy_urls:
    download_and_save_proxies(url, output_file)
    
with open('Ali Proxy.txt', 'r') as ceki:
    jumlh = sum(1 for line in ceki)
    
print(f"\nCongralutions You Got {Fore.WHITE}( {Fore.YELLOW}{jumlh} {Fore.WHITE}) Do u want check it ? {Fore.WHITE}({Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE}): ", end="")
choice = input().strip().lower()

if choice == 'y' or choice == 'Y':
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    ]
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--timeout", type=int, default=20, help="Dismiss the proxy after -t seconds")
    parser.add_argument("-p", "--proxy", default="http", help="Check HTTPS or HTTP proxies")
    parser.add_argument("-s", "--site", default="https://google.com/", help="Check with specific website like google.com")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    parser.add_argument("-r", "--random_agent", action="store_true", help="Use a random user agent per proxy")
    
    args = parser.parse_args()
    check(file=output_file, timeout=args.timeout, method=args.proxy, site=args.site, verbose=args.verbose, random_user_agent=args.random_agent)
    sys.exit(0)
else:
    print(f"{Fore.WHITE} Congratulations, the proxy scrape has been completed ")