<h1>A simple Python(flask) app dockerized and prepared for CI-CD on Google Cloud</h1>

A simple connectivity test made with a HTTP GET request

<h2>Building and running the app locally</h2>
Find yourself in the connectivity folder </br>

```
cd connectivity
docker build -t connectivity-test .
docker run -d -p 80:8080 connectivity-test`
```

<h2>Deploying to a k8s cluster manualy</h2>
In the root folder:

`kubectl apply -f /k8s`

Will apply a deployment of the app complete with two pods and the connecting service on the cluster. 

<h3>App resilience:</h3> 
For app resilience I utilised the built-in auto scaler, which is currently set at minimum 2 and max 10 instances based on CPU usage.
