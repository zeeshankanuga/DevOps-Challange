1️ User & Group Management
Learn about Linux users, groups, and permissions (/etc/passwd, /etc/group).
Task:
Create a user devops_user and add them to a group devops_team.
Set a password and grant sudo access.
Restrict SSH login for certain users in /etc/ssh/sshd_config.
```
Answer:
useradd devops_user
sudo useradd -m devops_user1

sudo groupadd devops_team
sudo usermod -aG devops_team devops_user1
```
-----------------------------------------------------

2️ File & Directory Permissions
Task:
Create /devops_workspace and a file project_notes.txt.
Set permissions:
Owner can edit, group can read, others have no access.
Use ls -l to verify permissions.
```
Answer:
mkdir devops_workspace
touch project_notes.txt
chmod 770 project_notes.txt
```
-----------------------------------------------------
3️ Log File Analysis with AWK, Grep & Sed
Logs are crucial in DevOps! You’ll analyze logs using the Linux_2k.log file from LogHub (GitHub Repo).

Task:
Download the log file from the repository.
Extract insights using commands:
Use grep to find all occurrences of the word "error".
Use awk to extract timestamps and log levels.
Use sed to replace all IP addresses with [REDACTED] for security.
Bonus: Find the most frequent log entry using awk or sort | uniq -c | sort -nr | head -10.
```
Answer:
wget https://github.com/logpai/loghub/blob/master/Linux/Linux_2k.log
grep -r "error" .
awk '{print $1}' Linux_2k.log
```
-----------------------------------------------------
4️ Volume Management & Disk Usage
Task:
Create a directory /mnt/devops_data.
Mount a new volume (or loop device for local practice).
Verify using df -h and mount | grep devops_data.
```
Answer:
sudo mkdir /mnt/devops_data
sudo mkfs.ext4 /dev/nvme1n1
sudo mount /dev/nvme1n1 /mnt/devops_data/

/dev/nvme1n1     9.8G   24K  9.3G   1% /mnt/devops_data
```
-----------------------------------------------------
5️ Process Management & Monitoring
Task:
Start a background process (ping google.com > ping_test.log &).
Use ps, top, and htop to monitor it.
Kill the process and verify it's gone.
```
Answer:
nohup ping google.com > ping_output.txt &
kill 1615
```
-----------------------------------------------------
6️ Automate Backups with Shell Scripting
Task:
Write a shell script to back up /devops_workspace as backup_$(date +%F).tar.gz.
Save it in /backups and schedule it using cron.
Make the script display a success message in green text using echo -e.
```
Answer:
ubuntu@ip-172-31-10-167:~/devops_workspace$ cat backup.sh
#!/bin/bash

# Define variables for the backup
SOURCE_DIR="/home/ubuntu/devops_workspace/"
BACKUP_DIR="/home/ubuntu/devops_workspace/backups"

# Create the backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create a unique filename with the current date
BACKUP_FILE="$BACKUP_DIR/backup_$(date +%F_%H-%M).tar.gz"

# Create the compressed tar archive
tar -czvf "$BACKUP_FILE" "$SOURCE_DIR"


echo "Backup completed successfully"
```