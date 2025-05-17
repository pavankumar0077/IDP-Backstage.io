```
  321  pip install psutil
  322  pip install jsonify
```
```
docker login -u pavan0077
  338  docker images;
  339  docker build -t python-app:v1 .
  340  docker run -p 5000:5000 python-app:v1
  341  docker tag python-app:v1 pavan0077/python-app:v1
  342  docker push pavan0077/python-app:v1
  344  kubectl get pods -A
  345  kubectl cluster-info
  346  docker ps
  349  kubectl config current-context
  350  kubectl get nodes
  351  kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.1/deploy/static/provider/cloud/deploy.yaml
  352  kubectl wait --namespace ingress-nginx   --for=condition=Ready pod   --selector=app.kubernetes.io/component=controller   --timeout=180s
  353  kubectl get svc -n ingress-nginx
  354  kubectl get pods -n ingress-nginx

  356  kubectl apply -f deploy.yaml 
  357  kubectl get deploy
  358  kubectl get pods

  360  kubectl apply -f service.yaml
  361  kubectl get svc
  362  kubectl describe service python-app
  363  kubectl get ingressclass
  364  kubectl apply -f ingress.yaml
  365  kubectl get ingress

  363  kubectl get ingressclass


```


