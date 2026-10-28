import resource
import sys
import time

def cgroup_value(name):
    try:
        path = open("/proc/self/cgroup").read().strip().split("::")[1]
        return open(f"/sys/fs/cgroup{path}/{name}").read().strip()
    except Exception:
        return "n/a"

target_mb = int(sys.argv[1]) if len(sys.argv) > 1 else 50
print("Configured memory.max:", cgroup_value("memory.max"))
print("Target allocation (MB):", target_mb)

chunks = []
for i in range(target_mb // 10):
    chunks.append(bytearray(b"\x01") * (10 * 1024 * 1024))
    print(f"Allocated {(i + 1) * 10} MB", flush=True)
    time.sleep(0.1)

peak_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
print(f"Peak RSS (MB): {peak_mb:.1f}")
print("Memory test finished.")

