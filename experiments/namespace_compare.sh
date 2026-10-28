#!/bin/bash
echo "Hostname:       $(hostname)"
echo "My PID:         $$"
echo "Process count:  $(ps -e --no-headers | wc -l)"
echo "PID namespace:  $(readlink /proc/self/ns/pid)"
echo "UTS namespace:  $(readlink /proc/self/ns/uts)"
echo
echo "--- Visible processes ---"
ps -eo pid,ppid,comm

