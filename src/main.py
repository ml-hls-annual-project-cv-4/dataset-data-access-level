from src.Factories.JsonDataSvcFactory import DataServiceFactory

factory = DataServiceFactory()

edaDataService = factory.GetEDADataService('../files/bdd100k_labels_images_train.json')
categories = edaDataService.GetCategories()
print(categories)

for category in categories:
    print(category, edaDataService.GetCategoryCount(category), sep=': ')
