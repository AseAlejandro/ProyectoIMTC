from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine, text
# from keyss import connection_string
from database import hitDB, hitUniqueDB, hitDBProyecto, hitUniqueProject, hitImg
import base64
from PIL import Image
import io

app = Flask(__name__)

connection_string = os.environ['connection_string']
engine = create_engine(connection_string,
                       connect_args={
                            "ssl": {
                                "ssl_ca": "/etc/ssl/cert.pem"
                            }
                       })

# Computers = [
#     {
#         "id": 1,
#         "Salon": "Sala B",
#         "Equipo": "CPU",
#         "Activo": "585800",
#         "No de serie": "2UA1180XZR",
#         "Marca": "HP",
#         "Modelo": "Z200",
#         "Windows": "10",
#         "CPU": "Intel Core i5",
#         "RAM (GB)": "4 GB",
#         "Disco Duro (GB)": "298 GB",
#         "Direccion IP": "148.234.69.80",
#         "Tarjeta de Video": "Nvida Quadro FX380lp"
#     },
#     {
#         "id": 2,
#         "Salon": "Sala B",
#         "Equipo": "CPU",
#         "Activo": "609064",
#         "No de serie": "2UA2250VBJ",
#         "Marca": "HP",
#         "Modelo": "Z210",
#         "Windows": "10",
#         "CPU": "Intel Xeon CPU E31225 3.10 GHz",
#         "RAM (GB)": "4 GB",
#         "Disco Duro (GB)": "466 GB",
#         "Direccion IP": "148.234.69.54",
#         "Tarjeta de Video": "ATI firepro 3800"
#     },
#     {
#         "id": 3,
#         "Salon": "Sala B",
#         "Equipo": "Monitor",
#         "Activo": "609111",
#         "No de serie": "6CM20709ZZ",
#         "Marca": "HP",
#         "Modelo": "HP LV1911",
#     }
# ]

@app.route("/")
def HelloWorld():
    # Computers = hitDB()
    proyectos = hitDBProyecto()
    return render_template("home.html", proyects=proyectos)
    # return render_template("home.html", computers=Computers)

@app.route("/computers")
def listJobs():
    Computers = hitDB()
    return jsonify(Computers)

@app.route("/computer/<id>")
def showComputer(id):
    computer = hitUniqueDB(id)
    if not computer:
        return "Not Found", 404
    computer = computer[0]

    # return jsonify(computer)
    return render_template("objects.html", computers = computer)

@app.route("/proyecto/<id>")
def showProyecto(id):
    proyecto = hitUniqueProject(id)
    img = hitImg(id)
    img = img[0]
    img = img["img"]
    # image = Image.open(io.BytesIO(binary_data))
    # print(img)
    encoded_image = base64.b64encode(img) # type: ignore
    encoded_image = encoded_image.decode("utf-8")
    # Convert the bytes into a PIL image
    # image = Image.open(io.BytesIO(encoded_image))
    
    # # Display the image
    # image.show()
    if not proyecto:
        return "Not Found", 404
    proyecto = proyecto[0]

    # return jsonify(computer)
    return render_template("objects.html", proyectos = proyecto, image2 = encoded_image)

@app.route('/computers', methods=['post'])
def addEquipo():
    data = request.args
    return jsonify(data)
    # data = request.form
    # AddEquipo(data)
    # return render_template('home.html',
    #                        application = data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
