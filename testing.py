def decrement_tank(progress_bars, tank_id, tank_frame_label, tank_label_widget, wine_type_label_widget):
    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]

    if tank_current_level:
        tank_level_user_input = tkinter.simpledialog.askinteger(f"Consuma il Contenuto della Vasca {tank_id}", f"Inserisci un valore (massimo {tank_current_level}):")

        if tank_level_user_input is not None and 0 <= tank_level_user_input <= tank_current_level:
            decrement_per_progress = (tank_level_user_input / tank_current_level) * 2

            for progress in progress_bars:
                ################
                target_value = max(progress["value"] - tank_level_user_input, 0)
                decrement_progress(progress, target_value, progress["value"], decrement_amount=decrement_per_progress)

            update_tank(tank_id, new_current_level=tank_current_level - tank_level_user_input)

            tank_data = extract_tank_data(tank_id)
            tank_current_level = tank_data['VAL'].values[0]
            tank_fill_percentage = calculate_fill_percentage(tank_current_level, total_capacity)
            tank_frame_label["text"] = f"Livello vasca: {tank_fill_percentage}%"

            tank_label_widget["text"] = "{} / {} HL".format(tank_data['VAL'].values[0], tank_data['CAP'].values[0])
            wine_type_label_widget["text"] = tank_data['TYPE'].values[0]

            tank_frame_label.update_idletasks()
            wine_type_label_widget.update_idletasks()
            tank_label_widget.update_idletasks()


def increment_tank(progress_bars, total_capacity, tank_id, tank_frame_label, tank_label_widget, wine_type_label_widget):
    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    max_addition = total_capacity - tank_current_level
    if max_addition > 0:
        if tank_current_level:
            tank_level_user_input = tkinter.simpledialog.askinteger(f"Riempi la Vasca {tank_id}", f"Inserisci un valore (massimo {max_addition}):")
        else:
            wine_type_user_input = tkinter.simpledialog.askstring(f"Prodotto Vasca {tank_id}", f"Inserisci la tipologia di prodotto:")
            tank_level_user_input = tkinter.simpledialog.askinteger(f"Riempi la Vasca {tank_id}", f"Inserisci un valore (massimo {max_addition}):")

        if tank_level_user_input is not None and 0 <= tank_level_user_input <= max_addition:
            increment_per_progress = (tank_level_user_input / (total_capacity - tank_current_level)) * 2

            for progress in progress_bars:
                target_value = min(progress["value"] + tank_level_user_input, progress["maximum"])
                increment_progress(progress, target_value, progress["value"], increment_amount=increment_per_progress)

            update_tank(tank_id, new_current_level=tank_current_level + tank_level_user_input, wine_type=wine_type_user_input)

            tank_data = extract_tank_data(tank_id)
            tank_current_level = tank_data['VAL'].values[0]
            tank_fill_percentage = calculate_fill_percentage(tank_current_level, total_capacity)
            tank_frame_label["text"] = f"Livello vasca: {tank_fill_percentage}%"

            tank_label_widget["text"] = "{} / {} HL".format(tank_data['VAL'].values[0], tank_data['CAP'].values[0])
            wine_type_label_widget["text"] = tank_data['TYPE'].values[0]

            tank_frame_label.update_idletasks()
            wine_type_label_widget.update_idletasks()
            tank_label_widget.update_idletasks()