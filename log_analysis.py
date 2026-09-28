# Author: Christopher Jones
# Log Analysis Learning Project. See README.md.

# This log analyzer expects logs in the following format:
# hostname service value status
# For example, a log that this tool can parse might look like:
# pollux api 90 CRITICAL

# import statement is required so that Python knows to refer to log.py when I use stuff from my log class.
from log import Log

# parsing a log
def parse_log(line):
    try:
        host, metric, value, status = line.split()
        log = Log(host, metric, float(value), status)
        print(f"Parsed:\t{host}\t{metric}\t{value}\t{status}")
        return log
    except ValueError as e:
        print(f"Error:\tCould not parse invalid log '{line}': {e}")
        return None

# parsing all logs
# This function is equivalent to (but significantly more readable than):
# log_obj_list = []
# for log in logs:
#     this_log = parse_log(log)
#     if this_log is None:
#         continue
#     log_obj_list.append(this_log)
# return log_obj_list # Previously forgot to return this, which resulted in a TypeError in the first count_statuses call.
def parse_all_logs(logs):
    return [parse_log(log) for log in logs if parse_log(log) is not None]

# finding unhealthy readings
# Note that this is equivalent to what I was doign before, which was 
# unhealthy = []
# for log in logs:
#     if log.status in {"WARNING", "CRITICAL"}:
#         unhealthy.append(log)
# return unhealthy
def get_unhealthy(logs):
    return [log for log in logs if log.status in {"WARNING", "CRITICAL"}]


# counting statuses
# Previously, I did this, which is correct, but if I wanna do something more Python, I can do something like the above.
# This assigns the default value of 0 if it does not already exist and then adds 1 for a default value of 1, also adding one each time that value is retrieved, 
# which essentially achieves the same as below.
# status = log.status; No need to have this anymore like I did before, I can simplify by adding log.status directly.
# if status not in counts:
#     counts[status] = 1
# else:
#     counts[status] += 1
def count_statuses(logs):
    counts = {}
    for log in logs:
        counts[log.status] = counts.get(log.status, 0) + 1
        
    return counts

# finding affected servers
# returns a set contianing every seerver that has experienced at least one WARNING or CRITICAL
# This function is equivalent to (but significantly more readable than):
# unhealthy_logs = get_unhealthy(logs)
# unhealthy_hosts = set()
# for log in unhealthy_logs:
#     # host = log.hostname; No need to have this anymore like I did before, I can simplify by adding log.hostname directly.
#     unhealthy_hosts.add(log.hostname)
def affected_servers(logs):
    return {log.hostname for log in get_unhealthy(logs)}

# average metrics
# returns the average of all numeric readings for each server
# NOTE: This currently averages all numeric readings for each server, which isn't particularly useful.
# Instead, this function should be tweaked so that it averages each different kind of metric for each server.
def average_by_server(logs):
    result = {}
    counts = {}
    for log in logs:
        host = log.hostname
        value = log.value
        if host not in result:
            result[host] = value    
            counts[host] = 1
        else:
            result[host] += value
            counts[host] += 1
    for host in result:
        result[host] /= counts[host]
    return result

# comparing metrics across hosts
# take a collection of logs and group readings by metric so that values from different hosts can be examined together
def compare_metrics(logs):
    # The output data structure should be a dictionary containing dictionaries for each metric. e.g.:
    # {
    #     "cpu": {
    #         "pollux": 81
    #         "castor": 91
    #         "pi": 75
    #     }
    #     "ram": {
    #         "pollux": 8
    #         "castor": 16
    #         "pi": 2
    #     }
    # }

    services = set()
    return_value = {}
    counts = {}
    for log in logs:
        if log.service not in services:
            services.add(log.service)

    for service in services:
        return_value[service] = {}
        counts[service] = {}
        for log in logs:
            if service != log.service:
                continue
            if log.hostname not in return_value[service]:
                return_value[service][log.hostname] = log.value
                counts[service][log.hostname] = 1
            else:
                return_value[service][log.hostname] += log.value
                counts[service][log.hostname] += 1

    # for service in return_value:
    #     for host in return_value[service]:
    #         return_value[service][host] /= counts[service][host]

    for service, reading in return_value.items():
        for host, value in reading.items():
            return_value[service][host] = value / counts[service][host]


    print(return_value.items())

    return return_value


# Use all functions above to print a clean report of all values
def generate_report(logs):
    with open("report.txt", "w") as file:
        file.write("======= HOMELAB HEALTH REPORT =======")

        file.write("\n\nAll hosts:\n")
        hosts = {log.hostname for log in logs}
        for host in hosts:
            file.write(host)
            file.write("\n")

        file.write("\n\nStatus Counts:")
        statuses = count_statuses(logs)

        # Previously, I was doing the following, which worked, but it assumed these things exist. Instead, I should've done what follows, had I known.
        # print(f"OK: {statuses["OK"]}")
        # print(f"WARNING: {statuses["WARNING"]}")
        # print(f"CRITICAL: {statuses["CRITICAL"]}")

        for status, count in statuses.items():
            file.write(f"\n{status}: {count}")

        file.write("\n\nAffected Servers:")
        servers = affected_servers(logs)
        for server in servers:
            file.write(f"\n{server}")

        file.write("\n\nAverage Readings:")
        averages = average_by_server(logs)
        for host, average in averages.items(): # using .items() to access both the host and its average value in the dict
            file.write(f"\n{host}: {average:.2f}")

        file.write("\n\nUnhealthy Readings:")
        unhealthy_logs = get_unhealthy(logs)
        for log in unhealthy_logs:
            host = log.hostname
            metric = log.service
            value = log.value
            status = log.status
            file.write(f"\n({status}): {host}'s {metric} at {value}.")

        file.write("\n\nMetrics by Service:\n")
        for service, reading in compare_metrics(logs).items():
            file.write(f"\nMetric: {service}")
            for hostname, value in reading.items():
                file.write(f"\n{hostname}: {value}")
            file.write("\n")

def main():
    # These are example logs.
    logs = Log.get_example_logs()
    parsed_logs = parse_all_logs(logs)

    generate_report(parsed_logs)
    print("\nReport written to report.txt.")

if __name__ == "__main__":
    main()
    
