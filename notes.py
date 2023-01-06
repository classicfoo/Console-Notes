import os
import pickle
import msvcrt

notes = []

def save_notes():
    with open("notes.pkl", "wb") as f:
        pickle.dump(notes, f)

def load_notes():
    global notes
    if os.path.exists("notes.pkl"):
        with open("notes.pkl", "rb") as f:
            notes = pickle.load(f)

def list_notes():
    for i, note in enumerate(notes):
        print(f"{i+1}: {note}")

load_notes()

while True:
    print("-" * 80)
    action = input("What would you like to do? [add/list/edit/delete/search/clear/quit] ")

    if action.startswith("add"):
        try:
            _, *note = action.split()
            note = " ".join(note)
            notes.append(note)
            save_notes()
        except ValueError:
            print("Please enter a note to add.")
    elif action == "list":
        list_notes()
    elif action.startswith("edit"):
        try:
            _, index = action.split()
            index = int(index)
            if index > 0 and index <= len(notes):
                print(f"Current note: {notes[index-1]}")
                note = input("Enter your new note: ")
                notes[index-1] = note
                save_notes()
            else:
                print("Invalid index. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    elif action.startswith("delete"):
        try:
            _, index = action.split()
            index = int(index)
            if index > 0 and index <= len(notes):
                notes.pop(index-1)
                save_notes()
            else:
                print("Invalid index. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    elif action.startswith("search"):
        try:
            _, *query = action.split()
            query = " ".join(query)
            found = False
            for i, note in enumerate(notes):
                if query in note:
                    print(f"{i+1}: {note}")
                    found = True
            if not found:
                print("No matching notes found.")
        except ValueError:
            print("Please enter a query string to search for.")
    elif action.startswith("clear"):
        os.system("cls")
    elif action == "quit":
        save_notes()
        break
    else:
        print("Invalid action. Please try again.")
    
