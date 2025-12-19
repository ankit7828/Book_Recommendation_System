# Book_Recommendation_System

# Project Overview

The Book Recommendation System is a web-based machine learning application that recommends relevant books to users based on a given book title. The system combines Popularity-Based Filtering and Collaborative Filtering techniques to generate accurate and meaningful recommendations. Users simply enter the name of a book, and the system suggests four similar books, helping them discover new titles based on user preferences and overall popularity trends.

Live Demo: https://web-production-7ff6.up.railway.app/  

# Objectives

To build an intelligent recommendation system using real-world datasets
To help users discover books similar to their interests
To combine popularity-based and collaborative filtering approaches
To deploy the model as an interactive web application

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
