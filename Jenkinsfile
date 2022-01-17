pipeline {
    agent {
        dockerfile {
            args '--privileged -v /zip:/zip'
            }
    }
    stages {
        stage ('first') {
            steps {
                sh 'python3 --version'
                sh '/tmp/get_info.sh'
            }	
        }
		stage ('Build') {
			steps {
                sh 'sudo python3 /tmp/zip_job.py'
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
					spec: '''{
                              "files": [
                                 {
                                  "pattern": "/tmp/zip/c_1.2.0.zip",
                                  "target": "binary-storage/"
                                } 
                             ]
                        }'''
				)
            }
		}
    }
}
