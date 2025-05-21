pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "wide-approach-459121-g5"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
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

                script {
                    echo 'Creating Virtual Environment............'
                    sh '''
                        python3 -m venv $VENV_DIR
                        . $VENV_DIR/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                    '''
                }

            }
        }

        stage('Building and Pushing Docker Image to GCR'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key' , variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and Pushing Docker Image to GCR.............'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}


                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .



                        '''
                    }
                }
            }
        }




    }
}