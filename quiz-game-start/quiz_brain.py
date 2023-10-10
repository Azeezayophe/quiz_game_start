class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        choice = input(f"Q.{self.question_number}: {current_question[0]} (True/False): ")
        self.check_answer(choice, current_question[1])


    def check_answer(self, choice, current_answer):
        if choice.lower() == current_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is {current_answer}.")
        print(f"Your current score is : {self.score}/{self.question_number}.")
        print("\n")

