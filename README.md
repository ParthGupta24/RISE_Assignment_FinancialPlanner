# Financial Planner
---
This is a simple financial planner which allows a user to plan out activites from a pool of available ventures, based on their budget. For the purpose of demonstration, This project uses an integrated dataset generator which randomly generates a new dataset, customised by the user.<br><br>

### Prerequisites:<br>
- Python 3.12 or above <br>
- Streamlit <br>
`pip install streamlit`<br>
- Numpy (Typically installed with Streamlit)<br>
`pip install numpy`<br>
- Pandas (Typically installed with Streamlit)<br>
`pip install pandas`<br>
- In case of any errors with a specific package, user can run<br>
`pip install --upgrade <package name>`<br><br>

### Deliverables:<br>
- app.py: Main logic for the application<br>
- datagen.py: Dataset generator. Can be loosely controlled using app.py<br>
- dataset.csv: Holds the Activities dataset<br><br>

### Usage:<br>
1. Enter the working directory of this Project in your terminal/Command prompt. Current working directory can be seen as the file path in terminal prompt.<br>
2. Enter this command:<br>
`streamlit run app.py`<br>
(In case you change the name of "app.py" file, change the command to `streamlit run <filename>`)