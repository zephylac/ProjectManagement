class question:
    def __init__(self, difficulty, question, answer, propositions):
        self._difficulty=difficulty
        self._question = question
        self._answer = answer
        self._propositions = propositions

    @def difficulty():
        doc = "The difficulty property."
        def fget(self):
            return self._difficulty
        def fset(self, value):
            self._difficulty = value
        def fdel(self):
            del self._difficulty
        return locals()
    difficulty = property(**difficulty())

    @def question():
        doc = "The question property."
        def fget(self):
            return self._question
        def fset(self, value):
            self._question = value
        def fdel(self):
            del self._question
        return locals()
    question = property(**question())

    @def answer():
        doc = "The answer property."
        def fget(self):
            return self._answer
        def fset(self, value):
            self._answer = value
        def fdel(self):
            del self._answer
        return locals()
        answer = property(**answer())

    @def propositions():
        doc = "The propositions property."
        def fget(self):
            return self._propositions
        def fset(self, value):
            self._propositions = value
        def fdel(self):
            del self._propositions
        return locals()
    propositions = property(**propositions())

def select_word_question(difficulty):
    question1 = Question(1,"je ... une pomme","mange",["mange","bois"])
    question2 = Question(2,"je ... en cours","vais",["vais","vait","va"])
    questions = [question1,question2]
    for quest in questions:
        if quest.difficulty() == difficulty:
            return quest

def go():
    return select_word_question(1).question()
