# 🎬 Movie Recommendation System  

A simple **content-based movie recommendation system** built with **Python, Pandas, and Scikit-learn**.  
It recommends movies similar to a user-provided movie title using **TF-IDF (Term Frequency–Inverse Document Frequency)** and **Cosine Similarity**.  

---

## 🚀 Features  
- Recommend top **N similar movies** to the one entered by the user.  
- Uses **movie overview, genres, and keywords** for similarity.  
- **Interactive** → takes movie name as input.  
- Lightweight, fast, and easy to run.  

---

## 🛠️ Tech Stack  
- Python 3.x  
- Pandas  
- Scikit-learn  

---

## 📂 Dataset Requirement
This project uses the [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).  
Download `tmdb_5000_movies.csv` and place it in the project folder.  

---

## ⚡ Installation  

Clone this repo and install dependencies:  
```bash
git clone https://github.com/ShivamQx/Movie-Predict.git
cd Movie-Predict
pip install -r requirements.txt
```

---

## ▶️ Usage  

Run the Python script:  
```bash
python app.py
```

Enter a movie name when prompted, e.g.:  
```
Enter a movie name: Avatar
```

Output:  
```
Recommended Movies:
- Guardians of the Galaxy
- John Carter
- Star Trek
- The Fifth Element
- The Matrix
```

---

## 📊 How It Works  
1. **Preprocessing**: Combine overview, genres, and keywords into a single text field.  
2. **TF-IDF Vectorization**: Convert text into numerical vectors.  
3. **Cosine Similarity**: Measure similarity between movies.  
4. **Recommendation**: Return top 5 most similar movies.  

---

## 📌 Future Improvements  
- Make search **case-insensitive**.  
- Build a **Streamlit/Flask web app interface**.  
- Add **user ratings (hybrid recommendation system)**.  

---

## 👨‍💻 Author  
Developed with ❤️ by [ShivamQx](https://github.com/ShivamQx).  
