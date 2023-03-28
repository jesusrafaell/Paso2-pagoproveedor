class Banco:
    def __init__(self, banCodBan: str, banDescBan: str, banSwift: str):
        self.banCodBan = banCodBan
        self.banDescBan = banDescBan
        self.banSwift = banSwift
    
    def getBanCodBan(self) -> str:
        return self.banCodBan
    
    def setBanCodBan(self, banCodBan: str) -> None:
        self.banCodBan = banCodBan
    
    def getBanDescBan(self) -> str:
        return self.banDescBan
    
    def setBanDescBan(self, banDescBan: str) -> None:
        self.banDescBan = banDescBan
    
    def getBanSwift(self) -> str:
        return self.banSwift
    
    def setBanSwift(self, banSwift: str) -> None:
        self.banSwift = banSwift
