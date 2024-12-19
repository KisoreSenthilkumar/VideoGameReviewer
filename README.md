# 🎮 **Video Game Reception Prediction** 🎮

Welcome to the **Video Game Reception Prediction** project hosted at https://videogameappcode-ve99unwv2suqfshnx42vob.streamlit.app/ !  
This project explores key factors influencing video game success, leveraging data analysis and predictive modeling to understand trends in the gaming industry. Below are the details of our amazing team and their contributions!

----

## 👥 **Team Members**

| **Team Member**          | **University ID** | 
|---------------------------|-------------------|
| 🎓 **Kisore Senthilkumar** | 50610194          |
| 🎓 **Harshitha Itta**       | 50605000          |
| 🎓 **Shashank Govindu**    | 50594030          |
| 🎓 **Neeraj Gummadi**      | 50594025          |

----
## **Questions Assigned**
| **Team Member**          | **Primary Hypotheses**                                                                                     | **Code Location**                  | **Model File Location**       | **Common Analysis Location**    |
|---------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------|--------------------------------|----------------------------------|
| **Kisore Senthilkumar**   | 1️⃣ Critic scores directly influence user ratings for games.                                               | `app/model_game_score.py`          | `app/model_game_score.pkl`    | `doc/analysis.txt`              |
|                           | 2️⃣ A higher user review count amplifies the reliability of user ratings.                                 |                                     |                                |                                  |
| **Harshitha Itta**        | 1️⃣ Certain genres, such as RPG and FPS, inherently receive higher ratings due to immersive gameplay.      | `app/model_ratings.py`             | `app/model_ratings.pkl`       | `doc/analysis.txt`              |
|                           | 2️⃣ Cooperative and multiplayer games are rated more positively compared to single-player experiences.    |                                     |                                |                                  |
| **Shashank Govindu**      | 1️⃣ Lower-priced games show exponential growth in ownership, especially during sales or discounts.         | `app/model_pricing.py`             | `app/model_pricing.pkl`       | `doc/analysis.txt`              |
|                           | 2️⃣ Free-to-play games experience higher ownership but might not correlate with equally high engagement.   |                                     |                                |                                  |
| **Neeraj Gummadi**        | 1️⃣ Games with longer playtime offer more value, correlating positively with ownership counts.             | `app/model_playtime.py`            | `app/model_playtime.pkl`      | `doc/analysis.txt`              |
|                           | 2️⃣ Highly engaging games with repetitive play sessions lead to higher player retention and ownership.     |                                     |                                |                                  |
-----
## 🚀 **Detailed Highlights**
### 🎯 **1. Game Score Prediction**
- **Algorithm**: Gradient Boosting Framework
- **Purpose**: Predict overall game scores based on genres (`is_action`, `is_indie`, etc.) and platform compatibility (`is_windows`, `is_mac`, etc.).
- **Key Highlights**:
  - Optimized for **low RMSE** with `num_boost_round=200` and `learning_rate=0.1`.
  - Efficiently handles genre and platform-based feature interactions.
  - Model saved as **`model_game_score.pkl`** for quick deployment.

---

### 🕒 **2. Playtime Prediction**
- **Algorithm**: LightGBM Regression
- **Purpose**: Estimate average playtime using features like:
  - `positive_ratings`, `negative_ratings`, `price`, `achievements`.
- **Key Highlights**:
  - Preprocessed for clean and accurate training.
  - Handles missing data effectively with robust LightGBM regression.
  - Saves the model as **`model_playtime.pkl`** for reuse in Streamlit apps.

---

### 💸 **3. Pricing Prediction**
- **Algorithm**: Decision Tree Regression
- **Purpose**: Predict game prices by analyzing:
  - `positive_ratings`, `negative_ratings`, `achievements`, and `playtime`.
- **Key Highlights**:
  - Simplistic and interpretable decision tree splits for actionable pricing insights.
  - Model saved as **`model_pricing.pkl`** to enable instant predictions.

---

### ⭐ **4. Ratings Prediction**
- **Algorithm**: Random Forest Regressor
- **Purpose**: Predict positive ratings using features such as:
  - `negative_ratings`, `price`, `achievements`, and `playtime`.
- **Key Highlights**:
  - Balanced accuracy with reduced hyperparameters for faster computation:
    - `n_estimators=50`, `max_depth=10`, `max_features='sqrt'`.
  - Serialized as **`model_ratings.pkl`** for efficient use in prediction pipelines.

---

## ✨ **General Strengths**
1. **Dynamic Data Handling**:
   - All models are integrated with a centralized **SQLite database** (`games.db`) for seamless data retrieval and preprocessing.
2. **Reusable Models**:
   - Models are stored in `.pkl` files, ensuring easy portability and deployment.
3. **Real-World Relevance**:
   - Focused on practical features like ratings, price, playtime, and genre for actionable insights.
4. **Scalability**:
   - Modular structure allows for the easy addition of new models or datasets.

---

## 📈 **Impact on Gaming Analytics**
- Provides game developers and publishers with actionable insights on:
  - Pricing strategies.
  - User satisfaction metrics.
  - Genre-specific trends.
- Enhances decision-making through accurate predictions of playtime, ratings, and scores.

---

## 🌟 **Detailed Hypotheses**

### 🎓 **Kisore Senthilkumar (Game Score Analysis)**

1️⃣ **Critic scores directly influence user ratings for games.**  
   📊 *Elaboration:* Critic scores serve as a benchmark for game quality and significantly affect players' perceptions. A high critic score can set high expectations and positively sway user ratings. For new or unfamiliar games, players often rely on critic scores as a primary decision-making factor.  

2️⃣ **A higher user review count amplifies the reliability of user ratings.**  
   📊 *Elaboration:* A larger number of user reviews helps mitigate the influence of outliers and biased opinions, resulting in more accurate and consistent ratings. Popular games with more reviews are viewed as more trustworthy, influencing potential buyers.

---

### 🎓 **Harshitha Itta (Ratings Prediction)**

1️⃣ **Certain genres, such as RPG and FPS, inherently receive higher ratings due to immersive gameplay.**  
   🌍 *Elaboration:* RPGs and FPS games often provide detailed world-building, rich storytelling, and engaging mechanics that resonate with players. These genres consistently outperform others, such as casual or puzzle games, in terms of user ratings.  

2️⃣ **Cooperative and multiplayer games are rated more positively compared to single-player experiences.**  
   👫 *Elaboration:* Social interaction in cooperative or multiplayer games significantly enhances user satisfaction. Players enjoy sharing achievements and competing with friends, which drives higher ratings compared to solo experiences.

---

### 🎓 **Shashank Govindu (Pricing Analysis)**

1️⃣ **Lower-priced games show exponential growth in ownership, especially during sales or discounts.**  
   💸 *Elaboration:* Price drops during sales events, such as the Steam Winter Sale, drastically increase game adoption. These periods lower the financial barrier for entry, prompting players to make impulse purchases and contributing to exponential growth in ownership.  

2️⃣ **Free-to-play games experience higher ownership but might not correlate with equally high engagement.**  

   🎮 *Elaboration:* Free-to-play games attract a massive audience due to their zero-cost entry but often fail to maintain high engagement levels. Players might try the game but leave without investing time unless incentivized by competitive mechanics or social features.

---

### 🎓 **Neeraj Gummadi (Playtime Analysis)**

1️⃣ **Games with longer playtime offer more value, correlating positively with ownership counts.**  
   ⏳ *Elaboration:* Players associate longer playtimes with better entertainment value, especially for expansive RPGs and open-world games. These games offer extended content, encouraging more purchases and higher ownership rates over time.  

2️⃣ **Highly engaging games with repetitive play sessions lead to higher player retention and ownership.**  
   🔄 *Elaboration:* Replayable games (e.g., multiplayer shooters or survival games) create lasting engagement, which fosters loyalty and attracts new players through word-of-mouth recommendations, driving higher ownership counts.
   
---
### 📂 Folder Structure

```plaintext
VideoGameReviewer/
├── app/                               # Application-related files
│   ├── app_sl.py                      # Main application script
│   ├── games.db                       # Database file for game information
│   ├── model_game_score.pkl           # Pickled model for game score analysis
│   ├── model_game_score.py            # Script for game score prediction
│   ├── model_playtime.pkl             # Pickled model for playtime prediction
│   ├── model_playtime.py              # Script for playtime prediction
│   ├── model_pricing.pkl              # Pickled model for pricing analysis
│   ├── model_pricing.py               # Script for pricing prediction
│   ├── model_ratings.pkl              # Pickled model for ratings prediction
│   ├── model_ratings.py               # Script for user ratings prediction
│   ├── output.csv                     # Output file containing analysis results
│   ├── requirements.txt               # Python dependencies
│   ├── runtime.txt                    # Runtime configuration logs
│   └── steam.csv                      # Steam dataset for analysis
│
├── data/                              # Raw and cleaned data files
│   ├── cleaned_data.csv               # Preprocessed dataset for analysis
│   ├── steam_app_data.csv             # Steam app-related raw dataset
│   └── steamspy_data.csv              # SteamSpy raw dataset
│
├── doc/                               # Documentation and analysis reports
│   ├── 50594025_Phase2.ipynb.pdf      # Execution report by Neeraj
│   ├── 50594030_Phase2.ipynb.pdf      # Execution report by Shashank
│   ├── 50605000_Harshitha_Itta_phase2.pdf # Execution report by Harshitha
│   ├── 50610194_Phase2DataProcessing.pdf # Data processing report by Kisore
│   ├── 50610194_Phase2Models.pdf      # Model execution report by Kisore
│   ├── README.txt                     # Project overview README
│   ├── analysis.txt                   # Common analysis details
│   └── report.pdf                     # Comprehensive project report
│
├── exp/                               # Experiment and phase-wise files
│   ├── 50594025_Phase2.ipynb          # Phase 2 notebook by Neeraj
│   ├── 50594030_Phase2.ipynb          # Phase 2 notebook by Shashank
│   ├── 50605000_Harshitha_Itta_phase2.ipynb # Phase 2 notebook by Harshitha
│   ├── 50610194_Phase2DataProcessing.ipynb # Data processing notebook
│   ├── 50610194_Phase2Models.ipynb    # Model experiments by Kisore
│   └── Steam_Data_Phase_1.ipynb       # Initial phase notebook
│
└── README.md                          # Main project documentation
```
---
# 🛠️ **Instructions to Build and Run the Video Game Reception Prediction App**

## 🧾 **Prerequisites**

Before you begin, ensure the following requirements are met:
1. **Operating System:** Windows, macOS, or Linux.  
2. **Python Version:** Python 3.8 or higher.  
3. **Python Package Manager:** `pip` must be installed.  
4. **Streamlit:** Ensure Streamlit is compatible with your Python version.

---

## 📂 **Step 1: Clone the Repository**

Download the repository from GitHub to your local machine. Open a terminal or command prompt and run:

```bash
git clone https://github.com/KisoreSenthilkumar/VideoGameReviewer.git
cd VideoGameReviewer
```

This will create a local copy of the project and navigate into its root directory.

---

## 🔧 **Step 2: Install Required Dependencies**

The project requires specific Python packages to function. Install them using the provided `requirements.txt` file. Run:

```bash
pip install -r requirements.txt
```

This command installs dependencies like:
- `streamlit` - For the web-based dashboard.
- `pandas` - For data manipulation.
- `lightgbm`, `scikit-learn` - For model training and predictions.
- `sqlite3` - For database management.

---

## 📁 **Step 3: Verify Data and Model Files**

Ensure the following files are present in the `app/` directory:

1. **Database File:**
   - `games.db` – The SQLite database containing Steam game data.

2. **Model Files:**  
   Pre-trained machine learning models:
   - `model_playtime.pkl` – Predicts average playtime.  
   - `model_ratings.pkl` – Predicts positive ratings.  
   - `model_pricing.pkl` – Predicts pricing.  
   - `model_game_score.pkl` – Predicts overall game score.

---

## 🚀 **Step 4: Run the Application**

Launch the application using Streamlit. Run the following command in your terminal:

```bash
streamlit run app/app_sl.py
```

This command will:
1. Start the Streamlit server.
2. Open the **Video Game Reception Prediction Dashboard** in your default web browser.

If the browser doesn’t open automatically, check the terminal for a link to access the app.

---

## 🧭 **Step 5: Navigate Through the App**

Once the dashboard is launched, use the sidebar to access its features:

1. **Home:**  
   Overview of the dashboard and its features.

2. **Manage Steam Games:**  
   - View all games in the database.  
   - Add new game records.  
   - Edit or delete existing game records.

3. **View Games:**  
   Explore game data stored in the `games.db` database.

4. **Prediction Tools:**
   - **Playtime Prediction:** Enter features like positive ratings, price, and achievements to estimate average playtime.
   - **Ratings Prediction:** Predict the number of positive ratings based on game attributes.
   - **Pricing Prediction:** Estimate a game’s price for market competitiveness.
   - **Game Score Prediction:** Evaluate a game’s reception score based on features like genre and platform compatibility.

---

## 🌟 **Step 6: Example Inputs for Predictions**

To test the app’s prediction features, use the following sample inputs:

### **Playtime Prediction**
- Positive Ratings: `5000`  
- Negative Ratings: `300`  
- Price: `$20`  
- Achievements: `10`

### **Ratings Prediction**
- Negative Ratings: `500`  
- Price: `$25`  
- Achievements: `15`  
- Average Playtime: `100`

### **Pricing Prediction**
- Positive Ratings: `2000`  
- Negative Ratings: `200`  
- Achievements: `8`  
- Average Playtime: `50`

---

## 🛑 **Troubleshooting**

Here are common issues and their solutions:

### **1. Database Not Found**
- **Error:** `FileNotFoundError: games.db not found`  
- **Fix:** Ensure `games.db` is present in the `app/` directory.

### **2. Missing Model Files**
- **Error:** `FileNotFoundError: model_playtime.pkl not found`  
- **Fix:** Ensure all `.pkl` files are available in the `app/` directory.

### **3. ModuleNotFoundError**
- **Error:** `ModuleNotFoundError: No module named '<package>'`  
- **Fix:** Re-run `pip install -r requirements.txt` to ensure all dependencies are installed.

