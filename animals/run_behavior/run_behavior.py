from abc import ABC


class RunBehavior(ABC):
    """
    Abstract class for running behavior
    """

    def perform_run(self, animal):
        pass
