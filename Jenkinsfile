pipeline {
    agent any
    
    
    stages {


        stage('Run Unit Test') {
            agent {
                    label "test"
                }
            steps {
                sh 'pip install --no-cache-dir --upgrade -r requirements.txt '
                sh 'python3 unit_test.py'
                // Assumes unit_test.py exists in the root directory and contains your unit tests
            }
        }
        stage('Create Images of Simple API') {
            agent {
                    label "test"
                }
            steps {
                sh 'docker stop simple-api-container'
                sh 'docker rm simple-api-container'
                sh 'docker build -t simple-api .'
                // Build Docker image using provided Dockerfile
            }
        }
        stage('Create Container of Simple API') {
            agent {
                    label "test"
                }
            steps {
                sh 'docker run -d -p 8000:8000 --name simple-api-container simple-api'
                // Create Docker container from the built image
            }
        }
          stage('Run Robot Tests') {
            agent {
                    label "test"
                }
            steps {
                sh 'curl http://192.168.88.1/Main_Login.asp'
                sh 'curl http://192.168.88.5:8000/getcode'
                sh 'robot test_plus.robot'
                // Assumes test_plus.robot exists in the root directory and contains your Robot Framework tests
            }
        }
        stage('Build and Push Docker Image') {
            agent {
                    label "test"
                }
            steps {
                sh 'docker build -t registry.gitlab.com/softdev3430402/softdevjenkins/simple-api-image .'
                // Build Docker image using provided Dockerfile
                sh 'docker push registry.gitlab.com/softdev3430402/softdevjenkins/simple-api-image'
                // Push Docker image to GitLab registry
            }
        }
    }
}
