def sjf(processes):
    completed = []
    ready_queue = []
    time = 0

    processes.sort(key=lambda x: x.at)

    while len(completed) < len(processes):
        for p in processes:
            if p.at <= time and p not in ready_queue and p not in completed:
                ready_queue.append(p)

        if not ready_queue:
            time += 1
            continue

        ready_queue.sort(key=lambda x: x.bt)
        current = ready_queue.pop(0)

        time += current.bt
        current.ct = time
        current.tat = current.ct - current.at
        current.wt = current.tat - current.bt

        completed.append(current)

    return completed
