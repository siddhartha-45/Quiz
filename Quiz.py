import random

# Define a dictionary with topics and questions
def load_quiz_questions():
    return {
        "World Capitals": {
            "questions": {
                "What is the capital of France?": {
                    "answer": "Paris",
                    "feedback": "Correct! Paris is a beautiful city.",
                    "options": ["London", "Paris", "Berlin", "Madrid"]
                },
                "What is the capital of Australia?": {
                    "answer": "Canberra",
                    "feedback": "That's correct! Canberra became the capital in 1927.",
                    "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"]
                },
                "What is the capital of Canada?": {
                    "answer": "Ottawa",
                    "feedback": "Well done! Ottawa is located in Ontario.",
                    "options": ["Toronto", "Vancouver", "Montreal", "Ottawa"]
                },
                "What is the capital of Brazil?": {
                    "answer": "Brasília",
                    "feedback": "Nice job! Brasília was founded in 1960.",
                    "options": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"]
                }
            }
        },
        "Animal Facts": {
            "questions": {
                "What is the largest animal on land?": {
                    "answer": "Elephant",
                    "feedback": "Correct! Elephants can weigh up to 14,000 pounds.",
                    "options": ["Giraffe", "Hippo", "Elephant", "Rhino"]
                },
                "What is the fastest land animal?": {
                    "answer": "Cheetah",
                    "feedback": "That's correct! Cheetahs can reach speeds of up to 75 mph.",
                    "options": ["Lion", "Leopard", "Cheetah", "Hyena"]
                },
                "What is the largest animal in the ocean?": {
                    "answer": "Blue Whale",
                    "feedback": "Well done! Blue whales can grow up to 110 feet long.",
                    "options": ["Whale Shark", "Blue Whale", "Great White Shark", "Orca"]
                },
                "What is the fastest animal in the ocean?": {
                    "answer": "Sailfish",
                    "feedback": "Nice job! Sailfish can reach speeds of up to 68 mph.",
                    "options": ["Marlin", "Tuna", "Sailfish", "Shark"]
                }
            }
        }
    }

# Function to ask a question and check the answer
def ask_question(question, answer, show_answer=False):
    if show_answer:
        print("The correct answer is: " + answer + "\n")
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print(topics[selected_topic]["questions"][question]["feedback"] + "\n")
        return True
    else:
        print("Sorry, that's incorrect.\n")
        return False

# Function to evaluate the user's answer for multiple-choice questions
def ask_multiple_choice_question(q, options):
    # Display the question and answer choices
    print("Question: " + q)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    # Prompt the user to select an answer
    user_answer = int(input("Enter the number corresponding to your answer: "))

    # Evaluate the user's answer
    if options[user_answer - 1] == topics[selected_topic]["questions"][q]["answer"]:
        print(topics[selected_topic]["questions"][q]["feedback"])
        return True
    else:
        print("Incorrect! The correct answer is:", topics[selected_topic]["questions"][q]["answer"])
        return False

# Function to evaluate the user's answer for fill-in-the-blank questions
def ask_fill_in_the_blank_question(q, answer):
    # Display the question
    print("Question: " + q)
    show_answer = input("Would you like to see the answer? (yes/no): ").lower()
    return ask_question(q, answer, show_answer == "yes")

# Function to run the quiz game
def play_quiz():
    global score, topics, selected_topic

    while True:
        # Welcome message and rules
        print("Welcome to the Quiz Game!")
        print("Select a topic and question type, then answer the questions to the best of your knowledge.")
        print("You will receive feedback after each question, and your final score will be displayed at the end.\n")

        # Select a topic
        print("Topics:")
        for i, topic in enumerate(topics.keys()):
            print(f"{i + 1}. {topic}")
        selected_topic_index = int(input("Enter the number of the topic you want to quiz on: ")) - 1
        if selected_topic_index in [0, 1]:
            selected_topic = list(topics.keys())[selected_topic_index]

        # Select a question type
        question_type = input("Enter the number of the question type you want to quiz on (1 for Multiple Choice, 2 for Fill in the Blank): ")

        score = 0

        questions = list(topics[selected_topic]["questions"].keys())
        random.shuffle(questions)  # Shuffle the questions

        user_answers = {}  # Dictionary to store user's answers for each question

        for q in questions:
            if question_type == "1":
                options = topics[selected_topic]["questions"][q]["options"]
                user_answers[q] = ask_multiple_choice_question(q, options)
                if user_answers[q]:
                    score += 1
            elif question_type == "2":
                answer = topics[selected_topic]["questions"][q]["answer"]
                user_answers[q] = ask_fill_in_the_blank_question(q, answer)
                if user_answers[q]:
                    score += 1
            else:
                print("Invalid input! Please select either 1 or 2 for question type.")

        # Display final score
        print("\nQuiz completed! Your final score is:", score, "/", len(questions))

        # Show correct answers
        print("\nCorrect Answers:")
        for q, is_correct in user_answers.items():
            print(f"{q}: {'Correct' if is_correct else 'Incorrect'} - {topics[selected_topic]['questions'][q]['answer']}")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    topics = load_quiz_questions()
    selected_topic = None
    play_quiz()
