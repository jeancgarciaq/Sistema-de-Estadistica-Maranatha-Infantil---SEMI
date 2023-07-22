from peewee import *

database = SqliteDatabase('database/semi.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Areas(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'areas'

class Salones(BaseModel):
    edad = TextField()
    id_area = ForeignKeyField(column_name='id_area', field='id', model=Areas)
    nombre = TextField()

    class Meta:
        table_name = 'salones'

class Aulas(BaseModel):
    integer = BareField(column_name='INTEGER')
    auxiliar = IntegerField()
    capitan = IntegerField()
    colaborador = IntegerField()
    condicion = TextField()
    edad = TextField()
    fecha = DateField(null=True)
    id_salon = ForeignKeyField(column_name='id_salon', field='id', model=Salones, null=True)
    maestra = IntegerField()
    ninas = IntegerField()
    ninos = IntegerField()
    subcapitan = IntegerField()

    class Meta:
        table_name = 'aulas'

class Donaciones(BaseModel):
    cantidad = IntegerField()
    descripcion = TextField()
    equipo = TextField()
    fecha = DateField(null=True)
    sembrador = TextField()

    class Meta:
        table_name = 'donaciones'

class DonacionesHasSalones(BaseModel):
    cantidad = IntegerField()
    id_donacion = ForeignKeyField(column_name='id_donacion', field='id', model=Donaciones)
    id_salon = ForeignKeyField(column_name='id_salon', field='id', model=Salones)

    class Meta:
        table_name = 'donaciones_has_salones'

class Ensenanza(BaseModel):
    capitan = TextField()
    fecha = DateField(null=True)
    subcapitan = IntegerField()

    class Meta:
        table_name = 'ensenanza'

class Logistica(BaseModel):
    almacen = IntegerField()
    capitan = IntegerField()
    distribucion = IntegerField()
    fecha = DateField(null=True)
    hidratacion = IntegerField()
    pasillo = IntegerField()
    secretaria = IntegerField()

    class Meta:
        table_name = 'logistica'

class OtrasAreas(BaseModel):
    alabanza = IntegerField()
    fecha = DateField(null=True)
    protocolo = IntegerField()
    seguridad = IntegerField()
    semillitas = IntegerField()
    sonido = IntegerField()
    teatro = IntegerField()
    tv = IntegerField()
    ujier = IntegerField()

    class Meta:
        table_name = 'otras_areas'

class Recepcion(BaseModel):
    id_area = ForeignKeyField(column_name='id_area', field='id', model=Areas, null=True)
    nombre = TextField(unique=True)

    class Meta:
        table_name = 'recepcion'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

