<b> WAZUH TEST <b> 

Wazuh technical test - [Python - Flask - React - TypeScript]



<b>EXECUTE<b> 

- Create both images

```
docker build --file=frontend/Dockerfile  -t wazuh-frontend .
docker build --file=backend/Dockerfile  -t wazuh-backend .
```

- Run containers

```
docker run --rm -it -p 8000:5000 wazuh-backend
docker run --rm -it -p 3000:3000 wazuh-frontend
```

Open navegator on url=localhost:3000