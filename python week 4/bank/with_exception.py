class InvalidWithdrawal(Exception):
    """Exception raised when withdrawal is attempted in account with not enought money
    """
    def __init__(self, invalid_ammount, message = "Not enough funds in the account"):
        super().__init__(message)
        self.invalid_amount = invalid_ammount
        