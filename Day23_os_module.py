import os

# 1. Create the parent directory safely if it doesn't exist
if not os.path.exists("python learning journey"):
    os.mkdir("python learning journey")

# 2. Create Day 1 to Day 100 (Notice range(100) starts from 0, making Day 1 to Day 100)
for x in range(100):
    folder_name = f"python learning journey/Day {x+1}"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

# 3. List the top-level directories
folders = os.listdir("python learning journey")
print("All Folders:", folders)

# 4. Safely list contents of Day 10 (Now it safely exists!)
print("Day 10 Contents:", os.listdir("python learning journey/Day 10"))
