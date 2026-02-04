import os
import sys
import inquirer

def main():
    """
    Main function to run the QT tutorials.
    """
    # Get the path to the QT_Documentation directory
    qt_doc_path = os.path.join(os.path.dirname(__file__), "QT_Documentation")

    # Get the list of python files in the QT_Documentation directory
    files = sorted([f for f in os.listdir(qt_doc_path) if f.endswith(".py") and f != "main.py" and f != "__init__.py"])

    questions = [
        inquirer.List(
            'file_to_run',
            message="Please choose a file to run",
            choices=files,
        ),
    ]
    answers = inquirer.prompt(questions)

    if answers:
        file_to_run = answers['file_to_run']
        # Run the file
        print(f"Running {file_to_run}...")
        os.system(f"python3 {os.path.join(qt_doc_path, file_to_run)}")
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()
