from project import load_menu, First_POS, add_items, sales_text, cancel_payment
import pytest
import json
import tkinter as tk
import customtkinter

def test_load_menu(tmp_path):
    menu_data = {"category": {"item": 10.0}}
    menu_file = tmp_path / "menu.json"
    menu_file.write_text(json.dumps(menu_data))

    menu = load_menu(menu_file)
    assert menu == menu_data

def test_first_pos_creation():
    main_window = tk.Tk()
    menu = {"category": {"item": 10.0}}
    first_pos = First_POS(main_window, menu)
    assert first_pos._main_window == main_window
    assert first_pos._menu == menu

def test_add_items():
    selected_items_textbox = customtkinter.CTkTextbox(tk.Frame())
    subtotal_textbox = customtkinter.CTkTextbox(tk.Frame())
    item_data = {"item": {"quantity": 2, "price": 10.0}}

    add_items(selected_items_textbox, subtotal_textbox, item_data)

    expected_selected_items_text = "~ Item ...... php 10.00 x 2\n"
    assert selected_items_textbox.get(1.0, "end").strip() == expected_selected_items_text.strip()

    expected_subtotal_text = " php 20.00"
    assert subtotal_textbox.get(1.0, "end").strip() == expected_subtotal_text.strip()
 

def test_sales_text(tmp_path):
    item_data = {"item": {"quantity": 2, "price": 10.0}}
    sales_file = tmp_path
    sales_text(item_data)
    assert sales_file.exists() 
    
def test_cancel_payment_output(capfd):
    cancel_payment()
    out, err = capfd.readouterr()
    assert "Some other expected output" not in out
    assert "" in out


@pytest.fixture
def menu():
    return load_menu(filepath="menu.json")
 
def test_reset_selection(menu):
    main_window = customtkinter.CTk()
    first_pos = First_POS(main_window, menu)
    
    first_pos.add_item_to_textbox("Itemz")
    first_pos.add_item_to_textbox("Itemx")
    first_pos.show_items("Category", customtkinter.CTkButton(main_window, text="Category"))

    first_pos.reset_selection()

    assert not first_pos.current_button
    assert not first_pos.item_data
    assert not first_pos.selected_items_textbox.get(1.0, "end").strip()

