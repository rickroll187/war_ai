import multiprocessing
from swarms.mini_swarm import run_tasks
from utils.agent_client import AgentClient

def main():
    print("[Mini Swarm] Starting Boss-Worker orchestrator...")
    agent_client = AgentClient(model='phi3-mini-amd')
    processes = []
    for task_name in ['github_triage', 'research', 'crypto_monitor']:
        p = multiprocessing.Process(target=run_tasks, args=(task_name, agent_client))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print("[Mini Swarm] All tasks completed.")

if __name__ == "__main__":
    main()
