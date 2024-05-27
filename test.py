import re

def divide_in_blocchi(stringa):
    blocchi = []
    blocco_corrente = []
    
    # Dividi la stringa in righe
    righe = stringa.strip().split('\n')
    
    # Inizializza le variabili per la data e il titolo
    data = None
    titolo = None
    
    for riga in righe:
        # Cerca la data nel formato DD/MM/YYYY
        match_data = re.search(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', riga)
        
        if match_data:
            # Se trova una data, inizia un nuovo blocco
            if blocco_corrente:
                blocchi.append(blocco_corrente)
                blocco_corrente = []
            
            # Estrae la data dalla riga
            data = match_data.group(0)
            
            # Estrae il titolo se presente
            titolo = riga.replace(data, '').strip()
            
            # Aggiunge la data e il titolo al blocco corrente
            if titolo:
                blocco_corrente.append(f"{data} {titolo}")
            else:
                blocco_corrente.append(data)
        elif riga.strip():  # Se la riga non è vuota
            # Aggiunge il testo al blocco corrente solo se non è vuota
            blocco_corrente.append(riga)
    
    # Aggiunge l'ultimo blocco corrente alla lista di blocchi
    if blocco_corrente:
        blocchi.append(blocco_corrente)
    
    return blocchi

# Esempio di utilizzo
stringa = """11/23/34 Vendemmia
proviamo

ad inserire
valori

12/3/2344


agg 4g nubi 
agg pepe 9g

13/2/23

Paperere 4 kg"""

blocchi_riformattati = divide_in_blocchi(stringa)

print(blocchi_riformattati)



