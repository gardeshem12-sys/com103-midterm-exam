project_title = input("Enter the project title: ")
group_name = input("Enter the group name: ")

# 2. Hardcoded task types (name + hours)
task_names = [
    "Program Logic / Coding",
    "UI / Output Formatting",
    "Testing & Debugging",
    "Documentation / README",
    "Presentation Slides"
]

task_hours = [6, 3, 2, 2, 2]


print("\n==========================================")
print("   COM 103 PROJECT -- TASK TYPES")
print("==========================================")


for i in range(5):  
    print(f"{i+1}. {task_names[i]} [{task_hours[i]} hours]")

print("==========================================")


assigned_tasks = []
total_points = 0
tasks_assigned = 0

for i in range(4):  
    print(f"\n--- TASK {i+1} ---")
   
    task_num = int(input("Enter task number (1-5), or 0 to skip: "))

    
    if task_num == 0:
        continue

    if 1 <= task_num <= 5:  
        member_name = input("Enter member's name: ")
        status = input("Enter status (done/pending): ").lower()

        
        if status == "done":
            points = 2
        elif status == "pending":
            points = 1
        else:
            print("Invalid status. Please use 'done' or 'pending'.")
            continue
       
        
        total_points += points
        tasks_assigned += 1
       
        assigned_tasks.append({
            "task_name": task_names[task_num - 1],
            "task_hours": task_hours[task_num - 1],
            "member_name": member_name,
            "status": status,
            "points": points
        })0


if tasks_assigned > 0:
    max_points = tasks_assigned * 2  
    progress = (total_points / max_points) * 100
else:
    max_points = 0
    progress = 0


if progress >= 75:
    project_status = "PROJECT READY!"
elif progress >= 50:
    project_status = "ON TRACK."
else:
    project_status = "NEEDS MORE WORK!"


print("\n================================================")
print(f"     {project_title} -- TASK BOARD")
print("================================================")
print(f"Project : {project_title}")
print(f"Group   : {group_name}")
print("------------------------------------------------")

for i in range(len(assigned_tasks)):
    task = assigned_tasks[i]
    print(f"Task {i+1}: {task['task_name']:<25} [{task['task_hours']} hours]")
    print(f"    Assigned to : {task['member_name']}")
    print(f"    Status      : {task['status']}")
    print(f"    Points      : {task['points']} / 2\n")

print("------------------------------------------------")
print(f"Total Points Earned   : {total_points} / {max_points}")
print(f"Progress              : {int(progress)}%")
print(f"Project Status        : {project_status}")
print("================================================")
