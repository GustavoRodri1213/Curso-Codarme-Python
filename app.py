from evento import Evento
from evento_online import Evento_Online

ev_online = Evento_Online("Live de Python")
ev2_online = Evento_Online("Live de JavaScript")  
# ev_online.imprime_informacoes()
# ev2_online.imprime_informacoes()
print(ev_online.to_json())
print(ev2_online.to_json())
ev = Evento("Aula de Python","Rio de Janeiro")
ev.imprime_informacoes()