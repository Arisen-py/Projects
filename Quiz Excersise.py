#This project is under development and is not fully completeled yet.

import random

questions = [["What is 2+2? "], ["What comes after G? "], ["What is the first letter in the alphabets? "]]
answers = [["A. 2, B. 3, C. 4, D. 22"], ["A. G, B. H, C. I, D. J"], ["A. a, B. b, C. z, D. y"]]
guesses = []
score = 0
qna = []

for q in questions:
    qna.append(q)
    for a in answers:
        qna.append(a)
        

print(qna)
