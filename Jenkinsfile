pipeline {
    agent {
        docker { image 'python:3.9' }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'ls -al'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}