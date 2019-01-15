#AUTHOR :_ARiful 4N!k;
#usr/bin/python3! 
#purpose :Education _Date:06\12\18;
#Relase : hope Thirty _1st.
# Ver:0.1
#____starting code__
# For stylish and transparent font;

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
print(c_c(f"welcome \t\t__________{name} ","cyan","bold=True"))

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
	sleep(.1)
	print("\n")
	print(f"[02.] Number of electron__{c}")
	sleep(.1)
	print("\n")
	print(f"[03.] Number of proton__{d}")
	sleep(.1)
	print("\n")
	print(f"[04.] Numner of neutron __{e}")
	sleep(.1)
	print("\n")
	print(f"[05.] Atomic number is __{f}")
	sleep(.1)
	print("\n")
	print(f"[06.] Atomic weight is-->{g} g/mol")
	sleep(.1)
	print("\n")
	print(f"[07.] Melting point --> {h} °C")
	sleep(.1)
	print("\n")
	print(f"[08.] Phase  →{i}")
	sleep(.1)
	print("\n")
	print(f"[09.] Period No. →{j}")
	sleep(.1)
	print("\n")
	print(f"[10]. Group No. →{k}")
	sleep(.1)
	print(f"\n")
	print(f"[11.] Block →{l}")
	sleep(.1)
	print("\n")
	print(f"[12.] Magnetic Type :  {m}magnetic")
	sleep(.1)
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
print(c_c("      ______________________________________________","red"))
print("\n\n")
print('_keep patient while program is loading..... \n\n ')
import sys , time
for i in range(100+1):
	time.sleep(0.1)
	sys.stdout.write("\r%d["%i + "%]" + "█" *int(i/2))
	




print("\n")

##############
# welcome note finished 
#user input starting 
print("\n\n\n")
print("\t\t←←←←←Main Program→→→→→→ ")
print("\n\n")
print(c_c(" 🔍🔍🔍What do you want ???? \n\n\n▶️{1}.At a glance Periodic Table.\n▶️{2}.Want to know Details  About an Atom.\n▶️{3}.Want to see Electronic Configaration of an Atom.\n▶️{4}.The Special Names of Elements in Differents Groups.\n▶️{5}.Periodic Properties.\n▶️{6}.About Periodic table.\n▶️{7}.My purpose.\n\n","puple","bold=True"))
usr=input(c_c("[example : Suposse you want to know atom details just write '2' and press enter.. ️]\n\n\n➡➡","red","bold=True"))
#for at a glance periodic table
# for eletric configration __facility
if usr=="3":
	ask=input(c_c("Please input a symbol of an  atom ✒️ ✒️ ✒️ ✒️ ✒️  \n\n[Ex: suppose you want to see Nitrogen's electronic configaration just write 'N' and press enter.....]\n \n ➡️ ","red"))
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
		ptb ("Hydrozen","1766","1","1","0","1","1.0079","-259.1","Gas","1","IA","S","Dia")
	elif atom.lower() =="he":
		ptb("Helium","1895","2","2","2","2","4.0026","-272.2","Gas","1","VIIA","S","Dia")
	elif atom.lower()=="li":
		ptb("Lithium","","","","","","","","","","","") 
	
	
	