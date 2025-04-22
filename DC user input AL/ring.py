class RingProcess:
    def __init__(self, id):
        self.id = id
        self.coordinator = None
        self.next = None 

    def start_election(self):
        print(f"\nProcess {self.id} starts an election.")
        active_list = [self.id]
        self.send_election_message(active_list)

    def send_election_message(self, active_list):
        if self.next:
            print(f"Process {self.id} forwards election list {active_list}.")
            self.next.receive_election_message(active_list)

    def receive_election_message(self, active_list):
        if self.id not in active_list:
            active_list.append(self.id)
            self.send_election_message(active_list)
        else:
            new_coordinator = max(active_list)
            print(f"\nProcess {self.id} elects {new_coordinator} as the coordinator.")
            self.send_coordinator_message(new_coordinator)

    def send_coordinator_message(self, new_coordinator):
        if self.next:
            print(f"Process {self.id} informs that {new_coordinator} is the new coordinator.")
            self.coordinator = new_coordinator
            self.next.receive_coordinator_message(new_coordinator)

    def receive_coordinator_message(self, new_coordinator):
        if self.coordinator is None:
            self.coordinator = new_coordinator
            self.send_coordinator_message(new_coordinator)


# ---------------- USER INPUT ----------------

n = int(input("Enter number of processes: "))
ids = []

print("Enter the IDs of the processes:")
for _ in range(n):
    ids.append(int(input()))

processes = [RingProcess(i) for i in ids]

# linking in ring
for i in range(len(processes)):
    processes[i].next = processes[(i + 1) % len(processes)]

starter_id = int(input("Enter ID of process that starts the election: "))

# find process with given ID and start election
for p in processes:
    if p.id == starter_id:
        p.start_election()
        break
