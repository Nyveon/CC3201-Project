from django.shortcuts import render
from django.http import HttpResponse
from uwuland.models import Players, Teams, Matches, Actions
from django.db import connection
from collections import namedtuple
from .forms import IDPlayerForm, SacarWnes, SeleccionarEquipo


def index(request):
    return render(request, "uwuland_index.html")

def partidos_por_equipo(request):
    titulo = "Partidos por equipo"
    if request.method == "POST":
        form = SeleccionarEquipo(request.POST)
        if form.is_valid():
            eq = form.cleaned_data["equipo"]
            sql_res = consultar_partidos_equipo(eq)
            if sql_res:

                table_info = ""
                
                for row in sql_res:
                    _, _, date, team2, goals1, goals2, pen1, pen2 = row

                    d = goals1 - goals2

                    color = "lime" if d > 0 else ("yellow" if d == 0 else "red")
                    w = "Triunfo" if d > 0 else ("Empate" if d == 0 else "Derrota")

                    table_info += f'''
                        <tr>
                            <td>{date.date().strftime("%d/%m/%Y")}</td>
                            <td>{team2}</td>
                            <td>{goals1}-{goals2}</td>
                            <td>{pen1}-{pen2}</td>
                            <td><span style="color: {color};">{w}</span></td>
                        </tr>'''

                table = f'''<h2>Partidos de {Teams.objects.filter(teamid=eq)[:1].get().name}</h2>
                    <table>
                        <tr>
                            <th>Fecha</th>
                            <th>Contra</th>
                            <th>Goles</th>
                            <th>Penales</th>
                            <th>Resultado</th>
                        </tr>
                        {table_info}
                    </table>'''

                res = {"titulo": titulo, "formulario": form, "resultados": table}
            else:
                res = {"titulo": titulo, "formulario": form, "resultados": "<p>Equipo incorrecto</p>"}
            return render(request, "template_consultas.html", res)
    else:
        form = SeleccionarEquipo()
    return render(request, "template_consultas.html", {"titulo": titulo, "formulario": form})

def jugadores_por_equipo(request):
    titulo = "Jugadores por equipo"
    if request.method == "POST":
        form = SeleccionarEquipo(request.POST)
        if form.is_valid():
            eq = form.cleaned_data["equipo"]
            sql_res = consultar_jugadores_equipo(eq)
            if sql_res:
                table_info = ""

                for row in sql_res:
                    name = reorder_name(row[1])
                    table_info += f'''
                        <tr>
                            <td><a href="../ficha_jugador?id={row[0]}">{name}</a></td>
                        </tr>'''

                table = f'''<h2>Jugadores de {Teams.objects.filter(teamid=eq)[:1].get().name}</h2>
                    <table>
                        <tr>
                            <th>Nombre</th>
                        </tr>
                        {table_info}
                    </table>'''

                res = table
            else:
                res = "<p>Equipo incorrecto</p>"
            return render(request, "template_consultas.html", {"titulo": titulo, "formulario": form, "resultados": res})
    else:
        form = SeleccionarEquipo()
    return render(request, "template_consultas.html", {"titulo": titulo, "formulario": form})

def estadisticas_jugador(request):
    if request.method == "GET":
        pid = request.GET["id"]
        sql_res = consultar_estadisticas_jugador(pid)
        if sql_res:
            p = sql_res[0]
            titulo = f"Estadísticas de {reorder_name(p[0])}"
            _, eq, goals, matches, time_played, passes, touches, duels_won, duels_lost, fouls_conceded, yellow_cards, red_cards, penalties_conceded, penalty_goals = [x for x in p]
            res = {"titulo": titulo, "equipo": eq, "partidos": matches, "goles": goals, "goles_penales": penalty_goals, "pases": passes, "toques": touches, "duelos_ganados": duels_won, "tiempo_jugado": time_played, "duelos_perdidos": duels_lost, "faltas_concedidas": fouls_conceded, "amarillas": yellow_cards, "rojas": red_cards, "penales_concedidos": penalties_conceded}
        else:
            res = {"titulo": "Jugador no encontrado"}
    else:
        res = {"titulo": "Jugador no encontrado"}
    return render(request, "template_estadisticas_jugador.html", res)


def players(request):
    form = SacarWnes(request.POST)
    table_info = ""
    for player in sacar_wnes(5):
        table_info += f'''
                <tr>
                    <td>{player[0]}</td>
                    <td>{player[1]}</td>
                </tr>
                '''
    table = f"""<p>Aquí hay 5 wnes, uwu.</p>
                        <table>
                            <tr>
                                <th>ID</th>
                                <th>Nombre</th>
                            </tr>
                            {table_info}
                        </table>"""
    res = {"titulo": "5 weones", "resultados": table}
    return render(request, "template_consultas.html", res)

def consultar_partidos_equipo(eq):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM partidos_equipo WHERE teamid=%s ORDER BY "Date" ASC;', [eq])
        results = namedtuplefetchall(cursor)
    return results

def consultar_jugadores_equipo(eq):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players WHERE playerid IN (SELECT DISTINCT A.playerid FROM actions A, teams T WHERE T.teamid=%s AND A.teamid=T.teamid);", [eq])
        results = namedtuplefetchall(cursor)
    return results

def consultar_estadisticas_jugador(jugador):
    with connection.cursor() as cursor:
        #cursor.execute("""SELECT "name", "team1" AS Equipo, SUM("goals") AS goals, COUNT(DISTINCT matchid) AS n_partidos, SUM("penaltygoals") AS penales FROM actions, players WHERE actions.playerid=%s AND actions.playerid = players.playerid GROUP BY "name", "team1", "penaltygoals";""", [jugador])
        cursor.execute("SELECT name, team_name, goals, matches, time_played, passes, touches, duels_won, duels_lost, fouls_conceded, yellow_cards, red_cards, penalties_conceded, penalty_goals FROM (players P JOIN (SELECT playerid, teamid, COUNT(DISTINCT matchid) AS matches, SUM(timeplayed) AS time_played, SUM(totalsuccessfulpassesall) AS passes, SUM(touches) AS touches, SUM(duelswon) AS duels_won, SUM(duelslost) AS duels_lost, SUM(totalfoulsconceded) AS fouls_conceded, SUM(yellowcards) AS yellow_cards, SUM(redcards) AS red_cards, SUM(goals) AS goals, SUM(penaltiesconceded) AS penalties_conceded, SUM(penaltygoals) AS penalty_goals FROM actions WHERE playerid=%s GROUP BY playerid, teamid) A ON A.playerid=P.playerid) B JOIN (SELECT teamid, name AS team_name FROM teams) T ON B.teamid=T.teamid;", [jugador])
        results = namedtuplefetchall(cursor)
    return results

def sacar_wnes(n):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM Players LIMIT {n};")
        results = namedtuplefetchall(cursor)
    return results

def player_id(request):
    if request.method == "POST":
        form = IDPlayerForm(request.POST)
        if form.is_valid():
            pid = form.cleaned_data["id_player"]
            sql_res = consultar_jugador_id(pid)
            if sql_res:
                res = f"<p>ID {sql_res[0][0]}: {sql_res[0][1]}</p>"
            else:
                res = f"<p>Este wn no existe.</p>"
            return render(request, "template_consultas.html",
                {"titulo": "ID de un wn", "formulario": form, "resultados": res})
    else:
        form = IDPlayerForm()
    return render(request, "template_consultas.html", {"titulo": "ID de un wn", "formulario": form})

def consultar_jugador_id(pid):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Players WHERE playerid = %s", [pid])
        results = namedtuplefetchall(cursor)
    return results

def reorder_name(name):
    n = name.split(" ")
    return f"{n[-1]} {' '.join(n[:-1])}"

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
