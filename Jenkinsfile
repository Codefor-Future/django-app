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
                sh 'docker build -t django-app:latest .'
                withCredentials([string(credentialsId: 'DockerHub', variable: 'DOCKERHUB_PASSWORD')]) {
                    sh 'docker login '
                }   
                // sh 'docker tag $DOCKER_IMAGE_NAME $DOCKER_HUB_REPO'
                // sh 'docker push $DOCKER_HUB_REPO'

                // def localImage = "django-app:latest"
                // def repositoryName = "abhinavparakkal/${localImage}"

                sh 'docker tag django-app:latest abhinavparakkal/django-app:latest'
                sh 'docker push abhinavparakkal/django-app:latest'
            }
        } // Success
// stage("Push to Dockerhub") {
//     steps {
//        script {
//          echo "Pushing the image to docker hub"
//          def localImage = "django-app:latest"
      
//          def repositoryName = "abhinavparakkal/${localImage}"
      
//          // Create a tag that going to push into DockerHub
//          sh "docker tag ${localImage} ${repositoryName} "        
//          docker.withRegistry("", "DockerHub") {
//            def image = docker.image("${repositoryName}");
//            image.push()
//          }
//        }
//     }
//    }
    }
}