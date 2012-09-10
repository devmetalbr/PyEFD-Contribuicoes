# -*- coding: iso-8859-1 -*-

##############################################################################
#                                                                            #
#  Copyright (C) 2012 Proge Informática Ltda (<http://www.proge.com.br>).    #
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


class Obrigatoriedade:
    '''
    Indica a obrigatoriedade do Registro.

    O - O registro sempre � obrigat�rio.

    OC - O registro � obrigat�rio, se houver informa��o a ser prestada.
        Ex.: Registro C100 s� dever� ser apresentado se houver movimenta��o ou
        opera��es utilizando os documentos de c�digos 01, 1B, 04 ou 55.

    O_SE - O(...) - O registro � obrigat�rio se atentida a condi��o.
        Ex.: Registro C191 O (Se existir C190) O registro � obrigat�rio sempre
        que houver o registro C190.

    N - O registro n�o precisa ser informado.
    '''
    O = 'O'
    OC = 'OC'
    O_SE = 'O_SE'
    N = 'N'


class Ocorrencia:
    '''
    Indica a ocorr�ncia do Registro.

    UM - um por arquivo

    VARIOS - v�rios por arquivo

    UM_PARA_UM
    - dever� haver um �nico registro filho para respectivo registro pai

    UM_PARA_MUITOS
    - pode haver v�rios registros filhos para respectivo registro pai
    '''
    UM = 'UM'
    VARIOS = 'VARIOS'
    UM_PARA_UM = 'UM_PARA_UM'
    UM_PARA_MUITOS = 'UM_PARA_MUITOS'
