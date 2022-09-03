pipeline {
    agent any
    stages {
        stage ('Init') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv env
                    pip3 install -r requirements.txt
                    pytest --lang=en-gb
                '''
                }
            post {
                always {
                    echo "Post-Init result: ${currentBuild.result}"
                    echo "THE RESULT OF THIS BUILD IS: ${currentBuild.currentResult}"
                }
            }
        }
    }
}
        
