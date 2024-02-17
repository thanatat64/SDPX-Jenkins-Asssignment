pipeline {
    agent any
       environment {
        IMAGE_NAME = "registry.gitlab.com/softdev3430402/softdevjenkins"
    } 
    
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
        stage("Push image ") {
            steps {
                withCredentials(
                [usernamePassword(
                    credentialsId: "656e0d84-f8fd-43ff-bca3-7e570bf3cc42",
                    passwordVariable: "gitlabPassword",
                    usernameVariable: "gitlabUser"
                )]
            ){
                    sh "docker login -u ${gitlabUser} -p ${gitlabPassword} registry.gitlab.com"
                    sh "docker pull ${IMAGE_NAME}"
                    sh "docker tag ${IMAGE_NAME} ${IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker push ${IMAGE_NAME}"
                    sh "docker push ${IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker rmi ${IMAGE_NAME}"
                    sh "docker rmi ${IMAGE_NAME}:${env.BUILD_NUMBER}"
                }
            }
        }
    }
}
