#datos para la coneccion a BD

dataBaseName="gestorbd"
userName="root"
usePassword=""
connectionPort=3306
server="localhost"

#creando la conexion a BD
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{usePassword}@{server}:{connectionPort}/{dataBaseName}"

print(dataBaseConnection)