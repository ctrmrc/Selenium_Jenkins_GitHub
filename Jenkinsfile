pipeline {
    agent any
    stages {
        stage ('Init') {
            steps {
                sh '''
                    python -m venv env
                    pip install -r requirements.txt
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
        