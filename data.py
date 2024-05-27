# data.py

import pandas as pd
import re

excel_file_path = "vasche.xlsx"

def read_from_excel(file_path=excel_file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    
    except Exception as e:
        print(f"Errore durante la lettura del file XLS: {e}")
        return []  # Return an empty list instead of None

def extract_tank_data(tank_id, file_path=excel_file_path):
    excel_data = read_from_excel(file_path)
    tank_data = excel_data.loc[excel_data['VASCA'] == tank_id]
    return tank_data

def update_tank(tank_id, file_path=excel_file_path, new_current_level=None, wine_type=None, new_items=None, tank_location=None, badd_items=None):
    excel_data = read_from_excel(file_path)
    # Trova l'indice della riga corrispondente al tank_id
    index_to_update = excel_data.index[excel_data['VASCA'] == tank_id].tolist()[0]

    if new_current_level is not None:
        excel_data.at[index_to_update, 'VAL'] = new_current_level
        if new_current_level == 0:
            excel_data.at[index_to_update, 'TYPE'] = "#0"
            excel_data.at[index_to_update, 'ADD'] = "#0"
            excel_data.at[index_to_update, 'BADD'] = "#0"

    if wine_type is not None:
        excel_data.at[index_to_update, 'TYPE'] = wine_type

    if new_items is not None:
        # Riformatta i nuovi items usando divide_in_blocchi
        blocchi_riformattati = divide_in_blocchi(new_items)
        reformatted_new_items = '\n\n'.join(['\n'.join(blocco) for blocco in blocchi_riformattati])
        excel_data.at[index_to_update, 'ADD'] = reformatted_new_items

    if badd_items is not None:
        tank_data = extract_tank_data(tank_id)
        tank_badd_items = tank_data['BADD'].values[0]
        print(badd_items[1])
        new_badd_block = f"#TANK{badd_items[1]}-{badd_items[2]}#{badd_items[0]}#END_TANK#\n"
        if tank_badd_items != "#0":
            excel_data.at[index_to_update, 'BADD'] = tank_badd_items + new_badd_block
        else:
            excel_data.at[index_to_update, 'BADD'] = new_badd_block

    if tank_location is not None:
        excel_data.at[index_to_update, 'LOC'] = tank_location

    # Scrittura
    excel_data.to_excel(file_path, index=False)

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


"""def reformat_ADD_string_to_save(input_string):
    # Replace each newline character with ", "
    reformatted_string = "#0"
    if not input_string.isspace():
        reformatted_string = input_string.replace('\n', ', ')

        # Remove trailing comma if it exists
        while(True):
            if reformatted_string.endswith(', '):
                reformatted_string = reformatted_string[:-2]
            elif reformatted_string.endswith(','):
                reformatted_string = reformatted_string[:-1]
            else:
                break

        # Remove spaces between commas
        segments = [segment.strip() for segment in reformatted_string.split(',')]
        reformatted_string = ', '.join(filter(None, segments))
    
    return reformatted_string"""

"""def reformat_ADD_string_to_print(input_string):
    lines = input_string.strip().split('\n')
    formatted_string = ""

    for line in lines:
        if '/' in line:
            formatted_string += line + '\n\n'
        else:
            formatted_string += line + '\n'

    return formatted_string.strip()"""




"""def reformat_BADD_string_to_print(badd_string):
    tanks = {}
    
    tank_entries = badd_string.split("#END_TANK#")
    for tank_entry in tank_entries:
        if tank_entry.strip():
            tank_num = int(tank_entry.split("#")[0].replace("TANK", ""))
            tanks[tank_num] = tank_entry
    
    sorted_tanks = sorted(tanks.items())
    result = [reformat_ADD_string_to_print(entry[1]) for entry in sorted_tanks]
    
    return result

def parse_input_string(input_string):
    pattern = r'#TANK(\d+)#(.*?)#END_TANK#'
    matches = re.findall(pattern, input_string, re.DOTALL)

    result = []
    for match in matches:
        tank_number = int(match[0])
        items = match[1].strip()
        result.append((tank_number, items))

    return tuple(result)"""


"""def parse_input_string(input_string):
    pattern = r'#TANK(\d+)-(\w+)#(.*?)#END_TANK#'
    matches = re.findall(pattern, input_string, re.DOTALL)

    result = []
    for match in matches:
        tank_id = int(match[0])
        tank_wine_type = match[1]
        tank_items = match[2].strip()
        result.append((tank_id, tank_wine_type, tank_items))
    print(input_string)
    print(result)
    return tuple(result)"""
def parse_input_string(input_string):
    pattern = r'#TANK(\d+)-([^#]+)#(.*?)#END_TANK#'
    matches = re.findall(pattern, input_string, re.DOTALL)

    result = []
    for match in matches:
        tank_name = match[0]
        tank_wine_type = match[1]
        tank_items = match[2].strip()
        result.append((tank_name, tank_wine_type, tank_items))

    return tuple(result)