# Sales Data Cleaner

## Project Title & Goal  
A simple Python project that cleans messy sales data from a CSV file and converts it into a structured JSON report.

---

## Setup Instructions  
Make sure Python is installed on your system, then open the project folder in terminal and run:

```bash
python main.py
After running the script, a new file called clean_sales.json will be generated.

The Logic (How I thought)
I approached this problem by first understanding what the input data looked like and what output was expected.

My solution works like this:

Read the data from sales.csv using Python’s built-in csv module

Clean the fields by removing unwanted characters like $ and extra quotes

Convert the price from USD to INR using the rate (1 USD = 83 INR)

Remove duplicate entries using a set (based on product name and price)

Store the final cleaned data into a JSON file using the json module

The hardest bug I faced:
At one point, my output file was always empty even though the program was running without errors.
After debugging, I realized that my data was saved in the wrong file (sales.csv.txt instead of sales.csv).
Fixing the file name and format solved the issue, and it taught me the importance of paying attention to file handling.

