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
stage("Push to Dockerhub") {
    steps {
       script {
         echo "Pushing the image to docker hub"
         def localImage = "django-app"
      
         // pcheajra is my username in the DockerHub
         // You can use your username
         def repositoryName = "abhinavparakkal/${localImage}"
      
         // Create a tag that going to push into DockerHub
         sh "docker tag ${localImage} ${repositoryName} "        
         docker.withRegistry("", "DockerHub") {
           def image = docker.image("${repositoryName}");
           image.push()
         }
       }
    }
   }
    }
}