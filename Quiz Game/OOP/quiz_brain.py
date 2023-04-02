class Quiz:
    def __init__(self, question_list) -> None:
        self.question_list = question_list
        self.question_no = 0
        self.points = 0

    def ask_question(self):
        q = self.question_list[self.question_no]
        a = input("Q %d. %s (True/False): " % (self.question_no + 1, q.text))
        self.question_no += 1
        self.check_answer(a)

    def question_remaining(self):
        if self.question_no + 1 == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, a):
        if a == self.question_list[self.question_no].answer:
            self.points += 1
            print(
                "You got it right\nCurrent score: %d out of %d"
                % (self.points, self.question_no)
            )
        else:
            print(
                "That's wrong\nThe correct answer was %s\nCurrent score: %d out of %d"
                % (
                    self.question_list[self.question_no].answer,
                    self.points,
                    self.question_no,
                )
            )
