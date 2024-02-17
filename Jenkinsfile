pipeline {
    agent any

    stages {
        stage('Clone simple-api') {
            steps {
                sh 'git clone git@gitlab.com:softdev3430402/softdevjenkins.git'
            }
        }
    }
     stages {
        stage('run unit-test') {
            steps {
                sh 'sudo apt install python3'
                sh 'python3 unit_test.py'
            }
        }
    }
}

