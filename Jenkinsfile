pipeline {
    agent {dockerfile true}
    stages {
        stage ('first') {
            steps {
                sh 'python3 --version'
                sh '/tmp/get_info.sh'
            }
        }
    }
}
//
