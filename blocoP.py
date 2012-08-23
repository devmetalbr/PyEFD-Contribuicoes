# -*- coding: iso-8859-1 -*-

##############################################################################
#                                                                            #
#  Copyright (C) 2012 Proge Inform�tica Ltda (<http://www.proge.com.br>).    #
#                                                                            #
#  Author Daniel Hartmann <daniel@proge.com.br>                              #
#                                                                            #
#  This program is free software: you can redistribute it and/or modify      #
#  it under the terms of the GNU Affero General Public License as            #
#  published by the Free Software Foundation, either version 3 of the        #
#  License, or (at your option) any later version.                           #
#                                                                            #
#  This program is distributed in the hope that it will be useful,           #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#  GNU Affero General Public License for more details.                       #
#                                                                            #
#  You should have received a copy of the GNU Affero General Public License  #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                            #
##############################################################################

from Registro import Registro, RegistroX001
from RegistroX990 import RegistroX990
from util import Ocorrencia, Obrigatoriedade

'''Abertura do bloco P'''
class RegistroP001(RegistroX001):

    def __init__(self):
        super(RegistroP001, self).__init__()
        self.REG_PAI = "0000"
        self.REG = "P001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM

        # se houver registro 0145
        self.obrigatoriedade = Obrigatoriedade.O_SE

        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_MOV,
            ))
        return linha + super(RegistroP001, self).gerar_linha()


'''Identifica��o do Estabelecimento'''
class RegistroP010(Registro):

    def __init__(self):
        self.REG_PAI = "P001"
        self.REG = "P010"
        self.CNPJ = ''
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS

        # se houver registro 0145
        self.obrigatoriedade = Obrigatoriedade.O_SE

        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.CNPJ,
            ))
        return linha + super(RegistroP010, self).gerar_linha()


'''Contribui��o Previdenci�ria sobre a Receita Bruta'''
class RegistroP100(Registro):

    def __init__(self):
        self.REG_PAI = "P010"
        self.REG = "P100"
        self.DT_INI = ''
        self.DT_FIN = ''
        self.VL_REC_TOT_EST = ''
        self.COD_ATIV_ECON = ''
        self.VL_REC_ATIV_ESTAB = ''
        self.VL_EXC = ''
        self.VL_BC_CONT = ''
        self.ALIQ_CONT = ''
        self.VL_CONT_APU = ''
        self.COD_CTA = ''
        self.INFO_COMPL = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS

        # se houver registro 0145
        self.obrigatoriedade = Obrigatoriedade.O_SE

        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.DT_INI,
            self.DT_FIN,
            self.VL_REC_TOT_EST,
            self.COD_ATIV_ECON,
            self.VL_REC_ATIV_ESTAB,
            self.VL_EXC,
            self.VL_BC_CONT,
            self.ALIQ_CONT,
            self.VL_CONT_APU,
            self.COD_CTA,
            self.INFO_COMPL,
            ))
        return linha + super(RegistroP100, self).gerar_linha()


'''Complemento da Escritura��o - Detalhamento da Apura��o da Contribui��o'''
class RegistroP110(Registro):

    def __init__(self):
        self.REG_PAI = "P100"
        self.REG = "P110"
        self.NUM_CAMPO = ''
        self.COD_DET = ''
        self.DET_VALOR = ''
        self.INF_COMPL = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_CAMPO,
            self.COD_DET,
            self.DET_VALOR,
            self.INF_COMPL,
            ))
        return linha + super(RegistroP110, self).gerar_linha()


'''Processo Referenciado'''
class RegistroP199(Registro):

    def __init__(self):
        self.REG_PAI = "P100"
        self.REG = "P199"
        self.NUM_PROC = ''
        self.IND_PROC = ''
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NUM_PROC,
            self.IND_PROC,
            ))
        return linha + super(RegistroP199, self).gerar_linha()


'''Consolida��o da Contribui��o Previdenci�ria sobre a Receita Bruta'''
class RegistroP200(Registro):

    def __init__(self):
        self.REG_PAI = "P001"
        self.REG = "P200"
        self.PER_REF = ''
        self.VL_TOT_CONT_APU = ''
        self.VL_TOT_AJ_REDUC = ''
        self.VL_TOT_AJ_ACRES = ''
        self.VL_TOT_CONT_DEV = ''
        self.COD_REC = ''
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS

        # se houver registro P100
        self.obrigatoriedade = Obrigatoriedade.O_SE

        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.PER_REF,
            self.VL_TOT_CONT_APU,
            self.VL_TOT_AJ_REDUC,
            self.VL_TOT_AJ_ACRES,
            self.VL_TOT_CONT_DEV,
            self.COD_REC,
            ))
        return linha + super(RegistroP200, self).gerar_linha()


'''Ajuste da Contribui��o Previdenci�ria Apurada sobre a Receita Bruta'''
class RegistroP210(Registro):

    def __init__(self):
        self.REG_PAI = "P200"
        self.REG = "P210"
        self.IND_AJ = ''
        self.VL_AJ = ''
        self.COD_AJ = ''
        self.NUM_DOC = ''
        self.DESCR_AJ = ''
        self.DT_REF = ''
        self.nivel = 3
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_AJ,
            self.VL_AJ,
            self.COD_AJ,
            self.NUM_DOC,
            self.DESCR_AJ,
            self.DT_REF,
            ))
        return linha + super(RegistroP210, self).gerar_linha()


'''Encerramento do bloco P'''
class RegistroP990(RegistroX990):

    def __init__(self):
        super(RegistroP990, self).__init__()
        self.REG_PAI = "0000"
        self.REG = "P990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM

        # se houver registro 0145
        self.obrigatoriedade = Obrigatoriedade.O_SE

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.QTD_LIN,
            ))
        return linha + super(RegistroP990, self).gerar_linha()

