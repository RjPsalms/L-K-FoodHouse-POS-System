import json
from tkinter import *
import tkinter as tk
import customtkinter
import datetime

def load_menu(filepath):   
    try:
        with open(filepath) as file:
            menu = json.load(file)
        return menu
    except FileNotFoundError:
        raise FileNotFoundError("Error: menu.json file not found.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Error: Failed to decode menu.json.")
       
class First_POS:
    def __init__(self, main_window_main_window, menu):
        self._main_window = main_window_main_window
        self._menu = menu
        self.create_frames()
        self.create_buttons()

        # Variable to store the currently selected button
        self.current_button = None
        # Dictionary to store the quantity and original price of each item
        self.item_data = {}

    def create_frames(self):
        # Here we created frames, where we can place our buttons and screens
        # This is the Menu frame
        self.frame1 = customtkinter.CTkScrollableFrame(self._main_window)
        self.frame1.pack(side="left", fill="y", expand=False, anchor="nw")
        customtkinter.CTkLabel(self.frame1, text=" MENU ", font=("Helvetica", 30), fg_color="#217b7e" ,corner_radius=15).pack(pady=5, fill="x")

        # This is the Selected Items frame 
        self.frame2 =  customtkinter.CTkScrollableFrame(self._main_window, width=565)
        self.frame2.pack(side="left", fill="y", expand=False, anchor="nw", padx=20, pady=30)
        customtkinter.CTkLabel(self.frame2, text="Please select\n your orders.", font=("", 30)).pack(pady=120)

        # This is the Selected items frame
        self.frame3 =  customtkinter.CTkFrame(self._main_window)
        self.frame3.pack(side="top", fill="both", expand=True)
        customtkinter.CTkLabel(self.frame3, text="Selected Items", font=("Helvetica", 24), text_color="#afeeee", fg_color="#217b7e",corner_radius=15).pack(pady=5, fill="x")

        self.selected_items_textbox =  customtkinter.CTkTextbox(self.frame3, font=("", 20))
        self.selected_items_textbox.pack(side="top", fill="both", expand=True)

        # This is the frame for the Cancel Item and Reset buttons
        self.cancel_reset_frame =  customtkinter.CTkFrame(self.frame3, fg_color="#afeeee", height=20)
        self.cancel_reset_frame.pack(side="bottom", fill="both", expand=False)

        # This is the frame of the Check out button
        self.frame4 =  customtkinter.CTkFrame(self._main_window, height=50, fg_color="transparent")
        self.frame4.pack(side="right", fill="x")

        # This is the subtotal frame, and inside it, a textbox for the subtotal
        self.frame5 =  customtkinter.CTkFrame(self._main_window, height=23, width=80)
        self.frame5.pack(side="bottom", pady=15)
        self.subtotal_textbox =  customtkinter.CTkTextbox(self.frame5, font=("Helvetica", 25), width=250, height=10)
        self.subtotal_textbox.pack(anchor="center", fill="x")
        customtkinter.CTkLabel(self.frame5, text="Subtotal", font=("Helvetica", 15)).pack()

    def create_buttons(self):
        for category in self._menu.keys():
            category_button =  customtkinter.CTkButton(self.frame1, text=category.capitalize(), text_color="#217b7e", 
                                        font=("", 24), border_width=6, corner_radius=30, border_color="#217b7e")
            category_button.pack(side="top", padx=10, pady=10, fill="x")
            category_button.configure(command=lambda cat=category, btn=category_button: self.show_items(cat, btn), fg_color="transparent")
            
        # Remove Item button
        customtkinter.CTkButton(self.cancel_reset_frame, text="Remove Item", width=80, height=30, font=("Helvetica", 18), 
                  command=lambda item=None: self.cancel_selected_item(item), fg_color="lightcoral", hover_color="red").pack(side="left",padx=20, pady=5)
        # Reset button
        customtkinter.CTkButton(self.cancel_reset_frame, text="Reset Selection", width=80, height=30, font=("Helvetica", 18), 
                  command=self.reset_selection, fg_color="lightcoral", hover_color="red").pack(side="right", padx=20, pady=5)
        
        customtkinter.CTkButton(self.frame4, text="Check Out", width=100, height=60, font=("Helvetica", 24), text_color="darkblue",
                  border_color="gold", border_width=4, corner_radius=20, command=self.checkout).pack(padx=15, fill="x")
        
            # Buttons to switch appearance mode
        customtkinter.set_appearance_mode("light")
        self.light_button = customtkinter.CTkSegmentedButton(self._main_window,height=10, values=("light","dark"), 
                                                    font=("",8), command=switch_appearance_mode)
        self.light_button.place(x=20, rely=0.98 , anchor="sw")
        self.light_button.set("light")

    def show_items(self, category, button):
        if category not in self._menu:
            return

        if category != self.current_button:
            for widget in self.frame2.winfo_children():
                widget.destroy()

        row = 0
        col = 0
        for item, price in self._menu[category].items():
            item_button_text = f"{item}\nphp {price:.2f}"
            if item not in self.item_data:
                self.item_data[item] = {'quantity': 0, 'price': price}

            item_button =  customtkinter.CTkButton(self.frame2, text=item_button_text.capitalize(), 
                                    height=30, font=("", 20), fg_color="#c6e2ff", text_color="darkblue", border_color="#27576d", border_width=4, 
                                    command=lambda i=item: self.add_item_to_textbox(i))
            item_button.grid(row=row, column=col, padx=15, pady=10, sticky="nsew")
            
            col += 1
            if col == 3:
                col = 0
                row += 1

        button.configure(fg_color="#c6e2ff")

        if self.current_button and self.current_button != button:
            self.current_button.configure(fg_color="transparent")

        self.current_button = button

    def add_item_to_textbox(self, item):
        # Use setdefault to ensure the key is present and initialize the quantity to 0 if it's not
        item_data_entry = self.item_data.setdefault(item, {'quantity': 0, 'price': 0.0})
        
        # Increment the quantity
        item_data_entry['quantity'] += 1
        
        # Rest of the method remains unchanged
        self.selected_items_textbox.delete(1.0, "end")
        self.subtotal = 0
        add_items(self.selected_items_textbox, self.subtotal_textbox, self.item_data)


    def cancel_selected_item(self, item):
        try:
            selected_text = self.selected_items_textbox.get("sel.first", "sel.last").strip().lower()

            if selected_text in self.item_data:
                self.item_data[selected_text]['quantity'] -= 1
                self.selected_items_textbox.delete(1.0, "end")
                 
            add_items(self.selected_items_textbox, self.subtotal_textbox, self.item_data)

        except tk.TclError:
            return

    def reset_selection(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        for button in self.frame1.winfo_children():
            button.configure(fg_color="transparent")

        self.item_data = {}
        self.selected_items_textbox.delete(1.0, "end")
        self.subtotal_textbox.delete(1.0, "end")
        self.current_button = None

    def checkout(self):
        if self.item_data == {} :
            return
        else:
            self.total_bill_window =  customtkinter.CTkToplevel()
            self.total_bill_window.title("Total Bill")
            self.total_bill_window.geometry("600x400")
            self.total_bill_window.grab_set()

            total_bill_label =  customtkinter.CTkLabel(self.total_bill_window, text="Thank you for your order!\nYour total bill is: ", font=("", 30))
            total_bill_label.pack(pady=20)

            total_bill_value = sum(data['price'] * data['quantity'] for data in self.item_data.values())
            total_bill_textbox =  customtkinter.CTkTextbox(self.total_bill_window, font=("", 40), width=300, height=50)
            total_bill_textbox.insert("end", f"php {total_bill_value:.2f}")
            total_bill_textbox.pack(pady=10)

            cashpay = lambda: pay_cash(total_bill_value, self)
            customtkinter.CTkButton(self.total_bill_window, text="Pay with Cash", width=50, height=30, font=("Helvetica", 18), command=cashpay).pack(padx=20, pady=10)
            customtkinter.CTkButton(self.total_bill_window, text="Pay With Card", width=50, height=30, font=("Helvetica", 18), command=self.clear_screen).pack(padx=20, pady=10)
            customtkinter.CTkButton(self.total_bill_window, text="Cancel", width=50, height=30, font=("Helvetica", 18), command=self.cancel_order).pack(padx=20, pady=20)

    def cancel_order(self):
            self.total_bill_window.destroy()

            for widget in self.frame2.winfo_children():
                widget.destroy()

            for button in self.frame1.winfo_children():
                button.configure(fg_color="transparent")

            self.current_button = None

    def clear_screen(self):
        
        item_data = self.item_data        
        sales_text(item_data)
        
        self.reset_selection()

        if hasattr(self, 'total_bill_window') and self.total_bill_window:
            self.total_bill_window.destroy()
        
        self.thanks = customtkinter.CTkToplevel()
        self.thanks.title("L&K FoodHouse")
        self.thanks.geometry("600x400")
        self.thanks.grab_set()
        
        thanks =  customtkinter.CTkLabel(self.thanks, text="Thank you for your support!\n Come again nect time! ", font=("", 40))
        thanks.pack(pady=130)

def add_items(selected_items_textbox, subtotal_textbox, item_data):
    subtotal = 0
    selected_items_text = ""

    for item, data in item_data.items():
        if data['quantity'] > 0:
            item_text = f"~ {item.capitalize()} ...... php {data['price']:,.2f} x {data['quantity']}\n"
            selected_items_text += item_text
            subtotal += data['price'] * data['quantity']

    selected_items_textbox.delete(1.0, "end")
    selected_items_textbox.insert("end", selected_items_text)

    subtotal_textbox.delete(1.0, "end")
    subtotal_textbox.insert("end", f" php {subtotal:,.2f}")

def sales_text(item_data):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("Sales.txt", "a") as sales_file:
        sales_file.write(f"Date: {current_date}\n")
        
        for item, data in item_data.items():
            if data['quantity'] > 0:
                item_text = f"{item.capitalize()}: ...... php {data['price']:,.2f} x {data['quantity']}\n"
                sales_file.write(item_text)

        total_bill_value = sum(data['price'] * data['quantity'] for data in item_data.values())
        sales_file.write(f"\n       Total Sales: ... php {total_bill_value:,.2f}\n")
        sales_file.write("=" * 35 + "\n \n")          

def cancel_payment():
    change_window = customtkinter.CTkToplevel()
    change_window.title("Cancel Payment")
    change_window.geometry("600x400")
    change_window.grab_set()
    customtkinter.CTkLabel(change_window, text="Cancelling transaction ...", font=("", 30)).pack(pady=120)

def pay_cash(total_bill_value, first_POS):
    cash_received = 0
    payment_trial = 0
    while total_bill_value > cash_received or not cash_received or cash_received <= 0:
        try:
            money = customtkinter.CTkInputDialog(text="Amount received: ", title="Customer Change")
            input_value = money.get_input()
            payment_trial += 1

            if payment_trial == 3:
                cancel_payment()
                break
            if input_value is None:
                return None

            cash_received = float(input_value)
        
        except:
            ValueError("Insufficient Amount")

    if cash_received >= total_bill_value:
        change = cash_received - total_bill_value
        change_window = customtkinter.CTkToplevel()
        change_window.title("Total Bill")
        change_window.geometry("600x400")
        change_window.grab_set()
        customtkinter.CTkLabel(change_window, text=f"Customer change: php {change:,.2f}\n \nThank you for your support!", font=("", 30)).pack(pady=80)

    item_data = first_POS.item_data
    sales_text(item_data)
        
    first_POS.reset_selection()

    if hasattr(first_POS, 'total_bill_window') and first_POS.total_bill_window:
        first_POS.total_bill_window.destroy()
    
def switch_appearance_mode(mode):
    if mode == "light":
        customtkinter.set_appearance_mode("light")
    elif mode == "dark":
        customtkinter.set_appearance_mode("dark")
  
def main():
    filepath = "menu.json"
    menu = load_menu(filepath)
    
    first_POS = First_POS(customtkinter.CTk(), menu)
    first_POS._main_window.geometry("1300x500")
    first_POS._main_window.title("L&K FoodHouse")
    first_POS._main_window.resizable(width=True, height=True)
    
    first_POS._main_window.mainloop()
    
if __name__ == "__main__":
    main()