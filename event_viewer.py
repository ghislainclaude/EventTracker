import tkinter as tk
import datetime
from tkinter import messagebox

class EventViewer:
    def __init__(self, parent, shared_events):
        self.parent = parent
        self.events = shared_events
        self.window = tk.Toplevel(parent)
        self.window.title("View Events")
        self.window.geometry("400x400")

        # Create a search bar
        self.search_entry = tk.Entry(self.window)
        self.search_entry.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        self.search_button = tk.Button(self.window, text="Search", command=self.search_events)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        # Create a listbox to display events
        self.events_listbox = tk.Listbox(self.window, height=15, width=50)
        self.events_listbox.grid(row=1, column=0, padx=10, pady=10)

        # Populate the listbox with event details
        self.populate_listbox()

        # Create a delete button
        self.delete_button = tk.Button(self.window, text="Delete Event", command=self.delete_event)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

        # Optionally, create a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.window, orient="vertical", command=self.events_listbox.yview)
        self.scrollbar.grid(row=1, column=1, sticky='ns')
        self.events_listbox.configure(yscrollcommand=self.scrollbar.set)

    def populate_listbox(self, filter_text=""):
        # Clear existing listbox entries
        self.events_listbox.delete(0, tk.END)
        
        # Sort events by date and time and populate listbox
        sorted_events = sorted(self.events, key=lambda event: event[2])
        for event in sorted_events:
            title, description, date_time = event
            event_info = f"{title} - {date_time.strftime('%Y-%m-%d %H:%M')}"
            if filter_text.lower() in title.lower() or filter_text.lower() in description.lower():
                self.events_listbox.insert(tk.END, event_info)

    def delete_event(self):
        selected_index = self.events_listbox.curselection()
        if selected_index:
            selected_event = self.events[selected_index[0]]
            self.events.remove(selected_event)
            self.populate_listbox()
        else:
            messagebox.showinfo("Delete Event", "No event selected or event does not exist.")

    def search_events(self):
        search_term = self.search_entry.get()
        self.populate_listbox(search_term)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    shared_events = []  # Initialize an empty list; this will be populated by EventCreator
    app = EventViewer(root, shared_events)
    root.mainloop()
