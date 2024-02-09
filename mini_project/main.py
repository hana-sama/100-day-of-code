from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
app = Flask(__name__)



wine_data = pd.read_csv('./wines/wines.csv')


num_of_full_mark_wines = 0
for index, row in wine_data.iterrows():
    if row['points'] == 100:
        num_of_full_mark_wines += 1
print(num_of_full_mark_wines)

num_of_lower_rating_brands = 0
for index, row in wine_data.iterrows():
    if 0 < row['points'] <= 5:
        num_of_lower_rating_brands += 1
print(num_of_lower_rating_brands)

filtered_data = wine_data.loc[wine_data['price'] < 100]
print(len(filtered_data))
print(filtered_data.describe())
plt.hist(filtered_data['price'])
@app.route("/")
def index():
    wine_data = pd.read_csv('./wines/wines.csv')
    highest = wine_data['price'].max()
    brand = wine_data.loc[wine_data['price'] == highest]['name'].squeeze()
    return render_template("index.html", data=wine_data, expensive=highest, wine_name=brand)

@app.route("/api/v1/<name>")
def wine_tasting_data(name):
    wine_tasting_data = pd.read_csv('./wines/wines.csv')
    user_choise = wine_tasting_data.loc[wine_tasting_data['name'] == name]
    return user_choise.to_dict(orient="records")

if __name__ == "__main__":
    app.run(debug=True)