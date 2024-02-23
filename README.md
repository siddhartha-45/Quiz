# Quiz
This Python script implements a quiz game that quizzes users on two topics: "World Capitals" and "Animal Facts.
 Here's a breakdown of the script:

load_quiz_questions(): This function returns a dictionary containing the quiz questions for each topic. Each topic has a set of questions, and each question includes the question itself, the correct answer, feedback for correct answers, and a list of options for multiple-choice questions.

ask_question(question, answer, show_answer=False): This function asks a question and checks the user's answer. If show_answer is True, it also prints the correct answer.

ask_multiple_choice_question(q, options): This function asks a multiple-choice question by displaying the question and answer options. It prompts the user to select an answer and evaluates if the selected answer is correct.

ask_fill_in_the_blank_question(q, answer): This function asks a fill-in-the-blank question. It displays the question and prompts the user to enter their answer. If the user wants to see the answer, it prints the correct answer after the user's input.

play_quiz(): This function runs the quiz game. It first welcomes the user and explains the rules. Then, it allows the user to select a topic and a question type (multiple-choice or fill-in-the-blank). It shuffles the questions, asks each question, and keeps track of the user's score. After completing the quiz, it displays the final score and the correct answers for each question.

__main__ block: It loads the quiz questions, initializes the selected topic to None, and calls the play_quiz() function to start the quiz game.

Overall, this script provides a simple interactive quiz game that tests the user's knowledge on the specified topics.





