pipeline{
    agent any
    stages{
        stage('Checkout SCM') {
           steps{
                cleanWs()
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '5b7c9541-bf47-44d8-b31a-cd33c3b8990e', url: 'https://github.com/kr19al0711/Jenkins_PythonPOC.git']]])
           }
        }
        stage('Running Health Check Script')
        {
            steps{
                powershell ''' python.exe ./health_check.py '''
            }
        }
    }
}
