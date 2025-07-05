import requests
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Currency Converter - Made By ThurZ")
        self.root.geometry("550x450")
        self.root.resizable(False, False)
        
        # API configuration (use your own API key)
        self.API_KEY = '1b507026159e113a359b51b1'  # Replace with your actual API key
        self.BASE_URL = f'https://v6.exchangerate-api.com/v6/{self.API_KEY}/latest/'
        
        # Popular currencies including MYR and IDR
        self.popular_currencies = [
            'USD', 'EUR', 'GBP', 'JPY', 'AUD', 
            'CAD', 'CHF', 'CNY', 'INR', 'SGD',
            'MYR', 'IDR', 'THB', 'VND', 'KRW',
            'AED', 'SAR', 'PHP', 'BRL', 'MXN'
        ]
        
        # Currency formatting information
        self.currency_formats = {
            'IDR': {'symbol': 'Rp', 'decimal_places': 0},
            'MYR': {'symbol': 'RM', 'decimal_places': 2},
            'JPY': {'symbol': '¥', 'decimal_places': 0},
            'KRW': {'symbol': '₩', 'decimal_places': 0},
            'VND': {'symbol': '₫', 'decimal_places': 0},
            # Default format for others
            'default': {'symbol': '', 'decimal_places': 2}
        }
        
        # GUI Elements
        self.create_widgets()
        self.setup_layout()
        
        # Initialize with default values
        self.update_time_label()
        
    def create_widgets(self):
        # Title
        self.title_label = ttk.Label(
            self.root, 
            text="🌍 Advanced Currency Converter", 
            font=('Helvetica', 16, 'bold')
        )
        self.credit_label = ttk.Label(
            self.root, 
            text="Made By ThurZ", 
            font=('Helvetica', 10, 'italic')
        )
        
        # From Currency
        self.from_label = ttk.Label(self.root, text="From Currency:")
        self.from_currency = ttk.Combobox(
            self.root, 
            values=self.popular_currencies, 
            state="readonly"
        )
        self.from_currency.current(0)
        
        # To Currency
        self.to_label = ttk.Label(self.root, text="To Currency:")
        self.to_currency = ttk.Combobox(
            self.root, 
            values=self.popular_currencies, 
            state="readonly"
        )
        self.to_currency.current(1)
        
        # Amount
        self.amount_label = ttk.Label(self.root, text="Amount:")
        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.insert(0, "1.00")
        
        # Result
        self.result_label = ttk.Label(
            self.root, 
            text="", 
            font=('Helvetica', 14)
        )
        self.rate_label = ttk.Label(
            self.root, 
            text="", 
            font=('Helvetica', 10)
        )
        
        # Time label
        self.time_label = ttk.Label(
            self.root, 
            text="", 
            font=('Helvetica', 8)
        )
        
        # Buttons
        self.convert_button = ttk.Button(
            self.root, 
            text="Convert", 
            command=self.convert_currency
        )
        self.swap_button = ttk.Button(
            self.root, 
            text="Swap Currencies", 
            command=self.swap_currencies
        )
        
    def setup_layout(self):
        # Grid layout
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)
        self.credit_label.grid(row=1, column=0, columnspan=3)
        
        self.from_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.from_currency.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        self.to_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.to_currency.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        self.amount_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.amount_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        
        self.convert_button.grid(row=5, column=1, pady=10, sticky="ew")
        self.swap_button.grid(row=5, column=0, pady=10, sticky="ew")
        
        self.result_label.grid(row=6, column=0, columnspan=3, pady=10)
        self.rate_label.grid(row=7, column=0, columnspan=3)
        self.time_label.grid(row=8, column=0, columnspan=3, pady=10)
        
        # Configure column weights
        self.root.columnconfigure(1, weight=1)
        
    def update_time_label(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=f"Last updated: {now}")
        
    def format_currency(self, amount, currency_code):
        """Format currency according to local conventions"""
        fmt = self.currency_formats.get(currency_code, self.currency_formats['default'])
        symbol = fmt['symbol']
        decimals = fmt['decimal_places']
        
        # Format number with proper decimal places and thousand separators
        formatted_amount = "{:,.{decimals}f}".format(float(amount), decimals=decimals)
        
        # Some currencies put symbol after the amount
        if currency_code in ['EUR', 'GBP']:
            return f"{formatted_amount} {symbol}"
        return f"{symbol} {formatted_amount}"
        
    def get_conversion_rate(self, from_curr, to_curr):
        try:
            response = requests.get(f"{self.BASE_URL}{from_curr}")
            data = response.json()
            
            if data.get('result') == 'success':
                return data['conversion_rates'].get(to_curr)
            else:
                error_msg = data.get('error-type', 'Unknown API error')
                messagebox.showerror("API Error", f"Failed to get rates: {error_msg}")
                return None
                
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Connection Error", f"Failed to connect to API: {str(e)}")
            return None
        except (KeyError, ValueError) as e:
            messagebox.showerror("Data Error", f"Failed to process API response: {str(e)}")
            return None
    
    def convert_currency(self):
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()
        
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            return
            
        rate = self.get_conversion_rate(from_curr, to_curr)
        if rate is not None:
            converted_amount = amount * rate
            
            # Format the currencies properly
            from_formatted = self.format_currency(amount, from_curr)
            to_formatted = self.format_currency(converted_amount, to_curr)
            
            self.result_label.config(
                text=f"{from_formatted} = {to_formatted}"
            )
            self.rate_label.config(
                text=f"Exchange Rate: 1 {from_curr} = {rate:.6f} {to_curr}"
            )
            self.update_time_label()
    
    def swap_currencies(self):
        current_from = self.from_currency.get()
        current_to = self.to_currency.get()
        
        self.from_currency.set(current_to)
        self.to_currency.set(current_from)
        
        # Auto-convert after swap if there's already a result
        if self.result_label['text']:
            self.convert_currency()

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()