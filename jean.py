# @app.route('/')
# def inicio():
#     if session:
#         if (session['usuario_logado'] == True):

#             cal = calendar.Calendar(firstweekday=6)
#             DIAS_DA_SEMANA = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY")
#             calDays = cal.monthdayscalendar(2022, 12)

#             return render_template('calendario.html', calDays=calDays, aux=0, DIAS_DA_SEMANA=DIAS_DA_SEMANA)
#         else:
#             return redirect(url_for('login'))
#     else:
#         return redirect('/login')