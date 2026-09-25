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
        logs = [
            "pollux cpu 72.5 OK",
            "castor memory 81.2 OK",
            "pollux memory 91.4 WARNING",
            "minecraft cpu 95.8 CRITICAL",

            # deliberately invalid log to show error handling
            "castor cpu banana OK",

            "minecraft memory 88.1 WARNING",
            "pollux cpu 78.2 OK",

            "minecraft 97.1 CRITICAL",

            "pihole memory 45.6 OK",
            "castor disk 92.0 WARNING",

            "pollux disk 84.3 VERY BAD",

            "minecraft cpu 99.2 CRITICAL"
        ]
        return logs

class ErrorLog(Log): # inheritance is done by passing the parent object into the subclass
    def __init__(self, hostname, service, value, status, message):
        super().__init__(hostname, service, value, status) # let's use the same data members as the parent class
        self.message = message # but also add a new data member specific to error logs

log = Log("pollux", "api", 500, 103.2) # instantiating an object
print(f"Log service: {log.service}") # accessing the data member
print(f"{log.service} status: {log.get_status()}") # using the method

print(Log.get_example_logs()) # using a static method