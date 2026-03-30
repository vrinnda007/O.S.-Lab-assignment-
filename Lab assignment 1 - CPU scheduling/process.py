class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at  # Arrival Time
        self.bt = bt  # Burst Time
        self.ct = 0   # Completion Time
        self.tat = 0  # Turnaround Time
        self.wt = 0   # Waiting Time
