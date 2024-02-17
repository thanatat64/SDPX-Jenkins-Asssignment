pipeline {
    agent any
    
    stages {
        stage('Clone Simple API') {
            steps {
                git 'https://github.com/your-simple-api-repo.git'
            }
        }
        stage('Run Unit Test') {
            steps {
                // Execute unit tests here
            }
        }
        stage('Create Images of Simple API') {
            steps {
                // Execute Docker build to create images
            }
        }
        stage('Create Container of Simple API') {
            steps {
                // Execute Docker run to create container
            }
        }
        stage('Clone Simple API Robot') {
            steps {
                git 'https://github.com/your-simple-api-robot.git'
            }
        }
        stage('Run Robot Test') {
            steps {
                // Execute Robot test suites
            }
        }
        stage('Push Images to Registry') {
            steps {
                // Execute Docker push to push images to registry
            }
        }
    }
}
