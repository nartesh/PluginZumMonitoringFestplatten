## CheckMK_Plugin_zum_Monitoring_Festplatten ##

Das CheckMK-Plugin zum Monitoring von Festplatten ermöglicht die **Überwachung der SMART-Werte** von SSDs und Festplatten in Echtzeit. <br>
Es können Probleme mit Festplatten frühzeitig erkannt und behoben werden, um potenzielle Ausfälle und Datenverlust zu vermeiden.<br>
Enthält zwei Skripte: Bash-Skript (mit Textdatei) und Python-Skript. 

## Werkzeuge ##
- **VMware Workstation** <br>
- **Oracle Linux 8** <br>
- **smartmontools** mit der Befehl **smartctl** um die SMART-Werte abzufragen. <br>
- **Python** <br>
- **CheckMK-Server**

## Installation ##
1. CheckMK-Sever für Linux: https://checkmk.com/de/download <br>
2. Die Datei "werte_random.py" soll in das Verzeichnis: "/omd/sites/dein_sites_name/local/lib/check_mk/base/plugins/agent_based" kopieren <br>
3. Die Datei "werte_random.sh" soll in das Verzeichnis: "/lib/check_mk_agent/plugins" auf dem Host kopieren
4. Sehr wichtig die Bash-Skript (auch Textdatei) muss ausführbar sein: chmod +x werte_random.sh (chmod +x werte_random.txt)

## Quelle ##
https://docs.checkmk.com/latest/de/
