# cloudbuild-demo-barbacoa

Demo of GCP software delivery tools


- Basic flask app; code is in `/app`
- K8s manifests in `/app/kubernetes`: (Ingress:Service:Deployment)
- Cloud deploy config in `delivery-config.yaml`: (Dev --> Stage --> Prod)
- CD is initiated by Cloud Build in `cloudbuild.yaml`
  - (Trigger config: when a new tag is generated on the repo, build the image and create a rollout [starting at Dev])
