import tkinter as tk
from tkcalendar import DateEntry
import datetime

class EventCreator:
    def __init__(self, parent, shared_events):
        self.parent = parent
        self.events = shared_events  # Use the shared events list
        self.window = tk.Toplevel(parent)
        self.window.title("Create Event")
        self.window.geometry("400x300")

        # Title input
        tk.Label(self.window, text="Title:").grid(row=0, column=0, padx=10, pady=5)
        self.title_entry = tk.Entry(self.window)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        # Description input
        tk.Label(self.window, text="Description:").grid(row=1, column=0, padx=10, pady=5)
        self.desc_entry = tk.Entry(self.window)
        self.desc_entry.grid(row=1, column=1, padx=10, pady=5)

        # Date input
        tk.Label(self.window, text="Date:").grid(row=2, column=0, padx=10, pady=5)
        self.date_entry = DateEntry(self.window, date_pattern='y-mm-dd')
        self.date_entry.grid(row=2, column=1, padx=10, pady=5)

        # Time input
        tk.Label(self.window, text="Time:").grid(row=3, column=0, padx=10, pady=5)
        self.hour_var = tk.StringVar(self.window)
        self.minute_var = tk.StringVar(self.window)
        hours = [f'{h:02d}' for h in range(24)]
        minutes = [f'{m:02d}' for m in range(60)]
        self.hour_menu = tk.OptionMenu(self.window, self.hour_var, *hours)
        self.minute_menu = tk.OptionMenu(self.window, self.minute_var, *minutes)
        self.hour_menu.grid(row=3, column=1, padx=10, pady=5, sticky='w')
        self.minute_menu.grid(row=3, column=1, padx=10, pady=5, sticky='e')

        # Submit button
        submit_button = tk.Button(self.window, text="Create Event", command=self.submit_event)
        submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def submit_event(self):
        try:
            # Collect event data
            title = self.title_entry.get()
            description = self.desc_entry.get()
            date = self.date_entry.get_date()
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            date_time = datetime.datetime.combine(date, datetime.time(hour, minute))

            # Store event data in the shared 2D array
            self.events.append([title, description, date_time])

            # Clear the entry fields after submission
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.hour_var.set('')
            self.minute_var.set('')

            print("Current events:", self.events)

        except ValueError as e:
            print("Error: Invalid date or time.", e)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    shared_events = []  # This list will be shared across different parts of the application
    app = EventCreator(root, shared_events)
    root.mainloop()
