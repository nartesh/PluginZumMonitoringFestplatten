## CheckMK Plugin zum Monitoring von Festplatten ##
Das CheckMK-Plugin zum Monitoring von Festplatten ermöglicht die ***Überwachung der SMART-Werte*** von SSDs und Festplatten in Echtzeit. <br>
Es können Probleme mit Festplatten frühzeitig erkannt und behoben werden, um potenzielle Ausfälle und Datenverlust zu vermeiden. <br>
Das Plugin verwendet für die Abfrage der Smart-Werte den Kommandozeile-Befehl **`smartctl`**. <br>
Für die Analyse relevante Parameter ist **`Critical Warning`**, der je nach nicht ordnungsgemäß funktionierendem SMART-Wert. <br>

> Dieses Projekt enthält zwei Dateien: <br>
+ **Bash-Skript**, das ein Textdokument (**`werte_random.txt`**) mit den von der Konsole gelesenen SMART-Informationen erstellt. <br>
+ **Python-Skript**, das dafür verantwortlich ist, dass die Informationen aus dem Bash-Skript (Textdokument) interpretiert und im Dashboard angezeigt werden. <br>

## Werkzeuge ##
- **VMware Workstation** <br>
- **Oracle Linux 8** <br>
- **smartmontools** <br>
- **Python** <br>
- **CheckMK-Server**

## Installation und Konfiguration ##
- Hypervisor **VMware Workstation** <br>
- Betriebssystem **Oracle Linux 8** <br>
- **CheckMK-Sever** für Linux (Plattform RedHat/CentOS und OS-Version 8.x): [checkmk](https://checkmk.com/de/download) <br>
- Die Software aufsetzen und eigene Instanz (Site / OMD) auf Server erstellen <br>
- Das Paket **smartmontools** mit der Befehl **smartctl** um die SMART-Werte abzufragen <br>
- Das Monitoring auf dem CheckMK-Server einrichten:
  - CheckMK-Server Verbindung: https://IP-Adresse:Port/instanz name
  - Login Daten einfügen
  - CheckMK-Agent herunterladen und installieren: `RPM für Linux`
  - Host erstellen (es reicht nur Hostname und IP-Adresse)
  - Diagnose: die Überprüfung der Verbindung zum Host
  - Services konfigurieren: welche Dienste werden in der Überwachung angezeigt
  - Änderungen aktiviren und dann in den Überwachungsprozess einbezogen
- Die Datei **`werte_random.py`** soll kopieren in das Verzeichnis: **`/omd/sites/dein_sites_name/local/lib/check_mk/base/plugins/agent_based`** <br>
- Die Datei **`werte_random.sh`** soll auf dem Host kopieren in das Verzeichnis: **`/lib/check_mk_agent/plugins`**. Hier **_sehr wichtig_** die Bash-Skript (auch Textdatei) muss ausführbar sein: **`chmod +x werte_random.sh (chmod +x werte_random.txt)`** <br>

## Ergebnisse ##
**_`OK`_** - Alles in Ordnung! <br>
**_`CRIT`_** - Eine der SMART-Wert funktioniert nicht richtig! <br>
**_`WARM`_** - Unbekannter Parameter! <br>
**_`UNKNOWN`_** - Datei wurde nicht gefunden! <br>

## Quelle ##
[checkmk](https://docs.checkmk.com/latest/de/)
