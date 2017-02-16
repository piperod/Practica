'''

  run.py module
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  :copyright: (c) 2017 by Jonathan Prieto-Cubides
  :license: MIT (see LICENSE.md)

'''

import os

from datetime import datetime, timedelta, date
from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager, Shell
from pony.orm import *
from pony.orm.serialization import to_json


app = Flask(__name__)
app.debug = True

manager = Manager(app)
manager.add_command("shell", Shell(use_bpython=True))

# -----------------------------------------------------------------------------
#
# Settings
#
# -----------------------------------------------------------------------------

app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
db = Database()

# -----------------------------------------------------------------------------
#
# Models
#
# -----------------------------------------------------------------------------

from datetime import datetime
from pony.orm import *


db = Database()


class Dia(db.Entity):
    id = PrimaryKey(int, auto=True)
    anotaciones = Set('Anotacion', cascade_delete=True)
    atendido_por = Required('Persona', reverse='dias_atencion')
    cierre_por = Required('Persona', reverse='dia')
    comision_movilred = Required(int, size=32, default=0)
    consignacion_ganancia_tecla = Required(int, default=0)
    consignacion_siguiente_movilred = Required(int, default=0)
    consignaciones = Set('ConsignacionMovilred')
    cuenta_billetes = Required('CuentaBilletes')
    cyberplanet = Required(int, size=32, default=0)
    descuentos = Set('Descuento')
    dinero_faltante = Required(int, default=0)
    fecha = Required(datetime, unique=True)
    fecha_modificacion = Optional(datetime)
    ganancia_efectivo = Required(int, default=0)
    ganancia_esperada = Required(int, default=0)
    ganancia_total = Required(int, default=0)
    inicio_saldo_caja = Required(int, size=32)
    inicio_saldo_tullave = Required(int, size=32, default=0)
    pago_salarios = Set('PagoSalario')
    registro_impresora = Required('RegistroImpresora')
    registro_modificado_por = Optional(
        'Persona', reverse='modificaciones_cierre')
    saldo_caja = Required(int, default=0)
    saldo_tullave = Required(int, size=32, default=0)
    total_efectivo = Required(int, default=0)
    total_efectivo_billetes = Required(int, default=0)
    total_facturas = Required(int, size=24, default=0)
    total_internet = Required(int, default=0)
    total_llamadas = Required(int, size=32, default=0)
    total_recolectado = Required(int, default=0)
    total_ventas = Required(int, default=0)
    transacciones_movilred = Required(int, size=32, default=0)


class Anotacion(db.Entity):
    id = PrimaryKey(int, auto=True)
    concepto = Optional(str)
    dia = Optional(Dia)
    persona = Optional(str)
    valor = Required(int, size=32, default=0)


class Persona(db.Entity):
    id = PrimaryKey(int, auto=True)
    consignacion_movilred = Optional('ConsignacionMovilred')
    dia = Optional(Dia, reverse='cierre_por')
    dias_atencion = Set(Dia, reverse='atendido_por')
    modificaciones_cierre = Set(Dia, reverse='registro_modificado_por')
    nombre = Required(str)
    pago_salarios = Set('PagoSalario', reverse='pagado_a')
    pagos_salario_hechos = Set('PagoSalario', reverse='pagado_por')
    permisos = Required(int, default=10)
    rol = Required(str, default='operario')


class RegistroImpresora(db.Entity):
    _table_ = 'Impresora'
    copias_bn = Required(int, size=32, default=0)
    copias_color = Required(int, default=0)
    dia = Optional(Dia)
    escaneres_bn = Required(int, default=0)
    escaneres_color = Required(int, default=0)
    id = PrimaryKey(int, auto=True)
    impresiones_bn = Required(int, default=0)
    impresiones_color = Required(int, default=0)


class ConsignacionMovilred(db.Entity):
    id = PrimaryKey(int, auto=True)
    dia = Optional(Dia)
    persona = Required(Persona)
    valor = Required(int, size=64, default=0)


class CuentaBilletes(db.Entity):
    id = PrimaryKey(int, auto=True)
    billete_cien = Required(int, size=32, default=0)
    billete_cinco = Required(int, default=0)
    billete_cinquenta = Required(int, default=0)
    billete_diez = Required(int, default=0)
    billete_dos = Required(int, default=0)
    billete_mil = Required(int, default=0)
    billete_veinte = Required(int, default=0)
    dia = Optional(Dia)
    moneda_cien = Required(int, default=0)
    moneda_cincuenta = Required(int, default=0)
    moneda_doscientos = Required(int, default=0)
    moneda_mil = Required(int, default=0)
    moneda_quinientos = Required(int, default=0)


class PagoSalario(db.Entity):
    id = PrimaryKey(int, auto=True)
    dia = Optional(Dia)
    fecha_pago = Required(datetime)
    modalidad = Optional(str)
    pagado_a = Required(Persona, reverse='pago_salarios')
    pagado_por = Required(Persona, reverse='pagos_salario_hechos')
    periodo = Required(unicode)
    periodo_final = Optional(datetime)
    periodo_inicio = Optional(datetime)
    valor = Required(int, default=0)


class Descuento(db.Entity):
    id = PrimaryKey(int, auto=True)
    concepto = Required(str)
    dia = Required(Dia)
    valor = Required(int)

db.bind('sqlite', 'cierres.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def populate_database():
    if select(s for s in Persona).count() > 0:
        return
    admin = Persona(nombre="jonathanprieto", rol="soporte")
    admin = Persona(nombre="luzmilacubides", rol="admin")
    admin = Persona(nombre="rafaelprieto", rol="admin")
    commit()


@app.route("/data")
@db_session
def index():
    return to_json(Persona.select())

@app.route("/")
def home():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    populate_database()
    manager.run()
