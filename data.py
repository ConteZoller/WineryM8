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
    excel_data = read_from_excel(excel_file_path)
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
        if badd_items is not None:
            if new_items != "#0":
                new_items = ", ".join([new_items, badd_items[0]])
            else:
                new_items = badd_items[0]
            ################  AGGIUNGERE FORMAZIONE DI BADD
            tank_data = extract_tank_data(tank_id)
            tank_badd_items = tank_data['BADD'].values[0]
            if tank_badd_items != "#0":
                excel_data.at[index_to_update, 'BADD'] = tank_badd_items + f"#TANK{badd_items[1]}#" + badd_items[0] + "#END_TANK#\n"# DA RIVEDERE LA SCRITTURA (doppio taglio cosa fa?)
            else:
                excel_data.at[index_to_update, 'BADD'] = f"#TANK{badd_items[1]}#" + badd_items[0] + "#END_TANK#\n"

        reformatted_new_items = reformat_ADD_string_to_save(new_items)
        excel_data.at[index_to_update, 'ADD'] = reformatted_new_items       # DA RIVEDERE LA SCRITTURA 

    if tank_location is not None:
        excel_data.at[index_to_update, 'LOC'] = tank_location       # DA RIVEDERE

    # Scrittura
    excel_data.to_excel(file_path, index=False)

def reformat_ADD_string_to_save(input_string):
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
    
    return reformatted_string

def reformat_ADD_string_to_print(input_string):
    if input_string == "#0":
        reformatted_string = "Nessuna aggiunta"
    else:
        reformatted_string = str(input_string).replace(', ', '\n')

    return reformatted_string


"""def reformat_BADD_string_to_print(badd_string):
    tank_entries = badd_string.split("#END_TANK#")
    all_text = ""

    tank_entries_sorted = sorted(tank_entries, key=lambda x: int(x.split("#")[1][4:]))

    for entry in tank_entries_sorted:
        if entry.strip():
            items = entry.strip().split("#")
            reformatted_items = items[2].strip()
            all_text += reformatted_items + "\n"

    return all_text"""


def reformat_BADD_string_to_print(badd_string):
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

    return tuple(result)
