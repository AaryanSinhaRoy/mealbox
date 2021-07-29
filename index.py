from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    randomMealdata=requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    randomMeal=json.loads(randomMealdata.content)

    allcatdata=requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")
    allcat=json.loads(allcatdata.content)
    return render_template("index.html",randomMeal=randomMeal,allcat=allcat)


@app.route('/meal/<mealname>/<mealid>')
def mealinfo(mealname,mealid):
    meal_info_data=requests.get("http://www.themealdb.com/api/json/v1/1/lookup.php?i="+mealid)
    meal_info=json.loads(meal_info_data.content)
    inglist=[]
    measurelist=[]
    for x in meal_info['meals']:
        for y in range(1,20):
            if len(x['strIngredient'+str(y)]) !=0:
                inglist.append(x['strIngredient'+str(y)])
            if len(x['strMeasure'+str(y)]) !=0:
                measurelist.append(x['strMeasure'+str(y)])

    return render_template("mealbox.html",meal_info=meal_info,mealname=mealname,inglist=inglist,measurelist=measurelist)

@app.route("/categories/<catname>")
def catinfo(catname):
    cat_info_data=requests.get("http://www.themealdb.com/api/json/v1/1/filter.php?c="+catname)
    cat_info=json.loads(cat_info_data.content)
    return render_template("categories.html",cat_info=cat_info,catname=catname)


if __name__ == '__main__':
    app.run(debug=True)