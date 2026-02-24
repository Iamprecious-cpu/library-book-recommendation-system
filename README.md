# 📚 Book Recommendation System (Computer Science Library)

## 🚀 Overview
## 🎯 Problem Statement
## 🧠 How It Works
## 🏗️ System Architecture
## 🛠️ Tech Stack
## 📊 Dataset
## 🔍 Algorithm Details
## 📈 Evaluation Metrics
## 💻 Installation & Setup
## 🖥️ How to Use
## 🧪 Sample Output
## 📌 Limitations
## 🔮 Future Improvements
## 🤝 Contributing
## 📜 License

###📚 CS Library Book Recommender
####🚀 Overview

This project implements an item-based collaborative filtering system that recommends similar Computer Science books and displays their physical location within a departmental library.

The system improves discoverability and resource utilization in an academic library setting.

###🎯 Problem Statement

Students interact with only a small fraction of available library books due to:

Limited exposure to relevant materials

Inefficient search processes

Absence of structured recommendation support

This system addresses underutilization by ranking and recommending books based on user rating similarity.

###🧠 Methodology
####1️⃣ Data Collection

Departmental book inventory

Ratings datasets sourced from:

Kaggle

LibraryThing

Goodreads

Since student borrowing ratings were unavailable, external rating data was used.

####2️⃣ Data Preprocessing

Merged book and rating datasets

Removed unnecessary columns

Created User × Book pivot matrix

Handled missing values using Pandas

3️⃣ Dimensionality Reduction

Applied Singular Value Decomposition (SVD) to:

Reduce matrix dimensionality

Extract latent features (concepts)

Improve computational efficiency

SVD decomposes the rating matrix into three matrices:

User → Concept

Concept

Concept → Book

Latent features represent hidden relationships between books (e.g., writing style, topic similarity).

4️⃣ Similarity Computation

Used Pearson Correlation Coefficient to compute similarity between book vectors.

Formula:

r = Σ[(Xi - X̄)(Yi - Ȳ)] / √(Σ(Xi - X̄)² Σ(Yi - Ȳ)²)

Higher correlation → stronger similarity → better recommendations.

5️⃣ Recommendation Pipeline

User searches for a book

System locates book index

Retrieves similarity scores

Filters highly correlated books

Returns Top 5 recommendations

Displays physical library location

🏗️ System Architecture

Data Layer (CSV storage)

Processing Layer (Pandas + NumPy + SVD)

Similarity Engine (Correlation Matrix)

Web Interface (Flask)

<img width="1353" height="689" alt="Screenshot 2026-02-24 093237" src="https://github.com/user-attachments/assets/ae0e9d96-ad48-4176-ae79-c7acc48f4e6f" />

Runs locally at:
http://127.0.0.1:5000

🛠️ Tech Stack

Python

Pandas

NumPy

Flask

HTML / CSS

Bootstrap

📊 Evaluation Metrics
Mean Absolute Error (MAE)

Best MAE: 3.8285 (90% training split)

Indicates accurate rating prediction

Recall

High recall indicates effective retrieval of relevant books

Demonstrates strong recommendation coverage

📌 Limitations

No real student borrowing history

Internet access required

Limited to Computer Science departmental collection

🔮 Future Improvements

Integrate real borrowing & rating system

Expand beyond CS department

Add hybrid recommendation (content + collaborative)
 
Improve scalability for large user base


Deploy to cloud infrastructure
