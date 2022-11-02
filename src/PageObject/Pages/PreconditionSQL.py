import os
import randomname
import pymssql
import random
import randomcolor
import datetime
import re
import names
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import date

global id_cal_detail
global id_jornada
global id_rangos
global new_id_ran
global id_calendario
global emp_id


def random_color():
    rand_color = randomcolor.RandomColor()
    colors_hex = rand_color.generate(format_='hex')
    for color_hex in colors_hex:
        ref_color = color_hex[1:]
        res = int(ref_color, 16)
        return str(res)

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/PlanificacionHoraria/.env')
load_dotenv(dotenv_path)


server = str(os.getenv('server'))
user = str(os.getenv('db_user'))
password = str(os.getenv('db_password'))
database = str(os.getenv('database'))
conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()

# Condicion --> Tener empleados con calendario asignado.



def condition_sql():
    # Jornada
    id_rangos = str(random.randint(0, 2 ** 31))
    id_jornada = str(random.randint(0, 2 ** 31))
    name_jor = randomname.get_name(adj='geometry')
    # Calendario
    id_calendario = str(random.randint(0, 2 ** 31))
    calendar_name = "Calendar" + randomname.get_name(adj='emotions')
    calendar_alt = date.today()

    jornadas_genericasS = "SET IDENTITY_INSERT JORNADAS_GENERICAS ON insert into JORNADAS_GENERICAS (id, nombre, color, horas_obligatorias, compensa_hs_normales, dias_horas_obligatorias, id_empresa) values (" + id_jornada + ", '" + name_jor + "', "+random_color()+", CAST(N'00:00:00' AS Time), 0, 0, 1); SET IDENTITY_INSERT JORNADAS_GENERICAS OFF"
    calendario = "SET IDENTITY_INSERT CALENDARIOS ON insert into calendarios (id, nombre, alta, id_empresa) VALUES (" + id_calendario + ", N'" + calendar_name + "', CAST(N'" + str(
        calendar_alt) + "' AS Date), 1); SET IDENTITY_INSERT CALENDARIOS OFF"

    cursor.execute(jornadas_genericasS)
    cursor.execute(calendario)
    conn.commit()

    id_cal_detail = random.randint(0, 2 ** 31)
    numdays = 365
    base = date(date.today().year, 1, 1)
    date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
    for days in date_list:
        id_cal_detail += 1
        calendario_detalle = "SET IDENTITY_INSERT CALENDARIOS_DETALLE ON insert into calendarios_detalle (id, id_calendario, id_jornada_generica, fecha, id_jornada_gen_multiple) values (" + str(
            id_cal_detail) + ", " + id_calendario + ", " + id_jornada + ", CAST(N'" + str(
            days) + "' AS Date), NULL); SET IDENTITY_INSERT CALENDARIOS_DETALLE OFF"
        cursor.execute(calendario_detalle)
        conn.commit()

    rango_flex = "SET IDENTITY_INSERT RANGOS ON insert into rangos (id, tipo, hora_desde, hora_hasta, tarde, suma_minutos, id_jornada_generica, id_porc_extra, dia_siguiente, disparo_redondeo, multiplo_redondeo, tipo_redondeo, penalizacion, horas_minimas, horas_maximas, cant_minutos_para_sumar, cant_minutos_a_sumar, PERTENECE_A_JORNADA) values (" + id_rangos + ", 0, CAST(N'20:00:00' AS Time), CAST(N'09:00:00' AS Time), 0, 0, " + id_jornada + ", NULL, 1, 0, 0, 0, NULL, NULL, NULL, 0, 0, 1); SET IDENTITY_INSERT RANGOS OFF"
    new_id_ran = int(id_rangos) + 1
    rango_normal = "SET IDENTITY_INSERT RANGOS ON insert into rangos (id, tipo, hora_desde, hora_hasta, tarde, suma_minutos, id_jornada_generica, id_porc_extra, dia_siguiente, disparo_redondeo, multiplo_redondeo, tipo_redondeo, penalizacion, horas_minimas, horas_maximas, cant_minutos_para_sumar, cant_minutos_a_sumar, PERTENECE_A_JORNADA) values (" + str(
        new_id_ran) + ", 1, CAST(N'22:00:00' AS Time), CAST(N'06:00:00' AS Time), 0, 0, " + id_jornada + ", NULL, 1, 0, 0, 0, NULL, NULL, NULL, 0, 0, 1); SET IDENTITY_INSERT RANGOS OFF"
    cursor.execute(rango_flex)
    cursor.execute(rango_normal)
    conn.commit()

    emp_id = random.randint(0, 2 ** 31)
    date_alt = str(datetime.datetime.today())
    m = re.sub(r'.\d+$', "", date_alt)
    employee_dni = str(random.randint(20000000, 20000000))
    nums = range(0, 20)
    # Crear 10 empleados
    for num in nums:
        employee_first_name = names.get_first_name()
        employee_last_name = names.get_last_name()
        emp_id += 1
        clientes = "INSERT INTO CLIENTES (id, nombre, apellido, alta, legajo, preciohora, extras, id_bioadmin, imagen, inc_reportes, eliminado, fecha_ingreso, contrasena, rol, direccion, dni, email, cel, tel, cp, vehiculo, patente, id_provincia, localidad, id_calendario, tarjetazk, fecha_venc, id_sector_por_empresa, remoto_password, envio_tarde, ultima_fecha_envio_tarde, email_trabajo, cuil, pass_myweb, modulos_habilitados, IDPHONE, ES_VISITA, V_EMPRESA_ORIGEN, V_EMPLEADO_VISITA, V_PERTENENCIAS, V_NRO_ART, V_MOTIVO_VISITA, V_VENCIDO, FECHA_NACIMIENTO, PUESTO_TRABAJO, DIAS_VACACIONES, DIAS_VACACIONES_PERIODO_ANT, ULTIMO_PERIODO_CALCULADO, ID_ESQUEMA_APROBACION, PAIS, PROVINCIA, SUBIDA_JL_AL_CLOUD, id_empresa, idPersonaLenox, dias_vacaciones_pendientes, eliminado_mobile, alta_mobile, redondear_dias_vacaciones, dias_a_sumar, forzar_dias_vacaciones, id_tabla_vacaciones) VALUES (" + str(
            emp_id) + ", N'" + employee_first_name + "', N'" + employee_last_name + "', CAST(N'" + str(
            m) + "' AS DateTime), NULL, CAST(0.00 AS Decimal(10, 2)), 1, NULL, NULL, 1, NULL, CAST(N'2022-10-19T14:47:00.000' AS DateTime), NULL, 0, NULL, N'" + employee_dni + "', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, "+id_calendario+", NULL, NULL, 0, NULL, 0, NULL, NULL, NULL, NULL, N'0000000', NULL, 0, NULL, 0, NULL, NULL, NULL, 0, NULL, NULL, 0, 0, 2022, NULL, NULL, NULL, 0, 1, 2, 0, NULL, NULL, 0, 0, 0, -1);"
        cursor.execute(clientes)
        conn.commit()


def delete_sql():
    cursor.execute("""delete from CALENDARIOS_DETALLE;
						delete from RANGOS;
						delete from JORNADAS_GENERICAS;
						delete from FICHA_DETA;
						delete from JORNADAS;
						delete from AUSENCIAS;
						delete from CLIENTES;
                        delete from CALENDARIOS;""")
    conn.commit()
    conn.close()











