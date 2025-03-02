# 🎬 Movie Recommender System Using Machine Learning

## 📌 Dataset Used:
[TMDb Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## 📌 Concept Used: Cosine Similarity

1. **Cosine Similarity** measures the similarity between two vectors (documents/movies) based on their angle.
2. It is a value between **0 and 1**:
   - **0**: Completely different
   - **1**: Completely similar
3. Used in recommendation systems to find movies with similar features.
4. More details: [Cosine Similarity Explanation](https://www.learndatasci.com/glossary/cosine-similarity/)

## 🚀 How to Run?

### 📥 Clone the Repository
```bash
https://github.com/rkdsai/Movie-Recommender.git
```

### 🛠 Step 1: Create a Virtual Environment
```bash
conda create -p venv python=3.10 -y
conda activate venv/
```

### 📦 Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔑 Step 3: Set Up API Key in `.env`
1. Create a `.env` file in the root directory.
2. Add your **TMDb API Key** inside it:
```bash
TMDB_API_KEY=your_tmdb_api_key_here
```

### 🏗 Step 4: Generate Models
Run the Jupyter notebook to preprocess data and generate models:
```bash
jupyter notebook movie_recommendation.ipynb
```

### 🚀 Step 5: Run the Streamlit App
```bash
streamlit run app.py
```

## 🔗 How to Use TMDb API in Code
Update the `fetch_poster()` function to load API key from `.env`:

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500/{data.get('poster_path', '')}"
```

## 📧 Author
**Ravi Kiran**  
📩 Email: ravikiran058@gmail.com  
💼 Role: Data Scientist  

