import json

#Cargar los datos desde peliculas.json
def loadData():
    with open ('peliculasP.json', 'r') as file:
        return json.load(file)

def saveData(data):
    with open ('pruebas/ejemplo.json', 'w') as file:
        json.dump(data, file, indent=4)

#Guardar los datos en peliculas.json
def saveData(data):
    with open ('peliculasP.json', 'w') as file:
        json.dump(data, file, indent=4)

#Crear registro en peliculas.json
def createRecord(data, peliID, newPeli):
    if peliID not in data:
        data.get("blockbuster").get("peliculas") [peliID] = newPeli
        
#Actualizar registro por ID en peliculas.json
def updateRecord(data, peliID, llave, valor):
    data = data.get("blockbuster").get("peliculas").get(peliID).get(peliID)
    if peliID in data:
        actualizar = {llave : valor}
        data.update(actualizar)
        print(f'Registro {peliID} actualizado')
    else:
        print('Registro no encontrado')

def readAllRecords(data):
    return data

#Leer registro por ID de peliculas.json
def readRecord(data, recordID):
    return data.get("blockbuster").get("peliculas").get(recordID, "Registro no encontrado")

#Eliminar registro por ID en peliculas.json
def deleteRecord(data, recordID):
    if recordID in data.get("blockbuster").get("peliculas"):
        del data[recordID]
    else:
        print('Registro no encontrado')

data = loadData()
newPeli = {
        "id": "P01",
        "nombre": "xxxxx",
        "duracion": "xxxx",
        "sinopsis": "xxxx",
        "generos": {
            "G01": {
                "id": "G01",
                "nombre": "xxxxx"
            }
        },
        "actores": {
            "A01": {
                "id": "A01",
                "nombre": "xxxx",
                "rol": "Protagonista  o Antagonista o Reparto"
            }
        },
        "formato": {
            "F01": {
                "id": "F01",
                "nombre": "DVD",
                "NroCopias": 2,
                "valorPrestamo": 5000
            },
            "F02": {
                "id": "F02",
                "nombre": "BlueRay",
                "NroCopias": 2,
                "valorPrestamo": 8000
            }
        }
    }
createRecord(data, "3", newPeli)


updateRecord(data, 'P01', 'id', 5050)
saveData(data)

#mostrar todos los registros en peliculas.json
print(f'Todos los registros {readAllRecords(data)}')

#leer registro por id en peliculas.json
print(f'Registro por ID {readRecord(data,"P01")}')

#elimiar registro por id
deleteRecord(data, "3")