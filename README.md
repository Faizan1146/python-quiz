# Python Quiz Application

A command-line quiz application built with Python that allows users to take quizzes, manage questions, and organize questions by category and difficulty.

## Features

* Start a quiz with a selected number of questions.
* Select questions by category and difficulty.
* Randomly select questions using Python's `random` module.
* Calculate and display the final score.
* Add new questions.
* Automatically assign IDs to new questions.
* View all available questions.
* Delete questions by ID.
* Search questions by:

  * Category
  * Difficulty
  * Question
  * Answer
  * ID
* Store questions persistently in a JSON file.
* Automatically create the question database if `question.json` does not exist.
* Handle cases where the requested number of questions is not available.

## Technologies Used

* Python
* JSON
* `os`
* `random`
* `sys`
* Object-Oriented Programming

## Project Structure

```text
python-quiz/
├── quiz.py
├── question.json
└── README.md
```

### `quiz.py`

Contains the main quiz application and the `Quiz` class, including quiz management, question searching, adding, deleting, and quiz execution.

### `question.json`

Stores the quiz questions and their information, including:

* ID
* Question
* Answer
* Category
* Difficulty

## How It Works

When the program starts, it checks whether `question.json` exists.

If the file exists, the questions are loaded from it.

If it does not exist, the program creates an initial set of questions and saves them to `question.json`.

The main menu provides the following options:

```text
===Main Menu===
1. Start Quiz
2. Add Question
3. View Questions
4. Delete Question
5. Search Questions
6. Exit
```

## Quiz System

When starting a quiz, the user selects:

1. Number of questions
2. Category
3. Difficulty

The program filters the available questions according to the selected criteria and randomly selects the requested number of questions.

The user's answers are then compared with the stored answers, and a final score is displayed.

Example:

```text
Final score: 4/5
```

## Question Management

The application provides basic CRUD-style question management.

### Add Questions

Users can enter a new question, answer, category, and difficulty.

The program automatically generates the next available question ID.

### View Questions

Displays the questions currently stored in the quiz database.

### Delete Questions

Users can enter a question ID to remove that question from the database.

### Search Questions

Questions can be searched using:

* Category
* Difficulty
* Question
* Answer
* ID

## Data Persistence

Questions are stored in `question.json` using Python's built-in JSON functionality.

Changes made through the application, such as adding or deleting questions, are saved back to the JSON file.

This allows the question database to persist after the program is closed.

## How to Run

Make sure Python is installed on your computer.

Clone or download the repository and open a terminal in the project directory.

Run:

```bash
python quiz.py
```

The application will open the main menu and allow you to choose an operation.

## Skills Demonstrated

* Python programming
* Object-Oriented Programming
* Classes and methods
* JSON data storage
* File handling
* CRUD operations
* Lists and dictionaries
* List comprehensions
* Exception handling
* User input handling
* Random data selection
* Data filtering
* Searching
* Basic command-line application development

## Future Improvements

Possible improvements include:

* Add stronger input validation.
* Add multiple-choice questions.
* Improve the command-line interface.
* Add partial or flexible answer matching.
* Add quiz history and high scores.
* Add more categories and difficulty levels.
* Separate the application into multiple Python modules.
* Add automated tests.
* Create a graphical user interface.

## Author

Created as a Python programming portfolio project.
