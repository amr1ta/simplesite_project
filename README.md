# Web application testing using pytest and selenium following Page Object Model Framework

### Target Application: https://mystifying-beaver-ee03b5.netlify.app/


## Run using Github-Actions
- Browse to https://github.com/amr1ta/simplesite_project/actions/workflows/python-app.yml
- Press *Run workflow*

## Run Locally
```
pip3 install -r requirements.txt
pytest -s --browser chrome --mode headless
```

## Test Scenarios Covered

**Scenario 1**: Verifying that a selected column is sorted from low to high

Supported columns for sorting: **NUMBER OF CASES**, **AVERAGE IMPACT SCORE**

Steps:
1. load url
2. From "Sort data" drop down, select the Column name passed as parameters
3. fetch the column data
4. expand to numbers in case ending with 'k', 'M' or 'B'
5. assert the column is sorted in ascending order


**Scenario 2**: Verifying if a string matches values in the NAME and COMPLEXITY columns, the corresponding rows are returned and other rows are filtered out

Steps:
1. load url
2. Insert string passed as parameters in "Filter data" text box
3. fetch values of NAME column
4. fetch values of COMPLEXITY column
5. combined cells from NAME and COMPLEXITY columns into tuples
6. assert the filter test criteria is available in any of the tuple values irrespective of case sensitivity


**Scenario 3**: Verifying if a string does not match values in the NAME and COMPLEXITY columns, all  rows are filtered out

Steps:
1. load url
2. Insert string passed as parameters in "Filter data" text box
3. store NAME column details
4. assert that no rows are returned for non existing criterias


## Test Environment

- OS: Ubuntu 18.04
- Python version: 3.6 and above
- Libraries:

    ```
    pytest==6.2.5
    selenium==3.141.0
    webdriver-manager==3.4.2
    ```
- Browser: Google Chrome=93.0.4577.63