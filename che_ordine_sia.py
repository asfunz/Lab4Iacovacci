#!/usr/bin/env python
# coding: utf-8

# # Importo i dati dal file e concateno la stringa per poterla poi riscrivere

# In[47]:


with open('acquisizione_dati_grezzi_400ms.txt', 'r') as file:
    misura = []
    tempo_di_acquisizione = []
    numero_di_bytes_in_ingresso = []
    stringa_bytes = []
    
     # Flag per saltare la prima riga
    prima_riga = True

    # Legge il file riga per riga
    for line in file:
        # Salta la prima riga
        if prima_riga:
            prima_riga = False
            continue
        
        columns = line.strip().split('\t')

        misura.append(columns[0])
        tempo_di_acquisizione.append(columns[1])
        numero_di_bytes_in_ingresso.append(columns[2])
        stringa_bytes.append(columns[3])

stringa_bytes_concatenata = ''.join(stringa_bytes)


# # Ricerco la posizione della parola di controllo all'interno della mia stringa concatena

# In[48]:


posizioni_aaaa = []
posizione = stringa_bytes_concatenata.find("aaaa")

while posizione != -1:
    posizioni_aaaa.append(posizione)
    posizione = stringa_bytes_concatenata.find("aaaa", posizione + 1)


# # Estrazione temperatura ed umidità e conversione in decimale

# In[53]:


temperatura_convertita = []
umidita_relativa_convertita = []

for i in posizioni_aaaa:
    umidita = str(int(''.join(stringa_bytes_concatenata[i-8:i-4]), 16))
    temperatura = str(int(''.join(stringa_bytes_concatenata[i-4:i]),16))
    umidita_relativa_convertita.append(umidita)
    temperatura_convertita.append(temperatura)


# # Creazione di un file con i dati convertiti

# In[59]:


fname = "Dati_400ms_ordinati"
with open(fname, "w") as file:
    dati_in_colonna = ['misura', 'tempo di acquisizione', 'umidità relativa', 'temperatura']
    file.write("\t".join(dati_in_colonna) + "\n")
    

with open(fname, "a") as file:
    for i in range(len(misura)):
        riga = [str(misura[i]), str(tempo_di_acquisizione[i]), str(umidita_relativa_convertita[i]), str(temperatura_convertita[i])]
        file.write("\t".join(riga) + "\n")


# In[ ]:




