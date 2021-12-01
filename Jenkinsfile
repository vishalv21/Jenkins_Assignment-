pipeline { 
agent any
    stages {
        stage('Clone Git Repository') {
            steps {
                git 'https://github.com/bansalc73/jenkins-demo.git'
            }
        }
        stage('Run Code') {
            steps {
                sh "/usr/bin/python3 main.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "/usr/bin/python3 test.py"
            }
        }
    } 
}