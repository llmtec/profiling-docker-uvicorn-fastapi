# In-Docker profiling of Uvicorn + FastAPI

This guide provides detailed instructions on how to profile a Uvicorn-deployed FastAPI application inside Docker. Follow these steps to build your image, run your container, and enable optional profiling for performance analysis.

Please see our blogpost here: 
https://www.llmtec.com/blogposts/profiling-app-combining-docker-uvicorn-fastapi

## Pre-requisites

- Docker installed on your system

## Building and Running Your Docker+Uvicorn+FastAPI Application

To deploy your FastAPI application without profiling, execute the following commands. These commands build your Docker image, remove any existing container with the same name, and run your application in a new container.

```sh
# Build the Docker image
docker build -t myfastapiapp .

# Remove any existing container
docker rm -f myfastapiapp_container || true

# Run the application in a new container
docker run -d --name myfastapiapp_container -p 8000:8000 myfastapiapp
```

Alternatively, you can combine these commands into a single line for convenience:

```sh
docker rm -f myfastapiapp_container || true && docker build -t myfastapiapp . && docker run -d --name myfastapiapp_container -p 8000:8000 myfastapiapp
```

## Version with Profiling Enabled

### Create the folder where you'll save profiling reports

```sh
mkdir profiling_results
```

### Build and run the application in a new container with profiling enabled

```sh
docker rm -f myfastapiapp_container || true && docker build --build-arg PROFILE_APP=true -t myfastapiapp . && docker run -d --name myfastapiapp_container -v $(PWD)/profiling_results:/app/profiling_results -p 8000:8000 myfastapiapp
```

In this command, `-v $(PWD)/profiling_results:/app/profiling_results` is the volume mount part. `$(PWD)/profiling_results` is the directory on your host machine where you want the profiling reports to be saved, and `/app/profiling_results` is the directory inside the container where profiling_app.py will save the profiling report. Make sure your `main.py` script is modified to save the profiling report to `/app/profiling_results/profiling_results.prof`, or adjust the paths accordingly.


### Test your FastAPI app

Run a simple request:

```shell
curl http://localhost:8000/sum/100
```

## Analyzing Profiling Results

Make sure you ran the application with profiling enabled (both Docker build and Docker run).

Shutdown the container in order to generate the profiling report. 
```sh
docker stop myfastapiapp_container
```

Then run the Python notebook provided.


