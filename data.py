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
    if wine_type is not None:
        excel_data.at[index_to_update, 'TYPE'] = wine_type
    if new_items is not None:
        excel_data.at[index_to_update, 'ADD'] = new_items       # DA RIVEDERE LA SCRITTURA 

    

    # Ora puoi salvare il DataFrame aggiornato in un nuovo file Excel
    excel_data.to_excel(file_path, index=False)



def update_tank_level(tank_id, new_current_level, file_path=excel_file_path):
    excel_data = read_from_excel(excel_file_path)
    # Trova l'indice della riga corrispondente al tank_id
    index_to_update = excel_data.index[excel_data['VASCA'] == tank_id].tolist()[0]
    # Aggiorna il valore della colonna 'VAL' con il nuovo livello
    excel_data.at[index_to_update, 'VAL'] = new_current_level

    # Ora puoi salvare il DataFrame aggiornato in un nuovo file Excel
    excel_data.to_excel(file_path, index=False)

def update_tank_items(tank_id, new_items, file_path=excel_file_path):
    excel_data = read_from_excel(excel_file_path)
    # Trova l'indice della riga corrispondente al tank_id
    index_to_update = excel_data.index[excel_data['VASCA'] == tank_id].tolist()[0]
    # Aggiorna il valore della colonna 'VAL' con il nuovo livello
    excel_data.at[index_to_update, 'ADD'] = new_items

    # Ora puoi salvare il DataFrame aggiornato in un nuovo file Excel
    excel_data.to_excel(file_path, index=False)

"""
def get_current_level(tank_id, file_path=excel_file_path):
    excel_data = read_from_excel(file_path)"""
