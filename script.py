import sqlite3
import json
import argparse
import os 
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join



# Define the table names
TABLE_TWEET = 'tweet'
TABLE_TWEET_MEDIA = 'tweet_media'
TABLE_TWEET_URL = 'tweet_url'

# Function to extract sqlite's data
def sqlite_data_extractor(table_name, archive_path, output_format='json'):
    # Connect to the sqlite database
    sqlite_db_path = os.path.join(archive_path, 'data.sqlite3')
    con = sqlite3.connect(sqlite_db_path)
    cur = con.cursor()

    cur.execute(f"SELECT * FROM {table_name}")
    cols = [description[0] for description in cur.description]
    rows = cur.fetchall()
    
    # Create a list of dictionaries for each row in the table
    tweet_data = [dict(zip(cols, row)) for row in rows]

    data_json = {
        'tweet': tweet_data
    }

    # Output file name
    output_filename = 'sqlite_extracted_data.json'

    # Writing the data to a JSON file
    if output_format == 'json':
        print("hey")
        with open(output_filename, 'w') as json_file:
            json.dump(data_json, json_file, indent=4)

    print(f"sqlite data extraction completed and stored in {output_filename}")
    
    con.close()
    

# Function to extract html's data
def html_data_extractor(archive_path):
    # html files path
    # html_file_path = os.path.join(archive_path, "Archived Tweets") 

    # onlyfiles = [f for f in listdir(html_file_path) if isfile(join(html_file_path, f))]

    # # Reading the html contents
    # for html_file in onlyfiles:
    #     tweet_file_path = os.path.join(html_file_path, html_file)

    #     # Storing the content of the file
    #     content = ""

    #     with open(tweet_file_path) as sf:
    #         for line in sf:
    #             content += line
        
    #     soup = BeautifulSoup(content, "lxml")

    #     user_logo_src = soup.select_one('img.css-9pa8cd').get('src')
    #     user_name = soup.find('div', {'data-testid': 'User-Name'}).find('span').text 
    #     print(user_name)
    pass


    

# Main function to extract data
def main():
        parser = argparse.ArgumentParser(description="Extract data from HTML and SQLite and export to JSON.")
        parser.add_argument('--file', type=str, help="Path to the archive folder", required=False)
        parser.add_argument('--output', type=str, help="Output JSON file", required=False)

        args = parser.parse_args()
        
        if args.file:
            sqlite_data_extractor(TABLE_TWEET_URL, args.file)

        if args.file:
            html_data_extractor(args.file)
        

if __name__ == "__main__":
    main()