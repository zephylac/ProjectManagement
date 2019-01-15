class Question:
    def __init__(self, difficulty, question, answer, propositions):
        self.difficulty=difficulty
        self.question = question
        self.answer = answer
        self.propositions = propositions

    def difficulty():
        return self.difficulty

    def question():
        return self.question

    def answer():
        return self.answer

    def propositions():
        return self.propositions



def select_word_question(difficulty):
    question1 = Question(1,"je ... une pomme","mange",["mange","bois"])
    question2 = Question(2,"je ... en cours","vais",["vais","vait","va"])
    questions = [question1,question2]
    for quest in questions:
        if quest.difficulty() == difficulty:
            return quest

def go():
    return select_word_question(1).question
