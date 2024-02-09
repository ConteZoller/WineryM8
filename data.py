# data.py

import pandas as pd

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

def update_tank(tank_id, file_path=excel_file_path, new_current_level=None, wine_type=None, new_items=None, tank_location=None):
    excel_data = read_from_excel(excel_file_path)
    # Trova l'indice della riga corrispondente al tank_id
    index_to_update = excel_data.index[excel_data['VASCA'] == tank_id].tolist()[0]

    if new_current_level is not None:
        excel_data.at[index_to_update, 'VAL'] = new_current_level
        if new_current_level == 0:
            excel_data.at[index_to_update, 'TYPE'] = "#0"
            excel_data.at[index_to_update, 'ADD'] = "#0"
    if wine_type is not None:
        excel_data.at[index_to_update, 'TYPE'] = wine_type
    if new_items is not None:
        reformatted_new_items = reformat_string_to_save(new_items)
        excel_data.at[index_to_update, 'ADD'] = reformatted_new_items       # DA RIVEDERE LA SCRITTURA 
    if tank_location is not None:
        excel_data.at[index_to_update, 'LOC'] = tank_location       # DA RIVEDERE

    # Scrittura
    excel_data.to_excel(file_path, index=False)

def reformat_string_to_save(input_string):
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

def reformat_string_to_print(input_string):
    if input_string == "#0":
        reformatted_string = "Nessuna aggiunta"
    else:
        reformatted_string = str(input_string).replace(', ', '\n')

    return reformatted_string
