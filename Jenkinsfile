pipeline {
    agent {
        docker { image 'python:3.9' }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'ls -al'
                sh 'pip install -e .[test]'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'pytest --junitxml=tmp/out_report.xml'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}