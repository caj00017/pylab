class Log:
    def __init__(self, service, status, latency): # __init__ is like a constructor in Java
        self.service = service #self.service is like this.service
        self.status = status 
        self.latency = latency

    # note: python requires that "self" goes in the constructor parameters. java doesn't require this.

    def get_latency(self): # this method belongs to the log class, note that self must be passed here also
        return self.latency

    @staticmethod # this is how we indicate the method is statically accessed
    def print_example_logs():
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
        print(logs)

class ErrorLog(Log): # inheritance is done by passing the parent object into the subclass
    def __init__(self, service, status, latency, message):
        super():__init__(service, status, latency) # let's use the same data members as the parent class
        self.message = message # but also add a new data member specific to error logs

log = Log("api", 500, 103.2) # instantiating an object
print(f"Log service: {log.service}") # accessing the data member
print(f"{log.service} latency: {log.get_latency()}") # using the method

Log.print_example_logs() # using a static method