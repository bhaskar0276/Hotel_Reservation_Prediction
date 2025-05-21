pipeline{
    
    agent any


    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins_github_token', url: 'https://github.com/bhaskar0276/Hotel_Reservation_Prediction.git']])
                }
            }
        }
    }
}