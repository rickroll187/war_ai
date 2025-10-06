def run_tasks(task_name, agent_client):
    print(f"[Mini Swarm] Executing {task_name} task...")
    result = agent_client.run(task_name)
    print(f"[Mini Swarm] {task_name} result: {result}")
