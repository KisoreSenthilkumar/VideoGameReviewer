# 🎮 **Video Game Reception Prediction** 🎮

Welcome to the **Video Game Reception Prediction** project!  
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
| **Kisore Senthilkumar** | 1️⃣ Critic scores directly influence user ratings for games.                                               | `app/model_game_score.py`          | `app/model_game_score.pkl`    | `doc/analysis.txt`              |
|                           | 2️⃣ A higher user review count amplifies the reliability of user ratings.                                 |                                     |                                |                                  |
| **Harshitha Itta**       | 1️⃣ Games with longer playtime offer more value, correlating positively with ownership counts.             | `app/model_playtime.py`            | `app/model_playtime.pkl`      | `doc/analysis.txt`              |
|                           | 2️⃣ Highly engaging games with repetitive play sessions lead to higher player retention and ownership.     |                                     |                                |                                  |
| **Shashank Govindu**    | 1️⃣ Lower-priced games show exponential growth in ownership, especially during sales or discounts.         | `app/model_pricing.py`             | `app/model_pricing.pkl`       | `doc/analysis.txt`              |
|                           | 2️⃣ Free-to-play games experience higher ownership but might not correlate with equally high engagement.   |                                     |                                |                                  |
| **Neeraj Gummadi**      | 1️⃣ Certain genres, such as RPG and FPS, inherently receive higher ratings due to immersive gameplay.      | `app/model_ratings.py`             | `app/model_ratings.pkl`       | `doc/analysis.txt`              |
|                           | 2️⃣ Cooperative and multiplayer games are rated more positively compared to single-player experiences.    |                                     |                                |                                  |

-----

## 🌟 **Detailed Hypotheses**

### 🎓 **Kisore Senthilkumar (Game Score Analysis)**

1️⃣ **Critic scores directly influence user ratings for games.**  
   📊 *Elaboration:* Critic scores serve as a benchmark for game quality and significantly affect players' perceptions. A high critic score can set high expectations and positively sway user ratings. For new or unfamiliar games, players often rely on critic scores as a primary decision-making factor.  

2️⃣ **A higher user review count amplifies the reliability of user ratings.**  
   📊 *Elaboration:* A larger number of user reviews helps mitigate the influence of outliers and biased opinions, resulting in more accurate and consistent ratings. Popular games with more reviews are viewed as more trustworthy, influencing potential buyers.

---

### 🎓 **Harshitha Itta (Playtime Prediction)**

1️⃣ **Games with longer playtime offer more value, correlating positively with ownership counts.**  
   ⏳ *Elaboration:* Players associate longer playtimes with better entertainment value, especially for expansive RPGs and open-world games. These games offer extended content, encouraging more purchases and higher ownership rates over time.  

2️⃣ **Highly engaging games with repetitive play sessions lead to higher player retention and ownership.**  
   🔄 *Elaboration:* Replayable games (e.g., multiplayer shooters or survival games) create lasting engagement, which fosters loyalty and attracts new players through word-of-mouth recommendations, driving higher ownership counts.

---

### 🎓 **Shashank Govindu (Pricing Analysis)**

1️⃣ **Lower-priced games show exponential growth in ownership, especially during sales or discounts.**  
   💸 *Elaboration:* Price drops during sales events, such as the Steam Winter Sale, drastically increase game adoption. These periods lower the financial barrier for entry, prompting players to make impulse purchases and contributing to exponential growth in ownership.  

2️⃣ **Free-to-play games experience higher ownership but might not correlate with equally high engagement.**  
   🎮 *Elaboration:* Free-to-play games attract a massive audience due to their zero-cost entry but often fail to maintain high engagement levels. Players might try the game but leave without investing time unless incentivized by competitive mechanics or social features.

---

### 🎓 **Neeraj Gummadi (Ratings Analysis)**

1️⃣ **Certain genres, such as RPG and FPS, inherently receive higher ratings due to immersive gameplay.**  
   🌍 *Elaboration:* RPGs and FPS games often provide detailed world-building, rich storytelling, and engaging mechanics that resonate with players. These genres consistently outperform others, such as casual or puzzle games, in terms of user ratings.  

2️⃣ **Cooperative and multiplayer games are rated more positively compared to single-player experiences.**  
   👫 *Elaboration:* Social interaction in cooperative or multiplayer games significantly enhances user satisfaction. Players enjoy sharing achievements and competing with friends, which drives higher ratings compared to solo experiences.

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
