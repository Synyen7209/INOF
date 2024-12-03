 
# Multiple-choice quiz game

def quiz_game():
    # Questions and answers
    questions = [
      
       {"question": "What is the process by which plants make their food?", 
        "options":["1. Photosynthesis", "2. Respiration", "3. Fermentation","4. Digestion" ],
        "answer": 1
           
       },

         {
            "question": "Who wrote 'Hamlet'?",
            "options": ["1. Charles Dickens", "2. J.K. Rowling", "3. William Shakespeare", "4. Mark Twain"],
            "answer": 3
        },

        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["1. Gold", "2. Iron", "3. Diamond", "4. Granite"],
            "answer": 3
        },

         {
            "question": "What is the capital of France?",
            "options": ["1. Madrid", "2. Paris", "3. Berlin", "4. Rome"],
            "answer": 2
        },

        {"question": "Who was the first President of the United States?",
         "options": ["1. Abraham Lincion", "2. George Washington", "3. John Adams", "4. Thomas Jefferson"],
         "answer": 2

        },
        
        
       
        {
            "question": "Which fictional wizard attends Hogwarts School of Witchcraft and Wizardry?",
            "options": ["1. Harry Potter", "2. Gandall", "3. Merlin", "4. Dumbledore"],
            "answer": 1
        },
        {
            "question":"What is the largest mammal?",
            "options": ["1. Elephant", "2. Blue Whale", "3. Giraffe", "4. Hippopotamus"],
            "answer": 2
        },
       
        { 
        
        "question": "Which religion is the most popular religion in Norway?",
        "options":["1. Buddhist", "2. Muslims", "3.Christian", "4.Hindu"],
        "answer": 3

        },

         {
            "question": "Which continent Kosovo is found with in?",
            "options": ["1. Europe", "2. Africa", "3. Asia", "4. Ocania"],
            "answer": 1

          },
            {
                "qustion": "What is the capital city of Angola?",
                "options": ["1. The Valley", "2. St John", "3. Luanda", "4. Yerevan"],
                "answer": 3


            },

            {
                "question": "What is the literacy rate of Morocco?",
                "options": ["1. 56.1%", "2. 70%", "3. 20%", "4. 2%"],
                "answer": 1
                

            },

            {
                "question": "What is the currency of Scotland?",
                "options": ["1. Italian Lira", "2. Dollars", "3. Europ", "4. Scottish Gaelic, Scots"],
                "answer": 4


            },


            {
                "question": "What is the maining os Egypt?",
                "options": ["1. Cold Water", "2. Gift of Nile", "3. Red Island", "4. Rising Sun"],
                "answer": 2


            },


        
        {
        "question": "What is the capital city of Denmark?",
        "options": ["1. Cyprus", "2. Cuba", "3. Costa Rica", "4. Copenhagen"],
        "answer": 4
        },

        {"question": "What is the currency of Austria?",
         "options": ["1. Bahamian Dollar", "2. Bahraini Dinar", "3. Euro", "4. Bangladeshi Taka"],
         "answer": 3

        },
        
        {
            "question": "What is the boiling point of water?",
            "options": ["1. 100°C", "2. 0°C", "3. 50°C", "4. 200°C"],
            "answer": 1
        }
           ]


    score = 0

    # Loop through the questions
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        try:
            # Get user's answer
            answer = int(input("Your answer (1-4): "))
            if answer == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {q['options'][q['answer'] - 1]}.\n")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.\n")

    # Display the final score
    print(f"Your final score is {score}/{len(questions)}.")

# Run the game
if __name__ == "__main__":
    quiz_game()
