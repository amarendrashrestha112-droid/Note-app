FILE_NAME = "notes.txt"

def load_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        return [note.strip() for note in notes]

    except FileNotFoundError:
        return []

def save_notes(notes):
    try:
        with open(FILE_NAME, "w") as file:
            for note in notes:
                file.write(note + "\n")
    except Exception as e:
        print("Error saving notes:", e)


def add_note(notes):
    note = input("Enter your note: ")

    if note.strip() == "":
        print("Note cannot be empty.")
    else:
        notes.append(note)
        save_notes(notes)
        print("Note added successfully!")

def view_notes(notes):
    if len(notes) == 0:
        print("No notes found.")
        return

    print("\n===== YOUR NOTES =====")

    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")


def delete_note(notes):
    view_notes(notes)

    if len(notes) == 0:
        return

    try:
        number = int(input("Enter note number to delete: "))

        if 1 <= number <= len(notes):
            deleted = notes.pop(number - 1)
            print("Deleted:", deleted)
        else:
            print("Invalid note number.")

    except ValueError:
        print("Please enter a number.")


def main():
    notes = load_notes()
    while True:
        print("\n===== NOTE APP =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            view_notes(notes)

        elif choice == "3":
            delete_note(notes)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


main()
