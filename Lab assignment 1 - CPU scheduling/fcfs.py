def fcfs(processes):
    processes.sort(key=lambda x: x.at)

    time = 0

    for p in processes:
        if time < p.at:
            time = p.at  # CPU idle

        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

    return processes
