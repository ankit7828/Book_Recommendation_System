<img width="1891" height="901" alt="image" src="https://github.com/user-attachments/assets/908fabdb-f0a1-4a9d-b0b3-042318167ef9" /># Book_Recommendation_System

# Project Overview

The Book Recommendation System is a web-based machine learning application that recommends relevant books to users based on a given book title. The system combines Popularity-Based Filtering and Collaborative Filtering techniques to generate accurate and meaningful recommendations. Users simply enter the name of a book, and the system suggests four similar books, helping them discover new titles based on user preferences and overall popularity trends.

Live Demo: https://web-production-7ff6.up.railway.app/  

# Objectives

To build an intelligent recommendation system using real-world datasets
To help users discover books similar to their interests
To combine popularity-based and collaborative filtering approaches
To deploy the model as an interactive web application

# Installation and Setup
## 1. Clone the repository
git clone https://github.com/Riya29Mehta/book-recommender.git
cd book-recommender
## 2. Install the dependencies
pip install -r requirements.txt

## 3. Run the Flask app
python app.py

## 4. Open in browser
http://127.0.0.1:5000/

# Datasets Used
The project uses three datasets:
## 1. Books Dataset
Book title ,
Author ,
Image URLs ,
ISBN

## 2. Users Dataset
User ID ,
Location ,
Age

## 3. Ratings Dataset
User ID ,
Book ISBN ,
Book Rating

Dataset link: https://www.kaggle.com/datasets/saurabhbagchi/books-dataset  
These datasets are preprocessed and merged to build a reliable recommendation pipeline.

# System Architecture
User enters a book title through the web interface  
Flask backend receives the input  
Recommendation model processes the request  
System returns four recommended books with relevant details  

# Recommendation Techniques Used
## 1. Popularity-Based Recommendation
Recommends books based on:  
Number of ratings  
Average rating score  

## 2. Collaborative Filtering
Uses user-book interaction data  ,
Builds a pivot table of users vs books  ,
Computes similarity between books using cosine similarity  ,
Recommends books similar to the input title  ,
Both techniques together improve accuracy and diversity of recommendations.

# Technology Stack
## 1. Backend
Python  ,
Flask  ,
NumPy  ,
Pandas  ,
Pickle

## 2. Frontend
HTML  ,
CSS  ,
JavaScript

# Model & Data Handling
Pickle for saving trained models  
Preprocessed similarity matrices  

# Key Features
User-friendly web interface  ,
Fast recommendation generation  ,
Accurate similarity-based suggestions  

# Implementation Details
Data cleaning and preprocessing performed using Pandas  ,
Similarity matrix generated using cosine similarity  ,
Model artifacts stored as .pkl files  ,
Flask routes handle user requests and responses  ,
HTML templates used for frontend rendering

# Results
The system successfully recommends four relevant books for a given input  ,
Combines both personalized and generic recommendations  ,
Ensures meaningful output even with sparse data  

# Future Enhancements
Add user login and personalized profiles  ,
Include content-based filtering  ,
Deploy the application on cloud platforms  ,
Improve UI with advanced frontend frameworks  ,
Add recommendation explanation features

# Conclusion
The Book Recommendation System demonstrates the effective use of machine learning techniques to solve a real-world problem. By integrating popularity-based and collaborative filtering approaches, the system provides accurate and useful recommendations while maintaining a smooth user experience. This project highlights strong skills in data preprocessing, machine learning, and full-stack web development.

<img width="1896" height="906" alt="Screenshot 2025-12-19 221935" src="https://github.com/user-attachments/assets/da58a8cb-8a7d-4918-8015-1fd852656539" />

<img width="1891" height="901" alt="Screenshot 2025-12-19 222016" src="https://github.com/user-attachments/assets/071bb365-8336-48c6-b3a5-a6456c9620b0" />

