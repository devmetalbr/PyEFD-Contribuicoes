# -*- coding: iso-8859-1 -*-

##############################################################################
#                                                                            #
#  Copyright (C) 2012 Proge Inform�tica Ltda (<http://www.proge.com.br>).    #
#                                                                            #
#  Author: Daniel Hartmann <daniel@proge.com.br>                             #
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

from Registro import RegistroX001, Registro
from RegistroX990 import RegistroX990
from util import Ocorrencia, Obrigatoriedade

'''Registro F001. Abertura do bloco F.'''
class RegistroF001(RegistroX001):

    def __init__(self):
        RegistroX001.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "F001"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.IND_MOV))
        return linha + super(RegistroF001, self).gerar_linha()


'''Registro F010. Identificacao do estabelecimento.'''
class RegistroF010(Registro):

    def __init__(self):
        self.REG_PAI = "F001"
        self.REG = "F010"
        self.CNPJ = ""
        self.nivel = 2
        self.ocorrencia = Ocorrencia.VARIOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((self.REG, self.CNPJ))
        return linha + super(RegistroF010, self).gerar_linha()


'''
Registro F100. Demais documentos e operacoes geradoras de contribuicao e 
creditos.
'''
class RegistroF100(Registro):

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F100"
        self.IND_OPER = ""
        self.COD_PART = ""
        self.COD_ITEM = ""
        self.DT_OPER = ""
        self.VL_OPER = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.NAT_BC_CRED = ""
        self.IND_ORIG_CRED = ""
        self.COD_CTA = ""
        self.COD_CCUS = ""
        self.DESC_DOC_OPER = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_OPER,
            self.COD_PART,
            self.COD_ITEM,
            self.DT_OPER,
            self.VL_OPER,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.NAT_BC_CRED,
            self.IND_ORIG_CRED,
            self.COD_CTA,
            self.COD_CCUS,
            self.DESC_DOC_OPER,
            ))
        return linha + super(RegistroF100, self).gerar_linha()


'''Registro F111. Processo referenciado.'''
class RegistroF111(Registro):

    def __init__(self):
        self.REG_PAI = "F100"
        self.REG = "F111"
        self.NUM_PROC = ""
        self.IND_PROC = ""
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
        return linha + super(RegistroF111, self).gerar_linha()


'''
Registro F120. 
Bens incorporados ao ativo imobilizado - operacoes geradoras de creditos
com base nos encargos de depreciacao e amortizacao.
'''
class RegistroF120(Registro):

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F120"
        self.NAT_BC_CRED = ""
        self.IDENT_BEM_IMOB = ""
        self.IND_ORIG_CRED = ""
        self.IND_UTIL_BEM_IMOB = ""
        self.VL_OPER_DEP = ""
        self.PARC_OPER_NAO_BC_C_RED = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.COD_CCUS = ""
        self.DESC_BEM_IMOB = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NAT_BC_CRED,
            self.IDENT_BEM_IMOB,
            self.IND_ORIG_CRED,
            self.IND_UTIL_BEM_IMOB,
            self.VL_OPER_DEP,
            self.PARC_OPER_NAO_BC_C_RED,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            self.COD_CCUS,
            self.DESC_BEM_IMOB,
            ))
        return linha + super(RegistroF120, self).gerar_linha()


'''Registro F129. Processo referenciado.'''
class RegistroF129(Registro):

    def __init__(self):
        self.REG_PAI = "F120"
        self.REG = "F129"
        self.NUM_PROC = ""
        self.IND_PROC = ""
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
        return linha + super(RegistroF129, self).gerar_linha()


'''
Registro F130. 
Bens incorporados ao ativo imobilizado - operacoes geradoras de creditos
com base no valor de aquisicao/contribuicao.
'''
class RegistroF130(Registro):

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F130"
        self.NAT_BC_CRED = ""
        self.IDENT_BEM_IMOB = ""
        self.IND_ORIG_CRED = ""
        self.IND_UTIL_BEM_IMOB = ""
        self.MES_OPER_AQUIS = ""
        self.VL_OPER_AQUIS = ""
        self.PARC_OPER_NAO_BC_CRED = ""
        self.VL_BC_CRED = ""
        self.IND_NR_PARC = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.COD_CTA = ""
        self.COD_CCUS = ""
        self.DESC_BEM_IMOB = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NAT_BC_CRED,
            self.IDENT_BEM_IMOB,
            self.IND_ORIG_CRED,
            self.IND_UTIL_BEM_IMOB,
            self.MES_OPER_AQUIS,
            self.VL_OPER_AQUIS,
            self.PARC_OPER_NAO_BC_CRED,
            self.VL_BC_CRED,
            self.IND_NR_PARC,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.COD_CTA,
            self.COD_CCUS,
            self.DESC_BEM_IMOB,
            ))
        return linha + super(RegistroF130, self).gerar_linha()


'''Registro F139. Processo referenciado.'''
class RegistroF139(Registro):

    def __init__(self):
        self.REG_PAI = "F130"
        self.REG = "F139"
        self.NUM_PROC = ""
        self.IND_PROC = ""
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
        return linha + super(RegistroF139, self).gerar_linha()


'''Registro F150. Credito presumido sobre estoque de abertura.'''
class RegistroF150(Registro):

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F150"
        self.NAT_BC_CRED = ""
        self.VL_TOT_EST = ""
        self.EST_IMP = ""
        self.VL_BC_EST = ""
        self.VL_BC_MEN_EST = ""
        self.CST_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_CRED_PIS = ""
        self.CST_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_CRED_COFINS = ""
        self.DESC_EST = ""
        self.COD_CTA = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.NAT_BC_CRED,
            self.VL_TOT_EST,
            self.EST_IMP,
            self.VL_BC_EST,
            self.VL_BC_MEN_EST,
            self.CST_PIS,
            self.ALIQ_PIS,
            self.VL_CRED_PIS,
            self.CST_COFINS,
            self.ALIQ_COFINS,
            self.VL_CRED_COFINS,
            self.DESC_EST,
            self.COD_CTA,
            ))
        return linha + super(RegistroF150, self).gerar_linha()


'''
Registro F200. Operacoes da atividade imobiliaria - Unidade imobiliaria vendida.
'''
class RegistroF200(Registro):

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F200"
        self.IND_OPER = ""
        self.UNID_IMOB = ""
        self.IDENT_EMP = ""
        self.DESC_UNID_IMOB = ""
        self.NUM_CONT = ""
        self.CPF_CNPJ_ADQU = ""
        self.DT_OPER = ""
        self.VL_TOT_VEND = ""
        self.VL_REC_ACUM = ""
        self.VL_TOT_REC = ""
        self.CST_PIS = ""
        self.VL_BC_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_PIS = ""
        self.CST_COFINS = ""
        self.VL_BC_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_COFINS = ""
        self.PERC_REC_RECEB = ""
        self.IND_NAT_EMP = ""
        self.INF_COMP = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_OPER,
            self.UNID_IMOB,
            self.IDENT_EMP,
            self.DESC_UNID_IMOB,
            self.NUM_CONT,
            self.CPF_CNPJ_ADQU,
            self.DT_OPER,
            self.VL_TOT_VEND,
            self.VL_REC_ACUM,
            self.VL_TOT_REC,
            self.CST_PIS,
            self.VL_BC_PIS,
            self.ALIQ_PIS,
            self.VL_PIS,
            self.CST_COFINS,
            self.VL_BC_COFINS,
            self.ALIQ_COFINS,
            self.VL_COFINS,
            self.PERC_REC_RECEB,
            self.IND_NAT_EMP,
            self.INF_COMP,
            ))
        return linha + super(RegistroF200, self).gerar_linha()


'''
Registro F205. 
Operacoes da atividade imobiliaria - Custo incorrido da unidade imobiliaria.

Obs.: no layout, faltam os campos de no. 14 e 15. Como deve ficar
      o formato correto do arquivo ?
'''
class RegistroF205(Registro):

    def __init__(self):
        self.REG_PAI = "F200"
        self.REG = "F205"
        self.VL_CUS_INC_ACUM_ANT = ""
        self.VL_CUS_INC_PER_ESC = ""
        self.VL_CUS_INC_ACUM = ""
        self.VL_EXC_BC_CUS_INC_ACUM = ""
        self.VL_BC_CUS_INC = ""
        self.CST_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_CRED_PIS_ACUM = ""
        self.VL_CRED_PIS_DESC_ANT = ""
        self.VL_CRED_PIS_DESC = ""
        self.VL_CRED_PIS_DESC_FUT = ""
        self.CST_COFINS = ""
        # Falta o campo 14 ?
        # Falta o campo 15 ?
        self.ALIQ_COFINS = ""
        self.VL_CRED_COFINS_ACUM = ""
        self.VL_CRED_COFINS_DESC_ANT = ""
        self.VL_CRED_COFINS_DESC = ""
        self.VL_CRED_COFINS_DESC_FUT = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_UM
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.VL_CUS_INC_ACUM_ANT,
            self.VL_CUS_INC_PER_ESC,
            self.VL_CUS_INC_ACUM,
            self.VL_EXC_BC_CUS_INC_ACUM,
            self.VL_BC_CUS_INC,
            self.CST_PIS,
            self.ALIQ_PIS,
            self.VL_CRED_PIS_ACUM,
            self.VL_CRED_PIS_DESC_ANT,
            self.VL_CRED_PIS_DESC,
            self.VL_CRED_PIS_DESC_FUT,
            self.CST_COFINS,
            # Falta o campo 14 ?
            # Falta o campo 15 ?
            self.ALIQ_COFINS,
            self.VL_CRED_COFINS_ACUM,
            self.VL_CRED_COFINS_DESC_ANT,
            self.VL_CRED_COFINS_DESC,
            self.VL_CRED_COFINS_DESC_FUT,
            ))
        return linha + super(RegistroF205, self).gerar_linha()


'''
Registro F210. 
Operacoes da atividade imobiliaria - Custo orcado da unidade imobiliaria
vendida.

Obs.: no layout, faltam os campos de no. 1 a 3. Como deve ficar
      o formato correto do arquivo ?
'''
class RegistroF210(Registro):

    def __init__(self):
        self.REG_PAI = "F200"
        # campo no. 1 deve ser o REG
        self.REG = "F210"
        # FIXME: campo no. 2 ???
        # FIXME: campo no. 3 ???
        self.VL_CUS_ORC = ""
        self.VL_EXC = ""
        self.VL_CUS_ORC_AJU = ""
        self.VL_BC_CRED = ""
        self.CST_PIS = ""
        self.ALIQ_PIS = ""
        self.VL_CRED_PIS_UTIL = ""
        self.CST_COFINS = ""
        self.ALIQ_COFINS = ""
        self.VL_CRED_COFINS_UTIL = ""
        self.nivel = 4
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            # FIXME: campo no. 2 ???
            # FIXME: campo no. 3 ???
            self.VL_CUS_ORC,
            self.VL_EXC,
            self.VL_CUS_ORC_AJU,
            self.VL_BC_CRED,
            self.CST_PIS,
            self.ALIQ_PIS,
            self.VL_CRED_PIS_UTIL,
            self.CST_COFINS,
            self.ALIQ_COFINS,
            self.VL_CRED_COFINS_UTIL,
            ))
        return linha + super(RegistroF210, self).gerar_linha()


'''Registro F211. Processo referenciado.'''
class RegistroF211(Registro):

    def __init__(self):
        self.REG_PAI = "F200"
        self.REG = "F211"
        self.NUM_PROC = ""
        self.IND_PROC = ""
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
        return linha + super(RegistroF211, self).gerar_linha()


'''Registro F600. Contribuicao retida na fonte.'''
class RegistroF600(Registro):

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F600"
        self.IND_NAT_RET = ""
        self.DT_REC_RET = ""
        self.VL_REC = ""
        self.VL_RET_FONT = ""
        self.COD_REC = ""
        self.IND_NAT_REC = ""
        self.CNPJ = ""
        self.VL_RET_PIS = ""
        self.VL_RET_COFINS = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_NAT_RET,
            self.DT_REC_RET,
            self.VL_REC,
            self.VL_RET_FONT,
            self.COD_REC,
            self.IND_NAT_REC,
            self.CNPJ,
            self.VL_RET_PIS,
            self.VL_RET_COFINS,
            ))
        return linha + super(RegistroF600, self).gerar_linha()


'''Registro F700. Deducoes diversas.'''
class RegistroF700(Registro):

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F700"
        self.IND_ORI_DED = ""
        self.IND_NAT_DED = ""
        self.VL_DED_PIS = ""
        self.VL_DED_COFINS = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_ORI_DED,
            self.IND_NAT_DED,
            self.VL_DED_PIS,
            self.VL_DED_COFINS,
            ))
        return linha + super(RegistroF700, self).gerar_linha()


'''Registro F800. Identificacao do estabelecimento.'''
class RegistroF800(Registro):

    def __init__(self):
        self.REG_PAI = "F010"
        self.REG = "F800"
        self.IND_NAT_EVEN = ""
        self.DT_EVEN = ""
        self.CNPJ_SUCED = ""
        self.PA_CONT_CRED = ""
        self.COD_CRED = ""
        self.VL_CRED = ""
        self.PER_CRED_CIS = ""
        self.nivel = 3
        self.ocorrencia = Ocorrencia.UM_PARA_MUITOS
        self.obrigatoriedade = Obrigatoriedade.OC
        self.registros_filhos = []

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.IND_NAT_EVEN,
            self.DT_EVEN,
            self.CNPJ_SUCED,
            self.PA_CONT_CRED,
            self.COD_CRED,
            self.VL_CRED,
            self.PER_CRED_CIS,
            ))
        return linha + super(RegistroF800, self).gerar_linha()


'''Registro F990. Encerramento do bloco F.'''
class RegistroF990(RegistroX990):

    def __init__(self):
        RegistroX990.__init__(self)
        self.REG_PAI = "0000"
        self.REG = "F990"
        self.nivel = 1
        self.ocorrencia = Ocorrencia.UM
        self.obrigatoriedade = Obrigatoriedade.O

    def gerar_linha(self):
        linha = self.gerar_linha_de_registros((
            self.REG,
            self.QTD_LIN,
            ))
        return linha + super(RegistroF990, self).gerar_linha()
