import random

#크림양
amount_of_cream = []
#수분
moistures = []
#당도
sugar_content = []
#짠맛
salty_taste = []
#재료
ingredients = []
#타입
zero_types = []
one_types = []
#선호
zero_preferences = []
one_preferences = []

#데이터준비 총 200개 num1 = 식사빵 갯수  num2 = 디저트빵 갯수

num1 = random.randrange(155, 165)

for i in range(num1):
    zero_types.insert(i, 0)
    moistures.insert(i, random.randrange(1,6))
    salty_taste.insert(i, random.randrange(1,6))
    ingredients.insert(i, random.randrange(2))
    if(salty_taste[i] <= 2 and ingredients[i] == 1 and moistures[i] >= 2):
        zero_preferences.insert(i, 1)
    else:
        zero_preferences.insert(i, 0)

num2 = 250 - (i + 1)

for i in range(num2):
    one_types.insert(i, 1)
    moistures.insert(i, random.randrange(1,6))
    amount_of_cream.insert(i, random.randrange(1,6))
    sugar_content.insert(i, random.randrange(1,6))
    if(amount_of_cream[i] >= 3 and moistures[i] >= 1 and sugar_content[i] >= 3):
        one_preferences.insert(i, 1)
    else:
        one_preferences.insert(i, 0)

