import os, sys, json, xml.dom.minidom as minidom

directory = "C:\\Kerem\\BUILD\\"+sys.argv[1]+"\\"      
with open('.\environment.json') as f:
    data = json.load(f)
    RedisServer = data[sys.argv[1]]['RedisServer']
    RabbitMQServer = data[sys.argv[1]]['RabbitMQServer']
    SQLServer = data[sys.argv[1]]['SQLServer']
    MongoDBServer = data[sys.argv[1]]['MongoDBServer']

for root, dirs, files in os.walk(directory):
    for file in files:
        if "TurkcellMicroService.exe.config" in file:
            current_file = os.path.join(root, file)
            print (current_file)
            doc = minidom.parse(current_file)            
            add_nodes = doc.getElementsByTagName('add')
            for node in add_nodes:
                if node.getAttribute('key') == 'RedisServerConnectionString':
                    node.setAttribute('value', RedisServer)
                    
                if node.getAttribute('key') == 'RabbitMQHostName':
                    node.setAttribute('value', RabbitMQServer)
                    
                if node.getAttribute('connectionString').startswith('Server ='):
                    node.parentNode.removeChild(node)
                    
                if node.getAttribute('key') == 'MongoDBServer':
                    node.setAttribute('value', MongoDBServer)                             

            with open(current_file, 'w') as f:
                f.write(doc.toxml())
                