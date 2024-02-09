def fill_tank(progress_bars, total_capacity, tank_id, tank_frame_label, tank_label_widget, wine_type_label_widget):
    def increment_progress(progress, target_value, current_value, increment_amount=1):
        new_value = min(current_value + increment_amount, target_value)
        progress["value"] = new_value
        if current_value < new_value:
            progress.after(10, increment_progress, progress, target_value, new_value, increment_amount)

    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    max_addition = total_capacity - tank_current_level
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

def full_fill_tank(progress_bars, total_capacity, tank_id, tank_frame_label, tank_label_widget, wine_type_label_widget):
    def increment_progress(progress, target_value, current_value, increment_amount=1):
        new_value = min(current_value + increment_amount, target_value)
        progress["value"] = new_value
        if current_value < new_value:
            progress.after(10, increment_progress, progress, target_value, new_value, increment_amount)

    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    max_addition = total_capacity - tank_current_level

    if not tank_current_level:
        wine_type_user_input = tkinter.simpledialog.askstring(f"Prodotto Vasca {tank_id}", f"Inserisci la tipologia di prodotto:")

    increment_per_progress = (max_addition / (total_capacity - tank_current_level)) * 2

    for progress in progress_bars:
        target_value = min(progress["value"] + max_addition, progress["maximum"])
        increment_progress(progress, target_value, progress["value"], increment_amount=increment_per_progress)

    update_tank(tank_id, new_current_level=tank_current_level + max_addition, wine_type=wine_type_user_input)

    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    tank_fill_percentage = calculate_fill_percentage(tank_current_level, total_capacity)
    tank_frame_label["text"] = f"Livello vasca: {tank_fill_percentage}%"

    tank_label_widget["text"] = "{} / {} HL".format(tank_data['VAL'].values[0], tank_data['CAP'].values[0])
    wine_type_label_widget["text"] = tank_data['TYPE'].values[0]

    tank_frame_label.update_idletasks()
    wine_type_label_widget.update_idletasks()
    tank_label_widget.update_idletasks()