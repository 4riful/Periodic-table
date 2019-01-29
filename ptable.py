#AUTHOR :_ARiful 4N!k;
#usr/bin/python3! 
#purpose :Education _Date:06\12\18;
#Relase : hope Thirty _1st.
# Ver:0.1
#____starting code__

#c_c is change colours func
def  c_c(text,color,bold=False,**kwarg): 
    colours={
        "red":"31",
        "green":"32",
        "yellow":"33",
        "blue":"34",
        "puple":"35",
        "cyan":"36",
        "white":"37",
        "bark_white":"38"
    }
    if bold != False:
        b=1
    else:
        b=0
    if color.lower() in colours.keys():
        tes=f"\033[{b};{colours.get(color)}m"
    else:
        return "Colour is not available"
#     c=c.format("0",colours.get(color),text)
    if not (kwarg):
        return tes + text
    else:
        if "end_white" in kwarg.keys():
            if kwarg["end_white"]==True:
                return tes + text + "\033[0;38m"
        elif "end_colour" in kwarg.keys():
            if kwarg["end_colour"] in colours.keys():
            	c=kwarg["end_colour"]
            	tess=f"\033[{b};{colours.get(c)}m"
            	return tes + text + tess
            	
            	
            	
# colour changing function finished_
from time import sleep
print(c_c(" \t\t🌷🌷Happy New Year   ","blue","bold=True"))
from time import sleep
print('┏━━┓┏━━┓┏┓┏━━┓  ')
sleep(0.1)
print('┗━┓┃┃┏┓┃┃┃┃┏┓┃  ')
sleep(0.01)
print('┏━┛┃┃┃┃┃┃┃┃┗┛┃  ')
sleep(0.1)
print('┃┏━┛┃┃┃┃┃┃┗━┓┃  ')
sleep(0.1)
print('┃┗━┓┃┗┛┃┃┃┃┗┛┃  ')
sleep(0.01)
print('┗━━┛┗━━┛┗┛┗━━┛  ')
print(c_c("________________from :_@riful 4N!k","red","bold=True"))
sleep(1.5)
print("\n\n")

name=input(c_c("Hi 🙂, What's your name???\n\n[NB. input your name and press inter to continue]\n\n ➡➡","green" ))
sleep(1)



print("\n")
print(c_c(f"welcome \t\t_{name} \tto my","cyan","bold=True"))
sleep(1)

print("\n\n\n")
print('  ___ __  __   _   ___ _____   ')
sleep(0.1)
print(' / __|  \/  | /_\ | _ \_   _|  ')
sleep(0.1)
print(' \__ \ |\/| |/ _ \|   / | |    ')
sleep(0.1)
print(' |___/_|  |_/_/ \_\_|_\ |_|    ')
sleep(1)
print("\n")

print('   ___          _         ___      ')
sleep(0.1)
print('  / _ \___ ____(_)__  ___/ (_)___  ')
sleep(0.1)
print(' / ___/ -_) __/ / _ \/ _  / / __/  ')
sleep(.1)
print('/_/   \__/_/ /_/\___/\_,_/_/\__/   ')
sleep(1)
print("\n\n")
print('  ______     __   __   ')  
sleep(0.1)
print(' /_  __/__ _/ /  / /__  ')
sleep(0.1)
print('  / / / _ `/ _ \/ / -_)  ')
sleep(.1)
print(' /_/  \_,_/_.__/_/\__/   ')
sleep(.1)
print('\t\t\t')                                      
# For smart flushup font_________

lines = ["*********************************************","_______________Version: 0.1__________________","#############################################","____ 🍅 🍅 Release on :Thirty _1st _2018 _____","#############################################"]
                                                                                                                              
from time import sleep
import sys

for line in lines:         
    for c in line:        
        print(c, end='')    # print a single character, and keep the cursor there.
        sys.stdout.flush()
        sleep(.007)       
    print('') 
#for details of atom func [ptb]
def ptb(a,b,c,d,e,f,g,h,i,j,k,l,m):
	print('\n')
	print("+-------------------------------------------+")
	print('|\t Atom  Details  \t    📝 📝   |')
	print('+-------------------------------------------+')
	sleep(1.2)
	print("\n")
	print(c_c('###########################','green',"bold=True"))
	print(f"__ English Name is {a}")
	print("###########################")
	sleep(.5)
	print("\n\n\n")
	print(f'[01.] It is  discoverd in {b}')
	sleep(.5)
	print("\n")
	print(f"[02.] Number of electron__ {c}")
	sleep(.5)
	print("\n")
	print(f"[03.] Number of proton__ {d}")
	sleep(.5)
	print("\n")
	print(f"[04.] Numner of neutron __ {e}")
	sleep(.5)
	print("\n")
	print(f"[05.] Atomic number is __ {f}")
	sleep(.5)
	print("\n")
	print(f"[06.] Atomic weight is--> {g} g/mol")
	sleep(.5)
	print("\n")
	print(f"[07.] Melting point --> {h} °C")
	sleep(.5)
	print("\n")
	print(f"[08.] Phase  → {i}")
	sleep(.5)
	print("\n")
	print(f"[09.] Period No. → {j}")
	sleep(.5)
	print("\n")
	print(f"[10]. Group No. → {k}")
	sleep(.5)
	print(f"\n")
	print(f"[11.] Block → {l}")
	sleep(.5)
	print("\n")
	print(f"[12.] Magnetic Type :  {m}magnetic")
	sleep(.5)
	print("\n\n")
	print("For more info search on google __xd 😂😂😂😂")
#function for elec. config.
def ec(a):
	print(c_c("+-------------------------------------------+","yellow","bold=True"))
	print('|\t 🌀 Eclectronic Configuration🌀     |')
	sleep(1)
	print('+-------------------------------------------+')
	print(f"\n\n\nElectronic Eonfigration of this atom is--->> {a}")
#Author info
from time import sleep
print("\n\n")
print(c_c(
"      _____________________________________________","yellow"))
print(c_c("         ⚠️ ******* 👉 Author info :****** ⚠️  ️ ","yellow","bold=True"))    
print(c_c("      _____________________________________________","green")) 
print("\n")  
print(c_c("      _____________________________________________","red"))
print(c_c("      🔯 €Name:_Ariful ANIK ","green","bold=True"))
print(c_c("      🔯 €Gmail:_4rifulanik@gmail.com ","red","bold=True"))
print(c_c(                        "      🔯 €Github:_github.com/4riful ","blue","bold=True"))        
print("      🔯 €fb :_ https://www.facebook.com/4rifulAnik")   
print("      🔯Institution:_ Police Lines School and College.     ")        
print(c_c("      ______________________________________________","red"))
print("\n\n")
print('_keep patient while program is loading..... \n\n ')
import sys , time
#for i in range(100+1):
	#time.sleep(0.1)
	#sys.stdout.write("\r%d["%i + "%]" + "█" *int(i/2))

	




print("\n")

##############
# welcome note finished 
#user input starting 
print("\n\n\n")
print("\t\t←←←←←Main Program→→→→→→ ")
print("\n\n")
print(c_c(" 🔍🔍🔍What do you want ???? \n\n\n▶️ {1}.At a glance Periodic Table.\n▶️ {2}.Want to know Details  About an Atom.\n▶️ {3}.Want to see Electronic Configaration of an Atom.\n▶️ {4}.The Special Names of Elements in Differents Groups.\n▶️ {5}.Periodic Properties.\n▶️ {6}.About Periodic table.\n▶️ {7}.My purpose.\n\n","puple","bold=True"))
usr=input(c_c("[example : Suposse you want to know atom details just write '2' and press enter.. ️]\n\n\n➡➡  ","red","bold=True"))






# for eletric configration __facility
if usr=="3":
	ask=input(c_c("Please input a symbol of an  atom ✒️ ✒️ ✒️ ✒️ ✒️  \n\n[Ex: suppose you want to see Nitrogen's electronic configaration just write 'N' and press enter.....]\n \n ➡️  ","red"))
	if ask.lower()=="h":
		ec("1s¹")
	elif ask.lower()=="he":
		ec("1s²")
	elif ask.lower()=="li":
		ec("1s² 2s¹")
	elif ask.lower()=="be":
		ec("[He]2s²")
	elif ask.lower()=="b":
		ec("[He]2s² 2p¹")
	elif ask.lower()=="c":
		ec('[He]2s² 2p²')
	elif ask.lower()=="n":
		ec("[He]2s² 2p³") 
	elif ask.lower()=="o":
		ec("[He]2s² 2p⁴")
	elif ask.lower()=="f":
	    ec("[He]2s² 2p5")
	elif ask.lower()=="ne":
	    ec("[He]2s²2p²")
	elif ask.lower()=="na":
		ec("[Ne]3s¹") 
	elif ask.lower()=="mg":
	 	 ec("[Ne]3s²") 
	 
elif usr=="2":
	atom=input("\nPlease input a Atom symbol ..\n\n[ Ex: if want to see Hydrozen's details ,just write 'H' ]\n\n ➡➡ ")
	if atom.lower()=="h":
		ptb ("Hydrozen","1766","1","1","0","1","1.0079","-259.1","Gas","1","IA","s","Dia")
	elif atom.lower() =="he":
		ptb("Helium","1895","2","2","2","2","4.0026","-272.2","Gas","1","VIIA","s","Dia")
	elif atom.lower()=="li":
		ptb("Lithium","1817","3","3","4","3","6.941","180.5","Solid","2","IA","s","Para")
	elif atom.lower()=="be":
		ptb("Berylium","1797","4","4","5","4","9.01","1278","Solid","2","IIA","s","Dia")
	elif atom.lower()=="b":
		ptb("Boron","1808","5","5","6","5","10.81","2075.8","Solid","2","IIA","P","Dia")
	elif atom.lower()=="c":
		ptb("Carbon","1791","6","6","6","6","12.01","3550","Solid","2","IVA","p","Dia")
	elif atom.lower()=="n":
		ptb("Nitrogen","1772","7","7","7","7","14.00","-209","Gas","2","VA","P","Dia")
	elif atom.lower()=="o":
		ptb("Oxigen","1774","8","8","8","8","15.999","-218.4","Gas","2","VIA","P","Dia")
	elif atom.lower()=="f":
		ptb("Florine","1886","9","9","10","9","18.994","-219.7","Gas","2","VIIA","P","Dia") 
	elif atom.lower()=="ne":
		ptb("Neon","1898","10","10","10","16","20.19","-248.6","Gas","2","VIIIA","P","Dia")
	elif atom.lower()=="na":
		ptb("Sodium","1807","11","11","12","11","22.98","97.8","Solid","3","IA","s","Para")
	elif atom.lower()=="mg":
		ptb("Magnesium","1755","12","12","12","12","24","650","Solid","3","IIA","s","Para")
	elif atom.lower()=="al":
		ptb("Aluminium","1825","13","13","14","13","26.98","660","Solid","3","IIIA","P","Para")
	elif atom.lower()=="si":
		ptb("Silicon","1824","14","14","14","14","28","1414.85","Solid","3","IVA","p","Dia")
	elif atom.lower()=="P":
		ptb("Phosphorus","1669","15","15","16","15","30.97","404.15","Solid","3","VA","P","Dia")
	elif atom.lower()=="s":
		ptb("Sulfur","1774","16","16","16","16","32.0625","112.85","Solid","3","VIA","P","Dia")
	elif atom.lower()=="cl":
		ptb("Cholorine","1774","17","17","18","17","35.45","-100.95","Gas","3","VIIA","P","Dia")
	elif atom.lower()=="ar":
		ptb("Argon","1894","18","18","22","18","39.94","-189.35","Gas","3","VIIIA","p","Dia")
	elif atom.lower()=="k":
		ptb("Potassium","1807","19","19","20","19","39.09","63.65","Solid","4","IA","s","Para")
	elif atom.lower()=="ca":
		ptb("Calcium","1808","20","20","20","20","40.078","838.85","Solid","4","IIA","s","Para")
	elif atom.lower()=="sc":
		ptb("Scandium","1879","21","21","24","21","44.95","1541","Solid","4","IIB","d","Para")
	elif atom.lower()=="ti":
		ptb("Titanium","1791","22","22","26","22","47.86","1660","Solid","4","IVB","d","Para")
	elif atom.lower()=="v":
		ptb("Vanadium","1801","23","23","28","23","50.94","1910","Solid","4","VB","d","Para")
	elif atom.lower()=="cr":
		ptb("Chromium","1797","24","24","28","24","51.9961","1855","Solid","4","VIB","d","Antiferro")
	elif atom.lower()=="mn":
		ptb("Manganese","1764","25","25","30","25","54.93","1242","Solid","4","VIIB","d","Para")
	elif atom.lower()=="fe":
		ptb("Iron","<not found>","26","26","30","26","55.845","1535.85","Solid","4","VIIIB","d","Ferro")
	elif atom.lower()=="co":
		ptb("Cobalt","1735","27","27","32","27","98.93","1493","Solid","4","VIIIB","d","Ferro")
	elif atom.lower()=="ni":
		ptb("Nikel","1751","28","28","31","28","58.69","1453","Solid","4","VIIIB","d","Antiferro")
	elif atom.lower()=="cu":
		ptb("Cupper","<not found>","29","29","35","29","63.54","1083.4","Solid","4","IB","d","Dia")
	elif atom.lower()=="zn":
		ptb("Zinc","1738","30","30","35","30","65.40","419.6","Solid","4","IIB","d","Dia")
	elif atom.lower()=="ga":
		ptb("Gallium","1875","31","31","39","31","69.72","29.8","Solid","4","IIA","p","Dia")
	elif atom.lower()=="ge":
		ptb("Germanium","1886","32","32","41","32","72.64","935.6","Solid","4","IVA","p","Dia")
	elif atom.lower()=="as":
		ptb("Arsenic","1250","33","33","42","33","74.92","816.8","Solid","4","VA","p","Para")
	elif atom.lower()=="se":
		ptb("Selenium","1817","34","34","45","34","78.96","215","Solid","4","VIA","p","Dia")
	elif atom.lower()=="br":
		ptb("Bromine","1826","35","35","45","35","79.90","-7.3","Liquid","4","VIIA","p","Dia")
	elif atom.lower()=="kr":
		ptb("Krypton","1898","36","36","48","36","83.79","-156.6","Gas","4","VIIIA","p","Dia")
	elif atom.lower()=="rb":
		ptb("Rubidium","1861","37","37","48","37","85.467","39","Solid","5","IA","s","Para")
	elif atom.lower()=="sr":
		ptb("Strontium","1790","38","38","50","38","87.62","777","Solid","5","IIA","s","Para")
	elif atom.lower()=="y":
		ptb("Yttrium","1794","39","39","50","39","88.905","1525","Solid","5","IIIB","d","Para")
	elif atom.lower()=="zr":
		ptb("Zirconium","1789","40","40","51","40","91.224","1852","Solid","5","IVB","d","Para")
	elif atom.lower()=="nb":
		ptb("Niobium","1801","41","41","52","41","92.906","2468","Solid","5","VB","d","Para")
	elif atom.lower()=="mo":
		ptb("Molybdenum","1781","42","42","54","42","95.94","2617","Solid","5","VIB","d","Para")
	elif atom.lower()=="tc":
		ptb("Technetium","1937","43","43","55","43","98.906","2157","Solid","5","VIIB","d","Para")
	elif atom.lower()=="ru":
		ptb("Ruthenium","1844","44","44","58","44","107.07","2334","Solid","5","VIIIB","d","Para")
	elif atom.lower()=="rh":
		ptb("Rhodium","1803","45","45","57","45","102.905","1966","Solid","5","VIIIB","d","Para")
	elif atom.lower()=="pd":
		ptb("Palladium","1803","46","46","60","46","106.42","1552","Solid","5","VIIIB","d","Para")
	elif atom.lower()=="ag":
		ptb("Silver","<not found>","47","47","61","47","107.868","961.9","Solid","5","IB","d","Dia")
	elif atom.lower()=="cd":
		ptb("Cadmium","1817","48","48","64","48","112.441","319.1","Solid","5","IIB","d","Dia")
	elif atom.lower()=="in":
		ptb("Indium","1863","49","49","66","49","114.818","156.2","Solid","5","IIIA","p","Dia")
	elif atom.lower()=="sn":
		ptb("Tin","<not found>","50","50","69","50","118.710","232","Solid","5","IVA","p","Para")
	elif atom.lower()=="sb":
		ptb("Antimony","<not found>","51","51","71","51","121.760","630.7","Solid","5","VA","p","Dia")
	elif atom.lower()=="te":
		ptb("Tellurium","1783","52","52","75","52","127.60","449.6","Solid","5","VIA","p","Dia")
	elif atom.lower()=="i":
		ptb("Iodine","1811","53","53","74","53","126.904","113.5","Solid","5","VIIA","p","Dia")
	elif atom.lower()=="xe":
		ptb("Xenon","1898","54","54","77","54","131.293","-111.9","Gas","5","VIIIA","p","Dia")
	elif atom.lower()=="cs":
		ptb("Cesium","1860","55","55","78","55","132.905","28.44","Solid","6","IA","s","Para")
	elif atom.lower()=="ba":
		ptb("Barium","1808","56","56","81","56","137.327","727","Solid","6","IIA","s","para")
	elif atom.lower()=="la":
		ptb("Lanthanum","1839","57","57","82","57","138.905","920","Solid","6","IIIB","d","Para")
	elif atom.lower()=="ce":
		ptb("Cerium","1803","58","58","82","58","140.16","798","Solid","6","n/a","f","para")
	elif atom.lower()=="pr":
		ptb("praseodymium","1885","59","59","82","59","140.904","931","Solid","6","n/a","f","Para")
	elif atom.lower()=="nd":
		ptb("Neodymium","1885","60","60","84","60","144.242","1010","Solid","6","n/a","f","Para")
	elif atom.lower()=="pm":
		ptb("Promethium","1945","61","61","85","61","146.915","1166","Solid","6","n/a","f","")



	
#special elements
elif usr =="4":
	print(" \n_Some special elements are :\n{1}.Alkaili metals\n{2}.inferior metals\nNoble metals \n{3}.Halozen metals .")
	
