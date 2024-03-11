"""
Suppose there are two lists - one contains questions and another contains list of 4 possible answers for each question.
Write a program to generate a list that contains lists of question and its  4 possible answers.
"""

qlist = ['What is capital of India', 'Which is your favorite color?']
alist = [['Delhi', 'Mumbai', 'Hyderabad', 'Bangalore'], ['Red', 'Blue', 'White', 'Black']]
print(qlist)
print(alist)
qalist = []

for que, ans in zip(qlist, alist):
    lst = [que, *ans]
    print(lst)
    qalist.append(lst)

print(qalist)
