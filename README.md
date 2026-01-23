# Containerization

: FindTheFlagChallenge, IBDChallenge

## What is Containerization?

Containerization is a lightweight form of virtualization that packages applications and their dependencies together. It allows for:

- Faster software deployment.
- Easier management of dependencies.
- Improved scalability and security.

## How Do Computer Programs Work?

### OS-Driven Application Development

(Source: *Operating Systems - Internals and Design Principles, 7th ed., W. Stallings, Pearson, 2012*)

- Operating Systems (OS) provide layers of abstraction.
- Developers work with high-level libraries while the OS manages low-level processes.
- The OS handles resource allocation, execution, and device communication.

### Example: Python Program Execution

```python
import numpy as np
a = np.array([1,2,3,4])
b = np.mean(a)
print(b)

```

- The Python interpreter locates and loads necessary libraries.
- Executes commands sequentially.
- The OS handles:
    - CPU interfacing for calculations.
    - Memory allocation.
    - Displaying results on the monitor.

## What are Virtual Machines (VM)?

- Allow multiple OS instances to run on a single physical machine.
- Examples: VMWare, VirtualBox.
- Users can run Linux, AIX, FreeBSD, and even macOS on Windows.

## What are Containers?

- Containers offer a more efficient alternative to VMs by virtualizing only the application layer.
- Benefits:
    - Reduces dependency management overhead.
    - Ensures consistency across environments.
    - Enables faster development and deployment.
- Popular container tools: **Docker, Podman**.

## How Do Containers Work?

1. **Install Docker Daemon** on development machines.
2. **Use Docker API** to create container images.
3. **Deploy images to a container registry** (Docker Hub, AWS ECR, etc.).
4. **Run containers** on any compatible machine.

## Benefits of Containerization

- Share and execute code seamlessly.
- Package software dependencies within containers.
- Run software across Linux, Windows, and macOS without modification.
- Rapid development and testing.

## Containerization Basics

### Key Concepts:

- **Container Creation**: Use base images to create customized environments.
- **Container Repositories**: Store and share container images.
- **Container Handling**: Run, stop, and manage containers.
- **Container Development**: Debugging, layering, and optimizing containers.

## Docker Configuration and Installation

1. **Download and Install Docker Desktop** ([Docker Official Site](https://www.docker.com/products/docker-desktop)).
2. **Create a Docker Hub Account**.
3. **For Windows Users**:
    - Use Windows Subsystem for Linux (WSL) ([WSL Installation Guide](https://learn.microsoft.com/en-us/windows/wsl/install)).

## Creating Docker Containers

### Example Dockerfile:

```
FROM python:3.7-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY /path/to/code/ .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

```

### Building and Running a Container:

```bash
docker build -t my_python_app .

#running on the backend as a daemon
docker run -d my_python_app

#running in the foreground
docker run -it my_python_app

#OPTIONAL: tag the image with a version number
docker tag my_python_app my_python_app:1.0

```

## Pushing Docker Images to a Repository

1. **Tag an Image**
    
    ```bash
    docker tag my_python_app my_dockerhub_user/my_python_app:latest
    
    #you can also append the tag instead of "latest"
    docker tag my_python_app my_dockerhub_user/my_python_app:1.0
    
    ```
    
2. **Push the Image**
    
    ```bash
    docker push my_dockerhub_user/my_python_app:latest
    
    ```
    

## Running Containers

- **One-time execution**:
    
    ```bash
    docker run my_python_app:1.0
    
    ```
    
- **Run in the background (daemon mode)**:
    
    ```bash
    docker run -d my_python_app:1.0
    
    ```
    
- **Assign a container name**:
    
    ```bash
    docker run -d --name my_container my_python_app:1.0
    
    ```
    

## Debugging Containers

### Using a Debug Dockerfile:

```
FROM python:3.7-alpine
CMD tail -f /dev/null  # Keeps the container running for debugging

```

### Running and Accessing the Debug Container:

```bash
docker build -t debug_python_app -f Dockerfile.debug .
docker run -d --name debug_container debug_python_app

```

To access the running container:

```bash
docker exec -it debug_container /bin/sh

```

## Layering Containers

- **Build and tag**: `docker build -t my_python_app:1.0 .`
- **Run container**: `docker run -d --name layered_ex1 my_python_app:1.0`

---

## Advanced Docker Topics

- **File and Data Handling**:
    - Mount local directories inside containers.
    - Read/write files between host and container.
    
    ```bash
    docker run --name data_container -v ~/data:/app/data my_python_app
    
    ```
    
- **Networking**:
    - **Port Mapping** (Expose services running inside a container to the host machine).
    
    ```bash
    docker run --name web_container -p 8080:80 my_web_app
    
    ```
    
    - **Bridge Mode**: Isolate container networks from the host system.

## Parting Thoughts

- Containers revolutionize software deployment by making it **portable, scalable, and efficient**.
- **Docker and Podman** are industry standards for container management.
- Using containers **reduces configuration issues and speeds up development**.
- Understanding Docker basics prepares you for **DevOps, cloud computing, and blockchain-based engineering applications**.

---

### 📌 References

- [Docker Official Site](https://www.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Microsoft WSL Installation Guide](https://learn.microsoft.com/en-us/windows/wsl/install)

---

## Lecture Videos from IEM5990 (Spring 2025)

### Containers P1

[https://okstate-edu.zoom.us/rec/share/kTH9IfecmBeK1FSxVSUTYYErqcxild4a_LtaOtzfcajhF-jqw6mIugpu3iPfgyfw.-lgHs7rLSG68WTQT?pwd=DhjQz4G5qdeG5q8XLmq8tTtsvwktSLw9](https://okstate-edu.zoom.us/rec/share/kTH9IfecmBeK1FSxVSUTYYErqcxild4a_LtaOtzfcajhF-jqw6mIugpu3iPfgyfw.-lgHs7rLSG68WTQT?pwd=DhjQz4G5qdeG5q8XLmq8tTtsvwktSLw9)

### Containers Part 2

[https://okstate-edu.zoom.us/rec/share/FEAL2ga5WjtAh6SYKl0VoKIpm_1A4v04_fI31Vgp3gpEt1Mhyd4162huZws8GEmi.42Zv2zKa3F8LnsfD?pwd=b1JZLeSYRjhr6qop77WG0-MF_tlPkmLH](https://okstate-edu.zoom.us/rec/share/FEAL2ga5WjtAh6SYKl0VoKIpm_1A4v04_fI31Vgp3gpEt1Mhyd4162huZws8GEmi.42Zv2zKa3F8LnsfD?pwd=b1JZLeSYRjhr6qop77WG0-MF_tlPkmLH)

### Lecture PDF

[ContainerizationBasics.pdf](Containerization/Lec3.pdf)