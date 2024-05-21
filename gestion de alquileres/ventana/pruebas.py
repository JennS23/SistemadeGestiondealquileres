import tkinter as tk
from modelo.gestor_de_usuarios import User, UserManager  # Assuming this import is necessary

def create_centered_entry(parent, width, show):
    """
    Creates an Entry widget with centered placement and optional password masking.

    Args:
        parent (tk.Widget): The parent widget for the Entry.
        width (int): The width of the Entry.
        show (str, optional): A character (or empty string) to display instead
            of the characters typed into the Entry. Defaults to "".

    Returns:
        tk.Entry: The created Entry widget.
    """
    entry = tk.Entry(parent, width=width, show=show)
    entry.pack(pady=10, anchor=tk.CENTER)  # Add vertical padding and center in parent
    return entry

def handle_button_click():
    """
    Function called when the button is clicked.

    Retrieves the text from the Entry widgets, creates new User objects with
    validation (assuming validation logic is defined in UserManager), and
    stores them using the UserManager instance. Displays a success message.
    """
    username = entry1.get()
    password = entry2.get()

    try:
        # Assuming UserManager has methods for validation and storage
        user1 = UserManager.create_user(username)
        user2 = UserManager.create_user(password)  # Password likely needs validation

        # Store users (replace `store_user` with actual implementation)
        UserManager.store_user(user1)
        UserManager.store_user(user2)

        success_label = tk.Label(root, text="Usuarios almacenados correctamente")
        success_label.grid(row=2, column=0, pady=10, columnspan=2)  # Center label below entries
    except ValueError as e:
        error_label = tk.Label(root, text=f"Error: {str(e)}", fg="red")
        error_label.grid(row=2, column=0, pady=10, columnspan=2)  # Display error message

# Create the main window
root = tk.Tk()
root.title("Gestor de Usuarios")
root.geometry("400x300")  # Adjusted to accommodate potential error messages

# Create a frame to center the Entry widgets (optional)
# frame = tk.Frame(root)
# frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create the Entry widgets (assuming centered placement is preferred)
entry1 = create_centered_entry(root, width=30, show="")
entry2 = create_centered_entry(root, width=30, show="*")  # Password masking

# Create the button with descriptive text
button = tk.Button(root, text="Crear Usuarios", padx=10, pady=10, command=handle_button_click)
button.grid(row=1, column=0, pady=10, columnspan=2)  # Center button below entries

root.mainloop()
