# Plataforma: Nexus 
# Geral: Acessar o bash (linux) dentro no Nexus 
#      run bash
# objetivo: Coletar o "show version do equipamento Nexus"
#
# Script: 
#!/bin/env python
from cli import *
show_version = cli('show version')
print(show_version)