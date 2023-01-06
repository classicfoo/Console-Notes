# Console-Notes
A simple command-line program for creating, editing, and deleting notes writtenwith the assistance of ChatGPT.

Features
- Add new notes
- List all notes
- Edit existing notes
- Delete notes
- Search for notes by keyword
- Save and load notes from file
- Clear the screen

# Requirements
- Python 3
- The pickle and msvcrt modules (these should be included with Python)
- Usage

To start the program, run python notes.py from the command line.

# Examples 
The program will prompt you to enter an action:

What would you like to do? [add/list/edit/delete/search/quit] 
To add a new note, type add followed by the note text:

What would you like to do? [add/list/edit/delete/search/quit] add This is a new note.
To list all notes, type list:

What would you like to do? [add/list/edit/delete/search/quit] list
1: This is a new note.
To edit a note, type edit followed by the index of the note to edit:

What would you like to do? [add/list/edit/delete/search/quit] edit 1
Current note: This is a new note.
Enter your new note: This is an edited note.
To delete a note, type delete followed by the index of the note to delete:

What would you like to do? [add/list/edit/delete/search/quit] delete 1
To search for a note, type search followed by the search query:

What would you like to do? [add/list/edit/delete/search/quit] search edited
1: This is an edited note.
To quit the program, type quit:

What would you like to do? [add/list/edit/delete/search/quit] quit

# Notes
Notes are saved to a file called notes.pkl in the current directory.
The program will load any existing notes from the file when it starts.
Indices for the list, edit, and delete actions are 1-based (e.g. the first note is index 1).
The search action is case-insensitive.
The clear action can be used to clear the screen.
