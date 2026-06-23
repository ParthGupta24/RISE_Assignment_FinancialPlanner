# Financial Planner
---
This is a simple financial planner which allows a user to plan out activites from a pool of available ventures, based on their budget. For the purpose of demonstration, This project uses an integrated dataset generator which randomly generates a new dataset, customised by the user.

### Prerequisites:
- Python 3.12 or above
- Streamlit
`pip install streamlit`
- Numpy (Typically installed with Streamlit)
`pip install numpy`
- Pandas (Typically installed with Streamlit)
`pip install pandas`
- In case of any errors with a specific package, user can run
`pip install --upgrade <package name>`

### Deliverables:
- app.py: Main logic for the application
- datagen.py: Dataset generator. Can be loosely controlled using app.py
- dataset.csv: Holds the Activities dataset