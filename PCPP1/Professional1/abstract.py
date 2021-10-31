import abc


class Scanner:
    @abc.abstractmethod
    def scan_document(self) -> str:
        pass

    @abc.abstractmethod
    def get_scanner_status(self) -> str:
        pass

class Printer:
    @abc.abstractmethod
    def print_document(self) -> str:
        pass

    @abc.abstractmethod
    def get_printer_status(self) -> str:
        pass

class MFDBase(Scanner, Printer):
    def scan_document(self) -> str:
        return 'Document has been scanned.'

    def print_document(self) -> str:
        return 'Document has been printed.'

class MFD1(MFDBase):
    def get_scanner_status(self) -> str:
        return 'Resolution: Low; Serial Number 1'

    def get_printer_status(self) -> str:
        return 'Resolution: Low, Serial Number 1'

class MFD2(MFDBase):
    def get_scanner_status(self) -> str:
        return 'Resolution: High; Serial Number 2'

    def get_printer_status(self) -> str:
        return 'Resolution: High; Serial Number 2'

for m in (MFD1(), MFD2()):
    print(m.get_scanner_status())

