class Log:
    def __init__(self, hostname, service, value, status): # __init__ is like a constructor in Java
        self.hostname = hostname
        self.service = service #self.service is like this.service
        self.status = status 
        self.value = value

    # note: python requires that "self" goes in the constructor parameters. java doesn't require this.

    def get_status(self): # this method belongs to the log class, note that self must be passed here also
        return self.status

    @staticmethod # this is how we indicate the method is statically accessed
    def get_example_logs():
        with open("logs.txt", "r") as file:
            for log in file:
                yield log       # rather than building a list, i am now yielding one log at a time