def to_host_port(runserver):
    runserver_list = runserver.split(":")
    host = runserver_list[0] if runserver_list[0] else None
    if len(runserver_list) == 2 and runserver_list[1]:
        port = int(runserver_list[1])
    else:
        port = None
    return host, port