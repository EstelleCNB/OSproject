#!/bin/bash
run() {
    label="$1"; shift
    echo "##### $label"
    echo "Command: $*"
    "$@" 2>&1
    echo "Exit status: $?"
    echo
}

CPU="python3 experiments/cpu_test.py"
MEM="python3 experiments/memory_test.py"

run "CPU: unlimited"        sudo systemd-run --scope -q $CPU
run "CPU: quota 20%"        sudo systemd-run --scope -q -p CPUQuota=20% $CPU
run "CPU: quota 50%"        sudo systemd-run --scope -q -p CPUQuota=50% $CPU

run "Memory: unlimited, 50 MB"            sudo systemd-run --scope -q $MEM 50
run "Memory: limit 100M, allocate 50 MB"  sudo systemd-run --scope -q -p MemoryMax=100M -p MemorySwapMax=0 $MEM 50
run "Memory: limit 100M, allocate 200 MB" sudo systemd-run --scope -q -p MemoryMax=100M -p MemorySwapMax=0 $MEM 200
