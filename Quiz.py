# Quiz

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

class Quiz:
    def __init__(self,allofquetions):
        self.allofquestions = allofquetions
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        print("Merhaba, Umit Ekmekci sınava hos geldiniz.")
        for self.questionIndex in range(0,len(list)):
            print(f"Soru-{self.questionIndex + 1}")
            print(listgeliyo.allofquestions[self.questionIndex].text)
            print(listgeliyo.allofquestions[self.questionIndex].choices)
            listgeliyo.CompareAnswer()
            self.questionIndex += 1
            if self.questionIndex == len(list):
                print(f"{len(list)} sorudan {self.score} tanesine dogru cevap verdiniz.")

    def CompareAnswer(self):
        guess = (input("Cevap: "))
        if (guess == listgeliyo.allofquestions[self.questionIndex].answer):
            self.score += 1
        else:
            self.score += 0
            
q1 = Question("Dunyanın en iyi takımı hangisidir?","A-) FB B-) BJK C-) GS","B")
q2 = Question("Dunyanın en iyi takımı hangisidir?","A-) FB,B-) BJK,C-) GS","B")
q3 = Question("Dunyanın en iyi takımı hangisidir?","A-) FB B-) BJK C-) GS","B")
q4 = Question("Dunyanın en iyi takımı hangisidir?","A-) FB,B-) BJKC-) GS","B")
q5 = Question("Dunyanın en iyi takımı hangisidir?","A-) FB B-) BJK C-) GS","B")
q6 = Question("Dunyanın en iyi takımı hangisidir?","A-) FB,B-) BJKC-) GS","B")
q7 = Question("Dunyanın en iyi takımı hangisidir?","A-) FB B-) BJK C-) GS","B")

list = [q1,q2,q3,q4,q5,q6,q7]
# print(q1.text) # Dunyanın en iyi takımı hangisidir?

listgeliyo = Quiz(list)
# print(listgeliyo.allofquestions)

listgeliyo.getQuestion()

