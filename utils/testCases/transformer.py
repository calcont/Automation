from abc import ABC, abstractmethod


class Transformer(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class BaseTransformer(Transformer):
    def execute(self, data):
        return data
