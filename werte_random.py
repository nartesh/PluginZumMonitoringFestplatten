# Import der benötigten Funktionen und der API-Version
from .agent_based_api.v1 import *


# Erzeugung eines passenden Services, wenn die Agentensektion "werte_random" vorhanden ist
def discover_werte_random(section):
	yield Service()

# Lesen in der Datei und prüfen ob, der Parameter "Critical Warning"
#  zu finden ist und welchen Zustand ein Service annehmen soll
def check_werte_random(section):
	try:
		with open("/usr/lib/check_mk_agent/plugins/werte_random.txt") as f:
			lines = f.readlines()
			for line in lines:
				if line.startswith("Critical"):
					# Aufteile in einzelne Wörter und speichere
					#  den Wert für "Critical Warning" Parameter
					wert = line.split()
					switch_list = {
						"0x00": (State.OK, "Critical Warning type: 0x00 - Alles in Ordnung!"),
						"0x01": (State.CRIT, "Critical Warning type: 0x01 - "
											 "Temperature is over or under temperature threshold"),
						"0x02": (State.CRIT, "Critical Warning type: 0x02 - "
											 "NVM subsystem reliability has been degraded due to significant"),
						"0x03": (State.CRIT, "Critical Warning type: 0x03 - "
											 "The media has been placed in read only mode"),
						"0x04": (State.CRIT, "Critical Warning type: 0x04 - "
											 "The volatile memory backup device has failed"),
						"0x05": (State.CRIT, "Critical Warning type: 0x05 - "
											 "The Persistent Memory Region has become read-only or unrealiable"),
					}
					if(wert[2]) in switch_list:
						state, summary = switch_list[wert[2]]
						yield Result(state=state, summary=summary)
						return
					else:
						yield Result(state=State.WARN, summary = "Unbekannter Wert: {}".format(wert[2]))
						return
			# Wenn keine Zeile mit "Critical" gefunden wurde
			yield Result(state=State.UNKNOWN, summary = "Keine kritische Parameter gefunden!")
	# Falls die Datei nicht gefunden wird
	except FileNotFoundError:
		yield Result(state = State.UNKNOWN, summary = "Datei wurde nicht gefunden!")

# Registrierung an CheckMK-Server
register.check_plugin(
	# Name des Checkplugins
	name = "werte_random",
	# Name des Services im Monitoring
	service_name = "Werte Random",
	# Funktion zur Service-Erkennen
	discovery_function = discover_werte_random,
	# Funktion zur Durchführung des Checks
	check_function = check_werte_random,
)
