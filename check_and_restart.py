import os
import subprocess
from datetime import datetime, timedelta

# Path to the log files
log_files = {
    "folding-miner": "/path/to/folding-miner.log",
    #"folding-miner2": "/path/to/folding-miner2.log"
}

# Time interval to check (in minutes)
time_interval = 90

def get_last_modified_time(file_path):
    try:
        return datetime.fromtimestamp(os.path.getmtime(file_path))
    except FileNotFoundError:
        return None

def restart_pm2_process(process_name):
    subprocess.run(["pm2", "restart", process_name])

def check_and_restart():
    now = datetime.now()
    for process_name, log_file in log_files.items():
        last_modified_time = get_last_modified_time(log_file)
        if last_modified_time is None:
            print(f"Log file for {process_name} not found.")
            continue
        time_diff = now - last_modified_time
        if time_diff > timedelta(minutes=time_interval):
            print(f"Restarting {process_name} as its log file has not been updated for {time_interval} minutes.")
            restart_pm2_process(process_name)

if __name__ == "__main__":
    check_and_restart()
