import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime
import pytz

class TimeDisplay:
    def __init__(self, root):
        self.root = root
        self.root.title("Luxembourg Time & Unix Epoch Display")
        self.root.geometry("600x300")
        self.root.configure(bg='#f0f0f0')
        
        # Create Luxembourg timezone
        self.luxembourg_tz = pytz.timezone('Europe/Luxembourg')
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="30")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for centering
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title label
        title_label = ttk.Label(main_frame, text="Time Display", 
                               font=('Arial', 20, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Unix Epoch Time section
        ttk.Label(main_frame, text="Unix Epoch Time:", 
                 font=('Arial', 12, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=10)
        
        self.epoch_var = tk.StringVar()
        self.epoch_label = ttk.Label(main_frame, textvariable=self.epoch_var, 
                                    font=('Courier', 16), foreground='#0066cc')
        self.epoch_label.grid(row=1, column=1, sticky=tk.W, padx=(20, 0), pady=10)
        
        # Luxembourg Time section
        ttk.Label(main_frame, text="Luxembourg Time:", 
                 font=('Arial', 12, 'bold')).grid(row=2, column=0, sticky=tk.W, pady=10)
        
        self.luxembourg_var = tk.StringVar()
        self.luxembourg_label = ttk.Label(main_frame, textvariable=self.luxembourg_var, 
                                         font=('Courier', 16), foreground='#cc6600')
        self.luxembourg_label.grid(row=2, column=1, sticky=tk.W, padx=(20, 0), pady=10)
        
        # Date section
        ttk.Label(main_frame, text="Date:", 
                 font=('Arial', 12, 'bold')).grid(row=3, column=0, sticky=tk.W, pady=10)
        
        self.date_var = tk.StringVar()
        self.date_label = ttk.Label(main_frame, textvariable=self.date_var, 
                                   font=('Arial', 14), foreground='#006600')
        self.date_label.grid(row=3, column=1, sticky=tk.W, padx=(20, 0), pady=10)
        
        # Start the clock update
        self.update_time()
    
    def update_time(self):
        # Get current time
        current_epoch = int(time.time())
        current_time = datetime.now(self.luxembourg_tz)
        
        # Update the display variables
        self.epoch_var.set(f"{current_epoch}")
        self.luxembourg_var.set(current_time.strftime("%H:%M:%S %Z"))
        self.date_var.set(current_time.strftime("%A, %B %d, %Y"))
        
        # Schedule next update in 1000ms (1 second)
        self.root.after(1000, self.update_time)

def main():
    root = tk.Tk()
    app = TimeDisplay(root)
    root.mainloop()

if __name__ == "__main__":
    main()