#!/usr/bin/env python3

import os

current_language = os.getenv("LANG")

msg = "Hello, World"

if current_language == "pt_BR":
    msg = "Ola, mundo"
elif current_language == "it_IT":
    msg = "Ciao, Mondo"    
elif current_language == "es_SP":
    msg = "Hola, Mundo"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"

print(msg)