class Process:
    def __init__(self, pid):
        self.pid = pid
        self.waiting_for = []

    def request_resource(self, resource_holders, initiator):
        if not resource_holders:
            print(f"Process {self.pid} found no resource holders.")
            return False
        
        for holder in resource_holders:
            probe = [initiator, self.pid, holder.pid]
            print(f"Process {self.pid} sending probe {probe} to {holder.pid}")
            if holder.receive_probe(probe):
                print(f"Deadlock detected involving process {initiator}!")
                return True
        return False

    def receive_probe(self, probe):
        initiator, sender, receiver = probe
        print(f"Process {self.pid} received probe {probe}")
        
        if self.pid == initiator:
            print(f"Cycle detected! Process {self.pid} is in a deadlock.")
            return True
        
        if not self.waiting_for:
            print(f"Process {self.pid} is not waiting for any resource. Ignoring probe.")
            return False
        
        for next_holder in self.waiting_for:
            new_probe = [initiator, self.pid, next_holder.pid]
            print(f"Process {self.pid} forwarding probe {new_probe} to {next_holder.pid}")
            if next_holder.receive_probe(new_probe):
                return True
        
        return False


# ---------------- USER INPUT ----------------

def create_processes():
    n = int(input("Enter number of processes: "))
    processes = {}

    for _ in range(n):
        pid = int(input("Enter process ID: "))
        processes[pid] = Process(pid)

    print("\nDefine 'waits-for' relationships.")
    for pid in processes:
        wait_ids = input(f"Process {pid} is waiting for (space-separated IDs, or press Enter if none): ")
        if wait_ids.strip():
            wait_list = list(map(int, wait_ids.strip().split()))
            processes[pid].waiting_for = [processes[wid] for wid in wait_list if wid in processes]

    return processes

# Run for one case
print("\n--- Deadlock Detection ---")
procs = create_processes()

start_pid = int(input("\nEnter initiator process ID: "))
target_pids = input("Enter process IDs this process is requesting resource from (space-separated): ")
targets = [procs[int(pid)] for pid in target_pids.strip().split() if int(pid) in procs]

if procs[start_pid].request_resource(targets, start_pid):
    print("Deadlock confirmed.")
else:
    print("No deadlock detected.")
