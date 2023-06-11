
import csv
import pandas as pd

class Csv():
    def __init__(self) -> None:
        pass
    def _UpdateCsv(self, dictData: dict, pathFile: str='output.csv'):
        try:
            self.File = open(pathFile,"a+",newline='',encoding='utf-8')
            self.writer = csv.writer(self.File, dialect='excel', delimiter=',')
            self.writer.writerow(dictData.values())
        except PermissionError:
            ()
    def _ReadCsv(self, pathFile: str='output.csv'):
        listLines = []
        with open(pathFile, 'r',encoding='utf-8') as file:
            readerLines = csv.reader(file)
            for i in readerLines: 
                listLines.append(i)
        return listLines


