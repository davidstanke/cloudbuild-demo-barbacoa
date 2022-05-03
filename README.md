# cloudbuild-demo-barbacoa

Demo of GCP software delivery tools


- Basic flask app; code is in `/app`
  - deployed app: [What's the Word?](http://prod.barbacoa.doingdevops.com/)
- K8s manifests in `/app/kubernetes`: (Ingress:Service:Deployment)
- Cloud deploy config in `delivery-config.yaml`: (Dev --> Stage --> Prod)
    - `gcloud deploy apply --file=delivery-config.yaml --region=us-east1`
- CD is initiated by Cloud Build in `cloudbuild.yaml`
  - Trigger config:
    - trigger on tag
    - (will run steps: build/push/cut a release and deploy to dev)
    - in trigger config, create a substitution var: `_SANITIZED_TAG_NAME` = `${TAG_NAME//./-}`
