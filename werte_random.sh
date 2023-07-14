#!/bin/bash

# Festplatte angeben
drive="/dev/nvme0n2"

# Dateiname angeben, in dem die Werte gespeichert werden sollen
filename="werte_random.txt"

# SMART-Parameter für kritische Meldung die Überwachen sollten
smart_param="Critical Warning:"

# Zufällige SMART-Werte generieren und in die Datei schreiben
value=$(($RANDOM % 7 + 0))
echo "echo \"<<<werte_random>>>\"" > $filename
echo "$smart_param 0x0$value" >> $filename