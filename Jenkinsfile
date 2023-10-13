pipeline{
    agent any
    stages {// stage blocks
     stage('Initialize'){
        steps {
            script {
               def dockerHome = tool 'docker'
                env.PATH = "${dockerHome}/bin:${env.PATH}"
            }
         }
    }

    stage('Build Docker image from Django project') {
            steps {
                sh 'docker build -t django-app .'
                // withCredentials([string(credentialsId: 'DOCKERHUB_PASSWORD', variable: 'DOCKERHUB_PASSWORD')]) {
                //     sh 'docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD'
                // }
                // sh 'docker tag $DOCKER_IMAGE_NAME $DOCKER_HUB_REPO'
                // sh 'docker push $DOCKER_HUB_REPO'
            }
        } // Success

    //   stage("Build docker images") {
    //      steps {
    //         script {
    //            echo "Bulding docker images"
    //            docker.build("django-app:latest")
    //         }
    //      }
    //   }
   }
}