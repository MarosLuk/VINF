import lucene
from java.nio.file import Paths
from org.apache.lucene.store import NIOFSDirectory
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader
from org.apache.lucene.document import Document, Field, TextField
import csv

def indexer():
    # Initialize the Lucene VM
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])

    # Specify the directory for the Lucene index
    indexDirectory = 'lucene/index'

    # Configure the IndexWriter
    indexWriterConfig = IndexWriterConfig(StandardAnalyzer())
    writer = IndexWriter(NIOFSDirectory(Paths.get(indexDirectory)), indexWriterConfig)

    # Open the CSV file with documents
    file = open("final_data_df.csv", "r", encoding="utf-8")
    data = csv.reader(file, delimiter=",")

    for line in data:
        # Create a Lucene Document for each line in the CSV
        document = Document()

        # Add fields to the document
        document.add(Field("NAME", line[0], TextField.TYPE_STORED))
        document.add(Field("AGE", line[1], TextField.TYPE_STORED))
        document.add(Field("POSSITION", line[2], TextField.TYPE_STORED))
        document.add(Field("GAMES_PLAYED", line[3], TextField.TYPE_STORED))
        document.add(Field("GOALS", line[4], TextField.TYPE_STORED))
        document.add(Field("ASSISTS", line[5], TextField.TYPE_STORED))
        document.add(Field("ICE_TIME", line[6], TextField.TYPE_STORED))
        document.add(Field("TEAM_NAME", line[7], TextField.TYPE_STORED))
        document.add(Field("YEAR", line[8], TextField.TYPE_STORED))
        document.add(Field("TEAM_WINS", line[9], TextField.TYPE_STORED))
        document.add(Field("TEAM_LOSE", line[10], TextField.TYPE_STORED))
        document.add(Field("TEAM_OVERTIME_LOSE", line[11], TextField.TYPE_STORED))
        document.add(Field("TEAM_POINTS", line[12], TextField.TYPE_STORED))
        document.add(Field("TEAM_DIVISSION", line[13], TextField.TYPE_STORED))
        document.add(Field("season", line[14], TextField.TYPE_STORED))
        document.add(Field("winner", line[15], TextField.TYPE_STORED))
        document.add(Field("player", line[16], TextField.TYPE_STORED))

        # Add the document to the Lucene index
        writer.addDocument(document)

    # Commit the changes to the index
    writer.commit()

# Call the indexer function to create the Lucene index
indexer()
