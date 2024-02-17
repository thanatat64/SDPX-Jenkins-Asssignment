pipeline {
    agent any
    
    stages {


        stage('Run Unit Test') {
            steps {
                sh 'pip install --no-cache-dir --upgrade -r requirements.txt '
                sh 'python3 unit_test.py'
                // Assumes unit_test.py exists in the root directory and contains your unit tests
            }
        }
        stage('Create Images of Simple API') {
            steps {
                sh 'docker stop simple-api-container'
                sh 'docker rm simple-api-container'
                sh 'docker build -t simple-api .'
                // Build Docker image using provided Dockerfile
            }
        }
        stage('Create Container of Simple API') {
            steps {
                sh 'docker run -d -p 8000:8000 --name simple-api-container simple-api'
                // Create Docker container from the built image
            }
        }
          stage('Run Robot Tests') {
            steps {
                sh 'robot test_plus.robot'
                // Assumes test_plus.robot exists in the root directory and contains your Robot Framework tests
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                sh 'docker build -t registry.gitlab.com/softdev3430402/softdevjenkins/simple-api-image .'
                // Build Docker image using provided Dockerfile
                sh 'docker push registry.gitlab.com/softdev3430402/softdevjenkins/simple-api-image'
                // Push Docker image to GitLab registry
            }
        }
    }
}
