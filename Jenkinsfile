pipeline{
    node{
        label 'agent1'
    }

    stage('Checkout SCM') {
        
        cleanWs()
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '5b7c9541-bf47-44d8-b31a-cd33c3b8990e', url: 'https://github.com/kr19al0711/Jenkins_PythonPOC.git']]])
    }
    stage('Running Health Check Script')
    {
        sh''''
            sudo chmod +x health_check.py
            ./health_check.py
        '''
    }
}