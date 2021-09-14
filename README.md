# Web application testing using pytest and selenium following Page Object Model Framework

### Target Web Application: https://mystifying-beaver-ee03b5.netlify.app/


## Instructions to execute

### Using Github-Actions
- Fork the project
- Browse to https://github.com/##USERNAME##/simplesite_project/actions/workflows/python-app.yml
- Press *Run workflow*

### Run Locally
```
pip3 install -r requirements.txt
pytest -s --browser chrome --mode headless
```

## Test Scenarios Covered

**Scenario 1**: Verify that a selected column is sorted from low to high

Supported columns for sorting: **NUMBER OF CASES**, **AVERAGE IMPACT SCORE**

Steps:
1. Open homepage url
2. From "Sort data" drop down, select the Column name passed as parameters
3. fetch the column data
4. expand to numbers in case ending with 'k', 'M' or 'B'
5. assert the column is sorted in ascending order


**Scenario 2**: Verify if a string matches values in the NAME and COMPLEXITY columns, the corresponding rows are returned and other rows are filtered out

Steps:
1. Open homepage url
2. Insert string passed as parameters in "Filter data" text box
3. fetch values of NAME column
4. fetch values of COMPLEXITY column
5. combined cells from NAME and COMPLEXITY columns into tuples
6. assert the filter test criteria is available in any of the tuple values irrespective of case sensitivity


**Scenario 3**: Verify if a string does not match values in the NAME and COMPLEXITY columns, all  rows are filtered out

Steps:
1. Open homepage url
2. Insert string passed as parameters in "Filter data" text box
3. store NAME column details
4. assert that no rows are returned for non existing criterias


**Scenario 4**: Verify combination of sorting first followed by filtering, the filtered columns should still be sorted

Steps:
1. Open homepage url
2. Sort table by Impact score column
3. Enter filter text (e.g "high") in the "Filter data" text box
4. assert that "AVERAGE IMPACT SCORE" column is sorted and COMPLEXITY column contains only filter text. 


**Scenario 5**: Verify combination of filtering first followed by sorting, the filtered columns should still be sorted

Steps:
1. Open homepage url
2. Enter filter text (e.g "ack") in the "Filter data" text box
3. Sort table by Number of cases score column
4. assert that "NUMBER OF CASES" column is sorted and NAME column contains only filter text. 


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