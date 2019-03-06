#AUTHOR :_ARiful 4N!k;
#usr/bin/python3! 
#purpose :Education _Date:06\12\18;
#first educational code of mine 
#Relase : hope Thirty _1st.
# Ver:0.1
#____starting code__








#function defining of electron conf.



def ec(a):
	print("\t+-------------------------------------------+")
	print('\t|\t 🌀 Eclectronic Configuration🌀     |')
	sleep(1)
	print('\t+-------------------------------------------+')
	print(f"\n\n\n\tElectronic Eonfigration of this atom is--->> {a}")# 'a'will thee parameter of atom




#defnining function for atom info;;;;
def ptb(a,b,c,d,e,f,g,h,i,j,k,l,m):
	print('\n')
	print("\t+-------------------------------------------+")
	print('\t|\t      Atom  Details  \t📝 📝       |')
	print('\t+-------------------------------------------+')
	sleep(1.2)
	print("\n")
	print('\t###########################')
	print(f"\t _English Name is {a}_")
	print("\t###########################")
	sleep(1)
	print("\n\n\n")
	print(f'\t[01.] It is  discoverd in {b}')
	sleep(1)
	print("\n")
	print(f"\t[02.] Number of electron__ {c}")
	sleep(1)
	print("\n")
	print(f"\t[03.] Number of proton__ {d}")
	sleep(1)
	print("\n")
	print(f"\t[04.] Numner of neutron __ {e}")
	sleep(1)
	print("\n")
	print(f"\t[05.] Atomic number is __ {f}")
	sleep(1)
	print("\n")
	print(f"\t[06.] Atomic weight is--> {g} g/mol")
	sleep(1)
	print("\n")
	print(f"\t[07.] Melting point --> {h} °C")
	sleep(1)
	print("\n")
	print(f"\t[08.] Phase  → {i}")
	sleep(1)
	print("\n")
	print(f"\t[09.] Period No. → {j}")
	sleep(1)
	print("\n")
	print(f"\t[10]. Group No. → {k}")
	sleep(1)
	print(f"\n")
	print(f"\t[11.] Block → {l}")
	sleep(1)
	print("\n")
	print(f"\t[12.] Magnetic Type :  {m}magnetic")
	sleep(1)
	print("\n\n")
	print("\n\n")









####################usr input #################



def speak(usr):
	if usr=="3":
		ask=input("\t\tPlease input a symbol of an  atom ✒️ ✒️ ✒️ ✒️ ✒️  \n\n[Ex: suppose you want to see Nitrogen's electronic configaration just write 'N' and press enter.....]\n \n ➡➡  ")
		if ask.lower()=="h":
			ec("1s¹")
		elif ask.lower()=="he":
			ec("1s²")
		elif ask.lower()=="li":
			ec("1s² 2s¹")
		elif ask.lower()=="be":
			ec("[He] 2s²")
		elif ask.lower()=="b":
			ec("[He] 2s² 2p¹")
		elif ask.lower()=="c":
			ec('[He] 2s² 2p²')
		elif ask.lower()=="n":
			ec("[He] 2s² 2p³") 
		elif ask.lower()=="o":
			ec("[He] 2s² 2p⁴")
		elif ask.lower()=="f":
		        ec("[He] 2s² 2p5")
		elif ask.lower()=="ne":
		        ec("[He] 2s² 2p²")
		elif ask.lower()=="na":
			ec("[Ne] 3s¹") 
		elif ask.lower()=="mg":
		 	ec("[Ne] 3s²") 
		elif ask.lower()=="al":
		 	ec("[Ne] 3s2 3p1")
		elif ask.lower()=="si":
		 	ec("[Ne] 3s2 3p2")
		elif ask.lower()=="p":
		 	ec("[Ne] 3s2 3p3") 
		elif ask.lower()=="s":
		 	ec("[Ne] 3s2 3p4") 
		elif ask.lower()=="cl":
		 	ec("[Ne] 3s2 3p4") 
		elif ask.lower()=="ar":
		 	ec("[Ne] 3s2 3p6") 
		elif ask.lower()=="k":
		 	ec("[Ar] 4s1") 
		elif ask.lower()=="ca":
		 	ec("[Ar] 4s2") 
		elif ask.lower()=="sc":
		 	ec("[Ar] 3d1 4s2") 
		elif ask.lower()=="ti":
		 	ec("[Ar] 3d2 4s2") 
		elif ask.lower()=="v":
		 	ec("[Ar] 3d3 4s2") 
		elif ask.lower()=="cr":
		 	ec("[Ar] 3d5 4s1") 
		elif ask.lower()=="mn":
		 	ec("[Ar] 3d5 4s2") 
		elif ask.lower()=="fe":
		 	ec("[Ar] 3d6 4s2") 
		elif ask.lower()=="co":
		 	ec("[Ar] 3d7 4s2") 
		elif ask.lower()=="ni":
		 	ec("[Ar] 3d8 4s2") 
		elif ask.lower()=="Cu":
		 	ec("[Ar] 3d10 4s1") 
		elif ask.lower()=="zn":
		 	ec("[Ar] 3d10 4s2") 
		elif ask.lower()=="ga":
		 	ec("[Ar] 3d10 4s2 4p1") 
		elif ask.lower()=="ge":
		 	ec("[Ar] 3d10 4s2 4p2") 
		elif ask.lower()=="as":
	 		ec("[Ar] 3d10 4s2 4p3") 
		elif ask.lower()=="se":
		 	ec("[Ar] 3d10 4s2 4p4") 
		elif ask.lower()=="br":
		 	ec("[Ar] 3d10 4s2 4p5") 
		elif ask.lower()=="kr":
		 	ec("[Ar] 3d10 4s2 4p6") 
		elif ask.lower()=="rb":
		 	ec("[Kr] 5s1") 
		elif ask.lower()=="sr":
		 	ec("[Kr] 5s2") 
		elif ask.lower()=="y":
		 	ec("[Kr] 4d1 5s2") 
		elif ask.lower()=="zr":
		 	ec("[Kr] 4d2 5s2") 
		elif ask.lower()=="nb":
		 	ec("[Kr] 4d4 5s1") 
		elif ask.lower()=="mo":
		 	ec("[Kr] 4d5 5s1") 
		elif ask.lower()=="tc":
		 	ec("[Kr] 4d5 5s2") 
		elif ask.lower()=="ru":
		 	ec("[Kr] 4d7 5s1") 
		elif ask.lower()=="rh":
		 	ec("[Kr] 4d8 5s1") 
		elif ask.lower()=="pd":
		 	ec("[Kr] 4d10") 
		elif ask.lower()=="ag":
		 	ec("[Kr] 4d10 5s1") 
		elif ask.lower()=="cd":
		 	ec("[Kr] 4d10 5s2") 
		elif ask.lower()=="in":
		 	ec("[Kr] 4d10 5s2 5p1") 
		elif ask.lower()=="sn":
		 	ec("[Kr] 4d10 5s2 5p2") 
		elif ask.lower()=="sb":
		 	ec("[Kr] 4d10 5s2 5p3") 
		elif ask.lower()=="te":
		 	ec("[Kr] 4d10 5s2 5p4") 
		elif ask.lower()=="i":
		 	ec("[Kr] 4d10 5s2 5p5") 
		elif ask.lower()=="xe":
		 	ec("[Kr] 4d10 5s2 5p6") 
		elif ask.lower()=="cs":
		 	ec("[Xe] 6s1") 
		elif ask.lower()=="ba":
		 	ec("[Xe] 6s2") 
		elif ask.lower()=="la":
		 	ec("[Xe] 5d1 6s2") 
		elif ask.lower()=="ce":
		 	ec("[Xe] 4f1 5d1 6s2") 
		elif ask.lower()=="pr":
		 	ec("[Xe] 4f3 6s2") 
		elif ask.lower()=="nd":
		 	ec("[Xe] 4f4 6s2") 
		elif ask.lower()=="pm":
		 	ec("[Xe] 4f5 6s2") 
		elif ask.lower()=="sm":
		 	ec("[Xe] 4f6 6s2") 
		elif ask.lower()=="eu":
		 	ec("[Xe] 4f7 6s2") 
		elif ask.lower()=="gd":
		 	ec("[Xe] 4f7 5d1 6s2") 
		elif ask.lower()=="tb":
		 	ec("[Xe] 4f9 6s2") 
		elif ask.lower()=="dy":
		 	ec("[Xe] 4f10 6s2") 
		elif ask.lower()=="ho":
		 	ec("[Xe] 4f11 6s2") 
		elif ask.lower()=="er":
		 	ec("[Xe] 4f12 6s2") 
		elif ask.lower()=="tm":
		 	ec("[Xe] 4f13 6s2") 
		elif ask.lower()=="yb":
		 	ec("[Xe] 4f14 6s2") 
		elif ask.lower()=="lu":
		 	ec("[Xe] 4f14 5d1 6s2") 
		elif ask.lower()=="hf":
		 	ec("[Xe] 4f14 5d2 6s2") 
		elif ask.lower()=="ta":
		 	ec("[Xe] 4f14 5d3 6s2") 
		elif ask.lower()=="w":
		 	ec("[Xe] 4f14 5d4 6s2") 
		elif ask.lower()=="re":
		 	ec("[Xe] 4f14 5d5 6s2") 
		elif ask.lower()=="os":
		 	ec("[Xe] 4f14 5d6 6s2") 
		elif ask.lower()=="ir":
		 	ec("[Xe] 4f14 5d7 6s2") 
		elif ask.lower()=="pt":
		 	ec("[Xe] 4f14 5d9 6s1") 
		elif ask.lower()=="au":
		 	ec("[Xe] 4f14 5d10 6s1") 
		elif ask.lower()=="hg":
		 	ec("[Xe] 4f14 5d10 6s2") 
		elif ask.lower()=="tl":
		 	ec("[Xe] 4f14 5d10 6s2 6p1") 
		elif ask.lower()=="pb":
		 	ec("[Xe] 4f14 5d10 6s2 6p2") 
		elif ask.lower()=="bi":
		 	ec("[Xe] 4f14 5d10 6s2 6p3") 
		elif ask.lower()=="po":
		 	ec("[Xe] 4f14 5d10 6s2 6p4") 
		elif ask.lower()=="at":
		 	ec("[Xe] 4f14 5d10 6s2 6p5") 
		elif ask.lower()=="rm":
		 	ec("[Xe] 4f14 5d10 6s2 6p6") 
		elif ask.lower()=="fr":
		 	ec("[Rn] 7s1") 
		elif ask.lower()=="ra":
		 	ec("[Rn] 7s2") 
		elif ask.lower()=="ac":
		 	ec("[Rn] 6d1 7s2") 
		elif ask.lower()=="th":
		 	ec("[Rn] 6d2 7s2") 
		elif ask.lower()=="pa":
		 	ec("[Rn] 6d2 7s2") 
		elif ask.lower()=="u":
		 	ec("[Rn] 5f3 6d1 7s2") 
		elif ask.lower()=="np":
		 	ec("[Rn] 5f4 6d1 7s2") 
		elif ask.lower()=="pu":
		 	ec("[Rn] 5f6 7s2") 
		elif ask.lower()=="am":
		 	ec("[Rn] 5f7 7s2") 
		elif ask.lower()=="cm":
		 	ec("[Rn] 5f7 6d1 7s2") 
		elif ask.lower()=="bk":
		 	ec("[Rn] 5f9 7s2") 
		elif ask.lower()=="cf":
		 	ec("[Rn] 5f10 7s2") 
		elif ask.lower()=="es":
		 	ec("[Rn] 5f11 7s2") 
		elif ask.lower()=="fm":
		 	ec("[Rn] 5f12 7s2") 
		elif ask.lower()=="md":
		 	ec("[Rn] 5f13 7s2") 
		elif ask.lower()=="no":
		 	ec("[Rn] 5f14 7s2") 
		elif ask.lower()=="lr":
		 	ec("[Rn] 5f14 7s2 7p1") 
		elif ask.lower()=="rf":
		 	ec("[Rn] 5f14 6d2 7s2") 
		elif ask.lower()=="db":
		 	ec("[Rn] 5f14 6d3 7s2") 
		elif ask.lower()=="sg":
		 	ec("[Rn] 5f14 6d4 7s2") 
		elif ask.lower()=="bh":
		 	ec("[Rn] 5f14 6d5 7s2") 
		elif ask.lower()=="hs":
		 	ec("[Rn] 5f14 6d6 7s2") 
		elif ask.lower()=="mt":
		 	ec("[Rn] 5f14 6d7 7s2") 
		elif ask.lower()=="ds":
		 	ec("[Rn] 5f14 6d9 7s1") 
		elif ask.lower()=="rg":
		 	ec("[Rn] 5f14 6d10 7s1") 
		elif ask.lower()=="cn":
		 	ec("[Rn] 5f14 6d10 7s2") 
		elif ask.lower()=="nh":
		 	ec("[Rn] 5f14 6d10 7s2 7p1") 
		elif ask.lower()=="fl":
		 	ec("[Rn] 5f14 6d10 7s2 7p2") 
		elif ask.lower()=="mc":
		 	ec("[Rn] 5f14 6d10 7s2 7p3") 
		elif ask.lower()=="lv":
		 	ec("[Rn] 5f14 6d10 7s2 7p4") 
		elif ask.lower()=="ts":
		 	ec("[Rn] 5f14 6d10 7s2 7p5") 
		elif ask.lower()=="og":
		 	ec("[Rn] 5f14 6d10 7s2 7p6") 
		
		 
	elif usr=="2":
		atom=input("\n\tPlease input an Atom symbol ..\n\n\t[ Ex: if want to see Hydrozen's details ,just write 'H' ]\n\n ➡➡ ")
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
			ptb("Promethium","1945","61","61","85","61","146.915","1166","Solid","6","n/a","f","Para")
		elif atom.lower()=="sm":
			ptb("Samarium","1879","62","62","88","62","150.36","1072","Solid","6","n/a","f","Para")
		elif atom.lower()=="eu":
			ptb("Europium","1901","63","63","89","63","151.964","822","Solid","6","n/a","f","Para")
		elif atom.lower()=="gd":
			ptb("Gadolinium","1880","64","64","93","64","157.25","1311","Solid","6","n/a","f","Ferro")
		elif atom.lower()=="tb":
			ptb("Terbium","1843","65","65","93","65","158.925","1360","Solid","6","n/a","f","Para")
		elif atom.lower()=="dy":
			ptb("Dysprosium","1886","66","66","96","66","162.500","1209","Solid","6","n/a","f","Para")
		elif atom.lower()=="ho":
			ptb("Holmium","1878","67","67","97","67","164.93","1470","Solid","6","n/a","f","Para")
		elif atom.lower()=="er":
			ptb("Erbium","1842","68","68","99","68","167.259","1522","Solid","6","n/a","f","Para")
		elif atom.lower()=="tm":
			ptb("Thulium","1879","69","69","99","69","168.934","1545","Solid","6","n/a","f","Para")
		elif atom.lower()=="yb":
			ptb("Ytterbium","1878","70","70","103","70","173.04","824","Solid","6","n/a","f","Para")
		elif atom.lower()=="lu":
			ptb("Lutetium","1906","71","71","103","71","174.967","1656","Solid","6","n/a","f","Para")
		elif atom.lower()=="hf":
			ptb("Hafnium","1923","72","72","107","72","178.49","2233","Solid","6","IVB","d","Para")
		elif atom.lower()=="ta":
			ptb("Tantalum","1802","73","73","108","73","180.947","3017","Solid","6","VB","d","Para")
		elif atom.lower()=="w":
			ptb("Tungsten","1763","74","74","109","74","183.84","3407","Solid","6","VIB","d","Para")
		elif atom.lower()=="re":
			ptb("Rhenium","1925","75","75","111","75","186.207","3180","Solid","6","VIIB","d","Para")
		elif atom.lower()=="os":
			ptb("Osmium","1803","76","76","115","76","190.23","3045","Solid","6","VIIIB","d","Para")
		elif atom.lower()=="ir":
			ptb("Iridium","1803","77","77","115","77","192.217","2410","Solid","6","VIIIB","d","Para")
		elif atom.lower()=="pt":
			ptb("Platinum","1735","78","78","117","78","195.084","1768","Solid","6","VIIIB","d","Para")
		elif atom.lower()=="au":
			ptb("Gold","<not found>","79","79","118","79","196.966","106414","Solid","6","IB","d","Dia")
		elif atom.lower()=="hg":
			ptb("Mercury","1735","80","80","120","80","200.59","-38.9","Liquid","6","IIB","d","Dia")
		elif atom.lower()=="tl":
			ptb("Thallium","1861","81","81","123","81","204.383","303.6","Solid","6","IIIB","p","Dia")
		elif atom.lower()=="pb":
			ptb("Lead","1899","82","82","125","82","207.2","327.5","Solid","6","IVB","p","Dia")
		elif atom.lower()=="bi":
			ptb("Bismuth","1739","83","83","125","83","208.980","71.4","Solid","6","VB","p","Dia")
		elif atom.lower()=="po":
			ptb("Polonium","1898","84","84","126","84","208.9828","254","Solid","6","VIB","p","Non-")
		elif atom.lower()=="at":
			ptb("Astatine","1940","85","85","125","85","209.98","230","Solid","6","VIIB","p","Non-")
		elif atom.lower()=="rn":
			ptb("Radon","1900","86","86","136","86","222.0176","-71","Gas","6","VIIIB","p","Non-")
		elif atom.lower()=="fr":
			ptb("Francium","1939","87","87","136","87","223.0197","20","Solid","7","IA","s","Para")
		elif atom.lower()=="ra":
			ptb("Radium","1898","88","88","138","88","226.0254","958","Solid","7","IIA","s","Non-")
		elif atom.lower()=="ac":
			ptb("Actinium","1899","89","89","138","89","227.0278","1047","Solid","7","IIIB","d","Non-")
		elif atom.lower()=="th":
			ptb("Thorium","1828","90","90","142","90","232.0380","1750","Solid","7","n/a","f","Para")
		elif atom.lower()=="pa":
			ptb("Protactinium","1913","91","91","140","91","231.03","1840","Solid","7","n/a","f","Para")
		elif atom.lower()=="u":
			ptb("Uranium","1789","92","92","146","92","238.0289","1132.4","Solid","7","n/a","f","Para")
		elif atom.lower()=="np":
			ptb("Neptunium","1940","93","93","144","93","237.0482","640","Solid","7","n/a","f","Para")
		elif atom.lower()=="pu":
			ptb("Plutonium","1940","94","94","150","94","244.0642","641","Solid","7","n/a","f","Para")
		elif atom.lower()=="am":
			ptb("Americium","1944","95","95","148","95","243.0614","1176","Solid","7","n/a","f","Para")
		elif atom.lower()=="cm":
			ptb("Curium","1944","96","96","151","96","247.0703","1340","Solid","7","n/a","f","Antiferro-Para")
		elif atom.lower()=="bk":
			ptb("Berkelium","1949","97","97","150","97","247.0703","986","Solid","7","n/a","f","Para")
		elif atom.lower()=="cf":
			ptb("Californium","1950","98","98","153","98","251.0796","900","Solid","7","n/a","f","Non-")
		elif atom.lower()=="es":
			ptb("Einsteinium","1952","99","99","153","99","252.0829","860","Solid","7","n/a","f","Para")
		elif atom.lower()=="fm":
			ptb("Fermium","1952","100","100","157","100","257.0951","1525","Unknown","7","n/a","f","Non-")
		elif atom.lower()=="md":
			ptb("Mendelevium","1955","101","101","157","101","258.09","825","Unknown","7","n/a","f","Non-")
		elif atom.lower()=="no":
			ptb("Noblium","1958","102","102","157","102","259.1009","825","Unknown","7","n/a","f","Non-")
		elif atom.lower()=="lr":
			ptb("Lawerencium","1961","103","103","163","103","266.1193","1625","Unknown","7","n/a","f","Non-")
		elif atom.lower()=="rf":
			ptb("Rutherfordium","1964-69","104","104","157","104","261","2100","Unknown","7","IVB","d","Non-")
		elif atom.lower()=="db":
			ptb("Dubnium","1967","105","105","157","105","262","**","Unknown","7","VB","d","Non-")
		elif atom.lower()=="sg":
			ptb("Seaborgium","1974","106","106","156","106","262","**","Unknown","7","VIB","d","Non-")
		elif atom.lower()=="bh":
			ptb("Bohrium","1976","107","107","157","107","264","**","Unknown","7","VIIB","d","Non-")
		elif atom.lower()=="hs":
			ptb("Hassium","1984","108","108","161","108","269","**","Unknown","7","VIIIB","d","Non-")
		elif atom.lower()=="mt":
			ptb("Meitnrium","1982","109","109","159","109","268","**","Unknown","7","VIIIB","d","Non-")
		elif atom.lower()=="ds":
			ptb("Darmstadtium","1994","110","110","171","110","281.1620","**","Unknown","7","VIIIB","d","Non-")
		elif atom.lower()=="rg":
			ptb("Roentgenium","1994","111","111","170","111","281.1684","**","Unknown","7","IA","d","Non-")
		elif atom.lower()=="cn":
			ptb("Copernicium","1996","112","112","173","112","285.1744","**","Unknown","7","IIA","d","Non-")
		elif atom.lower()=="nh":
			ptb("Nihondium","2004","113","113","173","113","286.1810","425","Unknown","7","IIIA","p","Non-")
		elif atom.lower()=="fl":
			ptb("Flerovium","1999","114","114","173","114","287.1904","68","Unknown","7","IVA","p","Non-")
		elif atom.lower()=="mc":
			ptb("Moscovium","2004","115","115","173","115","288.1943","**","Unknown","7","VA","p","Non-")
		elif atom.lower()=="lv":
			ptb("Livermorium","2000","116","116","175","116","291.2045","**","Unknown","7","VIA","p","Non-")
		elif atom.lower()=="ts":
			ptb("Tennessine","2010","117","117","177","117","294.2104","**","Unknown","7","VIIA","p","Non-")
		elif atom.lower()=="og":
			ptb("Oganesson","2006","118","118","176","118","295.2139","**","Liquid","7","VIIIA","p","Non-")
		else:
			print("\t\tPlease input a valid atom sign! 🤨")

	
	#special elements
	elif usr =="4":
	
		print("\t____________________________________")
		print("\t____________________________________")
		print("\n")
		print("\t######## Special Elements ##########")
		print("\n")
		print("\t____________________________________")
	
		print("\t____________________________________")
		qus=input("\n\n\t{1}.Alkaine Earth Metals\n\n\t{2}.Other Non-metals\n\n\t{3}.Alkaili metals\n\n\t{4}.Halogens\n\n\t{5}.Noble Gases\n\n\n\n\n[NB ....just select e number]\n\n ➡➡  ")
		if qus == "1":
			print("\n\n\nAlkaine Earth metals are :\n\t\t1.Beryllium\n\t\t2.Magnesium\n\t\t3.Calcium\n\t\t4.Strontium\n\t\t5.Barium\n\t\t6.Radium\n")
		elif qus == "2":
			print("\n\n\nOther Non-metals are :\n\t\t1.Hydrogen\n\t\t2.Carbon\n\t\t3.Nitrogen\n\t\t4.Oxygen\n\t\t5.Sulfur\n\t\t6.Phosphorus\n\t\t7.Selenium\n")
		elif qus == "3":
			print("\n\n\nAlkali Metals are :\n\t\t1.Lithum\n\t\t2.Sodium\n\t\t3.Potassium\n\t\t4.Rubidium\n\t\t5.Cesium\n\t\t6.Francium\n")
		elif qus == "4":
			print("\n\n\nHalogens are :\n\t1.Fluorine\n\t2.Chlorine\n\t3.Bromine\n\t4.Iodine\n\t5.Astatine\n\t6.Tennessine\n")
		elif qus == "5":
			print("\n\n\nNoble Gases are :\n\t1.Helium\n\t2.Neon\n\t3.Argon\n\t4.Krypton\n\t5.Xenon\n\t6.Radon\n\t7.Oganesson\n")




	elif usr == "5":
		para = "\t\t\t\t\t\tAbout Periodic Table\n\n\nThe periodic table, or periodic table of elements, is a tabular arrangement of the chemical elements, arranged by atomic number, electron configuration, and recurring chemical properties, whose structure shows periodic trends. The seven rows of the table, called periods, generally have metals on the left and non-metals on the right. The columns, called groups, contain elements with similar chemical behaviours. Six groups have accepted names as well as assigned numbers: for example, group 17 elements are the halogens; and group 18 are the noble gases. Also displayed are four simple rectangular areas or blocks associated with the filling of different atomic orbitals.\n\nThe organization of the periodic table can be used to derive relationships between the various element properties, and also to predict chemical properties and behaviours of undiscovered or newly synthesized elements. Russian chemist Dmitri Mendeleev published the first recognizable periodic table in 1869, developed mainly to illustrate periodic trends of the then-known elements. He also predicted some properties of unidentified elements that were expected to fill gaps within the table. Most of his forecasts proved to be correct. Mendeleev's idea has been slowly expanded and refined with the discovery or synthesis of further new elements and the development of new theoretical models to explain chemical behaviour. The modern periodic table now provides a useful framework for analyzing chemical reactions, and continues to be widely used in chemistry, nuclear physics and other sciences.\n\nThe elements from atomic numbers 1 (hydrogen) through 118 (oganesson) have been discovered or synthesized, completing seven full rows of the periodic table. The first 98 elements all occur naturally, though some are found only in trace amounts and a few were discovered in nature only after having first been synthesized. Elements 99 to 118 have only been synthesized in laboratories or nuclear reactors. The synthesis of elements having higher atomic numbers is currently being pursued: these elements would begin an eighth row, and theoretical work has been done to suggest possible candidates for this extension. Numerous synthetic radionuclides of naturally occurring elements have also been produced in laboratories.\n\n"
		for i in para:
			sleep(.003)
			print(i,end='')
		sleep(3)

	elif usr == "1":
		s=[[" " for i in range(18)] for i in range(7)]
		s[0][0]="	H "
		s[0][-1]="                He"
		r2=["	Li","Be",'B ','C ','N ','O ' ,'F ','Ne']
		r3=['	Na','Mg','Al','Si','P ','S ','Cl','Ar']
		r4=['	K ','Ca','Sc','Ti','V ','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr']
		r5=['	Rb','Sr','Y ','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I ','Xe']
		r6=['	Cs','Ba','* ','Hf','Ta','W ','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn']
		r7=['	Fr','Ra','**','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']
		print("\n\n\t\t   Periodic Table\n\n")
	
		count=0
		for i in range(18):
		    if i<2 or i>11:
		        s[1][i]=r2[count]
		        s[2][i]=r3[count]
		        count+=1
		    else:
		    	s[1][i]="  "
		    	s[2][i]="  "
		    s[3][i]=r4[i]
		    s[4][i]=r5[i]
		    s[5][i]=r6[i]
		    s[6][i]=r7[i]
		    sleep(.05)
		for r  in s:
			for c  in r:
				print(c,end=" ")
			print()
		print("\n\n")
		print("   	      * La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu")
		print("     	      **Ac Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr\n\n\n\n")


	elif usr == "6":
		print("\tExiting Program!\n")
		sleep(.5)
		print("\tThanks Mr.%s. Have a nice day!\n\n\n"%name)
		sleep(.2)
		sys.exit()

	else:
		print("You must enter number from above")	




































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
print('		  ┏━━┓┏━━┓┏┓┏━━┓  ')
sleep(0.1)
print('		  ┗━┓┃┃┏┓┃┃┃┃┏┓┃  ')
sleep(0.01)
print('		  ┏━┛┃┃┃┃┃┃┃┃┗┛┃  ')
sleep(0.1)
print('		  ┃┏━┛┃┃┃┃┃┃┗━┓┃  ')
sleep(0.1)
print('		  ┃┗━┓┃┗┛┃┃┃┃┗┛┃  ')
sleep(0.01)
print('		  ┗━━┛┗━━┛┗┛┗━━┛  ')
print(c_c("  ________________from 4N!k","red","bold=True"))
sleep(1.5)
print("\n\n")

name=input(c_c("             Hi 🙂, What's your name???\n\n  [NB. input your name and press inter to continue]\n\n ➡➡  ","green" ))
sleep(1)



print("\n")
print(c_c(f"	welcome \t\t_{name} \tto my","cyan","bold=True"))
sleep(1)

print("\n\n\n")
print(' 	 ___ __  __   _   ___ _____   ')
sleep(0.1)
print(' 	/ __|  \/  | /_\ | _ \_   _|  ')
sleep(0.1)
print(' 	\__ \ |\/| |/ _ \|   / | |    ')
sleep(0.1)
print(' 	|___/_|  |_/_/ \_\_|_\ |_|    ')
sleep(1)
print("\n")

print('  	   ___          _         ___      ')
sleep(0.1) 
print(' 	  / _ \___ ____(_)__  ___/ (_)___  ')
sleep(0.1)
print('         / ___/ -_) __/ / _ \/ _  / / __/  ')
sleep(.1)
print('	/_/   \__/_/ /_/\___/\_,_/_/\__/   ')
sleep(1)
print("\n\n")
print(' 	 ______     __   __   ')  
sleep(0.1)
print('        /_  __/__ _/ /  / /__  ')
sleep(0.1)
print('  	 / / / _ `/ _ \/ / -_)  ')
sleep(.1)
print(' 	/_/  \_,_/_.__/_/\__/   ')
sleep(.1)
print('\t\t\t')                                      
# For smart flushup font_________

lines = ["       *********************************************","       _______________Version: 1.0__________________","       #############################################","       ____ 🍅 🍅 Release on :Thirty _1st _2018 _____","       #############################################"]
                                                                                                                              
from time import sleep
import sys

for line in lines:         
    for c in line:        
        print(c, end='')    # print a single character, and keep the cursor there.
        sys.stdout.flush()
        sleep(0.01)       
    print('') 
#for details of atom func [ptb]





#function for elec. config.

#Author info
from time import sleep
print("\n\n")
print(c_c(
"       _____________________________________________","yellow"))
print(c_c("          ⚠️ ******* 👉 Author info :****** ⚠️  ️ ","yellow","bold=True"))    
print(c_c("       _____________________________________________","green")) 
print("\n")  
print(c_c("       _____________________________________________","red"))
print(c_c("       🔯 €Name:_Ariful ANIK ","green","bold=True"))
print(c_c("       🔯 €Gmail:_4rifulanik@gmail.com ","red","bold=True"))
print(c_c(                         "       🔯 €Github:_github.com/4riful ","blue","bold=True"))        
print("       🔯 €fb :_ https://www.facebook.com/4rifulAnik")   
print("       🔯 Institution:_ Police Lines School and College.     ")        
print(c_c("       ______________________________________________","red"))
print("\n\n")
print('	_keep patient while program is loading..... \n\n ')
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
print(c_c(" \t🔍🔍🔍What do you want ???? \n\n\n\t▶️ {1}.At a glance Periodic Table.\n\t▶️ {2}.Want to know Details  About an Atom.\n\t▶️ {3}.Want to see Electronic Configaration of an Atom.\n\t▶️ {4}.The Special Names of Elements in Differents Groups.\n\t▶️ {5}.About Periodic table.\n\t▶️ {6}.Exit Program.\n\n\n","puple","bold=True"))
usr2=input(c_c("	    [NB. Input a number from above. ]\n\n\n  ➡➡  ","red","bold=True"))

while usr2 < '6' or usr2 > '0' :
	try:
		speak(usr2)
		sleep(5)
		print(c_c("\n\n\n\t 🔍🔍🔍What do you want again???? \n\n\n\t▶️ {1}.At a glance Periodic Table.\n\t▶️ {2}.Want to know Details  About an Atom.\n\t▶️ {3}.Want to see Electronic Configaration of an Atom.\n\t▶️ {4}.The Special Names of Elements in Differents Groups.\n\t▶️ {5}.About Periodic table.\n\t▶️ {6}.Exit Program.\n\n\n","puple","bold=True"))
		usr2=input(c_c("\n\n\t[NB. Input a number from above. ]\n\n\n  ➡➡  ","red","bold=True"))
	except KeyboardInterrupt:
		sys.exit()




# for eletric configration __facility








































