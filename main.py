# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import time


# Function to scrape team data and write to 'teams.txt' file
def teams():
    # List of NHL team abbreviations
    teams = ['BOS', 'TOR', 'TBL', 'FLA', 'BUF', 'OTT', 'DET', 'MTL', 'COL', 'DAL', 'MIN', 'WPG', 'NSH', 'STL', 'ARI',
             'CHI', 'CAR', 'NJD', 'NYR', 'NYI', 'PIT', 'WSH', 'PHI', 'CBJ', 'VEG', 'EDM', 'LAK', 'SEA', 'CGY', 'VAN',
             'SJS', 'ANA']

    # Open 'teams.txt' file for writing
    file = open('teams.txt', 'w', encoding='utf-8')

    # Loop through years (2010 to 2019)
    for year in range(2010, 2020):
        # Loop through NHL teams
        for i in range(len(teams)):
            # Construct the URL for team data
            url1 = 'https://www.hockey-reference.com/teams/'
            url2 = '.html'
            url = url1 + str(teams[i]) + '/' + str(year) + url2

            # Send a request to the URL and parse the content
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            time.sleep(3)  # Pause for 3 seconds to avoid rate limiting

            # Write data to 'teams.txt' file
            file.write("sezonarok:" + str(year) + "\n" + "sezonatim:" + str(teams[i]) + "\n" + soup.text.strip() + '\n')
            print(f'All text data from {url} extracted and appended to teams.txt.')
            print(teams[i])


# Function to scrape season data and write to 'seasons.txt' file
def seasons():
    # Loop through years (2010 to 2019)
    for i in range(2010, 2020):
        # Construct the URL for season data
        url1 = 'https://www.hockey-reference.com/leagues/NHL_'
        url2 = '.html#all_stats'
        url = url1 + str(i) + url2

        # Send a request to the URL and parse the content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        time.sleep(3)  # Pause for 3 seconds to avoid rate limiting

        # Open 'seasons.txt' file for appending
        with open('seasons.txt', 'a', encoding='utf-8') as file:
            for element in soup.find_all(True):
                file.write(element.text + '\n')  # Write only the text content of the HTML element

        print(f'All text data from {url} extracted and appended to seasons.txt.')

        # Call the teams function for each year
        teams(i)


# Main function to execute the scraping process
def main():
    # Clear the content of the 'output.txt' file before starting the loop
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write('')

    # Call the seasons function
    seasons()


# Execute the teams function independently
teams()
