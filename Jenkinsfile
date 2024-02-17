pipeline {
    agent any

    stages {
        stage('Clone simple-api') {
            steps {
                sh 'ssh git@gitlab.com'
                sh 'git clone git@gitlab.com:softdev3430402/softdevjenkins.git'
            }
        }
    }
}

