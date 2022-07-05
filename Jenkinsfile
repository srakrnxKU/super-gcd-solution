pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root --privileged'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'ls -al'
                sh 'python3 -m pip install --user -e .[test]'
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