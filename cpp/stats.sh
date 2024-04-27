#!/bin/bash

run_executable() {
    local exec="$1"
    local instance="$2"
    local flags="$3"
    local instance_file="../instances/$instance.gr"
    local output=$(./build/"$exec" "$flags" < "$instance_file")
    local value=$(echo "$output" | grep "VALUE" | awk '{print $2}')
    local time=$(echo "$output" | grep "TIME" | awk '{print $2}')
    local nodes=$(grep "Nodes" "$instance_file" | awk '{print $2}')
    local edges=$(grep "Edges" "$instance_file" | awk '{print $2}')
    local terminals=$(awk '/^Terminals/{print $2}' "$instance_file")
    echo "$instance,$value,$time,$nodes,$edges,$terminals"
}

if [ $# -ne 5 ]; then
    echo "Usage: $0 <executable_name> <output_file_name> <start_instance> <end_instance> <flags>"
    exit 1
fi

executable_name="$1"
output_file="$2"
start_instance="$3"
end_instance="$4"
flags="$5"

create_or_append_csv() {
    local exec="$1"
    local output_file="$2"
    local start_instance="$3"
    local end_instance="$4"
    local flags="$5"
    if [ ! -f "results/$output_file" ]; then
        echo "instance,value,time,nodes,edges,terminals" > "results/$output_file"
    fi
    for ((instance=start_instance; instance<=end_instance; instance++)); do
        result=$(run_executable "$exec" "instance$(printf "%03d" "$instance")" "$flags")
        echo "$result" >> "results/$output_file"
    done
}

create_or_append_csv "$executable_name" "$output_file" "$start_instance" "$end_instance" "$flags"
