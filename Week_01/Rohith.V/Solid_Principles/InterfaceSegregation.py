from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class BasicPrinter(Printer):
    """This class only cares about printing."""
    def print_document(self):
        print("Printing standard black & white pages.")


class MultiFunctionPrinter(Printer, Scanner):
    """This class legitimately needs both capabilities."""
    def print_document(self):
        print("Printing high-quality color pages.")

    def scan_document(self):
        print("Scanning document to PDF.")


if __name__ == "__main__":
    # A simple printer works without being forced to have scanning code
    cheap_printer = BasicPrinter()
    cheap_printer.print_document()

    # An advanced printer combines both cleanly
    office_printer = MultiFunctionPrinter()
    office_printer.print_document()
    office_printer.scan_document()