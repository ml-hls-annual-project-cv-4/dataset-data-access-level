from abc import *


class AbstractEDADataService(ABC):

    @abstractmethod
    def GetCategories(self):
        pass

    @abstractmethod
    def GetCategoryCount(self, categoryName: str) -> int:
        pass
