pipeline {
    agent any
    stages {
        stage('1-Build') {
            steps {
                sh 'python3 -m venv env'
                sh 'call ./enc/Scripts/activate.bat'
                sh 'pip install -r requirements.txt'
                sh 'pip install seleniumbase'
                sh 'sbase install chromedriver latest'
                sh 'pytest -s -v --lang=en-gb'
            }
        }
    }
    post {
        success {
            bat 'curl -s -X POST https://api.telegram.org/bot5698947661:AAFmFW1PEUa7STMd6yXq9x91tJ2oyavqKAE/sendMessage -d chat_id=-746480341 -d text="%JOB_NAME% BUILD %BUILD_ID% finish with SUCCESS"'
        }
        failure {
            bat 'curl -s -X POST https://api.telegram.org/bot5698947661:AAFmFW1PEUa7STMd6yXq9x91tJ2oyavqKAE/sendMessage -d chat_id=-746480341 -d text="%JOB_NAME% BUILD %BUILD_ID% finish with FAIL"'
        }
    }
}
