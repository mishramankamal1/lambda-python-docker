## Docker Image Deployment to AWS ECR

1. **Retrieve Authentication Token**: Retrieve an authentication token and authenticate your Docker client to your registry using the AWS CLI:
    ```bash
    aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com
    ```
    Replace `<region>` with your AWS region and `<account>` with your AWS account ID.

2. **Build Docker Image**: Build your Docker image using the following command:
    ```bash
    docker build -t <repository-name> . -f Dockerfile
    ```
    Replace `<repository-name>` with the name of your Docker repository.

3. **Tag Image**: After the build is completed, tag your image so you can push it to your AWS repository:
    ```bash
    docker tag <repository-name>:latest <account>.dkr.ecr.<region>.amazonaws.com/<repository-name>:latest
    ```

4. **Push Image to AWS ECR**: Run the following command to push your image to your newly created AWS repository:
    ```bash
    docker push <account>.dkr.ecr.<region>.amazonaws.com/<repository-name>:latest
    ```
    Replace `<region>` with your AWS region, `<account>` with your AWS account ID, and `<repository-name>` with the name of your Docker repository.

5. **Upload the data to your s3 bucket**: Upload the data file to your s3 bucket

