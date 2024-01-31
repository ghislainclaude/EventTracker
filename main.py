import tkinter as tk
# import the other class into main
from event_creator import EventCreator
from event_viewer import EventViewer

events = []

def create_event():
    EventCreator(window, events)

def view_events():
    EventViewer(window, events)

# def delete_event():
#     # Placeholder for delete event logic
#     print("Deleting event...")

window = tk.Tk()
window.title("EventTracker")
window.geometry("400x300")

# Create a label for instructions
instruction_label = tk.Label(window, text="Select an option to manage events:", height=2, font=("Helvetica", 14))
instruction_label.grid(row=0, column=0, sticky="WE", padx=20, pady=10)

# Create buttons for each menu option
create_button = tk.Button(window, text="1. Create Event", command=create_event, font=("Helvetica", 12))
create_button.grid(row=1, column=0, sticky="WE", padx=20, pady=5)

view_button = tk.Button(window, text="2. View Events", command=view_events, font=("Helvetica", 12))
view_button.grid(row=2, column=0, sticky="WE", padx=20, pady=5)

# delete_button = tk.Button(window, text="3. Delete Event", command=delete_event, font=("Helvetica", 12))
# delete_button.grid(row=3, column=0, sticky="WE", padx=20, pady=5)

# Run the application
if __name__ == "__main__":
    window.mainloop()
