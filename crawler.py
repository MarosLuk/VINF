import re
import csv


def seasons():
    # Define input and output file names
    sezony = 'seasons.txt'
    output_file1 = 'seasons_clear.txt'

    # Define start and end markers for the first section
    prve_zaciatok = 'Eastern Conference \n'
    prve_koniec = 'Goals For/Against include shootout wins/losses, and may not match actual goal totals shown elsewhere.\n'

    # Initialize variables
    appender = 0
    counter = 0

    # Open input and output files
    subor_sezony = open(sezony, 'r')
    subor_data_sezony = open(output_file1, 'w', encoding='utf-8')

    try:
        for riadok in subor_sezony:
            counter += 1

            # Check if the current line is the start of the first section
            if prve_zaciatok == riadok:
                appender = 1

            # Check if the current line is the end of the first section
            if prve_koniec == riadok:
                appender = 0

            # Append lines to the output file if the appender is active
            if appender == 1:
                subor_data_sezony.write(riadok)
    except:
        pass


def seasons1():
    # Define input and output file names
    sezony = 'seasons_clear.txt'
    output_file2 = 'seasons_clear1.txt'

    # Define start and end markers for the second section
    prve_zaciatok = 'Atlantic Division'
    prve_koniec = 'Western Conference \n'
    druhe_zaciatok = 'Central Division'
    druhe_koniec = 'Eastern Conference \n'

    # Initialize variables
    appender = 0
    counter = 0

    # Open input and output files
    subor_sezony = open(sezony, 'r')
    subor_data_sezony = open(output_file2, 'w', encoding='utf-8')

    for riadok in subor_sezony:
        counter += 1

        # Check if the current line is the start of the first section
        if prve_zaciatok in riadok:
            appender = 1

        # Check if the current line is the end of the first section
        if prve_koniec == riadok:
            appender = 0

        # Check if the current line is the start of the second section
        if druhe_zaciatok in riadok:
            appender = 1

        # Check if the current line is the end of the second section
        if druhe_koniec == riadok:
            appender = 0

        # Write specific lines to the output file
        if "EAS Standings" in riadok:
            subor_data_sezony.write("\n")
            subor_data_sezony.write(riadok)

        if "WES Standings" in riadok:
            subor_data_sezony.write("\n")
            subor_data_sezony.write(riadok)

        # Append lines to the output file if the appender is active
        if appender == 1:
            if len(riadok) > 35:
                subor_data_sezony.write(riadok)


def seasons2():
    # Define input and output file names
    sezony = 'seasons_clear1.txt'
    output_file = 'seasons_clear2.txt'

    # Open input and output files
    subor_sezony = open(sezony, 'r')
    subor_data_sezony = open(output_file, 'w', encoding='utf-8')

    for riadok in subor_sezony:
        # Remove '*' character from the lines
        if "*" in riadok:
            a = riadok.split("*")
            b = a[0] + a[1]
            subor_data_sezony.write(b)
        else:
            subor_data_sezony.write(riadok)

    # Close and reopen the file for further processing
    subor_data_sezony.close()
    subor_data_sezony = open(output_file, 'w', encoding='utf-8')


def seasons3():
    # Define input and output file names
    sezony = 'seasons_clear2.txt'
    output_file = 'seasons_final.txt'

    # Open input and output files
    subor_sezony = open(sezony, 'r')
    subor_data_sezony = open(output_file, 'w', encoding='utf-8')

    for riadok in subor_sezony:
        if len(riadok) > 35:
            # Use regular expression to extract specific parts of the line
            match = re.match(r'([a-zA-Z ]+)([0-9.-]+)', riadok)

            if match:
                first_part = match.group(1)
                second_part = match.group(2)
                gp = second_part[0:2]
                w = second_part[2:4]
                l = second_part[4:6]

                # Extract additional information from the second part
                original_string = second_part[6:]
                dot_index = original_string.find(".")
                dot1 = original_string[:dot_index]
                ol = ''
                pts = ''

                # Extract OL and PTS values
                if len(dot1) == 3:
                    ol = dot1[0]
                    pts = dot1[1:]
                elif len(dot1) == 4:
                    ol = dot1[0]
                    pts = dot1[1:]
                    if int(pts) > 140:
                        ol = dot1[0:2]
                        pts = dot1[2:]
                elif len(dot1) == 5:
                    ol = dot1[0:2]
                    pts = dot1[2:]

                # Continue extracting values from the second part
                dot2 = original_string[dot_index + 1:]
                pts_per = dot2[0:3]
                gf = dot2[3:6]
                ga = dot2[6:9]
                dot2 = original_string[dot_index + 10:]
                dot3 = str(dot2)

                # Extract additional values from dot3
                if dot3[0:1] == '-':
                    srs = dot3[0:5]
                    dot3 = dot3[5:]
                else:
                    srs = dot3[0:4]
                    dot3 = dot3[4:]

                if dot3[0:1] == '-':
                    sos = dot3[0:5]
                    dot3 = dot3[5:]
                else:
                    sos = dot3[0:4]
                    dot3 = dot3[4:]

                rpt = dot3[1:4]
                row = dot3[4:6]
                rgRec = dot3[6:14]
                rgpt = dot3[15:]

                # Write the formatted data to the output file
                subor_data_sezony.write(first_part + " " + gp + " " + w + " " + l + " " + ol + " " + pts + " " +
                                        pts_per + " " + gf + " " + ga + " " + srs + " " + sos + " " + rpt + " " + row +
                                        " " + rgRec + " " + rgpt + "\n")
        else:
            subor_data_sezony.write(riadok)
    subor_data_sezony.close()


def season4():
    # Define input and output file names
    sezony = 'seasons_final.txt'
    output_file = 'seasons_final1.txt'

    # Open input and output files
    subor_sezony = open(sezony, 'r')
    subor_data_sezony = open(output_file, 'w', encoding='utf-8')

    # Initialize variables for storing information
    current_division = ""
    current_year = ""

    # Iterate through lines and process data
    for line in subor_sezony:
        # If line contains "Division", save the division name
        if "Division" in line:
            current_division = line.split()[0]
        # If line contains "Standings", save the year
        elif "Standings" in line:
            current_year = line.split()[0]
        else:
            # If line doesn't contain "Division" or "Standings", process the data
            numbers = re.findall(r'\b\d+\b', line)

            if numbers:
                # Get the first part (text before the first number)
                part1 = line.split(numbers[0])[0].strip()

                # Get the second part (numbers and the rest)
                part2 = line[len(part1):].strip()
                replace_result = part2.replace('  ', ' ')
                print(replace_result)

                formatted_data = f'{part1} {part2} {current_division} {current_year}\n'
                # Write the formatted data to the output file if it meets the length criteria
                if len(formatted_data) >= 35:
                    subor_data_sezony.write(formatted_data)


def season5():
    # Define file names
    teams_file = open("teams_final1.txt", 'r', encoding='utf-8')
    seasons_file = open("seasons_final1.txt", 'r', encoding='utf-8')
    updated_season = open("updated_seasons.txt", 'w', encoding='utf-8')

    # Mapping of team names to team codes
    team_mapping = {
        'New Jersey Devils': 'NJD',
        'Pittsburgh Penguins': 'PIT',
        'Philadelphia Flyers': 'PHI',
        'New York Rangers': 'NYR',
        'New York Islanders': 'NYI',
        'Buffalo Sabres': 'BUF',
        'Ottawa Senators': 'OTT',
        'Boston Bruins': 'BOS',
        'Montreal Canadiens': 'MTL',
        'Toronto Maple Leafs': 'TOR',
        'Washington Capitals': 'WSH',
        'Atlanta Thrashers': 'ATL',
        'Carolina Hurricanes': 'CAR',
        'Tampa Bay Lightning': 'TBL',
        'Florida Panthers': 'FLA',
        'Chicago Blackhawks': 'CHI',
        'Detroit Red Wings': 'DET',
        'Nashville Predators': 'NSH',
        'Columbus Blue Jackets': 'CBJ',
        'Vancouver Canucks': 'VAN',
        'Colorado Avalanche': 'COL',
        'Calgary Flames': 'CGY',
        'Minnesota Wild': 'MIN',
        'Edmonton Oilers': 'EDM',
        'San Jose Sharks': 'SJS',
        'Phoenix Coyotes': 'PHX',
        'Los Angeles Kings': 'LAK',
        'Anaheim Ducks': 'ANA',
        'Dallas Stars': 'DAL',
        'Winnipeg Jets': 'WPG',
        'Arizona Coyotes': 'ARI',
        'Vegas Golden Knights': 'VEG',
    }

    # Iterate through lines in seasons_file
    for line in seasons_file:
        match = re.search(r'\d', line)

        if match:
            # Split the line based on the position of the first number
            index_of_first_number = match.start()
            first_part = line[:index_of_first_number]
            team_code = team_mapping.get(first_part.strip())
            second_part = line[index_of_first_number:]
            updated_data = second_part.replace('  ', ' ')

            # Combine team code and updated data
            result = team_code + " " + updated_data
            split_data = result.split(" ")

            # Check if the split data has enough elements
            if len(split_data) >= 16:
                final = split_data[0] + " " + split_data[2] + " " + split_data[3] + " " + split_data[4] + " " + \
                        split_data[5] + " " + split_data[-2] + " " + split_data[-1]
                updated_season.write(final)



def adjust_df():
    # Open the file containing team data
    teams_file = open("joined_dataframes.csv", 'r', encoding='utf-8')

    # Team name to team code mapping
    team_mapping = {
        # ... (team name to code mappings)
    }

    # Read the CSV file
    csv_reader = csv.reader(teams_file, delimiter=';')

    # Open a new CSV file to write the adjusted data
    data_csv = open('final_data_df.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(data_csv)

    # Get the header of the CSV file
    header = next(csv_reader)

    # Process each row in the CSV file
    for row in csv_reader:
        split_words = re.findall(r'[A-Z][a-z]*', row[0])
        name = ' '.join(split_words)

        match = re.match(r'(.+?)\|', row[15])
        if match:
            result = match.group(1)
            team_code = team_mapping.get(result.strip())
            match1 = re.match(r'\[\[(.*?)\]\]', row[16])
            if match1:
                result1 = match1.group(1)
                new_row = [name] + row[1:15] + [team_code] + [result1]
                print(new_row)
                csv_writer.writerow(new_row)
            else:
                new_row = [name] + row[1:15] + [team_code] + [row[16]]
                print(new_row)
                csv_writer.writerow(new_row)

        # Process another case (similar to the above block)
        match1 = re.match(r'\[\[(.*?)\]\]', row[16])
        if match1:
            result1 = match1.group(1)
            new_row = [name] + row[1:15] + [""] + [result1]
            print(new_row)
            csv_writer.writerow(new_row)
        else:
            new_row = [name] + row[1:15] + [""] + [row[16]]
            print(new_row)
            csv_writer.writerow(new_row)

    # Close the files
    teams_file.close()
    data_csv.close()


def teams():
    # Process teams file to filter and format data
    team = 'teams.txt'
    subor_team = open(team, 'r', encoding='utf-8')
    subor_data_team = open('teams_clear.txt', 'w', encoding='utf-8')

    # Filter and write selected lines to 'teams_clear.txt'
    for riadok in subor_team:
        if len(riadok) > 35 or "sezonarok:" in riadok or "sezonatim:" in riadok:
            subor_data_team.write(riadok)

    subor_data_team.close()

    # Process 'teams_clear.txt' to extract and format relevant data
    subor_data_team1 = open('teams_clear.txt', 'r', encoding='utf-8')
    subor_data_team = open('teams_clear1.txt', 'w', encoding='utf-8')
    appender = 0
    year = ""
    team = ""

    for riadok in subor_data_team1:
        if "sezonarok:" in riadok:
            year = riadok.strip()[-4:]

        if "sezonatim:" in riadok:
            team = riadok.strip()[-3:]

        if "Players on this team's active" in riadok:
            appender = 1

        if "Team Total" in riadok:
            subor_data_team.write("\n")
            appender = 0

        if appender == 1:
            subor_data_team.write(riadok.strip() + " " + str(year) + " " + team + " " + "\n")

    # Close the files
    subor_data_team.close()
    subor_data_team1.close()


def teams2():
    # Process 'teams_clear1.txt' to format and extract player data
    couter = 0
    team_file = open('teams_clear1.txt', 'r', encoding='utf-8')
    team_final = open('teams_final.txt', 'w', encoding='utf-8')

    for riadok in team_file:
        if "Players on this team's" in riadok:
            couter += 1
            team_final.write("\n")
            if couter == 3:
                couter = 1
            continue

        if couter == 1:
            # Process and format player data
            result = re.split(r'([a-zA-Z]+)', riadok, 1)
            if len(result) == 3:
                number = result[1]
                second_part = result[2]
                actual = number + second_part

            result = re.split(r'(\d+)', actual, 1)
            if len(result) == 3:
                name = result[0]
                first_letter = result[1]
                rest_of_text = result[2]
            riadok = first_letter + rest_of_text

            age = riadok[0:2]
            actual = riadok[2:]
            result = re.split(r'(\d+)', actual, 1)
            if len(result) == 3:
                pos = result[0]
                first_number = result[1]
                rest = result[2]
                actual = first_number + rest

            # Process additional conditions and format data
            if actual[1:2] == "0":
                if actual[3:4] != "0":
                    gp = actual[0:1]
                    actual = actual[1:]
                else:
                    gp = actual[0:2]
                    actual = actual[2:]
            else:
                gp = actual[0:2]
                actual = actual[2:]

            atoi = actual.split(":")
            last = atoi[1][0:2]
            first = atoi[0][-2:]

            if int(first[0]) > 5:
                first = first[1]

            atoi = first + ":" + last
            g = actual[0:2]

            if g[1] == "-":
                g = g[0]
                actual = actual[2:]
            else:
                if int(g) > 30:
                    g = actual[0:1]
                    actual = actual[1:]
                else:
                    g = actual[0:2]
                    actual = actual[2:]

            a = actual[0:2]
            actual = actual[2:]

            team = actual[-5:].strip()
            actual = actual[:-5]

            year = actual[-5:]

        team_final.write(
            name + " " + age + " " + pos + " " + " " + gp + " " + g + " " + a + " " + atoi + " " + team + " " + year + "\n"
        )

        if couter == 2:
            # Process and format additional player data
            riadok = riadok[1:]

            result = re.split(r'(\d+)', riadok, 1)
            if len(result) == 3:
                name = result[0]
                number = result[1]
                second_part = result[2]
                actual = number + second_part

            age = actual[0:2]
            actual = actual[2:]

            gp = actual[0:2]
            actual = actual[2:]

            gs = actual[0:2]
            actual = actual[2:]

            w = actual[0:2]
            actual = actual[2:]

            l = actual[0:2]
            actual = actual[2:]

            sv = actual[12:15]
            actual = actual[15:]

            gaa = actual[0:4]

            team = actual[-5:].strip()
            actual = actual[:-5]

            year = actual[-5:]

            team_final.write(
                name + " " + gp + " " + gs + " " + w + " " + l + " " + sv + " " + gaa + " " + team + " " + year + "\n"
            )

    # Close the files
    team_file.close()
    team_final.close()


def teams3():
    # Process 'teams_final.txt' to filter and write data to 'teams_final1.txt'
    team_file = open('teams_final.txt', 'r', encoding='utf-8')
    team_final = open('teams_final1.txt', 'w', encoding='utf-8')

    for riadok in team_file:
        contains_letter = any(map(str.isalpha, riadok))
        if contains_letter:
            team_final.write(riadok)
        if riadok == "\n":
            team_final.write(riadok)

    # Close the files
    team_file.close()
    team_final.close()


def convert_to_csv():
    # Convert data from 'crawled_data1.txt' to CSV format
    input_file = 'crawled_data1.txt'
    output_file = 'crawled_data.csv'

    with open(input_file, 'r', encoding='utf-8') as txt_file:
        # Assuming values are separated by tabs
        reader = csv.reader(txt_file, delimiter='\t')

        with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter='\t')

            for row in reader:
                # Write each row to the CSV file
                writer.writerow(row)


def crawler():
    # Crawl and process data from 'teams_final1.txt' and 'updated_seasons.txt'
    team_file = open("teams_final1.txt", 'r', encoding='utf-8')
    season_file = open("updated_seasons.txt", 'r', encoding='utf-8')
    crawled_data = open("crawled_data.txt", 'w', encoding='utf-8')

    # Write header to 'crawled_data.txt'
    crawled_data.write('NAME' + "\t" + 'AGE' + "\t" + 'POSSITION' + "\t" + 'GAMES_PLAYED' + "\t" + 'GOALS' + "\t" +
                       'ASSISTS' + "\t" + 'ICE_TIME' + "\t" + 'TEAM_NAME' + "\t" + 'YEAR' + "\t" + 'TEAM_WINS' + "\t" +
                       'TEAM_LOSE' + "\t" + 'TEAM_OVERTIME_LOSE' + "\t" + 'TEAM_POINTS' + "\t" + 'TEAM_DIVISSION' + "\n")

    # Process each team from 'teams_final1.txt'
    for team in team_file:
        team = team.strip()
        split_line = team.split(" ")

        # Check if the split line length is 11
        if len(split_line) == 11:
            with open("updated_seasons.txt", "r", encoding='utf-8') as season_file:
                for season in season_file:
                    season = season.strip()
                    season_split = season.split(" ")

                    # Check if the last two elements of the split line match the first and last elements of season_split
                    if split_line[-1] == season_split[-1] and split_line[-2] == season_split[0]:
                        joined_data = ' '.join(season_split[1:-1])
                        result = team + " " + joined_data + "\n"
                        updated_data = result.replace('  ', ' ')

                        match = re.search(r'\d', updated_data)

                        if match:
                            # Split the string into two parts based on the position of the first number
                            index_of_first_number = match.start()
                            first_part = updated_data[:index_of_first_number]
                            first_part.strip()

                            second_part = updated_data[index_of_first_number:]

                            final = second_part.replace(' ', '\t')

                            # Write the formatted data to 'crawled_data.txt'
                            crawled_data.write(first_part + "\t" + final)
                        break

    # Close the files
    crawled_data.close()
    chcek_data = open("crawled_data.txt", 'r', encoding='utf-8')
    chceked_data = open("crawled_data1.txt", 'w', encoding='utf-8')

    # Process 'crawled_data.txt' to format and remove spaces
    for input_string in chcek_data:
        match = re.search(r'\d', input_string)

        if match:
            # Split the string into two parts based on the position of the first number
            first_part = input_string[:match.start()]
            second_part = input_string[match.start():]
            second_part = second_part.replace(" ", "\t")

            # Write the formatted data to 'crawled_data1.txt'
            chceked_data.write(first_part + "\t" + second_part)

    # Close the files
    chcek_data.close()
    chceked_data.close()


def space():
    with open('crawled_data.txt', "r", encoding='utf-8') as file:
        content = file.read()

    chceked_data = open("crawled_data1.txt", 'w', encoding='utf-8')
    content_without_spaces = content.replace(" ", "")
    chceked_data.write(content_without_spaces)


