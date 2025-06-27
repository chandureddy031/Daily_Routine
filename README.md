# Daily_Routine

mkdir ai-productivity-suite
cd ai-productivity-suite


# Save this as create_structure.sh in your root dir and run: bash create_structure.sh

mkdir -p backend/{agents,services,tasks,utils}
touch backend/agents/{orchestrator.py,parser_agent.py,booking_agent.py,payment_agent.py,research_agent.py}
touch backend/services/{email_service.py,calendar_service.py,payment_service.py,memory_service.py}
touch backend/tasks/task_manager.py
touch backend/utils/{config.py,logger.py,security.py}
touch backend/main.py

mkdir -p frontend/{public,src/components,src/services}
touch frontend/src/components/{Dashboard.jsx,TaskQueue.jsx,ApprovalModal.jsx}
touch frontend/src/services/api.js
touch frontend/src/{App.js,index.js}

mkdir -p infrastructure/{prometheus,grafana}
touch infrastructure/docker-compose.yml
touch infrastructure/prometheus/prometheus.yml
touch infrastructure/grafana/dashboard.json

mkdir -p models
touch models/llama-3-8b-instruct.Q4_K_M.gguf

mkdir -p scripts
touch scripts/{install_deps.sh,download_model.sh,run_scheduler.sh}

touch .env .gitignore requirements.txt package.json README.md

