pipeline {
    agent any
    stages {
        stage('Clonar código') {
            steps {
                script {
                    checkout scm
                }
            }
        }
        stage('Construir imagen Docker') {
            steps {
                sh 'docker build -t mi_app .'
            }
        }
        stage('Ejecutar contenedor') {
            steps {
                sh 'docker run -d -p 5000:5000 --name mi_app_container mi_app'
            }
        }
        stage('Verificar contenedores') {
            steps {
                sh 'docker ps'
            }
        }
        // Nueva etapa para ejecutar las pruebas de validation.py
        stage('Ejecutar pruebas de validation.py') {
            steps {
                script {
                    // Ejecutar las pruebas dentro del contenedor de Docker
                    sh 'docker exec mi_app_container python3 /app/validation.py'
                }
            }
        }
        // Nueva etapa para ejecutar las pruebas de selenium en test_banking.py
        stage('Ejecutar pruebas de Selenium en test_banking.py') {
            steps {
                script {
                    // Ejecutar las pruebas de Selenium en test_banking.py
                    sh 'docker exec mi_app_container pytest /test_banking.py'
                }
            }
        }
    }
}
