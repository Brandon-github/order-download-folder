import os
import shutil

homeFolder = '/home/brandon/'
downloadFolder = homeFolder + 'Descargas/'

# Obtener grupo de extensiones dependiendo del nombre
def getGroupExtension(group_name):
    try:
        # Dicionario de grupos de extensiones
        group = {
            'package': ['.deb', '.run', '.exe'],
            'image': ['.jpg', '.jpeg', '.png', '.svg', '.ico', '.gif', '.webp'],
            'compress': ['.zip', '.rar', '.iso', '.tar'],
            'code': ['.html', '.css', '.scss', '.sass', '.js', '.jsx', '.ts', '.tsx', '.php', '.java', '.cpp', '.cs', '.sql', '.py', '.sh'],
            'video': ['.mp4'],
            'music': ['.mp3', '.wav'],
            'doc': ['.pdf', '.docx', '.txt']
        }

        return group[group_name]
    except:
        print("Error group extension not found")

# Crear carpeta con nombre y guardar archivos de su grupo de extension
def createFolder(folderName, fileName):
    try:
        folderPath = downloadFolder + folderName# ruta de carpeta de grupo de extension
        os.makedirs(folderPath, exist_ok=True)# crear carpeta en ruta si no existe
        shutil.move(downloadFolder + fileName, folderPath + fileName)# mover archivo a carpeta creada
        # mensaje para saber la ruta anter y despues de mover el archivo
        print("move: " + downloadFolder + fileName +
              " --> " + folderName + fileName)
    except:
        print("Error creating folder or moving files to selected folder")
        


if __name__ == '__main__':
    # Recorriendo archivos del directorio de descargas
    for item in os.listdir(downloadFolder):
        # guardamos el nombre y la extension de cada archivo
        name, extension = os.path.splitext(downloadFolder + item)

        # Verificando si existen la extension del archivo esta en el grupo
        if extension in getGroupExtension('package'):
            createFolder('package/', item)

        if extension in getGroupExtension('image'):
            createFolder('image/', item)

        if extension in getGroupExtension('compress'):
            createFolder('compress/', item)

        if extension in getGroupExtension('code'):
            createFolder('code/', item)

        if extension in getGroupExtension('video'):
            createFolder('video/', item)

        if extension in getGroupExtension('music'):
            createFolder('music/', item)

        if extension in getGroupExtension('doc'):
            createFolder('doc/', item)

    print("\nProcess finish successfully!")