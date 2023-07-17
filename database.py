from sqlalchemy import create_engine, text
from keyss import connection_string


engine = create_engine(connection_string,
                       connect_args={
                            "ssl": {
                                "ssl_ca": "/etc/ssl/cert.pem"
                            }
                       })

def hitDB():
    with engine.connect() as conn:
        result = conn.execute(text("Select * from arqui.computadoras"))

        Computers = [dict(data._mapping) for data in result]

        return Computers   
    
def hitDBProyecto():
    with engine.connect() as conn:
        result = conn.execute(text("Select * from arqui.proyecto"))

        incidentes = [dict(data._mapping) for data in result]

        return incidentes
    
def hitUniqueDB(id):
    with engine.connect() as conn:
        # sqlCommand = "Select * from computadoras where id =" + id
        result = conn.execute(text("Select * from computadoras where id = " + id))
        rows = [dict(data._mapping) for data in result]
        # if len(result) == 0:
        #     return None
        # else:
        return rows

def hitUniqueProject(id):
    with engine.connect() as conn:
        # sqlCommand = "Select * from computadoras where id =" + id
        result = conn.execute(text("Select * from proyecto where id = " + id))
        rows = [dict(data._mapping) for data in result]
        # if len(result) == 0:
        #     return None
        # else:
        return rows

def hitImg(id):
    with engine.connect() as conn:
        # sqlCommand = "Select * from computadoras where id =" + id
        result = conn.execute(text("Select img from proyecto where id = " + id))
        rows = [dict(data._mapping) for data in result]
        # if len(result) == 0:
        #     return None
        # else:
        return rows
    
# def AddEquipo(data):
#     with engine.connect() as conn:
#         addSomething = "INSERT INTO `arqui`.`computadoras` (`departamento`, `equipo`, `salon`, `activo`, `serie`, `marca`, `modelo`, `windows`, `procesador`, `ram`, `discoduro`, `direccionip`, `tarjetavideo`) VALUES (:departamento, :equipo, :salon, :activo, :serie, :marca, :modelo, :windows, :procesador, :ram, :discoduro, :direccionip, :tarjetavideo;"
#         query = text(addSomething)

#         conn.execute(query,
#                      departamento = data['departamento'],
#                      equipo = data['equipo'],
#                      salon = data['salon'],
#                      activo = data['activo'],
#                      serie = data['serie'],
#                      marca = data['marca'],
#                      modelo = data['modelo'],
#                      windows = data['windows'],
#                      procesador = data['procesador'],
#                      ram = data['ram'],
#                      discoduro = data['discoduro'],
#                      direccionip = data['direccionip'],
#                      tarjetavideo = data['tarjetavideo'])

# with engine.connect() as conn:
#     result = conn.execute(text("Select * from computadoras"))

#     # d, a = {}, []

#     # for row in result:
#     #     for column, value in row.items():
#     #         d = {**d, **{column: value}}
#     #     a.append(d)

#     # print(a)

#     # data = [dict(row) for row in result]
#     # print(data)
#     data = [dict(data._mapping) for data in result]
#     print(data)
    # result_all = result.all()
    # first_result = result_all[0]
    # first_result_dict = first_result
    # print(result_all)
    # print(first_result_dict)

