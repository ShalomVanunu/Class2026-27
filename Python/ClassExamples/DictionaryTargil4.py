"""
import

NUMBER = 10

Def function ():
    pass

function()

"""
score_dicti= {}
def average(score_dicti):
    sum_scores = 0
    for score in score_dicti.values():
        sum_scores += score
    return  sum_scores/len(score_dicti.values())

def sort_dicti(score_dicti):
    return sorted(score_dicti.items())

for order in range(2):
    name = input("Enter you name :")
    score  = int(input("Enter you score :"))
    score_dicti[name] = score

print("the average is  :" ,average(score_dicti))
print(sort_dicti(score_dicti))