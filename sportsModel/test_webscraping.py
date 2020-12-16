from selenium import webdriver
import json
import requests
from bs4 import BeautifulSoup
import time
from csv import writer


team_handles_dict = {'Toronto Raptors': 'TOR',
          'Boston Celtics': 'BOS',
          'Philadelphia 76ers': 'PHI',
          'Cleveland Cavaliers': 'CLE',
          'Indiana Pacers': 'IND',
          'Miami Heat': 'MIA',
          'Milwaukee Bucks': 'MIL',
          'Washington Wizards': 'WAS',
          'Detroit Pistons': 'DET',
          'Charlotte Hornets': 'CHO',
          'Charlotte Bobcats': 'CHA',
          'New York Knicks': 'NYK',
          'Brooklyn Nets': 'BRK',
          'Chicago Bulls': 'CHI',
          'Orlando Magic': 'ORL',
          'Atlanta Hawks': 'ATL',
          'Houston Rockets': 'HOU',
          'Golden State Warriors': 'GSW',
          'Portland Trail Blazers': 'POR',
          'Oklahoma City Thunder': 'OKC',
          'Utah Jazz': 'UTA',
          'New Orleans Pelicans': 'NOP',
          'San Antonio Spurs': 'SAS',
          'Minnesota Timberwolves': 'MIN',
          'Denver Nuggets': 'DEN',
          'Los Angeles Clippers': 'LAC',
          'Los Angeles Lakers': 'LAL',
          'Sacramento Kings': 'SAC',
          'Dallas Mavericks': 'DAL',
          'Memphis Grizzlies': 'MEM',
          'Phoenix Suns': 'PHO'}
home_away_dict = {0: 'away', 1: 'home'}

#season_page = requests.get(f'https://www.basketball-reference.com/teams/{team_handle}/{year}_games.html')
#season_page = BeautifulSoup(season_page.text, 'html.parser')
response = requests.get ('https://www.basketball-reference.com/teams/LAL/2020_games.html')
soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='overthrow table_container')

for post in posts:
	title = post.find(class_='poptip sort_default_asc left').get_text().replace('\n', '')
	print(title)
	#opponent = post.find_all(class_='')

"""
with open('posts.csv', 'w') as csv_file:
	csv_writer = writer(csv_file)
	headers = ['Title', 'Link', 'Date']
	csv_writer.writerow(headers)
   	season_page = requests.get(f'https://www.basketball-reference.com/teams/LAL/2020_games.html')


/html/body/div[2]/div[5]/div[3]/div[2]/div/table/thead/tr/th[7]
<th aria-label="Opponent" data-stat="opp_name" scope="col" class=" poptip sort_default_asc left">Opponent</th>
"""