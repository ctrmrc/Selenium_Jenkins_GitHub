pipeline {
    agent any

    stages {
        stage('1-Build') {
            steps {
                sh '''
                    python -m venv env
                    call ./enc/Scripts/activate.bat
                    pip install -r requirements.txt
                    pip install seleniumbase
                    sbase install chromedriver latest
                    pytest -s -v --lang=en-gb
                '''
            }
        }
        boolean testPassed = False
        stage('2-Test') {
            try{
                bat 'curl -s -X POST https://api.telegram.org/bot5698947661:AAFmFW1PEUa7STMd6yXq9x91tJ2oyavqKAE/sendMessage -d chat_id=-746480341 -d text="%JOB_NAME% BUILD %BUILD_ID% finish with FAIL"'
            } catch (Exception e){
            testPassed = true
            }
        }
        stage('3-Deploy') {
            if(testPassed){
                bat 'curl -s -X POST https://api.telegram.org/bot5698947661:AAFmFW1PEUa7STMd6yXq9x91tJ2oyavqKAE/sendMessage -d chat_id=-746480341 -d text="%JOB_NAME% BUILD %BUILD_ID% finish with SUCCESS"'
                }
        }
    }
}
