pipeline {
    agent any

    stages {
        stage ('Test') {
            steps {
                sh 'python --version'
                sh 'pwd'
                sh 'py.test --junit-xml results.xml'
                sh 'python -m tests.affin_test'
            }
        }
    }
}