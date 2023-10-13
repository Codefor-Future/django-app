pipeline{
    agent any
    stages {// stage blocks
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