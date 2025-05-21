pipeline{
    
    agent any


    environment {
        VENV_DIR = 'venv'
    }


    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins_github_token', url: 'https://github.com/bhaskar0276/Hotel_Reservation_Prediction.git']])
                }
            }
        }

        stage('Creating Virtual Environment'){
            steps{
                script{
                    echo 'Creating Virtual Environment............'
                    sh '''
                        python3 -m venv $VENV_DIR
                        source $VENV_DIR/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                    '''
                }
            }
        }
    }
}