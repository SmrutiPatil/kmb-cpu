#!/bin/bash

run_executable() {
    local exec="$1"
    local instance="$2"
    local instance_file="../instances/$instance.gr"
    local output=$(./build/"$exec" < "$instance_file" -o)
    local value=$(echo "$output" | grep "VALUE" | awk '{print $2}')
    local time=$(echo "$output" | grep "TIME" | awk '{print $2}')
    local nodes=$(grep "Nodes" "$instance_file" | awk '{print $2}')
    local edges=$(grep "Edges" "$instance_file" | awk '{print $2}')
    local terminals=$(awk '/^Terminals/{print $2}' "$instance_file")
    echo "$instance,$value,$time,$nodes,$edges,$terminals"
}

create_or_append_csv() {
    local exec="$1"
    local output_file="results/$exec.csv"
    if [ ! -f "$output_file" ]; then
        echo "instance,value,time,nodes,edges,terminals" > "$output_file"
    fi
    for i in {1..50}; do
        instance=$(printf "instance%03d" "$i")
        result=$(run_executable "$exec" "$instance")
        echo "$result" >> "$output_file"
    done
}

if [ $# -ne 1 ]; then
    echo "Usage: $0 <executable_name>"
    exit 1
fi

executable_name="$1"
create_or_append_csv "$executable_name"
