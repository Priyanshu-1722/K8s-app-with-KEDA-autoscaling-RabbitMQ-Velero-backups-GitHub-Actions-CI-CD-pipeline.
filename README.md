```
# 🚀 Full-Stack Kubernetes App with KEDA, RabbitMQ, Velero & GitHub Actions CI/CD

This project demonstrates deploying a full-stack web application on Kubernetes with:

- ⚙️ KEDA for event-driven autoscaling using RabbitMQ
- 📨 RabbitMQ for messaging between frontend and backend
- 💾 Velero for scheduled backups of Kubernetes resources and persistent volumes
- 🔁 GitHub Actions for CI/CD (build, test, deploy)
- 📈 Prometheus + Grafana (optional) for monitoring and observability

> A production-grade, DevOps-ready application stack built with modern cloud-native tooling.

---

## 🧱 Tech Stack

| Layer         | Technology                             |
|--------------|-----------------------------------------|
| Frontend      | Vue.js (containerized)                 |
| Backend       | FastAPI (Python)                       |
| Messaging     | RabbitMQ                               |
| Database      | PostgreSQL (optional)                  |
| Infra         | Kubernetes (GKE, EKS, AKS, Minikube)   |
| CI/CD         | GitHub Actions                         |
| Autoscaling   | KEDA (based on RabbitMQ queue length)  |
| Backup        | Velero                                 |
| Monitoring    | Prometheus + Grafana (optional)        |

---
```
## 📁 Project Structure

````

.
├── frontend/           # Vue.js app
├── backend/            # FastAPI service
├── k8s/                # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── keda.yaml
│   ├── velero/
│   └── ...
├── .github/workflows/  # GitHub Actions CI/CD
├── Dockerfile          # For backend (FastAPI)
├── docker-compose.yml  # For local dev
└── README.md

````

---

## ⚙️ Prerequisites

- Docker
- Kubernetes cluster (Minikube or Cloud: GKE, EKS, AKS)
- kubectl
- Helm (for installing KEDA, RabbitMQ, Velero)
- GitHub account (for CI/CD)
- Velero CLI (`brew install velero` or [install](https://velero.io/docs/))

---

## 🚀 Deployment Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/k8s-fullstack-app.git
cd k8s-fullstack-app
````

---

### 2. Build and Push Docker Images

```bash
# Frontend
docker build -t your-dockerhub-user/frontend-app ./frontend
docker push your-dockerhub-user/frontend-app

# Backend
docker build -t your-dockerhub-user/backend-api ./backend
docker push your-dockerhub-user/backend-api
```

---

### 3. Deploy to Kubernetes

```bash
# Create namespace
kubectl create ns fullstack-app

# Deploy RabbitMQ using Helm
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install rabbitmq bitnami/rabbitmq -n fullstack-app

# Apply app manifests
kubectl apply -f k8s/ -n fullstack-app
```

---

### 4. Install and Configure KEDA

```bash
helm repo add kedacore https://kedacore.github.io/charts
helm install keda kedacore/keda --namespace keda --create-namespace

# Apply KEDA ScaledObject
kubectl apply -f k8s/keda.yaml -n fullstack-app
```

---

### 5. Install Velero for Backups

```bash
velero install \
  --provider <cloud-provider> \
  --plugins <plugin-image> \
  --bucket <your-bucket-name> \
  --backup-location-config <config>

# Example backup schedule
velero create schedule daily-backup --schedule="0 2 * * *"
```

---

### 6. GitHub Actions CI/CD Setup

* Add your DockerHub credentials and K8s config as GitHub Secrets:

  * `DOCKER_USERNAME`
  * `DOCKER_PASSWORD`
  * `KUBE_CONFIG`

* GitHub Actions workflow is in `.github/workflows/deploy.yaml`

---

## 📊 Monitoring 

Install Prometheus and Grafana using Helm:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack
```

Access Grafana:

```bash
kubectl port-forward svc/prometheus-grafana 3000:80 -n default
# Visit http://localhost:3000
# Default login: admin / prom-operator
```

---

## 🧪 Testing

You can test message flow with:

1. Sending frontend request (e.g., form submission)
2. Watching messages appear in RabbitMQ
3. Confirming backend scales via KEDA (use `kubectl get hpa` or `kubectl get pods`)
4. Check logs with `kubectl logs`

---

## 🛡️ Security Considerations

* Use Kubernetes Secrets to store credentials
* Enable RBAC and network policies
* Scan Docker images regularly

---

## 📦 Future Improvements

* Add PostgreSQL + persistent volume claims
* Ingress setup with HTTPS
* Argo CD for GitOps deployment

---
