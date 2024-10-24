# Russian Verb Conjugator

**Russian Verb Conjugator** is a console-based tool designed to help students of the Russian language learn verbs and their conjugations. Simply input a verb in Russian, and the program will return its meaning and a full conjugation table, including present, past, and future tenses.

## Features
- Accepts Russian verbs in any case (upper or lowercase).
- Returns the meaning and full conjugation of the verb.
- Reads a CSV file containing valid Russian verbs and their meanings.
- Scrapes [Master Russian](http://masterrussian.com/verbs/conjugations.htm) to display the conjugation table for each verb.
- Handles invalid input and prompts the user for a new verb.

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/russian-verb-conjugator.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd russian-verb-conjugator
   ```
3. Ensure you have the `russian_verbs.csv` file in the directory.
4. Install required dependencies (if not already installed):
   ```bash
   pip install pandas
   ```
5. Run the program:
   ```bash
   python russian-verb-conjugator.py
   ```
6. Input a Russian verb, and get the meaning and conjugation!


## CSV Structure

Ensure your `russian_verbs.csv` has the following structure:

| Verb   | Meaning       | URL                            |
|--------|---------------|---------------------------------|
| делать | to do         | conjugations.htm               |
| писать | to write      | conjugations.htm               |

## Tech Stack
- Python
- Pandas for web scraping
- CSV for data handling

## Future Improvements
- Add error handling for web scraping failures.
- Implement additional features like adding new verbs or conjugations from the console.

