import json
import os.path
from os import path


def createDirectory(directorypath):
    isdirectoryexist = path.exists(directorypath)
    print(isdirectoryexist)
    if isdirectoryexist:
        print("File exist already")
    else:
        os.mkdir(directorypath)


# Read microservice Json file
f = open('microservice.json', 'r')
# Read the data from Json
serviceInfo = f.read()
microserviceJsonInfo = json.loads(serviceInfo)
microserviceName = microserviceJsonInfo["microserviceName"]
print(microserviceName)
# Create a folder with service name
# Parent Directory path
parentDir = microserviceJsonInfo["folderName"]
print(parentDir)
# Path
microservicePath = parentDir + "/" + microserviceName
print(microservicePath)
createDirectory(microservicePath)
print("Directory '% s' created" % microserviceName)
# create folder as per package
srcPath = microservicePath+"/"+"src";
createDirectory(srcPath)
mainPath = srcPath+"/"+"main"
createDirectory(mainPath)
javaPath = mainPath+"/"+"java"
createDirectory(javaPath)
packagePath = javaPath;
rootPackage = microserviceJsonInfo["rootPackage"]
folders = rootPackage.split(".")
for folder in folders:
    packagePath = packagePath + "/" + folder
    createDirectory(packagePath)

# Create controller package
controllerPath = packagePath + "/" + "controllers"
createDirectory(controllerPath)

# Create service package
servicesPath = packagePath + "/" + "services"
createDirectory(servicesPath)

# Create repository package
repositoryPath = packagePath + "/" + "repositories"
createDirectory(repositoryPath)


# Create main spring boot application class

# Create sql script based on entity definition

# Create entity class

# Create JPA Crud operations class

# Create .yml files with h2 db

# Create a service class that connects to JPA

# Create a controller that connects that service and add end points to all CRUD operations

# Create base package
def createbasepackages(parentpath, packagename):
    print(parentpath)
    print(packagename)
