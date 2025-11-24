# Case Study Write-Up

## **1) Executive Summary**
**Problem**: Many people struggle to quickly find a movie that aligns with their content preferences, as it can be time-consuming to parse through long lists. The same is true for analysts or web developers who are examining film popularity to complete a large analysis or create a dashboard.

**Solution**: I created an app that organizes movie data to create structured lists based on what the user wants to see. The app lists the Top 20 Highest-Grossing Movies of 2016 and allows users to search by movie title and filter by genre, IMDB rating, and MPAA rating. The interactive user interface involves a search bar and multiple dropdown menus. This searching and filtering can be used to create a curated movie collection or analyze box office trends. The app is packaged so that it can run anywhere, enhancing accessibility and convenience.

## **2) System Overview**
**Course Concept**: This project demonstrates a containerized Flask API.

**Architecture Diagram**: 

<img src="https://image2url.com/images/1763953344612-8e6e3ace-779d-4e17-abd4-e48963a3c275.png" width="700" />

**Data/Models/Services**: The Flask Web Service is used to serve the API. My dataset was manually curated and sourced from a publicly available IMDb web page and its attached CSV file: [link to dataset](https://www.imdb.com/list/ls031261985/). The file is JSON and is 4 KB. The data was collected for educational use under Fair Use guidelines. 

## **3) How to Run (Local)**
**Docker**: 
```{python}
# build
docker build -t movies-api:latest .
# run
docker run --rm -p 5000:5000 movies-api:latest
# health check
curl http://localhost:5000/movies
```

## **4) Design Decisions**
**Why this concept?**: I thought about making an API that processes data like numbers or text and computes statistics, but I wanted to create something that demonstrates filtering logic and returns a structured dataset. I also considered using a CSV file instead of JSON, but I chose JSON because it is better for hierarchical data and works better with a web API.

**Tradeoffs**: This app has no costs since it does not use a paid API or database. The process of reading the JSON file is basically instantaneous for datasets under a few thousand records. For much larger datasets though, it wouldn’t be as efficient. Additionally, because the data is JSON, it is easy to update manually. However, this wouldn't be ideal for long-term maintainability in a real production system. 

**Security/Privacy**:  This app does not require API keys, authentication tokens, or passwords, so a .env file is optional. The query parameters (title, genre, IMDb rating, and MPPA rating) are sanitized by being converted to strings, and numerical fields are validated. The dataset used is publicly available and does not contain any personally identifiable information. 

**Ops**: Flask’s default development logs provide basic response visibility and are sufficient for this app. There is no metrics framework, but the /health endpoint supports basic checks while the app runs. The app is designed for a single user. Scaling horizontally would require more servers and containers to handle the increased requests. The current limitations are that the JSON file must be able to fit into the API's memory and that the filtering system is simple and not optimized for a much larger dataset. 

## **5) Results & Evaluation**
In terms of performance, the API successfully serves and filters the JSON movie dataset with fast responses. The validation consists of a health check to confirm that the server is running and a smoke test to ensure that the /movies endpoint results in a successful response. Screenshots of the endpoint checks and smoke test cann be found in /assets.

## **6) What's Next**
Future improvements and refactors could involve creating more filtering and search options, expanding the dataset, or having multiple datasets from different years. This would allow for deeper analyses and comparisons to be made. Additional stretch features could include allowing users to create accounts or bookmark movie collections.
