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
        stage("Clone/Setup Robot"){
            agent {label "test"} 
            steps{
                dir('./robot-test/'){
                    git branch: 'main', credentialsId: '656e0d84-f8fd-43ff-bca3-7e570bf3cc42',url: 'https://gitlab.com/softdev3430402/softdevrepo.git'
                }
                echo "clone done!"
            }
        }

        stage("Run Robot") {
            agent {label "test"} 
            steps{
                // sh "pwd"
                // sh "ls"
                sh "cd ./robot-test && python3 -m robot test_plus.robot"
            }
        }
        stage("Push image") {
             agent {
                    label "test"
                }
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
        stage("Pull image") {
             agent {
                    label "pre-prod"
                }
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
                    sh 'docker stop simple-api-container'
        }
        }
    }
    stage("runcontainer") {
             agent {
                    label "pre-prod"
                }
            steps {
                    sh "docker run -d -p 8000:8000 ${IMAGE_NAME}"
        }
    }
}
}
