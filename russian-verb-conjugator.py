import csv
import pandas as pd
from tabulate import tabulate

class Dictionary:
    def __init__(self):
        """Initialize the Dictionary with empty dictionaries for meanings and URLs."""
        self.meaning = {} 
        self.url = {} 
    
    def create_dictionary(self):
        """Create the dictionary by reading from a CSV file containing Russian verbs, their meanings, and URLs."""
        with open('russian_verbs.csv', newline='', encoding='utf8') as csvfile: 
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Update the meaning and URL dictionaries with the verb as the key
                self.meaning.update({row['\ufeffVerb']: row['Meaning']})
                self.url.update({row['\ufeffVerb']: row['URL']})

    def validate_verb(self, verb):
        """
        Validate if the verb exists in the dictionary.
        
        Args:
            verb (str): The verb to validate.
        
        Returns:
            str: The meaning of the verb if it exists, otherwise None.
        """
        self.verb = verb
        return self.meaning.get(self.verb)

    def print_meaning(self):
        """Print the meaning of the validated verb."""
        print(f'{self.verb} >>> means >>> {self.meaning.get(self.verb)}')
    
    def print_conjugation(self):
        """Print the conjugation tables for the validated verb."""
        df = pd.read_html('http://masterrussian.com/verbs/' + self.url.get(self.verb))

        print('\n')
        print('Conjugation Table')

        # Display the conjugation table with tabulate formatting
        print(tabulate(df[1], headers='keys', tablefmt='grid', showindex=False))  # Conjugation table
        print('\n')
        print('Present Tense')
        print(tabulate(df[3], headers='keys', tablefmt='grid', showindex=False))  # Present tense table
        print('\n')
        print('Past Tense')
        print(tabulate(df[4], headers='keys', tablefmt='grid', showindex=False))  # Past tense table
        print('\n')
        print('Future Tense')
        print(tabulate(df[5], headers='keys', tablefmt='grid', showindex=False))  # Future tense table
        print('\n')

# Main execution
verb = input('Enter your verb: ').lower()
dictionary = Dictionary()
dictionary.create_dictionary()
validation = dictionary.validate_verb(verb)

# Loop until a valid verb is entered
while validation is None:
    print("Your verb is not valid.")
    verb = input('Enter your verb: ').lower()
    validation = dictionary.validate_verb(verb)

# Print the meaning and conjugation of the valid verb
dictionary.print_meaning()
dictionary.print_conjugation()