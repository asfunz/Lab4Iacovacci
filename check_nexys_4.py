import serial
import time
sleep_time = 0.400 

ser = serial.Serial(port = "/dev/ttyUSB1", baudrate = 115200, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS)



if ser.isOpen():
	print("Porta aperta correttamente")
else:
	ser.close()
	ser.open()
	print("La porta è stata chiusa e riaperta")

#Creo il file
fname = "acquisizione_dati_grezzi_400ms"
outf = open(fname, "w")

#Blocco per aggiungere t0 di inizio delle misure

t0 = time.time()
gmp = time.gmtime(t0)
ora = gmp.tm_hour + 1
minuti = gmp.tm_min
secondi = gmp.tm_sec
t_somma = str(int(ora)*3600 + int(minuti)*60 + int(secondi))
mil1 = repr(t0).split(".")[1][0:1]
stringhe = [t_somma, mil1]
tempo = ".".join(stringhe)


contatore = 0
print('misura:', 'tempo di acquisizione:', 'numero di bytes in ingresso:', 'stringa bytes:')

#Blocco per dare un titolo alle colonne dei dati
dati_in_colonna = ['misura', 'tempo di acquisizione', 'numero di bytes in ingresso', 'stringa bytes']
with open("acquisizione_dati_grezzi_400ms", "w") as file:
	for i in dati_in_colonna:
		file.write(i+"\t")
	file.write("\n")

while True:

	# Numero di byte nella porta
	n = ser.inWaiting()  
	stringa_bytes = ""
	
	# Blocco per misurare il passare del tempo durante la misura ed ottenere i valore del tempo di acquisizione
	t_1 = time.time()
	gmp = time.gmtime(t_1)
	ora = gmp.tm_hour + 1
	minuti = gmp.tm_min
	secondi = gmp.tm_sec
	t_somma = str(int(ora)*3600 + int(minuti)*60 + int(secondi))
	mil1 = repr(t_1).split(".")[1][0:1]
	stringhe = [t_somma, mil1]
	tempo = ".".join(stringhe)

	t = float(str(t_1)[0:12])
	time_acq = float(t)-float(t0)	
	time_acq = float("{:.3f}".format(time_acq))


	# Uscire dal loop se superato il tempo di acquisizione
	if time_acq > 10: 
		print("superato il tempo di acquisizione massimo stabilito")
		break

	#If loop per registrare i dati 
	elif (n > 0) and time_acq > 0:
		for j in range(n):
			stringa_bytes += ser.read().hex()
		time.sleep(sleep_time)
		print(contatore, time_acq, n, stringa_bytes)
	  	
		#Scrivo i dati grezzi sul file
		dati_in_colonna = [str(contatore), str(time_acq), str(n), stringa_bytes]
		with open("acquisizione_dati_grezzi_400ms", "a") as file:
			for i in dati_in_colonna:
				file.write(i+"\t")
			file.write("\n")
		
		contatore += 1
		  
		#outf.write(contatore, time_acq, n, stringa_bytes)

