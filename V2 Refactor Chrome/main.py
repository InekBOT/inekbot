from selenium import webdriver
from time import sleep
import schedule
import time
import sys
import yaml
from datetime import *
from rich import print
from rich.panel import Panel
import os
def ekrantemizle():
	os.system('cls' if os.name == 'nt' else 'clear')
from tqdm import tqdm


a = '''
[red]
   _____ ______ _        _____            _    ____   ____ _______ 
  / ____|  ____| |      |_   _|          | |  |  _ \ / __ \__   __|  [green]\|/[/green]          (__)    
 | (___ | |__  | |        | |  _ __   ___| | _| |_) | |  | | | |          `\------(oo)      
  \___ \|  __| | |        | | | '_ \ / _ \ |/ /  _ <| |  | | | |            ||    (__)
  ____) | |    | |____   _| |_| | | |  __/   <| |_) | |__| | | |            ||w--||     [green]\|/[/green]
 |_____/|_|    |______| |_____|_| |_|\___|_|\_\____/ \____/  |_|       [green]\|/[/green]                                                                   
                                                                   
[/red]
'''

ekrantemizle()
saatler = ["10:02","12:02","14:02","13:30","15:30"]
sureuzun = 5400
surekisa = 3600
# ayarlar.yaml dosyasından bilgilerin çekilmesi
with open(r'ayarlar.txt') as file:
	ayarlar = yaml.load(file, Loader=yaml.FullLoader)

kullaniciadi = ayarlar["kullaniciadi"]
sifre = ayarlar["sifre"]
print("[green]Kullanıcı Adı: [/green] [red]{}[/red]".format(kullaniciadi))
print("[green]Şifre: [/green] [red]{}[/red]".format(sifre))
print("[#E66000]Chrome Versiyon[/#E66000] ")
print("[blue]Rüzgar Erik - Versiyon: 1.0.0[/blue]")
def yenile():
	ekrantemizle()
	print("[green]Kullanıcı Adı: [/green] [red]{}[/red]".format(kullaniciadi))
	print("[green]Şifre: [/green] [red]{}[/red]".format(sifre))
	print("[#E66000]Chrome Versiyon[/#E66000]")
	print("[blue]Rüzgar Erik - Versiyon: 1.0.0[/blue]")
	print(Panel(a, title="SFL İnekBOT"))





# genel fonksiyon
def canlidersekatil(dersid, sure):
	deneme = 0
	while deneme <= 5:
		browser = webdriver.Chrome(executable_path="chromedriver.exe")
		browser.get("http://sivasfen.canlikatilim.com/login/index.php")
		browser.implicitly_wait(2)
		username_input = browser.find_element_by_xpath('//*[@id="username"]')
		password_input = browser.find_element_by_xpath('//*[@id="password"]')
		username_input.send_keys(kullaniciadi)
		password_input.send_keys(sifre)
		sleep(1)
		login_button = browser.find_element_by_xpath('//*[@id="loginbtn"]')
		login_button.click()
		try:
			if browser.title == "Kontrol paneli":
				print("Giriş Yapıldı")
				sleep(1)
				browser.get("http://sivasfen.canlikatilim.com/mod/bigbluebuttonbn/view.php?id={}".format(dersid))
				print("ders sayfası açıldı")
				join_button = browser.find_element_by_xpath('//*[@id="join_button_input"]')
				join_button.click()
				sleep(1)
				if browser.title == "Sivas Fen Lisesi - CANLI DERS":
					for i in tqdm(range(sure)):
						sleep(1)
					browser.quit()
					break
				else:
					browser.quit()
					print("Canlı Derse Katılım Sağlanamadı Tekrar Deneniyor...")
					deneme += 1
					continue
		          
			else:
				browser.quit()
				print("Giriş Hatası")
				deneme += 1
				continue
        
		except Exception as e:
			print(e)
			browser.quit()
			continue
	yenile()



#pzt
schedule.every().monday.at(saatler[0]).do(lambda: canlidersekatil("77",sureuzun)) 
schedule.every().monday.at(saatler[1]).do(lambda: canlidersekatil("125",sureuzun)) 
schedule.every().monday.at(saatler[2]).do(lambda: canlidersekatil("132",surekisa)) 

#salı
schedule.every().tuesday.at(saatler[0]).do(lambda: canlidersekatil("90",sureuzun)) 
schedule.every().tuesday.at(saatler[1]).do(lambda:canlidersekatil("124",sureuzun)) 
schedule.every().tuesday.at(saatler[2]).do(lambda: canlidersekatil("71",surekisa))

#çrş
schedule.every().wednesday.at(saatler[0]).do(lambda: canlidersekatil("113",sureuzun)) 
schedule.every().wednesday.at(saatler[1]).do(lambda: canlidersekatil("115",sureuzun)) 
schedule.every().wednesday.at(saatler[2]).do(lambda: canlidersekatil("103",surekisa)) 

#prş

schedule.every().thursday.at(saatler[0]).do(lambda: canlidersekatil("72",sureuzun)) 
schedule.every().thursday.at(saatler[1]).do(lambda: canlidersekatil("126",sureuzun)) 
schedule.every().thursday.at(saatler[2]).do(lambda: canlidersekatil("73",surekisa)) 

#cuma
schedule.every().friday.at(saatler[0]).do(lambda: canlidersekatil("111",sureuzun)) 
schedule.every().friday.at(saatler[3]).do(lambda: canlidersekatil("117",sureuzun)) 
schedule.every().friday.at(saatler[4]).do(lambda: canlidersekatil("102",surekisa)) 
#schedule.every().friday.at(saatler[4]).do(lambda: canlidersekatil("157",sureuzun)) #bilgisayar





print(Panel(a, title="SFL İnekBOT"))


while True:
	schedule.run_pending()
	sleep(1)
	time_of_next_run = schedule.next_run()
	time_now = datetime.now()
	time_remaining = time_of_next_run - time_now
	print('Derse Katılmaya Kalan Zaman: ', time_remaining, end='\r')
	sys.stdout.flush()