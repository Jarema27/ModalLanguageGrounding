import csv
import os


"""
Class used specifically to extract observations from csv file.
Format of observation is:
position 0 , Identificator of observation
last position - timestamp
all inbetween - pair of trait index and State (1 - IS, 2 - IS_NOT, 3 - MAYHAPS)
"""


class CSVReader:

    @staticmethod
    def get_some_observations():
        """
        :return: observations read from Observations.csv
        """
        out = []
        with open(os.path.dirname(__file__) + '/Observations.csv', 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                if len(row) > 1:
                    ident = row[0]
                    timestamp = row[len(row)-1]
                    traitsNstates = []
                    for i in range(1, len(row)-1):
                        if i % 2 == 1:
                            traitsNstates.append((row[i], row[i+1]))
                    out.append((ident,traitsNstates,timestamp))
            return out
