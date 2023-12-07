import csv
import lucene
from org.apache.lucene.store import FSDirectory
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import DirectoryReader

from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.queryparser.classic import MultiFieldQueryParser

import indexer


# Function to get the count of goals/points for a specific player in a particular season
def pocet_konkretna_sezona(name, sezona, gol_bod):
    if gol_bod == 'gol':
        index_path = "lucene/index"
        directory = FSDirectory.open(Paths.get(index_path))
        reader = DirectoryReader.open(directory)
        searcher = IndexSearcher(reader)

        search_name = "NAME"

        # Create a query to search for the player's name in the specified season
        query_1 = MultiFieldQueryParser.parse(MultiFieldQueryParser([search_name], StandardAnalyzer()), name)

        # Perform the search
        answer_query_1 = searcher.search(query_1, 100)

        counter = 0
        meno_hraca = ''

        for score in answer_query_1.scoreDocs:
            doc = searcher.doc(score.doc)
            meno_hraca = str(doc.get("NAME"))
            if int(doc.get("YEAR")) == int(sezona):
                counter += int(doc.get("GOALS"))

        print("Hrac s menom: " + meno_hraca + " dal tolkoto golov: " + str(counter))
        counter = 0
    else:
        # Similar logic for points (goals + assists)
        index_path = "lucene/index"
        directory = FSDirectory.open(Paths.get(index_path))
        reader = DirectoryReader.open(directory)
        searcher = IndexSearcher(reader)

        search_name = "NAME"

        query_1 = MultiFieldQueryParser.parse(MultiFieldQueryParser([search_name], StandardAnalyzer()), name)

        answer_query_1 = searcher.search(query_1, 1000000)
        counter = 0
        meno_hraca = ""
        for score in answer_query_1.scoreDocs:
            doc = searcher.doc(score.doc)
            meno_hraca = str(doc.get("NAME"))
            if int(doc.get("YEAR")) == int(sezona):
                counter += int(doc.get("GOALS"))
                counter += int(doc.get("ASSISTS"))

        print("Hrac s menom: " + meno_hraca + " ziskal tolkoto bodov: " + str(counter))
        counter = 0


# Function to get the count of goals/points for a specific player across all seasons
def pocet_vsetky_sezony(name, gol_bod):
    if gol_bod == 'gol':
        index_path = "lucene/index"
        directory = FSDirectory.open(Paths.get(index_path))
        reader = DirectoryReader.open(directory)
        searcher = IndexSearcher(reader)

        search_name = "NAME"

        query_1 = MultiFieldQueryParser.parse(MultiFieldQueryParser([search_name], StandardAnalyzer()), name)

        answer_query_1 = searcher.search(query_1, 100)
        meno_hraca = ''
        counter = 0
        for score in answer_query_1.scoreDocs:
            doc = searcher.doc(score.doc)
            meno_hraca = str(doc.get("NAME"))
            counter += int(doc.get("GOALS"))

        print("Hrac s menom: " + meno_hraca + " dal tolkoto golov: " + str(counter))
        counter = 0
    else:
        # Similar logic for points (goals + assists)
        index_path = "lucene/index"
        directory = FSDirectory.open(Paths.get(index_path))
        reader = DirectoryReader.open(directory)
        searcher = IndexSearcher(reader)

        search_name = "NAME"

        query_1 = MultiFieldQueryParser.parse(MultiFieldQueryParser([search_name], StandardAnalyzer()), name)

        answer_query_1 = searcher.search(query_1, 100)

        counter = 0
        meno_hraca = ''
        for score in answer_query_1.scoreDocs:
            doc = searcher.doc(score.doc)
            meno_hraca = str(doc.get("NAME"))

            counter += int(doc.get("GOALS"))
            counter += int(doc.get("ASSISTS"))

        print("Hrac s menom: " + meno_hraca + " ziskal tolkoto bodov: " + str(counter))
        counter = 0


# Function to search and analyze player statistics
def searcher():
    while True:
        print("1. Pocet golov/bodov hraca v konkretnom sezone.")
        print("2. Pocet golov/bodov hraca vo vsetkych sezonnach.")
        choice = input("1 / 2 ")

        if choice == str(1):
            name = input("Zadaj meno hraca 1: ")
            if name == "konec":
                return 0
            sezona = input("Zadaj sezonu: ")
            if sezona == "konec":
                return 0
            gol_bod = input("gol/bod: ")
            if gol_bod == "konec":
                return 0

            # Call the function to get statistics for a specific season
            pocet_konkretna_sezona(name, sezona, gol_bod)

        elif choice == str(2):
            name = input("Zadaj meno hraca 1: ")
            if name == "konec":
                return 0
            gol_bod = input("gol/bod: ")
            if gol_bod == "konec":
                return 0

            # Call the function to get statistics across all seasons
            pocet_vsetky_sezony(name, gol_bod)
        elif choice == "konec":
            return 0


# Function to test statistics for joined data frames
def tester():
    index_path = "lucene/index"
    directory = FSDirectory.open(Paths.get(index_path))
    reader = DirectoryReader.open(directory)
    searcher = IndexSearcher(reader)

    search_season = "YEAR"
    all_counter = 0
    team_winner_counter = 0
    player_counter = 0
    for i in range(2010, 2019):
        query_season = MultiFieldQueryParser.parse(MultiFieldQueryParser([search_season], StandardAnalyzer()), str(i))

        # Perform the search for each season
        answer_query_1 = searcher.search(query_season, 1000)
        for score in answer_query_1.scoreDocs:
            doc = searcher.doc(score.doc)
            all_counter += 1

            meno_hraca = str(doc.get("NAME"))
            sezona = str(doc.get("YEAR"))
            player = str(doc.get("player"))

            # Counting found information
            if player != "":
                player_counter += 1

            winner_team = str(doc.get("winner"))
            if winner_team != "":
                team_winner_counter += 1

    print(
        "Celkova uspesnost najdenych vyhernych timov: " + str(round(team_winner_counter / all_counter, 4) * 100) + " %")
    print("Celkova uspesnost najdenych najlepsich hracov: " + str(round(player_counter / all_counter, 4) * 100) + " %")


# Function to perform unit testing
def unit():
    while True:
        choice = input("Won Stan.CUP ? = 1 / Played together ? = 2")

        if choice == str(1):
            name = input("Name : ")

            index_path = "lucene/index"
            directory = FSDirectory.open(Paths.get(index_path))
            reader = DirectoryReader.open(directory)
            searcher = IndexSearcher(reader)

            search_season = "YEAR"

            query_season = MultiFieldQueryParser.parse(MultiFieldQueryParser(["NAME"], StandardAnalyzer()), name)

            answer_query = searcher.search(query_season, 1000)
            counter = 0
            for score in answer_query.scoreDocs:

                doc = searcher.doc(score.doc)

                if str(doc.get("NAME")) == name:
                    team = str(doc.get("TEAM_NAME"))
                    winner = str(doc.get("winner"))

                    if team == winner:
                        counter += 1
                        print("Player " + name + " won a Stanley CUP with team: " + team + " in season: " + str(
                            doc.get("season")))
                        print("Best player of season " + str(doc.get("season")) + " was " + str(doc.get("player")))

            if counter > 0 :
                unit_teza2()
            if counter == 0:
                print("Player " + name + " DID NOT win a Stanley CUP.")
                unit_teza4()

        if choice == str(2):
            name = input("Name 1 : ")
            name2 = input("Name 2 : ")

            index_path = "lucene/index"
            directory = FSDirectory.open(Paths.get(index_path))
            reader = DirectoryReader.open(directory)
            searcher = IndexSearcher(reader)

            query_season = MultiFieldQueryParser.parse(MultiFieldQueryParser(["NAME"], StandardAnalyzer()), name)
            query_season2 = MultiFieldQueryParser.parse(MultiFieldQueryParser(["NAME"], StandardAnalyzer()), name2)

            answer_query = searcher.search(query_season, 1000)
            answer_query2 = searcher.search(query_season2, 1000)
            counter = 0
            for score in answer_query.scoreDocs:
                doc = searcher.doc(score.doc)
                name_query_1 = str(doc.get("NAME"))
                team_name_query_1 = str(doc.get("TEAM_NAME"))
                season_query_1 = str(doc.get("YEAR"))
                for x in answer_query2.scoreDocs:
                    doc2 = searcher.doc(x.doc)
                    name_query_2 = str(doc2.get("NAME"))
                    team_name_query_2 = str(doc2.get("TEAM_NAME"))

                    season_query_2 = str(doc2.get("YEAR"))
                    if team_name_query_1 == team_name_query_2 and season_query_1 == season_query_2:
                        counter += 1
                        print("Players " + name_query_1 + " and " + name_query_2 + " played together in season " + season_query_1 + " in " + team_name_query_1)
            if counter > 0:
                unit_teza1()
            if counter == 0:
                print("Players DID NOT play together.")
                unit_teza3()

def unit_teza1():
    print("")
    print("")
    print("Expected:  Sidney Crosby and Phil Kessel played together in 2016,2017,2018,2019 in PIT.")

def unit_teza2():
    print("")
    print("")
    print("Expected:  Sidney Crosby won Stan. Cup in 2015,2016.")

def unit_teza3():
    print("")
    print("")
    print("Expected:  Players DID NOT play together.")

def unit_teza4():
    print("")
    print("")
    print("Expected:  Player DID NOT win Stan. CUP.")
tester()