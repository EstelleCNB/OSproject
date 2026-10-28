import time

def cgroup_value(name):
    try:
        path = open("/proc/self/cgroup").read().strip().split("::")[1]
        return open(f"/sys/fs/cgroup{path}/{name}").read().strip()
    except Exception:
        return "n/a"

print("Configured cpu.max :", cgroup_value("cpu.max"))

start = time.monotonic()
cpu_start = time.process_time()
count = 0
while time.monotonic() - start < 5:
    count += 1

wall = time.monotonic() - start
cpu = time.process_time() - cpu_start
print(f"Iterations         : {count}")
print(f"Wall time (s)      : {wall:.2f}")
print(f"CPU time used (s)  : {cpu:.2f}")
print(f"Measured CPU share : {cpu / wall * 100:.1f}%")
