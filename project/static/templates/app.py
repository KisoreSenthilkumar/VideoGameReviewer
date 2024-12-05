import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import matplotlib.pyplot as plt  # For visualizations
import os
import pandas as pd
import pickle

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = "games.db"

# Load the trained models
with open('model_playtime.pkl', 'rb') as file:
    model_playtime = pickle.load(file)

with open('model_ratings.pkl', 'rb') as file:
    model_ratings = pickle.load(file)

with open('model_pricing.pkl', 'rb') as file:
    model_pricing = pickle.load(file)

with open('model_game_score.pkl', 'rb') as file:
    model_game_score = pickle.load(file)

def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""  
            CREATE TABLE IF NOT EXISTS Games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                release_date TEXT,
                price REAL
            )
        """)
        conn.commit()

def load_data_to_db(steam_csv, output_csv):
    """
    Load the dataset into the SteamGames table in the database.
    """
    try:
        # Read the dataset
        output_df = pd.read_csv(output_csv)
        steam_df = pd.read_csv(steam_csv)
        
        # Connect to the database
        conn = connect_db()
        
        # Load data into a new table named 'SteamGames'
        output_df.to_sql('OutputData', conn, if_exists='replace', index=False)
        steam_df.to_sql('SteamData', conn, if_exists='replace', index=False)

        conn.close()
        
        print("Dataset loaded into the 'SteamGames' table successfully!")
    except Exception as e:
        print(f"Error loading dataset: {e}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route("/admin_steam_games")
def admin_steam_games():
    """
    Display the games in the SteamData table for the admin to manage.
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    # Fetch all relevant columns from SteamData
    cursor.execute("""
        SELECT rowid, appid, name, release_date, english, developer, publisher,
               platforms, required_age, categories, genres, steamspy_tags,
               achievements, positive_ratings, negative_ratings, average_playtime,
               median_playtime, owners, price
        FROM SteamData
    """)
    steam_games = cursor.fetchall()
    conn.close()
    
    return render_template("admin_steam_games.html", games=steam_games)

@app.route('/user_steam_games')
def user_steam_games():
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    SELECT appid, name, release_date, developer, publisher, platforms, achievements, positive_ratings, negative_ratings, average_playtime, price
    FROM SteamData
    """
    cursor.execute(query)
    steam_games = cursor.fetchall()
    conn.close()
    return render_template('user_steam_games.html', steam_games=steam_games)


@app.route("/user_dashboard")
def user_dashboard():
    return render_template("user_dashboard.html")

# Search and Filter Games
@app.route("/search_games", methods=["GET", "POST"])
def search_games():
    search_results = []
    if request.method == "POST":
        search_query = request.form.get("query")
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Games WHERE name LIKE ?", (f"%{search_query}%",))
        search_results = cursor.fetchall()
        conn.close()
    return render_template("search_games.html", results=search_results)

# Example Visualization: Average Price of Games
@app.route("/visualize_price")
def visualize_price():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM Games")
    data = cursor.fetchall()
    conn.close()
    
    # Create a bar chart
    names = [row[0] for row in data]
    prices = [row[1] for row in data]
    plt.figure(figsize=(10, 6))
    plt.bar(names, prices, color='skyblue')
    plt.xlabel("Game Names")
    plt.ylabel("Prices")
    plt.title("Game Prices")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    chart_path = os.path.join("static", "price_chart.png")
    plt.savefig(chart_path)
    plt.close()
    return render_template("visualize_price.html", chart_url=chart_path)


@app.route("/add_steam_game", methods=["GET", "POST"])
def add_steam_game():
    if request.method == "POST":
        # Get data from form inputs
        appid = request.form.get("appid")
        name = request.form.get("name")
        release_date = request.form.get("release_date")
        english = request.form.get("english")
        developer = request.form.get("developer")
        publisher = request.form.get("publisher")
        platforms = request.form.get("platforms")
        required_age = request.form.get("required_age")
        categories = request.form.get("categories")
        genres = request.form.get("genres")
        steamspy_tags = request.form.get("steamspy_tags")
        achievements = request.form.get("achievements")
        positive_ratings = request.form.get("positive_ratings")
        negative_ratings = request.form.get("negative_ratings")
        average_playtime = request.form.get("average_playtime")
        median_playtime = request.form.get("median_playtime")
        owners = request.form.get("owners")
        price = request.form.get("price")
        
        try:
            # Insert data into SteamData table
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO SteamData (
                    appid, name, release_date, english, developer, publisher,
                    platforms, required_age, categories, genres, steamspy_tags,
                    achievements, positive_ratings, negative_ratings, average_playtime,
                    median_playtime, owners, price
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (appid, name, release_date, english, developer, publisher,
                  platforms, required_age, categories, genres, steamspy_tags,
                  achievements, positive_ratings, negative_ratings, average_playtime,
                  median_playtime, owners, price))
            conn.commit()
            conn.close()
            flash("New Steam game added successfully!", "success")
        except Exception as e:
            flash(f"Error adding Steam game: {e}", "danger")
        return redirect(url_for("admin_steam_games"))
    return render_template("add_steam_game.html")

@app.route("/add_steam_game_entry", methods=["GET", "POST"])
def add_steam_game_entry():
    """
    Add a new game to the SteamData table.
    """
    if request.method == "POST":
        # Collect form data
        appid = request.form.get("appid")
        name = request.form.get("name")
        release_date = request.form.get("release_date")
        english = request.form.get("english")
        developer = request.form.get("developer")
        publisher = request.form.get("publisher")
        platforms = request.form.get("platforms")
        required_age = request.form.get("required_age")
        categories = request.form.get("categories")
        genres = request.form.get("genres")
        steamspy_tags = request.form.get("steamspy_tags")
        achievements = request.form.get("achievements")
        positive_ratings = request.form.get("positive_ratings")
        negative_ratings = request.form.get("negative_ratings")
        average_playtime = request.form.get("average_playtime")
        median_playtime = request.form.get("median_playtime")
        owners = request.form.get("owners")
        price = request.form.get("price")
        
        try:
            # Insert into SteamData table
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO SteamData (
                    appid, name, release_date, english, developer, publisher,
                    platforms, required_age, categories, genres, steamspy_tags,
                    achievements, positive_ratings, negative_ratings, average_playtime,
                    median_playtime, owners, price
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (appid, name, release_date, english, developer, publisher,
                  platforms, required_age, categories, genres, steamspy_tags,
                  achievements, positive_ratings, negative_ratings, average_playtime,
                  median_playtime, owners, price))
            conn.commit()
            conn.close()
            flash("New Steam game added successfully!", "success")
        except Exception as e:
            flash(f"Error adding Steam game: {e}", "danger")
        return redirect(url_for("admin_steam_games"))
    return render_template("add_steam_game.html")

@app.route('/edit_steam_game/<int:game_id>', methods=["GET", "POST"])
def edit_steam_game(game_id):
    """
    Edit a game entry in the SteamData table.
    """
    conn = connect_db()
    cursor = conn.cursor()

    if request.method == "POST":
        # Get the updated values from the form
        name = request.form.get("name")
        positive_ratings = request.form.get("positive_ratings")
        negative_ratings = request.form.get("negative_ratings")
        price = request.form.get("price")
        achievements = request.form.get("achievements")
        average_playtime = request.form.get("average_playtime")

        # Update the database
        cursor.execute("""
            UPDATE SteamData
            SET name = ?, positive_ratings = ?, negative_ratings = ?, price = ?, achievements = ?, average_playtime = ?
            WHERE rowid = ?
        """, (name, positive_ratings, negative_ratings, price, achievements, average_playtime, game_id))
        conn.commit()
        conn.close()

        flash("Game updated successfully!", "success")
        return redirect(url_for("admin_steam_games"))

    # Fetch the game details for pre-filling the form
    cursor.execute("SELECT rowid, * FROM SteamData WHERE rowid = ?", (game_id,))
    game = cursor.fetchone()
    conn.close()
    return render_template('edit_steam_game.html', game=game)


@app.route('/delete_steam_game/<int:game_id>')
def delete_steam_game(game_id):
    """
    Delete a game entry from the SteamData table.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM SteamData WHERE rowid = ?", (game_id,))
    conn.commit()
    conn.close()

    flash("Game deleted successfully!", "success")
    return redirect(url_for("admin_steam_games"))

@app.route('/view_games')
def view_steam_games():
    """
    Fetch and display all games from the SteamData table.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SteamData")  # Query to fetch all games from SteamData
    steam_games = cursor.fetchall()
    conn.close()
    return render_template('view_steam_games.html', steam_games=steam_games)



@app.route('/predict_playtime', methods=['GET', 'POST'])
def predict_playtime():
    prediction = None
    if request.method == 'POST':
        inputs = {
            'positive_ratings': float(request.form['positive_ratings']),
            'negative_ratings': float(request.form['negative_ratings']),
            'price': float(request.form['price']),
            'achievements': int(request.form['achievements']),
        }
        input_df = pd.DataFrame([inputs])
        prediction = model_playtime.predict(input_df)[0]
    return render_template('predict_playtime.html', prediction=prediction)

@app.route('/predict_ratings', methods=['GET', 'POST'])
def predict_ratings():
    prediction = None
    if request.method == 'POST':
        inputs = {
            'negative_ratings': float(request.form['negative_ratings']),
            'price': float(request.form['price']),
            'achievements': int(request.form['achievements']),
            'average_playtime': float(request.form['average_playtime']),
        }
        input_df = pd.DataFrame([inputs])
        prediction = model_ratings.predict(input_df)[0]
    return render_template('predict_ratings.html', prediction=prediction)

@app.route('/predict_pricing', methods=['GET', 'POST'])
def predict_pricing():
    prediction = None
    if request.method == 'POST':
        inputs = {
            'positive_ratings': float(request.form['positive_ratings']),
            'negative_ratings': float(request.form['negative_ratings']),
            'achievements': int(request.form['achievements']),
            'average_playtime': float(request.form['average_playtime']),
        }
        input_df = pd.DataFrame([inputs])
        prediction = model_pricing.predict(input_df)[0]
    return render_template('predict_pricing.html', prediction=prediction)

@app.route('/predict_game_score', methods=['GET', 'POST'])
def predict_game_score():
    prediction = None
    if request.method == 'POST':
        inputs = {
            'is_action': int(request.form['is_action']),
            'is_indie': int(request.form['is_indie']),
            'is_casual': int(request.form['is_casual']),
            'is_strat': int(request.form['is_strat']),
            'is_adv': int(request.form['is_adv']),
            'is_f2p': int(request.form['is_f2p']),
            'is_sim': int(request.form['is_sim']),
            'is_windows': int(request.form['is_windows']),
            'is_mac': int(request.form['is_mac']),
            'is_linux': int(request.form['is_linux']),
        }
        input_df = pd.DataFrame([inputs])
        prediction = model_game_score.predict(input_df)[0]
    return render_template('predict_game_score.html', prediction=prediction)

@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        release_date = request.form.get("release_date")
        price = request.form.get("price")
        tags = request.form.get("tags")  # Tags entered as comma-separated values

        if not name or not price:
            flash("Name and Price are required fields!", "warning")
            return redirect(url_for("add_game"))

        try:
            conn = connect_db()
            cursor = conn.cursor()
            # Insert game
            cursor.execute("""
                INSERT INTO Games (name, description, release_date, price) 
                VALUES (?, ?, ?, ?)
            """, (name, description, release_date, price))
            game_id = cursor.lastrowid
            # Insert tags
            if tags:
                tag_list = [tag.strip() for tag in tags.split(",")]
                for tag in tag_list:
                    cursor.execute("INSERT INTO Tags (game_id, tag) VALUES (?, ?)", (game_id, tag))
            conn.commit()
            flash("Game added successfully with tags!", "success")
        except sqlite3.Error as e:
            flash(f"Database error: {e}", "error")
        finally:
            conn.close()
        return redirect(url_for("view_games"))
    return render_template("add_game.html")

@app.route("/delete_game/<int:game_id>")
def delete_game(game_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        # Delete tags first
        cursor.execute("DELETE FROM Tags WHERE game_id = ?", (game_id,))
        # Delete the game
        cursor.execute("DELETE FROM Games WHERE id = ?", (game_id,))
        conn.commit()
        flash("Game and its tags deleted successfully!", "success")
    except sqlite3.Error as e:
        flash(f"Database error: {e}", "error")
    finally:
        conn.close()
    return redirect(url_for("view_games"))



@app.route("/edit_game/<int:game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    conn = connect_db()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        release_date = request.form.get("release_date")
        price = request.form.get("price")
        tags = request.form.get("tags")  # Tags entered as comma-separated values

        if not name or not price:
            flash("Name and Price are required fields!", "warning")
            return redirect(url_for("edit_game", game_id=game_id))

        try:
            # Update game details
            cursor.execute("""
                UPDATE Games
                SET name = ?, description = ?, release_date = ?, price = ?
                WHERE id = ?
            """, (name, description, release_date, price, game_id))
            # Update tags
            cursor.execute("DELETE FROM Tags WHERE game_id = ?", (game_id,))
            if tags:
                tag_list = [tag.strip() for tag in tags.split(",")]
                for tag in tag_list:
                    cursor.execute("INSERT INTO Tags (game_id, tag) VALUES (?, ?)", (game_id, tag))
            conn.commit()
            flash("Game and tags updated successfully!", "success")
        except sqlite3.Error as e:
            flash(f"Database error: {e}", "error")
        finally:
            conn.close()
        return redirect(url_for("view_games"))
    
    

    # Fetch game details and tags
    cursor.execute("SELECT * FROM Games WHERE id = ?", (game_id,))
    game = cursor.fetchone()
    cursor.execute("SELECT tag FROM Tags WHERE game_id = ?", (game_id,))
    tags = ", ".join([row[0] for row in cursor.fetchall()])
    conn.close()
    return render_template("edit_game.html", game=game, tags=tags)

if __name__ == "__main__":
    init_db()
    load_data_to_db('/Users/neeraj_gummadi/Documents/project/steam.csv', '/Users/neeraj_gummadi/Documents/project/output.csv')
    app.run(debug=True, port=5001)