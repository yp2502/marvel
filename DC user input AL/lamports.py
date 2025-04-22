class LamportClock:
    def __init__(self, process_id):
        self.process_id = process_id
        self.clock = 0

    def internal_event(self):
        self.clock += 1
        print(f"[Process {self.process_id}] Internal event → Clock = {self.clock}")

    def send_request(self, to_process_id):
        self.clock += 1
        print(f"[Process {self.process_id}] Sent message to Process {to_process_id} → Timestamp = {self.clock}")
        return self.clock

    def receive_request(self, timestamp, from_process_id):
        self.clock = max(self.clock, timestamp) + 1
        print(f"[Process {self.process_id}] Received message from Process {from_process_id} (timestamp {timestamp}) → Clock = {self.clock}")


def simulate_with_input():
    n = int(input("Enter number of processes: "))
    processes = {i: LamportClock(i) for i in range(1, n + 1)}
    send_history = {}  # key = (from, to), value = timestamp

    print("\nDefine events for each process:")
    print("For each event, enter:\n  - 'i' for internal\n  - 's <to_pid>' to send to process\n  - 'r <from_pid>' to receive from process")
    print("Example: i\n         s 2\n         r 1")

    event_lists = {}

    for pid in processes:
        num_events = int(input(f"\nHow many events for Process {pid}? "))
        event_lists[pid] = []
        for _ in range(num_events):
            event = input(f"Enter event for Process {pid}: ").strip().split()
            event_lists[pid].append(event)

    print("\n--- Simulation Start ---\n")
    for round in range(max(len(v) for v in event_lists.values())):
        for pid in range(1, n + 1):
            if round < len(event_lists[pid]):
                event = event_lists[pid][round]
                proc = processes[pid]

                if event[0] == "i":
                    proc.internal_event()

                elif event[0] == "s":
                    to_pid = int(event[1])
                    timestamp = proc.send_request(to_pid)
                    send_history[(pid, to_pid)] = timestamp

                elif event[0] == "r":
                    from_pid = int(event[1])
                    if (from_pid, pid) in send_history:
                        recv_timestamp = send_history[(from_pid, pid)]
                        proc.receive_request(recv_timestamp, from_pid)
                    else:
                        print(f"[Process {pid}] ERROR: No message found from Process {from_pid}")

    print("\n--- Simulation End ---\n")

simulate_with_input()
