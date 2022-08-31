pipeline {
    agent any
    stages {
        
        stage('Checkout') {
            steps {
            // script here
            }
            echo 'Done'
            }
        }
        stage('Build') {
            steps {
            // script here
            }
            echo 'Done'
            }
        }
        stage('Publish') {
            steps {
                // script here
                echo "Deployed Successfully!"
            }
        }
    }
          post {
     success { 
        withCredentials([string(credentialsId: 'J_Notification_404_token', variable: '5493377417:AAH-twR5yxDd6z5N6i1lpE2TiWDrFdv6t-M'), string(credentialsId: 'J_Notification_404_ID', variable: '126062127')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC *Branch*: ${env.GIT_BRANCH} *Build* : OK *Published* = YES'
        """)
        }
     }

     aborted {
        withCredentials([string(credentialsId: 'J_Notification_404_token', variable: '5493377417:AAH-twR5yxDd6z5N6i1lpE2TiWDrFdv6t-M'), string(credentialsId: 'J_Notification_404_ID', variable: '126062127')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC *Branch*: ${env.GIT_BRANCH} *Build* : `Aborted` *Published* = `Aborted`'
        """)
        }
     
     }
     failure {
        withCredentials([string(credentialsId: 'J_Notification_404_token', variable: '5493377417:AAH-twR5yxDd6z5N6i1lpE2TiWDrFdv6t-M'), string(credentialsId: 'J_Notification_404_ID', variable: '126062127')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC  *Branch*: ${env.GIT_BRANCH} *Build* : `not OK` *Published* = `no`'
        """)
        }
     }

 }

