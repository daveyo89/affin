pipeline {
    agent any

    stages {
        stage ('Test') {
            steps {
                sh 'python --version'
                sh 'pwd'
                sh 'python -m tests.affin_test'
            }
        }
    }
}