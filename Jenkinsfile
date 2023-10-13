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

      stage("Build docker images") {
         steps {
            script {
               echo "Bulding docker images"
               docker.build("django-app:latest")
            }
         }
      }
   }
}