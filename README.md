Just run

file-name is the image name.
```
docker build -t <file-name> .
docker run -p 5001:5000 <file-name>

```

The server will start runnuing locally at localhost:5001


Sample Data
```
curl -X POST -H "Content-Type: application/json" \
-d '{"text": "Docker is an amazing technology!"}' \
http://localhost:5001/analyze

```
