from fcfs import fcfs
from sjf import sjf
from process import Process

def take_input():
    processes = []
    n = int(input("Enter number of processes: "))

    for i in range(n):
        print(f"\nProcess {i+1}")
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))
        processes.append(Process(i+1, at, bt))

    return processes


def display(processes):
    print("\nPID\tAT\tBT")
    for p in processes:
        print(f"P{p.pid}\t{p.at}\t{p.bt}")


def display_full(processes):
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    total_tat = total_wt = 0

    for p in processes:
        total_tat += p.tat
        total_wt += p.wt
        print(f"P{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

    print("\nAverage TAT:", total_tat / len(processes))
    print("Average WT:", total_wt / len(processes))


def gantt_chart(processes):
    print("\nGantt Chart:")

    for p in processes:
        print(f"| P{p.pid} ", end="")
    print("|")

    print("0", end="")
    for p in processes:
        print(f"\t{p.ct}", end="")
    print()


if __name__ == "__main__":
    processes = take_input()

    print("\n--- INPUT ---")
    display(processes)

    fcfs_result = fcfs([Process(p.pid, p.at, p.bt) for p in processes])
    print("\n--- FCFS ---")
    display_full(fcfs_result)
    gantt_chart(fcfs_result)

    sjf_result = sjf([Process(p.pid, p.at, p.bt) for p in processes])
    print("\n--- SJF ---")
    display_full(sjf_result)
    gantt_chart(sjf_result)
