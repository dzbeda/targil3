pipeline {
    agent {dockerfile true}
    stages {
        stage ('first') {
            steps {
                sh 'python3 --version'
                sh '/tmp/get_info.sh'
            }	
        }
		stage ('Build') {
			steps {
                sh 'python3 /tmp/zip_job.py'
            }
		}
		stage ('Show Log File') {
			steps {
                sh 'cat /tmp/output.log'
            }
		}
		stage ('Publish') {
			steps {
                rtUpload (
					serverId: 'jfrog1',
					specPath: '/tmp/zip/d_1.2.0.zip'
				)
            }
		}
    }
}
