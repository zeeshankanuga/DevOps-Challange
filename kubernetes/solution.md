## Task-1

### Kubernetes Architecture

#### Master Node Components

* **API Server**: responsible for serving the Kubernetes API.
* **Scheduler**: determines which node a pod should run on.
* **etcd**: a distributed key-value store used for storing cluster state.
* **Controller Manager**: runs controllers that manage the cluster.

#### Worker Node Components

* **kubelet**: responsible for running and managing containers on the node.
* **kube proxy**: provides network access to services running inside pods.

#### Networking Components

* **CNI (Container Network Interface)**: responsible for providing networking to containers.
* **kubectl**: a command-line tool used for interacting with the Kubernetes cluster.

### Pod Configuration
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: nginx-ns

spec:
  containers:
  - name: nginx
    image: nginx:latest
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
    ports:
      - containerPort: 80
```

## Task-2
### Namespace YAML File
The namespace YAML file is created and deployed in Kubernetes.

here is namespace yaml
```
apiVersion: v1
kind : Namespace
metadata:
  name: nginx-ns
```