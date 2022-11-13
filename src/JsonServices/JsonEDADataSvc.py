from src.Contracts.DataServices.EDADataSvc import AbstractEDADataService
import pandas as pd
import json


class EDADataService(AbstractEDADataService):
    def __init__(self, jsonFileName: str):
        self.__jsonFileName = jsonFileName
        self.__jsonTable = pd.read_json(jsonFileName)

    def GetCategories(self):
        labels = self.__jsonTable['labels']

        categoriesSet = set()

        for rowIndex in range(0, len(labels)):
            for label in labels[rowIndex]:
                categoriesSet.add(label['category'])

        return list(sorted(categoriesSet))

    def GetCategoryCount(self, categoryName: str) -> int:
        categoryCount = 0

        labels = self.__jsonTable['labels']

        for rowIndex in range(0, len(labels)):
            for label in labels[rowIndex]:
                if categoryName == label['category']:
                    categoryCount += 1

        return categoryCount
