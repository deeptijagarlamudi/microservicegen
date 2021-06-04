import json
import os.path
from os import path


def createDirectory(directorypath):
    isdirectoryexist = path.exists(directorypath)
    print(isdirectoryexist)
    if isdirectoryexist:
        print("Folder exist already")
    else:
        os.mkdir(directorypath)


def copycontent(sourcefile, targetfile):
    # open both files
    with open(sourcefile, 'r') as firstfile, open(targetfile, 'a') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)


# Read microservice Json file

f = open('microservice.json', 'r')
# Read the data from Json
serviceInfo = f.read()
microserviceJsonInfo = json.loads(serviceInfo)
microserviceName = microserviceJsonInfo["microserviceName"]
# Create a folder with service name
# Parent Directory path
parentDir = microserviceJsonInfo["folderName"]
microservicePath = parentDir + "/" + microserviceName
createDirectory(microservicePath)
print("Directory '% s' created" % microserviceName)
# create POM xml
with open(microservicePath + "/" + 'pom.xml', 'w') as f:
    copycontent('C://Users//deept//PycharmProjects//microservicegen//templates//restApiCRUDOperations//pom.txt',
                microservicePath + "/" + 'pom.xml')
# create folder as per package
srcPath = microservicePath + "/" + "src";
createDirectory(srcPath)
mainPath = srcPath + "/" + "main"
createDirectory(mainPath)
javaPath = mainPath + "/" + "java"
createDirectory(javaPath)
resourcesPath = mainPath + "/" + "resources"
# Create application.yml
with open(resourcesPath + "/" + 'application.xml', 'w') as f:
    copycontent('C://Users//deept//PycharmProjects//microservicegen//templates//restApiCRUDOperations//application.yml',
                resourcesPath + "/" + 'application.xml')
createDirectory(resourcesPath)
packagePath = javaPath
rootPackage = microserviceJsonInfo["rootPackage"]
folders = rootPackage.split(".")
for folder in folders:
    packagePath = packagePath + "/" + folder
    createDirectory(packagePath)
entityName = microserviceJsonInfo["entityDetails"]["name"]
# Create main class
with open(packagePath + "/" + entityName+'ServiceApplication.java', 'w') as f:

    with open('C://Users//deept//PycharmProjects//microservicegen//templates//restApiCRUDOperations//mainClass.txt','r+') as mainFile:
        # read file
        file_source = mainFile.read()
        replace_string = file_source.replace('${rootPackage}', rootPackage).replace('${entityName}', entityName).replace('${entityNameinSmallCase}',entityName.lower())
        mainFile.truncate()
        # save output
        print(replace_string)
        f.write(replace_string)
# Create controller package
controllerPath = packagePath + "/" + "controllers"
createDirectory(controllerPath)
print(entityName)

with open(controllerPath + "/" + entityName+'Controller.java', 'w') as f:

    with open('C://Users//deept//PycharmProjects//microservicegen//templates//restApiCRUDOperations//controllerClass.txt','r+') as controllerfile:
        # read file
        file_source = controllerfile.read()
        replace_string = file_source.replace('${rootPackage}', rootPackage).replace('${entityName}', entityName).replace('${entityNameinSmallCase}',entityName.lower())
        controllerfile.truncate()
        # save output
        print(replace_string)
        f.write(replace_string)
# Create service package
servicesPath = packagePath + "/" + "services"
createDirectory(servicesPath)

with open(servicesPath + "/" + entityName+'Service.java', 'w') as f:

    with open('C://Users//deept//PycharmProjects//microservicegen//templates//restApiCRUDOperations//serviceClass.txt','r+') as serviceClass:
        # read file
        file_source = serviceClass.read()
        replace_string = file_source.replace('${rootPackage}', rootPackage).replace('${entityName}', entityName).replace('${entityNameinSmallCase}',entityName.lower())
        serviceClass.truncate()
        # save output
        print(replace_string)
        f.write(replace_string)

# Create repository package
repositoryPath = packagePath + "/" + "repositories"
createDirectory(repositoryPath)
with open(repositoryPath + "/" + entityName+'Repository.java', 'w') as f:
    with open('C://Users//deept//PycharmProjects//microservicegen//templates//restApiCRUDOperations//repositoryInterface.txt','r+') as repositoryFile:
        # read file
        file_source = repositoryFile.read()
        replace_string = file_source.replace('${rootPackage}', rootPackage).replace('${entityName}', entityName).replace('${entityNameinSmallCase}',entityName.lower())
        repositoryFile.truncate()
        # save output
        print(replace_string)
        f.write(replace_string)

# Create sql script based on entity definition

# Create entity class

# Create JPA Crud operations class

# Create .yml files with h2 db

# Create a service class that connects to JPA

# Create a controller that connects that service and add end points to all CRUD operations
