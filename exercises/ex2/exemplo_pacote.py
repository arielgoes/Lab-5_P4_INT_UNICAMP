#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from probe_hdrs import *

# Define o tipo para o cabeçalho Probe
TYPE_PROBE = 0x812

# Cria o cabeçalho Probe
probe_header = Probe(hop_cnt=2)  # Exemplo: hop_cnt=2

# Cria o cabeçalho ProbeData
probe_data_header = ProbeData(bos=1, swid=3, port=2, byte_cnt=1000, last_time=12345, cur_time=23456)  # Exemplo

# Cria o cabeçalho ProbeFwd
probe_fwd_header = ProbeFwd(egress_spec=1)  # Exemplo: egress_spec=1

# Constrói o pacote com os cabeçalhos
packet = Ether() / probe_header / probe_data_header / probe_fwd_header

# Exibe o pacote criado
print("Pacote formado:")
print(packet.show())