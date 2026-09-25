# These are example logs.
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

# parsing a log
def parse_log(line):
    try:
        host, metric, value, status = line.split()
        return (host, metric, float(value), status)
    except ValueError as e:
        print(f"Invalid log '{line}': {e}")
        return None

# finding unhealthy readings
def get_unhealthy(logs):
    result = []
    for log in logs:
        parsed = parse_log(log)
        if parsed is None:
            continue
        host, metric, value, status = parsed
        # if status == "WARNING" or status == "CRITICAL": This is what I had before, and it's a bit Java-y, what i have below is more uniquely Python
        if status in {"WARNING", "CRITICAL"}:
            result.append((host, metric, float(value), status))
    return result

# counting statuses
def count_statuses(logs):
    counts = {}
    for log in logs:
        parsed = parse_log(log)
        if parsed is None:
            continue
        host, metric, value, status = parsed
        counts[status] = counts.get(status, 0) + 1
        # Previously, I did this, which is correct, but if I wanna do something more Python, I can do something like the above.
        # This assigns the default value of 0 if it does not already exist and then adds 1 for a default value of 1, also adding one each time that value is retrieved, 
        # which essentially achieves the same as below.
        # if status not in counts:
        #     counts[status] = 1
        # else:
        #     counts[status] += 1
    return counts


# finding affected servers
# returns a set contianing every seerver that has experienced at least one WARNING or CRITICAL
def affected_servers(logs):
    unhealthy_logs = get_unhealthy(logs)
    unhealthy_hosts = set()
    for log in unhealthy_logs:
        host, metric, value, status = log
        unhealthy_hosts.add(host)
    return unhealthy_hosts

# average metrics
# returns the average of all numeric readings for each server
def average_by_server(logs):
    result = {}
    counts = {}
    for log in logs:
        parsed = parse_log(log)
        if parsed is None:
            continue
        host, metric, value, status = parsed
        if host not in result:
            result[host] = value    
            counts[host] = 1
        else:
            result[host] += value
            counts[host] += 1
    for host in result:
        result[host] /= counts[host]
    return result

# Use all functions above to print a clean report of all values
def generate_report(logs):
    print("======= HOMELAB HEALTH REPORT =======")

    print("\nStatus Counts:")
    statuses = count_statuses(logs)

    # Previously, I was doing the following, which worked, but it assumed these things exist. Instead, I should've done what follows, had I known.
    # print(f"OK: {statuses["OK"]}")
    # print(f"WARNING: {statuses["WARNING"]}")
    # print(f"CRITICAL: {statuses["CRITICAL"]}")

    for status, count in statuses.items():
        print(f"{status}: {count}")

    print("\nAffected Servers:")
    servers = affected_servers(logs)
    for server in servers:
        print(server)

    print("\nAverage Readings:")
    averages = average_by_server(logs)
    for host, average in averages.items(): # using .items() to access both the host and its average value in the dict
        print(f"{host}: {average:.2f}")

    print("\nUnhealthy Readings:")
    unhealthy_logs = get_unhealthy(logs)
    for log in unhealthy_logs:
        host, metric, value, status = log
        print(f"({status}): {host}'s {metric} at {value}.")

generate_report(logs)
    
