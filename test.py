import requests
import json

randomMealdata=requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
randomMeal=json.loads(randomMealdata.content)

for x in randomMeal['meals']:
    print(x['strMeal']+" \n\n")
    for y in range(1,20):
        if len(x['strIngredient'+str(y)]) !=0:
            print(x['strIngredient'+str(y)]+"  "+x['strMeasure'+str(y)])
    
    print("\n\n "+x['strInstructions'])