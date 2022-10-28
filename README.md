## Submission
- To run the server, we will do the following. Make sure the server can be **started this way**.

```shell
cd django_exercise
docker build -t exercise .
docker run --rm -p 8000:8000 -v $(pwd):/app exercise
```a