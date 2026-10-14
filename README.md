# 📚 CS Library Book Recommender
 
An item-based collaborative filtering system that recommends similar Computer Science books and shows where each one sits in the departmental library.


---
 
## Table of Contents
 
1. [Problem Statement](#problem-statement)
2. [How It Works](#how-it-works)
3. [System Architecture](#system-architecture)
4. [Tech Stack](#tech-stack)
5. [Dataset](#dataset)
6. [Evaluation](#evaluation)
7. [Installation & Setup](#installation--setup)
8. [Usage](#usage)
9. [Limitations](#limitations)
10. [Future Improvements](#future-improvements)
11. [License](#license)
---
 
## Problem Statement
 
Students interact with only a small fraction of the books a departmental library holds, because of:
 
- Limited exposure to relevant materials
- Inefficient search
- No structured recommendation support
This project addresses that underutilization by ranking and recommending books based on rating similarity, and by telling the student exactly where to find each book on the shelf.
 
## How It Works
 
**1. Data collection**
- Departmental book inventory
- Ratings from Kaggle, LibraryThing and Goodreads (student borrowing ratings were not available, so external rating data was used)
**2. Preprocessing**
- Merged the book and rating datasets
- Dropped unnecessary columns
- Built a User × Book pivot matrix
- Handled missing values with Pandas
**3. Dimensionality reduction (SVD)**
 
Singular Value Decomposition factorizes the rating matrix into three matrices (User → Concept, Concept, Concept → Book). This reduces dimensionality, extracts latent features such as topic similarity, and improves computational efficiency.
 
**4. Similarity computation**
 
Pearson correlation between book vectors:
 
```
r = Σ[(Xi − X̄)(Yi − Ȳ)] / √(Σ(Xi − X̄)² · Σ(Yi − Ȳ)²)
```
 
Higher correlation means stronger similarity.
 
**5. Recommendation pipeline**
 
1. User searches for a book
2. System locates the book's index
3. Retrieves its similarity scores
4. Filters for highly correlated books
5. Returns the top 5 and displays each book's physical library location
## System Architecture
 
| Layer | Component |
|---|---|
| Data | CSV files |
| Processing | Pandas, NumPy, SVD |
| Similarity engine | Correlation matrix |
| Web interface | Flask |
 
## Tech Stack
 
Python · Pandas · NumPy · Flask · HTML/CSS · Bootstrap
 
## Dataset
 
| Source | Used for |
|---|---|
| Departmental inventory | Book titles and shelf locations |
| Kaggle / LibraryThing / Goodreads | User ratings |
 
<!-- Name the exact datasets (with links) and the size of the final matrix: users × books. -->
 
## Evaluation
 
| Metric | Result | Notes |
|---|---|---|
| MAE | 3.8285 | Best result, at a 90% training split |
| Recall | [add value] | |
 
<!-- State the rating scale next to the MAE so readers can judge it. -->
 
## Installation & Setup
 
```bash
git clone https://github.com/Iamprecious-cpu/library-book-recommendation-system.git
cd library-book-recommendation-system
 
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
 
pip install -r requirements.txt
python recwebapp.py
```
 
Then open <http://127.0.0.1:5000>.
 
## Usage
 
1. Open the app in your browser.
2. Search for a Computer Science book by title.
3. View the top 5 similar books and their location in the library.
### Sample output
 
```
Search: [book title]
1. [Recommended book]   Shelf: [location]
2. ...
```
 
## Limitations
 
- No real student borrowing history; ratings come from external sources
- Limited to the Computer Science departmental collection
- Internet access required [explain why, or remove this line]
## Future Improvements
 
- Integrate a real borrowing and rating system
- Expand beyond the CS department
- Add a hybrid approach (content + collaborative)
- Improve scalability for larger user bases
- Deploy to cloud infrastructure
## License
 
Released under the [MIT License](LICENSE).
