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

### Deployment:
it is used when we need to maintain rolling update of the application.
Example: Let's say we have an application with multiple versions, and we want to roll out a new version while keeping the previous one available in case something goes wrong. We can use a deployment YAML file like this:

### StatefulSet:
Imagine you're running a database application where data needs to be persisted even when pods restart or get deleted. A StatefulSet is like a pod, but it guarantees that each replica has a unique identity and that the replicas maintain their state.

Let's say we have a WordPress application with 3 pods, named `wp-0`, `wp-1`, and `wp-2`. The StatefulSet will ensure that:

* Each pod has its own persistent storage (e.g., an SSD) where data is stored.
* When a pod restarts or gets deleted, it can be replaced by a new one with the same name and identical configuration.
* The pods are scaled up or down as needed.

### DaemonSets
A DaemonSet is used when you need to run a container on every node in your cluster. This is useful for applications that require a service to be running on each node, such as:

* Logging agents (e.g., Fluentd)
* Monitoring agents (e.g., Prometheus)
* File system backup tools

For example, let's say we have an application that requires a logging agent to run on every node. We can use a DaemonSet YAML file like this:


### Horizontal Pod Scaling
Horizontal Pod Scaling is used when you need to scale your application based on demand. This is useful for applications that require more resources as the load
increases, such as:

* A web server
* A database server

For example, let's say we have a web server that requires 2 CPU cores and 4GB of RAM. We
can use a Horizontal Pod Scaling YAML file like this to scale our application based on demand

### RBAC
Role-Based Access Control (RBAC) is used when you need to control access to your cluster resources. This is useful for applications that require fine-grained access control.

### HELM
Helm is a package manager which can help to deploy application. It helps to manage the deployment of multiple Kubernetes objects in a declarative way, making it easier to manage and update your applications.


### ISTIO

Istio is an open-source service mesh platform that allows you to manage traffic, security, and observability across microservices. Here's how it works with Kubernetes:

* **Sidecar Pattern**: Istio uses a sidecar pattern where each application has a companion container (the "sidecar") that manages the traffic and communication between the application and other services.
* **Service Mesh**: The service mesh is a layer of abstraction between the application and the underlying infrastructure. It provides a standardized way to manage traffic, security, and observability across microservices.

To deploy Istio with Kubernetes, you need to create several YAML files:

### istio-config.yaml
apiVersion: install.istio.io/v1beta1
kind: IstioConfiguration
metadata:
  name: sample-istioconfig
spec:
  clusterName: kubernetes
  istioNamespace: istio-system

---
### gateway.yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: sample-gateway
spec:
  selector:
    istio: ingressgateway # use the istio default ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*"

---
### virtual-service.yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: sample-virtualservice
spec:
  hosts:
  - "sample.com"
  http:
  - match:
      uri:
        prefix: "/"
    rewrite:
      uri: "/new-path"
---
### destination-rule.yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: sample-destinationrule
spec:
  host: sample.com
  trafficPolicy:
    tls:
      mode: ISTIO_MUTUAL


## Author

Zeeshan Kanuga — Technical Architect