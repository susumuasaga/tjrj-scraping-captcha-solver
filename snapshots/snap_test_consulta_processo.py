# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_parse_process_page1 1'] = {
    'advogados': [
        {
            'nome': 'VITAL JUARES FERREIRA RAPOSO',
            'oab': 'RJ106959'
        }
    ],
    'assunto': 'Furto Qualificado  (Art. 155, § 4o. - CP)',
    'autor': 'MINISTÉRIO PÚBLICO DO ESTADO DO RIO DE JANEIRO',
    'classe': 'Ação Penal - Procedimento Ordinário',
    'comarca': 'Comarca de Nova Iguaçu',
    'movimentacoes': [
        {
            'data': GenericRepr('datetime.date(2017, 8, 16)'),
            'integra': '''O Ministério Público do Estado do Rio de Janeiro ofereceu denúncia, às fls.02/02B,  contra MARCELO BARCELOS DA SILVA, qualificado às fl. 02, dando-o como incurso na pena prevista no artigo 155, §4°, II do Código Penal, porque, em breve síntese, no dia 12/07/2014, por volta das 16h30min, no interior do Posto de Gasolina Shell, localizado Rodovia Presidente Dutra, 464, Califórnia, nesta Comarca, o DENUNCIADO, agindo de forma consciente e voluntariamente, subtraiu com emprego de fraude, 24,26 litros de gasolina aditivada, totalizando a quantia de R$74,70, de propriedade do Posto de Gasolina Shell.\r
\tSegundo relatado, o denunciado solicitou ao frentista do Posto de Gasolina Shell o abastecimento de 24,26 litros de gasolina aditivada em seu veículo e após dirigir-se ao caixa para efetuar o pagamento do combustível, deparou-se com um veículo a frente que finalizava o pagamento no caixa.\r
\tAto contínuo, o denunciado aproveitou que a cancela, que impede a saída de veículos, abriu para liberar o veículo à frente e passou juntamente com este, impedindo que a cancela voltasse ao estado inicial, rumando fuga do local, sem efetuar o pagamento da conta.\r
\r
\tDenuncia às fls.02/02B; Relatório final de inquérito às fls.31/31v; FAC do acusado às fls.38/42 e 97/100v; Decisão de recebimento da denúncia às fls.33; Resposta a acusação às fls.60; Assentada da AIJ às fls.75/77, 86/88 e 92/94; em alegações finais, fls.101/105, o Ministério Público requereu que seja julgado improcedente a pretensão punitiva estatal, para absolver o acusado do delito imputado na denúncia, ante a ausência de tipicidade material da conduta; a Defesa, em alegações finais, às fls.106/109, requereu a absolvição do acusado.\r
\t             É O RELATÓRIO. EXAMINADOS, DECIDO.\r
\r
\r
Encerrada a instrução criminal, a pretensão punitiva deduzida na denúncia restou comprovada.\r
\r
A materialidade está devidamente comprovada pela prova documental e bem como pela prova oral produzida tanto em sede policial quanto em Juízo, que atesta a existência do crime.\r
\r
A autoria, por sua vez, foi devidamente comprovada pelos elementos probatórios carreados aos autos, em face da homogeneidade da prova oral produzida.\r
\r
Testemunhas afirmaram em juízo ao crivo do contraditório e da ampla defesa que o acusado solicitou ao frentista do Posto de Gasolina Shell o abastecimento de 24,26 litros de gasolina aditivada em seu veículo e após dirigir-se ao caixa para efetuar o pagamento do combustível, deparou-se com um veículo a frente que finalizava o pagamento no caixa. Ato contínuo, o denunciado aproveitou que a cancela, que impede a saída de veículos, abriu para liberar o veículo à frente e passou juntamente com este, impedindo que a cancela voltasse ao estado inicial, rumando fuga do local, sem efetuar o pagamento da conta.\r
\r
Interrogado em juízo o denunciado confirma que no momento devido não efetuou o pagamento referente ao abastecimento de combustível. Alega que se aborreceu durante o atendimento e depois retornou ao estabelecimento lesado para acertar os valores devidos.\r
\r
No que tange a aplicação do princípio da insignificância in casu, cabe observar que não há amparo à aplicação do mesmo em nosso ordenamento jurídico, senão de forma excepcional, não se devendo confundir bem de pequeno valor com o de valor insignificante, este ensejador, necessariamente, da exclusão do crime, à ausência de ofensa ao bem jurídico tutelado, e aquele, eventualmente, caracterizador do privilégio insculpido no §2º, do artigo 155, do Código Penal. A tese de tratar-se de bem de pequena monta e, em consequência, insignificante, deve ser analisada no caso concreto, passível de admissão, se tal resultar da prova colhida durante a instrução criminal, em que se verificar ausência de potencialidade lesiva ao lesado, sem diminuição de seu patrimônio. Aceitá-la de forma irrestrita e abstrata, importaria em permitir a qualquer um, dela se valer, para cometer pequenos furtos, incentivando condutas que atentam contra a ordem social e a segurança da coletividade. Evidentemente, a subtração de bem, cujo valor não pode ser desconsiderado, não comporta a consideração de penalmente irrelevante, sob a pena de incentivar a prática de pequenos delitos, conduzindo à desordem social.\r
\r
\r
Deste modo, o princípio da insignificância ou bagatela deve ser aplicado com cautela, considerando-se insignificante aquilo que realmente o é, sempre observadas as circunstâncias objetivas e subjetivas que circundam o caso concreto, impedindo-se o desvirtuamento do real alcance do instituto e transformação de seu conteúdo em porta aberta para a impunidade. Descabe, portanto, invocar os princípios da bagatela ou da intervenção mínima do Estado, a fim de tornar atípica a conduta, sobretudo ao analisar in casu os antecedentes do denunciado. Na hipótese em testilha, a absolvição do réu serviria como verdadeiro estímulo à prática de crimes dessa natureza e, portanto, não se insere na concepção doutrinária e jurisprudencial de crime de bagatela, impondo-se necessário o decreto condenatório.\r
\r
Insta registrar, que o denunciado possui anotações em sua folha de antecedentes criminais por supostos envolvimentos em delitos de furtos , inclusive condenação com transito em julgado , como se pode observar em sua FAC acostada aos autos. Entendo que o Princípio da Bagatela reclama não só a análise de critério objetivo, não bastando a avaliação do quantum da lesão patrimonial. É imperioso aferir também o comportamento do agente. O réu, com sua conduta reiterada, revelou elevada reprovabilidade em seu comportamento, que deve ser repudiado e devidamente punido pelo Estado. Verifica-se pela natureza do objeto furtado (combustível), logo se percebe que a intenção do acusado não era a de satisfazer situação de extrema necessidade pessoal (sobrevida, saúde, alimentação, higiene, moradia ou proteção contra intempéries), mas sim obter vantagem em prejuízo de terceiro. Acusado não praticou a infração para garantir sua subsistência, portanto, não há que falar em aplicação do princípio da insignificância. Com efeito, absolver o acusado na presente ação poderia acarretar em mais um furto, dado o elevado grau de audácia do acusado que sequer modificou seu alvo.\r
\r
E nem há de se dizer em eventual alegação de nulidade em razão do posicionamento favorável do Parquet, que opinou pela absolvição do denunciado, já que, nos exatos termos do artigo 385 do Código de Processo Penal, o juiz poderá proferir sentença condenatória, ainda que o Ministério Público tenha opinado pela absolvição, podendo, inclusive, reconhecer agravantes, embora nenhuma tenha sido alegada. Deste modo, o juiz não está vinculado à manifestação ministerial e tampouco defensiva, em razão do seu livre convencimento nos termos do artigo 155 do Código de Processo Penal, no cogitando, in casu, portanto, de julgamento extra petita.\r
\r
\r
\r
Ademais, a jurisprudência do Superior Tribunal de Justiça se firmou no sentido de ser possível a prolação de Sentença Condenatória, ainda que haja pedido de absolvição formulado pelo Ministério Público, a teor do art. 385 do Código de Processo Penal.\r
\r
\r
Portanto, a prova constante dos autos é firme ao apontar o réu como autor do delito descrito no artigo 155, §4º, II do Código Penal.\r
\r
Quanto à majorante, ressalte-se que no furto mediante fraude o autor visa um plano ardiloso que supere a vigilância da vítima, fazendo com que deixe os bens desprotegidos, facilitando, assim, a ação criminosa. In casu, restou evidenciado pelas provas colacionadas no presente feito, especialmente nos depoimentos destacados, que o acusado agiu, de forma fraudulenta, com o fim de ludibriar a vigilância da vítima e permitir a subtração, consubstanciando proteção insuficiente ao bem jurídico tutelado pela norma penal.\r
\r
Inafastável, por conseguinte, o juízo de reprovabilidade da conduta.\r
\r
Em síntese: a conduta típica não está amparada em causa excludente de sua ilicitude, sendo o réu culpável - porquanto imputável -, possuindo consciência de que contrariavam o ordenamento legal, e, nas condições em que o fato ocorreu, podia e devia agir em conformidade com as normas proibitivas contidas no tipo penal violado.\r
\r
Isto posto, JULGO PROCEDENTE a pretensão punitiva deduzida na denúncia para CONDENAR MARCELO BARCELOS DA SILVA, por violação ao artigo 155, §4º, II do Código Penal .\r
\r
DA DOSIMETRIA DA PENA\r
\r
Em atenção às diretrizes do artigo 68 do Código Penal e pelo exame das circunstâncias judiciais delineadas no artigo 59 do Código Penal, favoráveis ao acusado, bem como a fim de atender ao caráter de prevenção geral e especial da pena, fixo a pena-base no mínimo cominado abstratamente à espécie, isto é, 02 (DOIS) ANOS DE RECLUSÃO E 10 (DEZ) DIAS-MULTA.\r
\r
.\r
2ª fase: Não há circunstâncias agravantes ou atenuantes a serem reconhecidas.\r
\r
 3ª fase: Não há causas que aumentem ou diminuam a pena razão pela qual torno definitiva a pena 02 (DOIS) ANOS DE RECLUSÃO E 10 (DEZ) DIAS-MULTA.\r
\r
\r
Com fulcro no artigo 33, § 2º, alíneas ´b´ e ´c´, a contrario sensu, c/c §3º, do Código Penal, é estabelecido o REGIME ABERTO para o início de cumprimento de sua pena privativa de liberdade, por ser este o mais adequado, especialmente para os fins de prevenção da pena aplicada.\r
\r
\r
\r
Incabível a substituição da pena, nos moldes do art. 44 do CP ou de aplicação de sursis, nos termos do art. 77 do CP, diante das condições subjetivas do acusado que possui condenação com transito em julgado por delitos da mesma natureza, não sendo as medidas despenalizadora adequadas, portanto, para o caso.\r
\r
                            Condeno-o, ainda, ao pagamento das custas processuais (art. 804 do CPP). Fica o réu condenado, também, nos termos do AVISO CGJ Nº 821/2011 nos valores devidos pelos atos de fornecimento de CD com conteúdo da audiência realizada por meio de gravação audiovisual e de expedição de certidão com a transcrição da audiência.\r
\r
\r
                          Intime-se, por mandado, o réu para ciência da sentença condenatória, sendo certo que poderá apelar em liberdade, vez que não vislumbro a necessidade de sua segregação cautelar.\r
\r
\r
                         Certifique nos autos o cumprimento da Resolução nº 63/08 do CNJ.\r
\r
                           Transitada em julgado de forma definitiva, lance o nome do acusado no rol dos culpados, anote-se, comunique-se e cumpra-se o artigo 105 da LEP, arquivando-se o feito. Cumpra-se o Aviso Conjunto TJ/CGJ nº 08/2013.\r
\r
                                                P. na íntegra.\r
\r
Nova Iguaçu, 16 de agosto de 2017.''',
            'resumo': 'Isto posto, JULGO PROCEDENTE a pretensão punitiva deduzida na denúncia para CONDENAR MARCELO BARCELOS DA SILVA, por violação ao artigo 155, §4º, II do Código Penal .',
            'tipo': 'sentença',
            'titulo': 'Sentença - Julgado procedente o pedido'
        },
        {
            'data': GenericRepr('datetime.date(2016, 7, 21)'),
            'integra': '''PROCESSO: 007003-08.2014.8.19.0038\r
Autor: MINISTÉRIO PÚBLICO\r
RÉU: MARCELO BARCELOS DA SILVA\r
\r
ASSENTADA\r
\r
Aos 21 de julho de 2016, na Sala de Audiências deste Juízo, onde se encontravam presentes a MM. Juiz de Direito Dr. ANNA CHRISTINA DA SILVEIRA FERNANDES e o representante do Ministério Público Dr. Luís Fernando Ferreira Gomes.\r
\r
Aberta a Audiência às 15h 20min, determinou a MM Dr. Juiz que fosse feito pregão, ao qual estava presente o acusado, bem como o patrono Dr. Vital Juares Ferreira Raposo.\r
\r
Foi interrogado o acusado, através do sistema audiovisual, conforme mídia em apartado.\r
\r
Pela MM. Dr. Juiz foi proferida a seguinte decisão:\r
\r
1º) Dê-se vista às partes para apresentação das alegações finais no prazo legal.\r
\r
Cientes os presentes. Encerrada a presente às 15h 30mins. Nada mais havendo, lida e achada conforme vai devidamente assinada. Eu, Victor Daniel, Assistente de Gabinete, digitei.\r
\r
\r
\r
ANNA CHRISTINA DA SILVEIRA FERNANDES\r
JUIZ DE DIREITO\r
\r
\r
PROMOTOR DE JUSTIÇA                                                                  DEFESA\r
\r
\r
    _____________________________\r
    ACUSADO''',
            'resumo': '''Pela MM. Dr. Juiz foi proferida a seguinte decisão:\r
\r
1º) Dê-se vista às partes para apresentação das alegações finais no prazo legal.''',
            'tipo': 'despacho',
            'titulo': 'Despacho em Audiência  - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2015, 12, 11)'),
            'integra': 'Ao 10º dia do mês de dezembro do ano 2015, na sala de audiências deste Juízo, presentes se encontravam o MM. Juiz de Direito ANNA CHRISTINA DA SILVEIRA FERNANDES e o(a) ilustre presentante do Ministério Público. Ao pregão, não foi apresentado o acusado, havendo noticias de sua prisão. PRESENTE a testemunha Leidiana Braga Valadão. Aberta a audiência, as partes ficaram cientes sobre a utilização do registro fonográfico e audiovisual, bem como foram advertidos da vedação de divulgação não autorizada dos registros audiovisuais a pessoas estranhas ao processo. Iniciada a instrução, foi colhido o depoimento da testemunha presente, cujo depoimento segue em mídia própria acostada aos autos, não tendo a defesa se oposto á realização do ato. Pelo MP nada foi requerido. Pela defesa nada foi requerido. O registro fonográfico e audiovisual da audiência foi gravado em mídia própria (cd/dvd) e será juntado aos autos, passando a ser parte integrante desta assentada, conforme previsto no inciso III, do artigo 5º da Resolução 14/2010, do TJRJ. Pelo MM. Juiz foi proferido o seguinte DESPACHO/DECISÃO: Aguarde-se o retorno da CP.',
            'resumo': 'Pela defesa nada foi requerido. O registro fonográfico e audiovisual da audiência foi gravado em mídia própria (cd/dvd) e será juntado aos autos, passando a ser parte integrante desta assentada, conforme previsto no inci...',
            'tipo': 'despacho',
            'titulo': 'Despacho em Audiência  - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2015, 6, 26)'),
            'integra': '''1 - Trata-se de ação penal pública proposta pelo Ministério Público do Rio de Janeiro em face de MARCELO BARCELOS DA SILVA.\r
\r
O denunciado, regularmente citado, apresentou defesa prévia.\r
\r
Constata-se que a denúncia sob o aspecto formal é perfeita. Estão presentes todos os requisitos legais inerentes ao exercício da ação penal in casu, incluída a indispensável justa causa. O processo está regular e válido, inexistindo vício a ensejar o reconhecimento de nulidade.\r
\r
Com efeito, os fatos e fundamentos deduzidos na defesa escrita não afastam os indícios de autoria e materialidade coligidos em sede extrajudicial, impondo-se a apuração dos fatos narrados na exordial da presente ação penal, garantindo-se ao acusado a ampla defesa e o contraditório.\r
\r
Ademais, não se configuram quaisquer das hipóteses previstas no art. 397 do CPP a ensejar a absolvição sumária do réu.\r
\r
Desta forma, as questões pertinentes ao mérito da ação serão analisadas oportunamente, quando do julgamento do mérito.\r
\r
Por tais razões, MANTENHO O RECEBIMENTO DA DENÚNCIA e, na forma do art. 399, do CPP, designo o dia 08/10/2015 às 12:35 h, para realização da AIJ, quando o réu será interrogado ao final. Requisitem-se/Intimem-se o acusado e as testemunhas arroladas na denúncia e na defesa prévia.\r
\r
No caso das testemunhas residirem fora da Comarca, expeça-se carta precatória para inquirição.\r
\r
Dê-se ciência ao M.P. e à Defesa.\r
\r
2 - Intime-se o patrono subscritor de fls.36, para cumprir  o disposto no art. 45 CPC. Sem prejuízo, intime-se o réu para indicar novo patrono no prazo de 05 dias ou manifestar interesse em ser patrocinado pela D.P, ressalvando-se que no caso de inércia será nomeada a Defensoria.''',
            'resumo': 'Por tais razões, MANTENHO O RECEBIMENTO DA DENÚNCIA e, na forma do art. 399, do CPP, designo o dia 08/10/2015 às 12:35 h, para realização da AIJ, quando o réu será interrogado ao final. Requisitem-se/Intimem-se o acusado...',
            'tipo': 'decisão',
            'titulo': 'Decisão - Decisão Determinação'
        },
        {
            'data': GenericRepr('datetime.date(2014, 9, 23)'),
            'integra': '''Trata-se de ação penal pública incondicionada movida contra MARCELO BARCELOS DA SILVA, por infração ao artigo 155, §4º, II, do Código Penal, oferecendo o ilustre representante do Ministério Público Estadual a denúncia de fls. 02.\r
\r
O processo está regular e válido, inexistindo vício a ensejar o reconhecimento de nulidade. Estão presentes as condições da ação e os pressupostos processuais, inclusive a indispensável justa causa.\r
\r
Assim, com fulcro em interpretação a contrário sensu do que dispõe o art. 395, CPP, RECEBO A DENÚNCIA.  Cite-se o acusado para, em 10 (dez) dias, oferecer defesa escrita (art. 396, CPP), por advogado que venha a constituir, ficando ciente que o não-oferecimento da defesa no prazo, implicará na nomeação da Defensoria Pública para o patrocínio de seus interesses processuais.\r
\r
Em caso de nomeação do Defensor Público, dê-se vista para oferecimento da defesa preliminar.\r
\r
Atenda-se à promoção do M.P. Expeça-se MBA dos laudos, se for o caso.\r
\r
Venha a FAC - on-line e, não sendo possível sua extração, expeça-se mandado de busca e apreensão da FAC.\r
\r
Dê-se ciência ao MP.''',
            'resumo': 'Assim, com fulcro em interpretação a contrário sensu do que dispõe o art. 395, CPP, RECEBO A DENÚNCIA.  Cite-se o acusado para, em 10 (dez) dias, oferecer defesa escrita (art. 396, CPP), por advogado que venha a constitu...',
            'tipo': 'decisão',
            'titulo': 'Decisão - Recebida a denúncia'
        }
    ],
    'numero': '0070033-08.2014.8.19.0038',
    'reus': [
        {
            'cpf': None,
            'nome': 'MARCELO BARCELOS DA SILVA'
        }
    ],
    'vara': '1ª Vara Criminal'
}

snapshots['test_parse_process_page2 1'] = {
    'advogados': [
        {
            'nome': 'MARCIO DE BARROS BAIÃO',
            'oab': 'RJ074024'
        },
        {
            'nome': 'DEFENSOR PÚBLICO',
            'oab': 'TJ000002'
        }
    ],
    'assunto': 'Furto  (Art. 155 - CP) N/F Crime Tentado (Art. 14, II, Cp)., II',
    'autor': 'MINISTERIO PUBLICO DO ESTADO DO RIO DE JANEIRO',
    'classe': 'Ação Penal - Procedimento Ordinário',
    'comarca': 'Comarca da Capital',
    'movimentacoes': [
        {
            'data': GenericRepr('datetime.date(2015, 9, 30)'),
            'integra': '''O Ministério Público ofereceu denúncia em face de JONATHA NASCIMENTO GOUVEIA E JACKSON AVELINO DE OLIVEIRA, pela prática da conduta delituosa prevista no artigo 155, § 4º, inciso IV na forma do artigo 14, inciso II, ambos do Código Penal, ambos devidamente qualificados à fl. 02. Narra a peça inaugural que:\r
\r
´No dia 13 de janeiro de 2015, por volta das 17h, na Avenida Francisco Bhering, Ipanema, nesta Comarca, os denunciados, agindo de forma livre e consciente, em comunhão de ações e desígnios, tentaram subtrair para ambos, 02 (duas) mochilas marca Jansport, uma roxa outra estampada, contendo 1 (um) telefone celular marca Apple IPhone azul, 1 (um) telefone celular de cor preta, 1 (um) telefone celular marca Samsung Duos de cor azul, 1 (um) telefone celular de cor azul, 1 (uma) bola LFP branca e vermelha, uma canga, vários objetos de uso pessoal, chaves e a quantia de R$ 29,90 (vinte e nove reais e noventa centavos), tudo descrito no auto de apreensão de fls. 09/10, de propriedade das vítimas Mariana Tavares de Lima Scelza, Marina Thees Romita, Eduardo Willian Fon Wu Mesquita e Matheus Lires Neto, evadindo-se, em seguida, do local.\r
\r
O crime não se consumou por circunstâncias alheias à vontade dos agentes, uma vez que foram perseguidos, alcançados e presos.\r
\r
Na ocasião do evento, policiais militares que faziam ronda regular na região foram alertados por banhistas que perseguiam os denunciados, quando os alcançaram e retomaram seus pertences, ocasião em que os policiais realizaram a prisão.´ - fls. 02/02A.\r
\r
A denúncia de fls. 02/02B, recebida em 04/02/2015, à fls. 86/87, veio instruída com a decisão do flagrante de fls. 02D/03; o auto de prisão em flagrante de fls. 05/06; o registro de ocorrência de fls. 07/08vº; o auto de apreensão de fls. 09/10; os autos de encaminhamento de fls. 11, 12 e 13; a nota de culpa de fl. 23; as guias de recolhimento de preso de fls. 25/26; os relatórios de vida pregressa e boletim individual de fls. 29/30;\r
\r
Petição defensiva do acusado Jackson Avelino de Oliveira à fls. 36/48, requerendo a sua liberdade provisória.\r
\r
Petição defensiva dos acusados Jônatha Nascimento Gouveia e Jackson Avelino de Oliveira às fls. 49/52, requerendo a concessão de liberdade provisória e, subsidiariamente, substituição da prisão por medida cautelar diversa.\r
\r
Folha de antecedentes criminais do acusado Jônatha Nascimento Gouveia de fls. 58/62, da qual consta 01 (uma) anotação referente ao presente feito.\r
\r
Folha de antecedentes criminais do acusado Jackson Avelino de Oliveira de fls. 63/69, da qual constam 03 (três) anotações criminais.\r
\r
Cota ministerial de fls. 70/72, oferecendo denúncia, requerendo conversão da prisão em flagrante de Jackson Avelino em prisão preventiva e a de Jônatha Nascimento em medida cautelar prevista no artigo 319 do CPP.\r
\r
Petição da defesa técnica de Jackson Avelino de fls. 73/74 reiterando pedido de liberdade provisória do acusado.\r
\r
Decisão de fls. 86/87 recebendo a denúncia, concedendo a liberdade provisória a Jônatha Nascimento mediante a imposição de medidas cautelares e decretando a prisão preventiva de Jackson Avelino.\r
\r
Petição da defesa técnica do acusado Jackson Avelino à fls. 107/110, juntando cópias de sua documentação.\r
\r
Petição da defesa técnica do acusado Jônatha Nascimento à fls. 111/114, juntando cópias de sua documentação.\r
\r
Mandado de citação do acusado Jônatha devidamente cumprido às fls. 116/118.\r
\r
Alvará de soltura do acusado Jônatha Nascimento Gouveia devidamente cumprido às fls. 119/120.\r
\r
Termo de compromisso do acusado Jônatha Nascimento Gouveia à fl. 127.\r
\r
Resposta de ofício requisitório sobre o habeas corpus do acusado Jackson Avelino às fls. 131/132.\r
\r
Petição da defesa de Jônatha à fl. 134 juntando documentos.\r
\r
 Defesa preliminar do acusado Jônatha Nascimento Gouveia de fl. 136 requerendo a sua absolvição sumária com fulcro no artigo 397, inciso I, do CPP.\r
\r
Termo de compromisso do acusado Jônatha Nascimento Gouveia à fl. 137.\r
\r
Mandado de citação positivo do acusado Jackson às fls. 138/139.\r
\r
Petição da defesa técnica de Jackson Avelino de fls. 140/141 requerendo revogação da prisão preventiva do acusado.\r
\r
Defesa preliminar do acusado Jackson Avelino de fls. 145/165 requerendo a rejeição da denúncia e, como consequência, a sua absolvição com base no princípio in dubio pro reo.\r
\r
Decisão de fl. 167 mantendo o recebimento da denúncia e designando audiência de instrução e julgamento para o dia 27/04/15.\r
\r
Despacho de fl. 168 redesignando audiência de instrução e julgamento para o dia 14/05/15.\r
\r
Mandado de prisão preventiva do acusado Jackson Avelino devidamente cumprido à fl. 171.\r
\r
Audiência de instrução e julgamento retratada na assentada de fls. 198/ 199, na qual foram ouvidas as testemunhas Marina Thees Romita, José Wilson Mendonça e Eloi Alves Neto. Na mesma oportunidade foram interrogados os réus. A Defesa do acusado Jackson requereu a revogação de sua prisão preventiva. O Ministério Público requereu vista dos autos para apreciação do pleito defensivo e retificação da imputação dos autos para o artigo 155, § 4º, IV c.c artigo 14, II, todos do CP. Deferiu-se a retificação e abriu-se vista ao Ministério Público.\r
\r
Cota ministerial de fl. 215vº pelo indeferimento do pedido de liberdade do réu Jackson Avelino.\r
\r
Alegações finais do Ministério Público de fls. 216/221 pugnando pela condenação dos acusados às penas do artigo 155, § 4º, inciso IV, na forma do artigo 14, II, todos do Código Penal.\r
\r
Despacho de fl. 222 indeferindo o pedido de fl. 198.\r
\r
Termo de compromisso do acusado Jônatha Nascimento Gouveia à fl. 223.\r
\r
Laudo de exame de avaliação indireta em fl. 225.\r
\r
Decisão de fl. 226 mantendo o decreto prisional.\r
\r
Alegações finais da defesa técnica do acusado Jonatha Nascimento de fls. 227/301 pugnando pela reconsideração do deferimento da retificação da imputação dos autos e sua absolvição.\r
\r
Alegações finais da defesa técnica do acusado Jackson Avelino de fls. 302/ pugnando pela reconsideração do deferimento da retificação da imputação dos autos e sua absolvição.\r
\r
Termo de compromisso do acusado Jônatha Nascimento Gouveia à fl. 310.\r
\r
Termo de compromisso do acusado Jônatha Nascimento Gouveia à fl. 311.\r
\r
Laudo de exame material de fls. 312/313.\r
\r
Petição do acusado Jackson Avelino de fls. 314/315 requerendo a juntada da revogação de mandato e a assistência da Defensoria Pública.\r
\r
Alegações finais do acusado Jackson Avelino de fls. 318/323 pugnando pela sua absolvição com fulcro no artigo 386, inciso V, do CPP. Subsidiariamente, requer seja afastada a qualificadora, declassificado o delito para a  modalidade simples do artigo 155, caput, na forma do artigo 14, inciso II, ambos do Código Penal, aplicando pena mínima e os benefícios cabíveis.\r
\r
É O RELATÓRIO.\r
DECIDO.\r
\r
Trata-se da imputação aos acusados Jonatha Nascimento Gouveia e Jackson Avelino de Oliveira pela da prática do delito tipificado no artigo 155, § 4º, inciso IV, na forma do artigo 14, inciso II, ambos do Código Penal.\r
\r
Segundo a narrativa constante da peça acusatória, os acusados, no dia 13 de janeiro de 2015, no bairro de Ipanema, agindo de forma livre e consciente, em comunhão de ações e desígnios, tentaram subtrair bens alheios.\r
\r
Em seu depoimento em sede judicial, a testemunha Marina Thees Romita, narrou que, no dia dos fatos, estava na praia com alguns amigos e que deixaram três mochilas na areia para entrarem no mar. Pouco tempo depois, uma senhora disse ter visto dois homens pegarem suas mochilas e que seu marido teria corrido atrás deles. Nesse momento, a testemunha e seus amigos foram falar com policiais que estavam no calçadão. Esclareceu que os policiais ´passaram um rádio´ a outros policiais que estavam mais a frente e soube que eles haviam capturado os acusados. Afirmou que reconheceu os acusados, pois, momentos antes do ocorrido, os mesmos estavam importunando-a com gracejos. Declarou ter recuperado todos os seus pertences.\r
\r
Em seu depoimento em sede judicial, o policial José Wilson Mendonça da Silva, afirmou ter participado da prisão dos acusados. Declarou ter visto uma multidão correndo atrás dos acusados na praia, tendo alcançado-os apenas quando a multidão os cercou. Afirmou que as vítimas reconheceram seus pertences.\r
\r
Na ocasião de seu depoimento em sede judicial, o policial Eloi Alves Neto, corroborou o depoimento de seu colega. Declarou que as pessoas que perseguiram os réus afirmaram que os mesmos teriam furtado as mochilas na praia, mas os acusados negavam.\r
\r
Em seu interrogatório em sede judicial, o acusado Jonatha Nascimento, declarou que, no dia dos fatos, estava na praia com seu amigo Jackson. Enquanto seu amigo estava comprando refrigerante, viu as mochilas na areia e pegou os bens, alegando, entretanto, que pensou que estas estavam abandonadas. Negou ter combinado de furtar as mochilas juntamente com o acusado Jackson.\r
\r
Em seu interrogatório em sede judicial, o acusado Jackson Avelino, negou que tivesse praticado os fatos narrados na inicial. Declarou que foi comprar refrigerante e, quando retornou, viu Jonatha correndo. Decidiu, então, ir atrás do amigo para saber o que estava acontecendo. Quando o alcançou, as pessoas disseram que eles teriam furtado as mochilas juntos, motivo pelo qual foi levado para a delegacia.\r
\r
A materialidade delitiva do crime de furto se comprova por qualquer meio admitido em Direito, haja vista que a subtração é um fato transeunte, no vertente caso, restou demonstrada pelo auto de apreensão de fls. 09/10, bem como pelos depoimentos prestados em sede judicial.\r
\r
A autoria quanto ao acusado Jonatha Nascimento pode ser extraída do auto de prisão em flagrante de fls. 05/06 e dos depoimentos prestados em sede judicial. Ressalte-se que, submetido ao crivo do contraditório, o acusado não negou que tivesse levado as  mochilas, tentando justificar o ato afirmando que acreditava que estavam abandonadas.\r
\r
Ademais, conforme relatado pela vítima Marina em seu depoimento, os acusados faziam gracejos com ela e suas amigas momentos antes da ocorrência dos fatos. Desta forma, a versão apresentada pelo acusado não se mostra crível, vez que o mesmo já teria visto que as mochilas pertenciam as vitimas e não se encontravam abandonadas.\r
\r
Outrossim, alegar que as mochilas estavam abandonadas não justifica a subtração da coisa.\r
\r
Quanto ao acusado Jackson Avelino, a autoria não pode ser comprovada, vez que nenhuma testemunha que prestou depoimento neste juízo presenciou os fatos. Ademais, após leitura atenta dos autos, verifica-se que não há quaisquer outras provas de que o acusado concorreu para a ação delituosa. Por ocasião de seu interrogatório, negou a prática delituosa.\r
\r
Desta forma, impõe-se a absolvição do acusado Jackson Avelino de Oliveira das imputações versadas na denúncia e a condenação do acusado Jonatha Nascimento Gouveia.\r
\r
Acolho o pleito defensivo quanto ao afastamento da qualificadora do crime de furto pelo concurso de pessoas, vez que não foi possível comprovar durante a instrução processual a comunhão de ações e desígnios entre os réus Jonatha e Jackson.\r
\r
A hipótese é de delito tentado, posto que os bens foram recuperados imediatamente após a subtração.\r
\r
Derradeiramente há que se reconhecer a atenuante prevista do artigo 65, inciso I, do Código Penal, posto ser o acusado menor de 21 (vinte e um) anos.\r
\r
Ausentes quaisquer circunstâncias que afastem a tipicidade, imputabilidade ou culpabilidade de sua conduta.\r
\r
Face ao exposto, JULGO PARCIALMENTE PROCEDENTE o pedido e CONDENO o acusado JONATHA NASCIMENTO GOUVEIA nas sanções do artigo 155, caput, na forma do artigo 14, II c.c artigo 65, I, todos do Código Penal e ABSOLVO o acusado JACKSON AVELINO DE OLIVEIRA com fulcro no art. 386, VII, do Código de Processo Penal.\r
\r
Atenta às diretrizes dos artigos 59 e 68, ambos do Código Penal, passo a dosimetria da pena do acusado Jonatha Nascimento Gouveia:\r
\r
Na primeira fase, tendo em vista que o acusado agiu com a culpabilidade normal do tipo, fixo a pena-base no mínimo legal, ou seja, em 01 (um) ano de reclusão e 10 (dez) dias-multa à razão do mínimo legal.\r
\r
Na segunda fase, deixo de diminuir a pena em razão da atenuante prevista no artigo 65, inciso I, do CP, posto que a pena não pode quedar-se abaixo do mínimo legal, conforme dispõe a Súmula nº 231, do STJ. Assim, mantenho a pena em 01 (um) ano de reclusão e 10 (dez) dias-multa à razão do mínimo legal.\r
\r
Na terceira fase, diminuo de 2/3 (dois terços) a pena, ante a causa de diminuição prevista no artigo 14, II, do Código Penal, encontrando uma pena de 04 (quatro) meses de reclusão e 03 (três) dias-multa à razão do mínimo legal, pena que torno definitiva à míngua de outras causas influenciadoras no cálculo da pena.\r
\r
Fixo o regime inicialmente aberto para cumprimento de pena, na forma do artigo 33, § 2º, alínea c, do Código Penal.\r
\r
Outrossim, entendo que a substituição da pena privativa de liberdade por restritiva de direito é suficiente, na forma do artigo 44, do Código Penal, modificado pela Lei 9.714/98, visto que o condenado é réu primário e possui bons antecedentes. Desta forma, procedo à substituição por uma pena restritiva de direitos, a ser fixada pelo Juízo da execução penal.\r
\r
No caso em exame verifica-se que a custódia cautelar do condenado não se afigura necessária, eis que permaneceu solto durante o curso do processo, sendo substituída a pena privativa de liberdade por restritiva de direitos.\r
\r
Deixo de condenar o acusado Jônatha Nascimento Gouveia no pagamento das custas do processo, diante de sua patente hipossuficiência.\r
\r
Expeçam-se alvarás de soltura.\r
\r
Transitada em julgado a presente, procedam-se às anotações devidas.\r
\r
Publicada nas mãos do Sr. Escrivão. Registre-se e intimem-se.''',
            'resumo': 'Face ao exposto, JULGO PARCIALMENTE PROCEDENTE o pedido e CONDENO o acusado JONATHA NASCIMENTO GOUVEIA nas sanções do artigo 155, caput, na forma do artigo 14, II c.c artigo 65, I, todos do Código Penal e ABSOLVO o acusa...',
            'tipo': 'sentença',
            'titulo': 'Sentença - Julgado procedente em parte do pedido'
        },
        {
            'data': GenericRepr('datetime.date(2015, 6, 17)'),
            'integra': '''Em cumprimento ao ATO EXECUTIVO CONJUNTO TJ/CNJ N.º 03/2015, o qual instituiu o mutirão carcerário, procedo a revisão da prisão preventiva do denunciado.\r
\r
Compulsando os autos verifico que permanecem íntegros os requisitos autorizadores da segregação cautelar. A custódia deve ser mantida considerando-se a gravidade concreta do crime, evidenciada pelo modus operandi da ação delituosa e na violência empregada no delito.\r
\r
Cumpre ressaltar que o feito segue seu regular trâmite, não havendo que se falar em excesso de prazo para encerramento da instrução criminal. Com efeito, não se pode fazer uma simples soma matemática para aferir o prazo, sem levar em conta as peculiaridades do caso concreto e a complexidade do processo.\r
\r
Portanto, conclui-se que a prisão preventiva é a única medida eficiente para se atingir o fim colimado na hipótese vertente de preservação da ordem pública, garantia da aplicação da lei penal e conveniência da instrução criminal.\r
\r
Ante o exposto, MANTENHO o decreto prisional. Dê-se ciência.\r
\r
À Defesa para alegações finais.\r
\r
Após, ao MM Juiz vinculado (fls. 198/199).''',
            'resumo': '''Ante o exposto, MANTENHO o decreto prisional. Dê-se ciência.\r
\r
À Defesa para alegações finais.\r
\r
Após, ao MM Juiz vinculado (fls. 198/199).''',
            'tipo': 'decisão',
            'titulo': 'Decisão - Decisão ou Despacho Não-Concessão'
        },
        {
            'data': GenericRepr('datetime.date(2015, 5, 28)'),
            'integra': '''Uma vez encerrada a instrução criminal, já tendo o MP inclusive apresentado suas alegações finais, fica superada a alegação de constrangimento ilegal por excesso de prazo (Súmula 52 do STJ). Ademais, como bem salientou o MP, não houve demora considerável na instrução do feito. À conta de tais razões, indefiro o pedido de fls. 198.\r
À Defesa em alegações finais por memoriais.\r
Após, ao MM Juiz vinculado.''',
            'resumo': 'Uma vez encerrada a instrução criminal, já tendo o MP inclusive apresentado suas alegações finais, fica superada a alegação de constrangimento ilegal por excesso de prazo (Súmula 52 do STJ). Ademais, como bem salientou o...',
            'tipo': 'despacho',
            'titulo': 'Despacho - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2015, 5, 14)'),
            'integra': '''Processo: 0012232-17.2015.8.19.0001 - Distribuído em: 14/01/2015\r
Art. 155,  c/c art. 14, II, do CP\r
Réu: JONATHA NASCIMENTO GOUVEIA\r
Réu: JACKSON AVELINO DE OLIVEIRA\r
Advogado: Márcio de Barros Baião - OAB RJ 74.024\r
Audiência: Instrução e Julgamento\r
Data da Audiência: 14/05/2015\r
\r
ASSENTADA\r
\r
Aos 14 (quatorze) dias do mês de maio de 2015, à hora designada, na sala de audiências deste Juízo, perante o MM. Juiz de Direito, Dra. RENATA GIL DE ALCANTARA VIDEIRA, realizou-se a audiência designada nestes autos. Presentes a ilustre representante do Ministério Público, Dra. DENISE DE MATTOS MARTINEZ GERACI, os acusados, devidamente assistidos por advogado constituído, bem como as testemunhas Marina Thees Romita, José Wilson Mendonça da Silva e Eloi Alves Neto, que foram ouvidas. A seguir, foram os réus interrogados, conforme termos e registros audiovisuais acostados aos autos. Não havendo outras diligências requeridas pelas partes, foi declarada encerrada a instrução criminal e dada a palavra às mesmas em alegações finais orais, conforme registro audiovisual. Pela defesa foi dito que o acusado Jackson encontra-se preso desde janeiro do corrente pela suposta prática de crime de furto. O mesmo é trabalhador, tecnicamente primário, com residência fixa, tudo devidamente comprovado nos autos e caso venta a ocorrer uma eventual condenação , obviamente a apena a ser aplicada não será a corporal, aliando-se ao fato de que esse delito não é daqueles que se usa a violência, razão pela qual requer a revogação da prisão preventiva do acusado Jackson, expedindo-se o competente contramandado de prisão. Pelo Ministério Público foi dito que requer vista para apreciação do pleito libertário. Pelo Ministério Público foi requerida a retificação da imputação dos autos para o artigo 155, §4º, IV c.c. artigo 14, II, todos do Código Penal, eis que já devidamente descritos na denúncia.  Pelo MM Juiz de Direito, foi proferida a seguinte decisão: Defiro a retificação. Vista ao Ministério Público.  Cientes e intimados os presentes. Nada mais havendo, foi determinado o encerramento da presente que, após lido e achado conforme, vai devidamente assinado. Eu, Secretário de Juiz, ____digitei e subscrevo.\r
\r
RENATA GIL DE ALCANTARA VIDEIRA\r
JUIZ DE DIREITO TITULAR''',
            'resumo': 'Pelo MM Juiz de Direito, foi proferida a seguinte decisão: Defiro a retificação. Vista ao Ministério Público.  Cientes e intimados os presentes. Nada mais havendo, foi determinado o encerramento da presente que, após lid...',
            'tipo': 'despacho',
            'titulo': 'Despacho em Audiência  - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2015, 4, 22)'),
            'integra': '''Tendo em vista que, em razão dos feriados dos dias 21/04 e 23/04/2015, não é possível cumprir, em tempo hábil, as diligências determinadas às fls. 167, retiro o feito da pauta do dia 27/04/2015 e redesigno o ato para o dia 14/05/2015, às 14h15min.\r
Cumpra-se, no mais, no que couber, fls. 167.''',
            'resumo': 'Tendo em vista que, em razão dos feriados dos dias 21/04 e 23/04/2015, não é possível cumprir, em tempo hábil, as diligências determinadas às fls. 167, retiro o feito da pauta do dia 27/04/2015 e redesigno o ato para o d...',
            'tipo': 'despacho',
            'titulo': 'Despacho - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2015, 4, 17)'),
            'integra': '''Trata-se de ação penal pública incondicionada movida contra Jonatha Nascimento Gouveia e Jackson Avelino de Oliveira por infração da norma contida no artigo 155, caput, c/c art. 14, II, ambos do Código Penal.\r
       Os denunciados apresentaram respostas às fls. 136 (primeiro denunciado) e fls. 145/165 (segundo denunciado), afirmando, em síntese, não serem verdadeiros os fatos narrados na denúncia.\r
       A denúncia sob o aspecto formal é perfeita. Presentes todos os requisitos legais inerentes ao exercício da ação penal ´in casu´, incluída a indispensável justa causa.\r
       Com efeito, as questões pertinentes ao mérito da ação serão analisadas, oportunamente, cabendo ressaltar que persistem os indícios de autoria e materialidade coligidos em sede policial, impondo-se, agora,   a instrução probatória  no âmbito da presente ação penal, garantindo-se ao imputado a ampla defesa e o contraditório.\r
       Por tais razões, MANTENHO O RECEBIMENTO DA DENÚNCIA.\r
       Designo audiência de instrução e julgamento para o dia 27/04/2015 às 14h:30min.\r
       Requisitem-se/Intimem-se todos.\r
       Intimem-se o MP, a DP e a Defesa do segundo réu.''',
            'resumo': '''Por tais razões, MANTENHO O RECEBIMENTO DA DENÚNCIA.\r
       Designo audiência de instrução e julgamento para o dia 27/04/2015 às 14h:30min.\r
       Requisitem-se/Intimem-se todos.\r
       Intimem-se o MP, a DP e ...''',
            'tipo': 'decisão',
            'titulo': 'Decisão - Decisão Determinação'
        },
        {
            'data': GenericRepr('datetime.date(2015, 3, 16)'),
            'integra': '''Expeça-se novo mandado de citação para o acusado JACKSON, a ser cumprido pelo OJA de plantão.\r
\r
Decorrido o prazo para apresentação de resposta ´in albis´, nomeio a Defensoria Pública para patrocínio dos interesses processuais do acusado JONATHA.\r
\r
Aguarde-se o retorno do mandado de citação e dê-se vista à DP.''',
            'resumo': '''Expeça-se novo mandado de citação para o acusado JACKSON, a ser cumprido pelo OJA de plantão.\r
\r
Decorrido o prazo para apresentação de resposta "in albis", nomeio a Defensoria Pública para patrocínio dos interesses proc...''',
            'tipo': 'despacho',
            'titulo': 'Despacho - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2015, 2, 4)'),
            'integra': '''Trata-se de ação penal movida em face de JÔNATHA NASCIMENTO GOUVEA e JACKSON AVELINO DE OLIVEIRA, onde se lhe imputa a prática do delito tipificado no art. 155, caput, c/c art. 14, II, do Código Penal.\r
\r
1) RECEBO A DENÚNCIA.\r
\r
2) Citem-se e intimem-se os acusado para, em 10 (dez) dias, oferecerem defesa escrita (Art. 396, CPP), por advogado que venham a constituir, ficando cientes que o não oferecimento da defesa no prazo implicará na nomeação da Defensoria Pública para o patrocínio de seus interesses no âmbito desta ação penal.\r
\r
3) No que toca ao requerimento de liberdade provisória dos acusados, tenho que, com o advento da Lei nº 12.403/2011, a segregação cautelar somente se justifica quando presentes os requisitos do art. 312 e nas hipóteses previstas nos incisos I, II, III e parágrafo único, do artigo 313, ambos do CPP.\r
\r
O que deve nortear a aplicação de tais medidas cautelares é o binômio necessidade (art. 282, I, CPP) e adequação (art. 282, II, CPP): ´necessidade para aplicação da lei penal, para a investigação ou instrução criminal(...) e adequação da medida à gravidade do crime, circunstâncias do fato e condições pessoais do indiciado ou acusado.´\r
\r
No caso que ora se analisa, o acusado JÔNATHA é primário e menor de 21 anos, sendo certo, de acordo com a capitulação da denúncia, faz jus a suspensão condicional do processo, de modo que não estão presentes os requisitos autorizadores da custódia cautelar.\r
\r
De outro lado, considerando, ainda, a necessidade da instrução processual, assim como visando a aplicação da lei penal, entendo adequada a aplicação das medidas cautelares de  comparecimento periódico em Juízo - sempre nos 10 (dez) primeiros dias do mês, em periodicidade mensal, além da comprovação de residência - (art. 319, I, CPP) e de proibição de ausentar-se da Comarca (art. 319, V, CPP), em relação as quais deve o acusado prestar compromisso.\r
Faço notar, que a citação do denunciado será procedida imediatamente - ainda no estabelecimento em se encontra custodiado -, dado que existe alguma incerteza quanto ao respectivo endereço residencial.\r
\r
Por outro lado, o acusado JACKSON AVELINO DE OLIVEIRA ostenta condenações em sua FAC. Em que pese não haver o trânsito em julgado das referidas anotações, há que observar que o acusado delinquiu reiteradas vezes, o que demonstra que faz o crime meio de vida, assim, a custódia cautelar justifica-se para manutenção da ordem pública, tão vulnerada pela prática de crimes semelhantes.\r
\r
Isto posto, CONCEDO LIBERDADE PROVISÓRIA a JÔNATHA NASCIMENTO GOUVEA, mediante a imposição das medidas cautelares supramencionadas e DECRETO A PRISÃO PREVENTIVA de JACKSON AVELINO DE OLIVEIRA.\r
\r
Expeça-se alvará de soltura para JÔNATHA NASCIMENTO GOUVEA, que deverá ser cumprido concomitantemente ao mandado de citação.\r
\r
Expeça-se mandado de prisão em desfavor de JACKSON AVELINO DE OLIVEIRA, com validade até 12/01/2023.''',
            'resumo': '''1) RECEBO A DENÚNCIA.\r
\r
2) Citem-se e intimem-se os acusado para, em 10 (dez) dias, oferecerem defesa escrita (Art. 396, CPP), por advogado que venham a constituir, ficando cientes que o não oferecimento da defesa no p...''',
            'tipo': 'decisão',
            'titulo': 'Decisão - Recebida a denúncia'
        }
    ],
    'numero': '0012232-17.2015.8.19.0001',
    'reus': [
        {
            'cpf': None,
            'nome': 'JONATHA NASCIMENTO GOUVEIA'
        }
    ],
    'vara': '5ª Vara Criminal'
}

snapshots['test_parse_process_page3 1'] = {
    'advogados': [
        {
            'nome': 'DEFENSOR PÚBLICO',
            'oab': 'TJ000002'
        }
    ],
    'assunto': 'Posse Ou Porte Ilegal de Arma de Fogo de Uso Restrito e Outros (Art. 16 - Lei 10.826/03), e art. 37 lei 11.343/2006',
    'autor': 'MINISTERIO PUBLICO DO ESTADO DO RIO DE JANEIRO',
    'classe': 'Ação Penal - Procedimento Ordinário',
    'comarca': 'Comarca da Capital',
    'movimentacoes': [
        {
            'data': GenericRepr('datetime.date(2018, 6, 18)'),
            'integra': '''Cumpram-se os v. acórdãos (fls. 355/373 e 399/405). Considerando que a sentença de fls. 238/241 condenou somente o réu Lucas a três anos e quatro meses de reclusão, no regime semiaberto, e pagamento de quinhentos dias-multa, pela prática do crime previsto no art. 37 c/c art. 40, IV e VI da Lei 11.343/2006, tendo sido a sentença mantida pelos referidos acórdãos, EXPEÇA-SE MANDADO DE PRISÃO EM DESFAVOR DE LUCAS SOUZA SILVA, com prazo para cumprimento até 17/06/2026.\r
\r
Com a captura do réu, expeça-se CES definitiva. Façam-se as comunicações de praxe. Tudo cumprido, arquivem-se.''',
            'resumo': 'Cumpram-se os v. acórdãos (fls. 355/373 e 399/405). Considerando que a sentença de fls. 238/241 condenou somente o réu Lucas a três anos e quatro meses de reclusão, no regime semiaberto, e pagamento de quinhentos dias-mu...',
            'tipo': 'decisão',
            'titulo': 'Decisão - Reforma de decisão anterior'
        },
        {
            'data': GenericRepr('datetime.date(2015, 12, 1)'),
            'integra': '''1 - Cumpra-se, imediatamente, o determinado à fl. 275.\r
\r
2 - Recebo o recurso interposto pelo Ministério Público à fl. 250 nos seus regulares efeitos.\r
\r
Dê-se vista ao Ministério Público para a apresentação de suas razões.\r
\r
Após, dê-se vista à Defesa Técnica para ciência da sentença proferida às fls. 214/218, bem como para a apresentação das contrarrazões.\r
\r
Por fim, remetam-se os autos ao e. TJRJ.''',
            'resumo': '''1 - Cumpra-se, imediatamente, o determinado à fl. 275.\r
\r
2 - Recebo o recurso interposto pelo Ministério Público à fl. 250 nos seus regulares efeitos.\r
\r
Dê-se vista ao Ministério Público para a apresentação de suas raz...''',
            'tipo': 'decisão',
            'titulo': 'Decisão - Recebido o recurso Sem efeito suspensivo'
        },
        {
            'data': GenericRepr('datetime.date(2015, 7, 14)'),
            'integra': '''Vistos, etc.\r
\r
A Ilustre Representante do Ministério Público ofereceu denúncia em face de LUCAS SOUZA SILVA e PAULO SÉRGIO DE SANTANA MARIS na data de 09 de março de 2015, que foi recebida em 17/03/2015 (fl.74), pela prática da conduta descrita no art. 37, da Lei nº 11.343/06, art. 16, caput, da Lei nº 10.826/03, e art.244-B da lei 8069/90, em concurso material, conforme fatos assim resumidos:\r
\r
´No dia 07 de janeiro de 2015, por volta das 15h, na rua Almirante Tamandaré esquina com Beco da Paz, Comunidade Proença Rosa, Pavuna, nesta cidade, os denunciados, com vontade livre e consciente, em comunhão de ações e desígnios entre si e os adolescentes Wallace de Oliveira Alfena e Ezequiel Carlos Emilio, colaboravam, como informantes, com grupo, organização ou associação destinados à prática de tráfico ilícito de entorpecentes, utilizando-se de quatro rádios transmissores, conforme auto de apreensão de flS.15/16.\r
Nas mesmas circunstâncias de tempo e lugar, os denunciados, consciente e voluntariamente, detinham, arma de fogo de uso restrito, qual seja, uma pistola calibre 9mm, marca não identificada, municiada com 12 munições de mesmo calibre, tudo sem autorização e em desacordo com determinação legal ou regulamentar.\r
Ainda nas mesmas circunstâncias de tempo e lugar acima descritas, os denunciados de forma livre e consciente corromperam os adolescentes Wallace de Oliveira Alfena e Ezequiel Carlos Emiliano, com ele praticando os crimes de porte ilegal de arma de uso restrito (art.16 da lei 10.826/03) e colaboração ao tráfico (art.37 da lei 11.343/06).\r
Policiais militares realizavam operação na comunidade quando avistaram a presença dos denunciados e dos adolescentes em localidade conhecida como boca de fumo, sentados próximos ao valão. Ao serem abordados foram encontrados com cada um dos indivíduos, denunciados e adolescentes, um rádio comunicador, num total de quatro rádios e a arma de fogo que estava em poder do adolescente Ezequiel.´\r
\r
O feito encontra-se instruído com as seguintes peças: APF e AAAPI (fls.02d/03); Termos de Declaração (fls.07 e 08); Registro de Ocorrência nº 039-00144/2015 (fls.09/10); Nota de Culpa (fls.11 e 12); Auto de Apreensão (fls.15/16); FAC do acusado Lucas (fls.41/46); FAC do acusado Paulo Sérgio (fls.47/51); Laudo de Exame em Arma de Fogo (fls.132/135 e 148/149verso); Laudo de Exame de Material - Carregador (fls.136/137 e 152/153); Laudo de Exame de Material - Rádios Transmissores (fls.138/139, 149/149verso e 157/157verso);.\r
\r
Decisão, às fls.52/53, convertendo a prisão em flagrante em prisão preventiva.\r
\r
Às fls.67/73, o Ministério público, ao oferecer a denúncia e a cota ministerial, opinou pela manutenção da prisão dos acusados.\r
\r
Decisão, à fl.74, recebendo a denúncia e determinando a citação dos acusados.\r
\r
Juntada de documentos pela Defesa, às fls.75/84, porém pertencentes réu de outro processo.\r
\r
Juntada de mandado citatório, devidamente cumprido, às fls.105/106, tendo o réu Lucas se manifestado no sentido de ser assistido pela Defensoria Pública.\r
\r
Juntada de mandado citatório, devidamente cumprido, às fls.107/108, tendo o réu Paulo Sérgio se manifestado no sentido de ser assistido pela Defensoria Pública.\r
\r
Resposta à acusação, às fls.109/116.\r
\r
Decisão, às fls.117/118, mantendo a decisão de recebimento da denúncia, indeferindo a preliminar arguida, designando AIJ para o dia 21/05/2015 às 13:45 horas e determinando a expedição de mandado de busca e apreensão.\r
\r
Audiência de Instrução e Julgamento, em dia 21 de maio de 2015, onde foram ouvidas duas testemunhas de acusação, uma testemunha de defesa, bem como procedido o interrogatório dos acusados, conforme mídia acostada aos autos. Pelas Defesas foi requerida a juntada de documentos, o que foi deferido. Pela MM Dra. Juíza foi determinada a abertura de vistas as partes para apresentação de alegações finais, fl.166.\r
\r
Em Alegações Finais, o Ministério Público, às fls. 183/191, pugnou pela condenação dos réus nos exatos termos da denúncia.\r
\r
Alegações Finais da Defesa pugnando: 1- pela absolvição dos acusados de todos os delitos; 2- subsidiariamente, na hipótese de condenação pelo delito previsto no art.37 da lei 11.343/06, que seja reconhecida a causa especial de aumento de pena previsto no inciso IV, do art.40 da referida lei, e não o delito autônomo previsto no art.16 da lei 10.826/03, e da causa de diminuição prevista no §4º, do art.33 da lei 11.343/06 em seu patamar máximo, bem como a atenuante da menoridade.\r
\r
Em apenso o procedimento dos menores Wallace e Ezequiel.\r
\r
É o relatório.\r
Decido\r
\r
Imputa-se aos acusados a prática das condutas ilícitas descritas no art. 37, da Lei nº 11.343/06, no art. 16, caput, da Lei nº 10.826/03 e art.244-B da Lei 8.069, em concurso material.\r
\r
Mister se faz algumas considerações.\r
\r
Considerando que a arma foi apreendida no mesmo contexto fático, por ocasião da prisão dos acusados, entendo que a figura típica prevista no art. 16, caput, da Lei nº 10.826/03, deve ser absorvida pela majorante prevista no art. 40, inciso IV, da Lei nº 11.343/06.\r
\r
Mesmo caminho deve ser seguido em relação ao delito previsto no art.244-B da lei 8069/90, eis que aplicável a causa especial de aumento de pena prevista no inciso VI, do art.40 da Lei 11.343/06.\r
\r
Passo analisar, assim, o delito previsto no art. 37, da Lei nº 11.343/06:\r
\r
Da análise dos autos, verifica-se comprovada a OCORRÊNCIA do delito pelos depoimentos prestados em sede policial e em Juízo, bem como pelo auto de apreensão de fls.15/16, laudo de exame em arma de fogo (fls.132/135 e 148/149verso), laudo  de exame de material - carregador (fls.136/137 e 152/153) e laudo de exame de material - rádios transmissores (fls.138/139, 149/149verso e 157/157verso).\r
\r
A AUTORIA restou devidamente comprovada em relação ao acusado Lucas.\r
\r
No dia dos fatos, policiais militares em operação na localidade observaram quatro elementos sentados em uma esquina, sendo os dois acusados e dois menores. Procedida a abordagem foi encontrado ao lado dos mesmos quatro rádios transmissores e na cintura de um deles uma pistola calibre 9mm.\r
\r
O policial Deivid informou que deu para ouvir no rádio apreendido o informe que a polícia estava chegando à comunidade.\r
\r
Segundo os policiais militares os acusados e os menores informaram que trabalhavam para o tráfico na função de ´atividade´. Diante das circunstâncias, todos foram conduzidos para a Delegacia Policial.\r
\r
O acusado Lucas, por ocasião de seu interrogatório, se utilizou o direito de permanecer em silêncio.\r
\r
 Já o acusado Paulo Sérgio negou a veracidade dos fatos, afirmando que havia quatro elementos sentados, sendo que, com a chegada da polícia, um deles ocorreu e que estava próximo, sendo abordado pelos policiais. Informou, também, que estava com duas amigas.\r
\r
Vale registrar que a Defesa trouxe uma testemunha, a Srª. Edilaine, que declarou que o acusado Paulo Sérgio é trabalhador e que quando passou no local ele estava abordado com outros elementos pelos policiais. Afirmou, ainda, que viu os rádios e a arma de fogo apreendida.\r
\r
Observa-se no depoimento do menor Ezequiel na audiência de apresentação junto à Vara de Infância, que se encontra no apenso, que o mesmo faz referência a um elemento, conhecido como ´Parazinho´ que correu e que era esse elemento que estaria com a arma de fogo. Registre-se que o réu nega que tenha o apelido de ´Parazinho´.\r
\r
Assim, diante da prova colhida entendo haver dúvidas em relação ao acusado Paulo Sérgio, impondo-se sua absolvição.\r
\r
Está presente o elemento subjetivo, pois o acusado Lucas agiu com vontade livre e consciente voltada para o cometimento do ilícito, não existindo causas excludentes de ilicitude ou que isente o réu de pena.\r
\r
Saliente-se que os policiais militares divergiram na indicação de quem estaria com a arma de fogo, eis que o policial militar Elielson apontou o réu Paulo Sérgio e o policial Deivid o menor Ezequiel.\r
\r
No mais, é fato que o grupo estava com uma arma de fogo de uso restrito, havendo, contudo dúvidas se o acusado Paulo Sérgio integrava o grupo.\r
\r
Presente a causa especial de aumento de pena prevista no inciso IV, do art.40 da Lei 11.343/06, eis que o crime de colaboração com informações para o tráfico ilícito era praticado com o uso de arma de fogo, sendo apreendido, juntamente com os rádios, uma arma de fogo, marca BUL, de calibre 9mm, Luger e 12 (doze) munições. Registre-se que, conforme laudo de fls. 132/135 e 148/149verso, a arma apresentou capacidade de efetuar disparos, além de ser de uso restrito.\r
\r
Presente, também, a causa especial de aumento de pena prevista no inciso VI, do art.40 da Lei 11.343/06, eis o acusado Lucas praticou a conduta criminosa com os menores Ezequiel e Wallace.\r
\r
Inaplicável à causa especial de diminuição de pena prevista no parágrafo 4º do art.33 da Lei nº 11.343/06,  eis que o acusado Lucas possui processo junto à 37ª Vara Criminal da Capital, por tráfico ilícito de entorpecentes e associação para o tráfico estando o feito suspenso na forma do art.366 do CPP, não preenchendo, assim, aos requisitos estabelecidos em lei.\r
\r
ISTO POSTO, JULGO PROCEDENTE EM PARTE a pretensão punitiva para:\r
\r
´\tCONDENAR LUCAS SOUZA SILVA como incurso nas penas do art. 37, c/c art. 40, IV e VI, ambos da Lei nº 11.343/06, da Lei nº 11.343/06 e ABSOLVÊ-LO, em relação à conduta prevista no art.16, da Lei nº 10.826/03 e art.244-B da Lei 8069/90, com fulcro no inciso III do art.386 do CPP.\r
´\tABSOLVER PAULO SÉRGIO DE SANTANA MARINS, em relação aos crimes previstos no art. 37, c/c art. 40, IV e VI, ambos da Lei nº 11.343/06, da Lei nº 11.343/06, no art.16, da Lei nº 10.826/03 e no art.244-B da Lei 8069/90, com fulcro, respectivamente, nos incisos VII e III do art.386 do CPP.\r
\r
\r
Passo a dosimetria da pena:\r
\r
Em atendimento às diretrizes traçadas pelo art. 59 do Código Penal, considerando, as circunstâncias e consequências do delito, a personalidade e os antecedentes do réu, fixo-lhe a pena-base no mínimo legal, em 02 (dois) anos de reclusão de reclusão e 300 (trezentos) dias multa, à base de 1/30 (um trinta avos) do salário-mínimo vigente à época do fato, nos termos do art. 43 da Lei nº 11.343/06.\r
\r
Reconheço a circunstância atenuante prevista no inciso I, do art.65 do CP, deixo, contudo, de reduzir a pena eis que já se encontra no mínimo legal.\r
\r
Reconheço as causas especiais de aumento de pena, prevista no art.40, inciso IV e VI, da Lei nº. 11.343/06, eis que juntamente com os rádios foi apreendida uma arma de fogo, marca BUL, de calibre 9mm, Luger e 12 (doze) munições e o acusado Lucas praticou a conduta criminosa com os menores Ezequiel e Wallace, e, por consequência,  exaspero a pena em 2/3 (dois terços), perfazendo um aumento de 01 (um) anos e 04 (quatro) meses de reclusão e 200 (dezentos) dias, no valor já mencionado.\r
\r
Torno a pena definitiva, na ausência de outros moduladores, em 03 (três) anos e 04 (quatro) meses de reclusão e 500 (quinhentos) dias-multa, no valor já mencionado.\r
\r
A pena privativa de liberdade do delito será cumprida no REGIME SEMIABERTO, eis que o acusado praticou crime gravíssimo.\r
\r
Condeno o réu ao pagamento das custas e taxa judiciária.\r
\r
O réu não demonstra periculosidade elevada, sendo a pena restritiva de direitos a que melhor se adéqua ao caso. Assim, CONVERTO a pena privativa de liberdade em duas penas restritivas de direito, que na forma do art. 45 c/c art.46, ambos do Código Penal, e seus parágrafos, serão de prestação de serviço à comunidade, ou a entidades públicas, e limitação de fim de semana. A entidade beneficiária será designada pelo juízo da execução.\r
\r
A pena restritiva de direitos, em sua modalidade prestação de serviço, será cumprida pelo prazo da pena privativa de liberdade com carga horária de 07 (sete) horas semanais.\r
\r
Considerando a aplicação da pena restritiva de direitos e a absolvição do acusado Paulo Sérgio, expeçam-se os competentes alvarás de soltura.\r
\r
Determino a destruição dos rádios transmissores, da arma, carregador e munições apreendidas. Oficie-se.\r
\r
Desentranhem-se os documentos de fls.75/84, eis que não pertencem a este feito. O cartório deverá diligenciar visando juntá-los no processo correto.\r
\r
Oficie-se a 37ª Vara Criminal informando o resultado do presente e o endereço fornecido pelo acusado Lucas.\r
\r
Após o trânsito em julgado, proceda-se às anotações e comunicações necessárias, envie-se ao contador para cálculo, expeça-se carta de sentença e arquivem-se.\r
\r
Publique-se. Registre-se. Intime-se, devendo os réus serem intimados quando do cumprimento dos alvarás de soltura e informar seus endereços.''',
            'resumo': '''...ISTO POSTO, JULGO PROCEDENTE EM PARTE a pretensão punitiva para:\r
"\tCONDENAR LUCAS SOUZA SILVA como incurso nas penas do art. 37, c/c art. 40, IV e VI, ambos da Lei nº 11.343/06, da Lei nº 11.343/06 e ABSOLVÊ-LO, em r...''',
            'tipo': 'sentença',
            'titulo': 'Sentença - Julgado improcedente o pedido'
        },
        {
            'data': GenericRepr('datetime.date(2015, 6, 17)'),
            'integra': '''Em cumprimento ao ATO EXECUTIVO CONJUNTO TJ/CNJ N.º 03/2015, o qual instituiu o mutirão carcerário, procedo a revisão da prisão preventiva do denunciado.\r
\r
Compulsando os autos verifico que permanecem íntegros os requisitos autorizadores da segregação cautelar. A custódia deve ser mantida considerando-se a gravidade concreta do crime, evidenciada pelo modus operandi da ação delituosa e na violência empregada no delito.\r
\r
Cumpre ressaltar que o feito segue seu regular trâmite, não havendo que se falar em excesso de prazo para encerramento da instrução criminal. Com efeito, não se pode fazer uma simples soma matemática para aferir o prazo, sem levar em conta as peculiaridades do caso concreto e a complexidade do processo.\r
\r
Portanto, conclui-se que a prisão preventiva é a única medida eficiente para se atingir o fim colimado na hipótese vertente de preservação da ordem pública, garantia da aplicação da lei penal e conveniência da instrução criminal.\r
\r
Ante o exposto, MANTENHO o decreto prisional. Dê-se ciência.''',
            'resumo': 'Portanto, conclui-se que a prisão preventiva é a única medida eficiente para se atingir o fim colimado na hipótese vertente de preservação da ordem pública, garantia da aplicação da lei penal e conveniência da instrução ...',
            'tipo': 'decisão',
            'titulo': 'Decisão - Decisão ou Despacho Não-Concessão'
        },
        {
            'data': GenericRepr('datetime.date(2015, 5, 21)'),
            'integra': '''TRIBUNAL DE JUSTIÇA DO ESTADO DO RIO DE JANEIRO\r
COMARCA DA CAPITAL\r
JUÍZO DE DIREITO DA 5ª VARA CRIMINAL\r
\r
Réu preso\r
\r
Processo: 0004879-23.2015.8.19.0001 - Distribuído em: 08/01/2015\r
Art. 16 da Lei 10.826/03 e art. 37 da Lei 11.343/2006\r
Réu: LUCAS SOUZA SILVA\r
Réu: PAULO SERGIO DE SANTANA MARINS\r
Advogado: DEFENSOR PÚBLICO (TJ000002)\r
Audiência: Instrução e Julgamento\r
Data da Audiência: 21/05/2015\r
\r
ASSENTADA\r
\r
Aos 21 (vinte e um) dias do mês de maio de 2015, à hora designada, na sala de audiências deste Juízo, perante o MM. Juiz de Direito, Dra. ANA HELENA MOTA LIMA VALLE, abriu-se a audiência designada nestes autos. Presentes a ilustre representante do Ministério Público, Dra. DENISE DE MATTOS MARTINEZ GERACI, os réus, devidamente assistidos pela ilustre Defensora Pública, Dra. FERNANDA CRISTINA DE MORAES CAMPOS, bem como as testemunhas arroladas pelas partes. A seguir, foram ouvidas as testemunhas presentes e interrogados os réus, conforme termos e registros audiovisuais acostados aos autos. Pela Defesa, foi requerida a juntada de declarações de caráter do réu Paulo Sérgio, o que foi deferido. Pelo MM Juiz de Direito, foi proferido o seguinte despacho: ´Declaro encerrada a instrução criminal e determino a abertura de vista às partes para apresentação de alegações finais por memoriais; após, conclusos para sentença.´ Cientes e intimados os presentes. Nada mais havendo, foi determinado o encerramento da presente que, após lido e achado conforme, vai devidamente assinado. Eu, Secretário de Juiz, ____digitei e subscrevo.\r
\r
\r
ANA HELENA MOTA LIMA VALLE\r
JUIZ DE DIREITO\r
\r
DENISE DE MATTOS MARTINEZ GERACI\r
PROMOTORA DE JUSTIÇA\r
\r
FERNANDA CRISTINA DE MORAES CAMPOS\r
DEFENSORA PÚBLICA\r
\r
PRIMEIRO ACUSADO\r
\r
SEGUNDO ACUSADO''',
            'resumo': 'Pelo MM Juiz de Direito, foi proferido o seguinte despacho: "Declaro encerrada a instrução criminal e determino a abertura de vista às partes para apresentação de alegações finais por memoriais; após, conclusos para sent...',
            'tipo': 'despacho',
            'titulo': 'Despacho em Audiência  - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2015, 5, 4)'),
            'integra': '''1)\tTrata-se de ação penal pública movida em face de Lucas Souza Silva e Paulo Sérgio de Santana Marins, como incurso nas penas do art. 37 da Lei 11.343/06, art. 16 da lei 10.826/03 e art. 244-B da Lei 8.069/90, n/f do art. 69 do CP.\r
Os acusados, devidamente citados, apresentaram resposta à acusação às fls. 109/116, onde arguiram preliminar de cerceamento de defesa, sustentando que a não requisição do preso para entrevista no prédio do Fórum Central, em observância à Resolução nº 45/2013, ´... acarreta flagrante CERCEAMENTO DE DEFESA, já que aborta a possibilidade de o Réu colaborar com seu defensor para apresentar resposta escrita ou oral, sacrificando toda a defesa...´.\r
É cediço que ´nulidade´ trata-se de vício insanável que macula a marcha processual quando há inobservância de norma legal, podendo levar a inutilidade e consequente repetição do ato maculado. Também é notório que a ´nulidade´ será declarada caso a prática do ato cause prejuízo à parte, consoante regra do art. 563 do CPP.\r
Todavia, em que pesem os brilhantes argumentos da Defesa, não há prova da ocorrência de qualquer prejuízo à parte, cabendo ressaltar que o contato com o réu pode se dar na unidade prisional onde o mesmo encontra-se acautelado, cabendo salientar que, no presente caso, houve apresentação de resposta preliminar, inclusive com rol de testemunhas. Destarte, não há, in casu, qualquer violação aos princípios do contraditório e da ampla defesa. Neste sentido, entendimento deste e. TJERJ, conforme acórdão do Órgão Especial que deu solução ao Incidente de inconstitucionalidade nº 0026804-15.2014.8.19.0000: ´INCIDENTE DE INCONSTITUCIONALIDADE. RESOLUÇÃO TJ/OE Nº. 45/2013, QUE VEDA REQUISIÇÕES, PELO JUIZ, DE RÉU PRESO PARA ENTREVISTA COM O DEFENSOR PÚBLICO ANTES DO OFERECIMENTO DA RESPOSTA INICIAL À ACUSAÇÃO. RELEVÂNCIA DA ENTREVISTA PESSOAL. ATRIBUIÇÃO DA DEFENSORIA PÚBLICA QUE NÃO PODE SER TRANSFERIDA A OUTRAS INSTITUIÇÕES. RACIONALIZAÇÃO DO TRABALHO QUE SE IMPÕE, SEM QUE SE DESCONSIDEREM O DIREITO DO RÉU PRESO À AMPLA DEFESA E OS PRINCÍPIOS DA ECONOMIA E CELERIDADE PROCESSUAIS. ART. 22, § 4º DA LEI COMPLEMENTAR ESTADUAL Nº 6/1977. UNIDADE E INDIVISIBILIDADE DA DEFENSORIA PÚBLICA. VEDAÇÃO DA REQUISIÇÃO DO RÉU PRESO PARA ENTREVISTA PESSOAL COM O DEFENSOR PÚBLICO QUE NÃO IMPLICA CERCEAMENTO DE DEFESA. PRINCÍPIOS DA AMPLA DEFESA E DOCONTRADITÓRIO QUE SE MANTÊM ÍNTEGROS. INCIDENTE QUE SE REJEITA.´\r
Além do mais, a marcha processual - que acaba de iniciar-se - respeita o ´due process of law´ e, antes dos interrogatórios, em estrito cumprimento do disposto no art. 185, § 5º, do CPP, os acusados terão oportunidade de entrevistarem-se reservada, particular e livremente com a Dra. Defensora Pública.\r
À conta do exposto, rejeito a preliminar de cerceamento de defesa.\r
2)\tTendo em vista que o caso concreto não se subsume a nenhuma das causas de absolvição sumária, mantenho o recebimento da denúncia.\r
3)\tDesigno AIJ para o dia 21/05/2015 às 13h45min. Intimem-se e/ou requisitem-se todos.\r
4)\tExpeça(m)-se mandado(s) de busca e apreensão de eventual laudo não encaminhado e/ou ofício não respondido.\r
5)\tEsclareçam-se as FAC's.\r
6)\tDê-se ciência ao MP e à DP.\r
7)         Desentranhem-se fls. 75/84, juntando-as nos autos do processo correspondente.''',
            'resumo': '''À conta do exposto, rejeito a preliminar de cerceamento de defesa.\r
2)\tTendo em vista que o caso concreto não se subsume a nenhuma das causas de absolvição sumária, mantenho o recebimento da denúncia.\r
3)\tDesigno AIJ par...''',
            'tipo': 'decisão',
            'titulo': 'Decisão - Decisão Determinação'
        },
        {
            'data': GenericRepr('datetime.date(2015, 3, 17)'),
            'integra': '''Trata-se de ação penal pública promovida em face de LUCAS SOUZA SILVA e PAULO SERGIO DE SANTANA MARINS por infração ao art. 37, da Lei nº 11.343/06, art. 16 da Lei nº 10.826/03 e art. 244-B do ECA.\r
\r
RECEBO A DENÚNCIA.\r
\r
Citem-se os acusados para, em 10 (dez) dias, oferecerem defesa escrita (art. 396, CPP), por Advogado que venham a constituir, ficando cientes de que o não oferecimento da defesa no prazo implicará na nomeação da Defensoria Pública para o patrocínio de seus interesses.\r
\r
Defiro a cota do MP de fl. 67.\r
\r
Comunique-se a prisão de Lucas ao Juízo da 37ª VCRI.\r
\r
Providencie o cartório as anotações pertinentes.''',
            'resumo': '''Trata-se de ação penal pública promovida em face de LUCAS SOUZA SILVA e PAULO SERGIO DE SANTANA MARINS por infração ao art. 37, da Lei nº 11.343/06, art. 16 da Lei nº 10.826/03 e art. 244-B do ECA.\r
\r
RECEBO A DENÚNCIA....''',
            'tipo': 'decisão',
            'titulo': 'Decisão - Recebida a denúncia'
        },
        {
            'data': GenericRepr('datetime.date(2015, 2, 10)'),
            'integra': '''Constato que o flagrante encontra-se formal e materialmente regular, não havendo razão para se cogitar de relaxamento da prisão do indiciado.\r
\r
Por outro lado, há suficientes indícios de autoria e prova da existência do crime, como se depreende das declarações acostadas aos autos; o indiciado LUCAS ostenta outra anotação por crime semelhante, conforme consta de sua FAC; não há nos autos, até o momento, comprovação acerca do domicílio dos indiciados e do exercício de atividade laborativa lícita pelos mesmos. Assim sendo, revela-se imprescindível a custódia cautelar dos indiciados para garantir a aplicação da lei penal e assegurar a instrução criminal.\r
\r
Finalmente, registro que, pelos mesmos motivos acima elencados, entendo insuficientes e inadequadas à hipótese em foco a imposição das medidas cautelares previstas nos arts. 319 e 320 do CPP.\r
\r
Desse modo, independente da prévia manifestação do MP, tendo em vista que a remessa dos autos ao Órgão Ministerial implicará inevitavelmente em excesso de prazo da prisão, converto a prisão flagrancial de LUCAS SOUZA SILVA e PAULO SÉRGIO DE SANTANA MARINS  em prisão preventiva, na forma do art. 310, II, do CPP.\r
\r
EXPEÇAM-SE MANDADOS DE PRISÃO.\r
\r
Em cumprimento à Resolução CNJ nº 137/2011, determino que conste do mandado de prisão a ser expedido a data presumida para o seu cumprimento, de acordo com a prescrição em abstrato, ou seja, a data de 06/01/2027.\r
\r
Procedam-se às anotações e comunicações pertinentes.\r
\r
Cobre-se a vinda dos autos principais, COM URGÊNCIA, após, abra-se vista ao MP.''',
            'resumo': '''Constato que o flagrante encontra-se formal e materialmente regular, não havendo razão para se cogitar de relaxamento da prisão do indiciado.\r
\r
Por outro lado, há suficientes indícios de autoria e prova da existência do...''',
            'tipo': 'decisão',
            'titulo': 'Decisão - Decretada a prisão preventiva de parte'
        }
    ],
    'numero': '0004879-23.2015.8.19.0001',
    'reus': [
        {
            'cpf': None,
            'nome': 'LUCAS SOUZA SILVA'
        },
        {
            'cpf': None,
            'nome': 'PAULO SERGIO DE SANTANA MARINS'
        }
    ],
    'vara': '5ª Vara Criminal'
}

snapshots['test_parse_process_page4 1'] = {
    'advogados': [
        {
            'nome': 'FLAVIO JORGE DA GRAÇA MARTINS',
            'oab': 'RJ032442'
        },
        {
            'nome': 'MICHELLE FELIX BARCELLOS DE ALVARENGA',
            'oab': 'RJ177721'
        },
        {
            'nome': 'MARCO ANTONIO AUGUSTO DOS SANTOS',
            'oab': 'RJ127014'
        }
    ],
    'assunto': 'Tráfico de Drogas e Condutas Afins (Art. 33 - Lei 11.343/06) E Associação para a Produção e Tráfico e Condutas Afins (Art. 35 - Lei 11.343/06)',
    'autor': 'MINISTERIO PUBLICO DO RIO DE JANEIRO',
    'classe': 'Procedimento Especial da Lei Antitóxicos - Criminal (Lei 11.343/06)',
    'comarca': 'Comarca de Itaboraí',
    'movimentacoes': [
        {
            'data': GenericRepr('datetime.date(2018, 10, 22)'),
            'integra': '''Nesta data prestei as informações que seguem.\r
\r
\tIntime-se o réu para que regularize a sua representação processual, no prazo legal, caso não haja manifestação dentro do referido prazo, fica desde já nomeado o Defensor Público para atuar em favor do mesmo.''',
            'resumo': '''Nesta data prestei as informações que seguem.\r
\r
\tIntime-se o réu para que regularize a sua representação processual, no prazo legal, caso não haja manifestação dentro do referido prazo, fica desde já nomeado o Defensor ...''',
            'tipo': 'despacho',
            'titulo': 'Despacho - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2018, 8, 14)'),
            'integra': '''LUIZ FERNANDO DA COSTA ARAÚJO ROSA, foi denunciado como incurso nas penas dos arts. 33, caput, e art. 35 da Lei 11343/2006, consoante os termos da denúncia de fls. 2-A/2-D.\r
\r
Registro de Ocorrência Aditado, fls. 03.\r
\r
Auto de Prisão em Flagrante, fls. 04.\r
\r
Laudo de Exame de Definitivo de Material Entorpecente, fls. 07/08.\r
\r
Auto de Apreensão, fls. 09.\r
\r
Decisão da Central de Custódia de fls. 35/36, que converteu a prisão em flagrante dos acusados em prisão preventiva.\r
\r
F.A.C do acusado Luan da Silva Menezes, fls. 43/47.\r
\r
Determinada a notificação dos acusados, fls. 55.\r
\r
Laudo de Exame de Definitivo de Material Entorpecente, fls. 63/64.\r
\r
Defesa Prévia de Luan da Silva Menezes, fls. 70/71.\r
\r
Defesa  Prévia de Luiz Fernando Rosa, fls. 78/81.\r
\r
C.A.C do acusado Luan, fls. 82/83.\r
\r
C.A.C do acusado Luiz Fernando da Costa Araujo Rosa, fls. 84.\r
\r
Decisão de recebimento da denúncia, fls. 85.\r
\r
Pedido de Revogação da Prisão Preventiva em favor do acusado Luiz Fernando, fls. 91/97.\r
\r
Decisão de fls. 112, indeferiu o pleito libertário.\r
\r
F.A.C do acusado Luiz Fernando, fls. 117/119.\r
\r
F.A.C do acusado Luan Menezes, fls. 120/123.\r
\r
Audiência de instrução e julgamento, conforme assentada de fls. 128, oportunidade em que foram ouvidas as testemunhasEvelin da Conceição Pinto, Cleber Correa da Conceição, Nathalia Soares Sodré, Jefferson Ferreira de Oliveira e Rodolfo Barreto Peixoto. Pela defesa do acusado Luiz Fernando foi requerida a revogação da prisão. Pelo MP foi dito que se opõe ao pleito de revogação. Foi proferido despacho que determinou o desmembramento do feito em relação ao acusado Luan da Silva e designou novo ato.\r
\r
Laudo de Exame de Definitivo de material Entorpecente, fls. 140/142.\r
\r
Laudo de Exame de descrição de material, fls. 143/146.\r
\r
Audiência de instrução e julgamento, conforme assentada de fls. 151, oportunidade em que foi realizado o interrogatório do acusado. Foi proferido despacho determinando a manifestação das partes em alegações finais.\r
\r
Alegações Finais do Ministério Público, às fls. 158/161, pela condenação do acusado, nos termos da denúncia.\r
\r
Alegações Finais da Defesa, às fls. 169/175, pela absolvição do acusados, nos termos do art. 386, V do CPP.\r
\r
Vieram os autos conclusos para sentença.\r
\r
É o relatório. Decido.\r
\r
Trata-se de ação penal proposta em face deLUIZ FERNANDO DA COSTA ARAÚJO ROSA pela prática dos delitos previstos nosarts. 33, caput, e 35 da Lei 11343/06.\r
\r
Compulsando os autos, verifica-se que há razões suficientes a impor a condenação que agora se realiza.\r
\r
Como são imputados ao acusado delitos diversos, os crimes devem ser analisados em separado.\r
\r
01- Do delito previsto no artigo 33, caput da Lei 11.343/06:\r
\r
A materialidade do delito está evidenciada pelo Registro de Ocorrência que instrui o feito, pelo Auto de Prisão em Flagrante de fls. 04, pelo Auto de apreensão  (fls. 09) pelo laudo  definitivo de substância entorpecente de fls. 07/08.\r
\r
Passo a analisar a autoria do delito em tela.\r
\r
Ouvido em Juízo, o policial militar Rodolfo Barreto Peixoto\r
\r
que receberam a informação de que os acusados estavam fazendo parte da venda de entorpecentes, que nesta informação não citava o nome dos dois, mas citava as características de um deles e a residência; que informaram que eles estavam na prática de venda de entorpecentes na Praça do Apollo; que foram até o local e nada foi encontrado, porém foram na casa do acusado, ele atendeu e o reconheceram pelas características(...); que chegaram no local, (...) conversaram com o acusado; que ele confessou e foi na parte debaixo da casa, onde foi apreendida uma sacola, que tinha maconha; que a cocaína foi encontrada em outra residência apontada pelo acusado; que foram até a outra residência, onde foram atendidos pelo outro acusado; que nessa segunda residência foi encontrada a cocaína, que estava dentro de uma mochila em cima do armário; que o acusado apontou, não precisou revistar; que os acusados eram conhecidos; (...) que ele não apontou mais nenhum integrante; que as características que foram passadas para os policiais eram do acusado Luan; que depois que prenderam o Luan se dirigiram diretamente para a outra residência.\r
\r
No mesmo sentido foram as declarações de seu colega de farda, Jefferson Ferreira de Oliveira:\r
\r
Que estavam de serviço regular, na parte da manhã, patrulhando no Bairro do Apollo, que tiveram a informação com as características de um indivíduo que estaria fazendo a venda de entorpecente (...); que a pessoa que passou a informação, falou que se o acusado não estivesse na praça, estaria em casa com as drogas, apontou o endereço do acusado Luan; que foram até a quadra e não o encontraram e foram para o endereço; que ao chegar no local, a esposa atendeu e disse que ele não estava, porém, logo em seguida, ele apareceu na sala para ver quem era; que ele se exaltou um pouco; que adentraram a residência e conversaram com o acusado; que ele confessou onde estaria a droga, no sótão, embaixo da casa; que encontraram a droga; que eram uns tabletes de maconha, que não se recorda a quantidade; que ele admitiu que a droga seria para a venda, mas que ele não era o gerente; que perguntaram ao acusado, onde ele arrecadava as drogas e ele apontou o Luiz Fernando e passou o endereço do mesmo, para que fossem até o local e lá foi encontrado, no quarto dele uma mochila com droga; que a região tem bastante ocorrência de tráfico; que não conhecia os acusados; que inicialmente só receberam as características do Luan; que não viu a hora em que seu colega pegou as drogas.\r
\r
\r
Frise-se que os depoimentos dos autores do flagrante, são harmônicos, seguros e coerentes entre si, merecendo destacar que tais depoimentos são dotados de presunção de idoneidade.\r
\r
A testemunha de defesa Cleber Correa da Conceição narrou que:\r
\r
Conhece o acusado somente de vista; que viu quando os policiais entraram na casa do Luiz Fernando e quando saíram; que os policiais antes de entrarem na casa do acusado, foram em uma outra casa; que a rua, onde mora o acusado é um ponto de venda de drogas; que na hora que os policiais entraram na rua, uns meninos do tráfico correram e se espalharam; (...) que dois deles entraram na avenida onde o acusado mora; que viu que um deles estava com uma mochila; que é normal, o pessoal invadir as casas, pois quando chega a polícia, eles correm, pulam o muro dos outros, invadem as casas, para poderem se livrar; que não viu nenhum desses meninos entrarem na casa do Luiz Fernando; que não sabe afirmar que o acusado seja envolvido com o tráfico.\r
\r
A testemunha de defesa Nathalia Soares Sodré afirmou que:\r
\r
Que estava em frente do portão e no dia dos fatos, estava tendo muito barulho de meninos passando na rua, em razão de time de futebol; que em seguida, viu um carro de polícia na esquina da quadra e revistaram os meninos; que na quadra tem um foco de drogas; que no dia dos fatos, logo cedo, já estava tendo um movimento de meninos vendendo drogas; que os meninos, quando viram que os policiais estavam indo em direção dos mesmos, correram, entraram no primeiro portão que estava aberto, onde tem uma vila cheia de casa; que o policial parou o carro no local e dois policiais entraram procurando; que Luiz Fernando não é um dos meninos que correu; que um dos meninos que entrou na avenida estava com uma mochila preta; que na vila tem como os meninos se evadirem, pois ela dá acesso a Rua Onze e a Rua Oito; que no local é comum, eles saírem entrando nos locais, que eles encontrem facilidade, portão aberto ou porta aberta; que um dos meninos entrou na casa do acusado Luiz Fernando.\r
\r
A testemunha de defesa Evelin da Conceição Pinto, companheira do acusado, narrou que:\r
\r
(...) que o acusado estava na cozinha, quando entrou um menino correndo e foi para o quarto da depoente com uma mochila na mão e jogou em cima do guarda-roupa; que era uma mochila preta; que o menino fez ameaça e estava com uma arma prata na mão e disse que iria volta para pegar a mochila (...).\r
\r
Em sede de audiência de continuação, foi interrogado o réu, o qual afirmou que:\r
\r
´Os fatos contidos na denúncia não são verdadeiros; que não conhece o Luan e que as drogas não lhe pertenciam; que nunca foi preso antes e não faz uso de drogas; (...) que estava em casa e ouviu uns passos, quando olhou pela janela, viu um ´pretinho´ correndo com uma mochila na mão; (...) que viu o ´pretinho´ saindo de dentro de sua casa, com uma arma prata na mão; que foi até o quarto e a companheira falou que ele (o pretinho) jogou a mochila em cima do armário; que não conhecia ele; que o local, onde mora tem tráfico e a facção dominante é o Comando Vermelho´.\r
\r
No entanto, tal versão restou no mínimo não convincente no canteiro probatório, tendo em vista o teor dos depoimentos dos policiais. Assim, a prova indicativa da venda de entorpecente pelo réu é robusta e inconteste, aplicável à hipótese o verbete nº 70 da Súmula deste Tribunal.\r
\r
A defesa técnica do acusado não produziu qualquer prova, pelo que não há como chegar à conclusão diversa daquela constante da denúncia.\r
\r
Frise-se que, não se está, data vênia do alegado pela defesa, diante de insuficiência de prova a embasar a condenação, uma vez que finda a instrução, a prova indicativa do tráfico ilícito de entorpecentes pelo réu é robusta e inconteste.\r
\r
Conclui-se, pois, que não há dúvidas de que o acusado vendia e mantinha em seu poder substância entorpecente, o que vem a caracterizar o delito previsto no artigo 33, caput, da Lei 11343/2006.\r
\r
2 -  Quanto ao delito previsto no art. 35 da lei de Tóxicos:\r
\r
A materialidade delitiva está comprovada pelo auto de prisão em flagrante (fls. 04) , pelo registro de ocorrência (fls. 03), pelo auto de apreensão (fls. 09) e pelos laudos de exame de entorpecente (fls. 07/08, 63/64 e 140/142).\r
No que tange à autoria, finda a instrução, o conjunto probatório é contundente e não deixa qualquer dúvida quanto à atuação criminosa do réu, no que diz respeito ao cometimento da conduta prevista no dispositivo suso mencionado, valendo ressaltar o depoimento dos policiais militares, os quais são uníssonos e coerentes em afirmar que o acusado Luan foi quem apontou o réu Luiz Fernando, tendo inclusive informado o endereço deste.\r
\r
Consigno que, no caso ´sub judice´, estão presentes elementos empíricos que, conjugados com aqueles colhidos no curso da instrução probatória, demonstram a indisfarçável prática do delito de associação ao tráfico.\r
Ademais, verifica-se que a prisão se deu em área, conhecida como ponto de venda de drogas, sendo encontrada com o mesmo quantidade expressiva de substância entorpecente, contendo a inscrição referente à facção criminosa do Comando Vermelho, desta feita, diante de todos os elementos constantes nos autos, resta patente a estabilidade própria de uma associação para a prática do crime de tráfico, não se tratando o denunciado de traficante autônomo ou independente. Ressalto, que tal condição de estabilidade não foi afastada por nenhum elemento de prova existente no presente feito.\r
\r
Portanto, conclui-se, pois, que não há dúvidas de que o denunciado estava associado para a prática do tráfico de entorpecentes, na modalidade prevista no artigo 35 da Lei 11.343/06.\r
\r
Neste Sentido:\r
\r
´0040641-97.2015.8.19.0002  - APELAÇÃO\r
\r
1ª Ementa\r
Des(a). KÁTIA MARIA AMARAL JANGUTTA - Julgamento: 12/06/2018 - SEGUNDA CÂMARA CRIMINAL\r
\r
\r
APELAÇÃO. Artigos 33 e 35, ambos da Lei 11.343/06, em concurso material. Condenação. Agente que, no dia 24/08/2015, por volta das 8 horas, na Rua Seis, no interior da Comunidade Nova Brasília, em Engenhoca, Niterói, de forma livre e consciente, e, em associação estável com outros indivíduos não identificados, integrantes do tráfico de drogas local, guardava, para fins de tráfico, sem autorização e em desacordo com determinação legal ou regulamentar, 125,8 gramas de cloridrato de cocaína, distribuídos em 242 tubos plásticos, além de 01 rádio comunicador e 1 telefone celular. RECURSO DO MINISTÉRIO PÚBLICO. Exclusão da causa de diminuição de pena, prevista no §4º, do artigo 33, da Lei 11.343/06. RECURSO DEFENSIVO. Absolvição por ambos os delitos, por fragilidade probatória. Aplicação das penas-base em seu mínimo legal. Aplicação da causa de diminuição do artigo 33, §4º, da Lei Antidrogas em seu patamar máximo. Substituição da pena privativa de liberdade por restritiva de direitos. Concessão de sursis. 1. Induvidosas a materialidade e a autoria do crime de tráfico ilícito de drogas, devidamente comprovadas pelas peças técnicas acostadas aos autos, bem como pela segura prova testemunhal colhida no decorrer do processo, especialmente, nos depoimentos firmes e seguros de policiais responsáveis pela prisão, sobre os quais não se evidenciou qualquer motivo para quererem, propositadamente, prejudicar o réu, incidindo, na hipótese, o disposto na Súmula 70, desse Tribunal. O acusado, durante o interrogatório judicial, apresentou versão contrária à oferecida em sede policial, negando os fatos, com o objetivo de se furtar da responsabilidade penal. A afirmação de que, as drogas que estavam no fundo de sua casa, no mesmo terreno de sua residência, não lhe pertenciam, não tem substrato de verossimilhança. Ademais, ele próprio admitiu que não conhecia os agentes da lei que o prenderam. Frise-se que, foram encontrados na residência em que estava o acusado 125,8 g de cloridrato de cocaína, distribuída em 242 pequenos tubos, isto é, prontos para venda. 2. Para a configuração do crime previsto no artigo 35, da Lei 11.343/06, é imprescindível a verificação do elemento subjetivo do tipo, qual seja o animus associativo, consubstanciado na convergência de vontade do agente em se unir de forma reiterada ou não, com a finalidade de exercer o comércio ilícito de drogas. No caso, as circunstâncias fáticas delineadas revelam com clareza, o animus associativo, existente entre o acusado e os elementos não identificados. Ambos os agentes da lei foram uníssonos em afirmar que, o acusado estava unido a outros indivíduos, quando empreendeu fuga, logrando ser capturado, tendo a prisão ocorrido em comunidade dominada pela organização criminosa Comando Vermelho, não sendo crível que alguém que não pertença a esta facção, possa estar guardando tamanha quantidade de drogas embaladas para a venda na residência em que se encontrava, além do fato de ter sido apreendido rádio transmissor. 3. Incabível a concessão da benesse prevista no §4º, do artigo 33, da Lei 11.343/06, pois o apelante não preenche os requisitos legais e necessários à sua obtenção, posto que a condenação por atividade ilícita de tráfico de drogas, somada à associação para tanto, é incompatível com o presente redutor. 4. Penas-base fixadas no mínimo legal, em concurso material, totalizando valores que tornam inviável a substituição da pena privativa de liberdade por restritiva de direitos, bem como a concessão de sursis, a teor do disposto nos artigos 44, I, e 77, do Código Penal. RECURSO MINISTERIAL PROVIDO. RECURSO DEFENSIVO DESPROVIDO. ´\r
\r
Pelo exposto, JULGO PROCEDENTES os pedidos contidos na denúncia, para condenar o acusado LUIZ FERNANDO DA COSTA ARAÚJO ROSA como incurso nas penas dos artigos 33, caput e 35 da Lei 11.343/06, na forma do art. 69 do Código Penal.\r
\r
Passo a dosar a pena, consoante as diretrizes da Lei Penal.\r
\r
1)-Crime previsto no art. 33, caput da Lei 11.343:\r
\r
Na primeira etapa, doso a pena base em 5 (cinco) anos de reclusão e 500 (quinhentos) dias-multa, tendo em vista não se configurar nenhuma circunstância judicial em desfavor do acusado, nos moldes do art.59 do CP.\r
\r
Na segunda fase da aplicação da pena, não se visualiza nenhuma agravante ou atenuante aplicável ao caso em análise. Assim, a pena intermediária permanece no mesmo patamar acima fixado.\r
\r
Na terceira fase de aplicação da pena, deve-se frisar a impossibilidade de aplicação da causa de diminuição de pena constante no art. 33, § 4º da Lei 11343/2006, uma vez que foi encontrada com o acusado quantidade expressiva de material entorpecente, de qualidade variada, contendo inscrição da facção criminosa ´Comando Vermelho´, o que afasta a caracterização do acusado como traficante episódico. Na esteira desse entendimento:\r
\r
´0025781-91.2015.8.19.0002 -APELACAO - 1ª Ementa - DES. ELIZABETE ALVES DE AGUIAR - Julgamento: 17/02/2016 - OITAVA CAMARA CRIMINAL\r
APELAÇÃO. TRÁFICO ILÍCITO DE ENTORPECENTES. RECURSO DEFENSIVO BUSCANDO: 1) A ABSOLVIÇÃO POR ALEGADA INSUFICIÊNCIA DE PROVAS. SUBSIDIARIAMENTE PRETENDE: 2) A APLICAÇÃO DA CAUSA DE DIMINUIÇÃO DO ARTIGO 33, §4º DA LEI ANTIDROGAS; 3) A SUBSTITUIÇÃO DA PENA PRIVATIVA DE LIBERDADE POR RESTRITIVA DE DIREITOS. CONHECIMENTO E DESPROVIMENTO DO RECURSO Autoria e materialidade incontroversas. Quanto ao pleito absolutório, certo é que o conjunto probatório produzido, ao contrário do que alega a Defesa, é firme e seguro no sentido de proclamar o real envolvimento do acusado na empreitada criminosa ora em comento. As circunstâncias da prisão do apelante, somada a grande quantidade e diversidade de drogas encontradas: maconha - 652g (seiscentos e cinquenta e dois gramas), distribuída em 205 (duzentos e cinco) embalagens; cocaína 410g (quatrocentos e dez gramas), distribuído em 375 (trezentos e setenta e cinco) microtubos em plástico rígido incolor e, ainda, uma arma de fogo, leva a concluir que o réu apelante se dedica à atividade criminosa, de mercancia de entorpecentes. Descabimento da substituição da pena privativa de liberdade por restritivas de direitos, porquanto o requisito objetivo temporal não está satisfeito, valendo registrar que, em consonância com a Resolução nº 05/2012 do Senado Federal, embora atualmente possível a substituição da pena privativa de liberdade por restritiva de direitos, tal benesse é direcionada ao réu que tenha a pena fixada abaixo do limite previsto no artigo 44 do Código Penal, o que não é o caso dos autos. CONHECIMENTO E DESPROVIMENTO DO RECURSO.´\r
\r
Assim, resta o acusado LUIZ FERNANDO DA COSTA ARAÚJO ROSA definitivamente condenado a 5 (cinco) anos de reclusão, acrescidos da pecuniária de 500 (quinhentos) dias-multa.\r
\r
Fixo o dia-multa na razão unitária mínima legal.\r
\r
2)-Crime previsto no art. 35 da Lei 11.343:\r
\r
Na primeira etapa, doso a pena base em 3 (três) anos de reclusão e 500 (quinhentos) dias-multa, tendo em vista não se configurar nenhuma circunstância judicial em desfavor do acusado, nos moldes do art.59 do CP.\r
\r
Na segunda fase da aplicação da pena, não se visualiza nenhuma agravante ou atenuante aplicável ao caso em análise. Assim, a pena intermediária permanece no mesmo patamar acima fixado.\r
\r
Na terceira fase, tendo em vista a inocorrência de qualquer causa de aumento ou de diminuição de pena, mantenho a pena acima aplicada, chegando-se, assim, à pena definitiva.\r
\r
Em decorrência do cúmulo material das penas, previsto no art. 69 do CP, a pena total referente à prática de ambos os delitos é de 8 (oito) anos de reclusão  e 1.200 (mil e duzentos) dias-multa, no valor unitário mínimo legal, a ser cumprida em regime fechado, nos moldes fixados no art. 33, § 2º, ´a´ do CP.\r
\r
Deixo de substituir a reprimenda aplicada, nos moldes do disposto no art. 44 do CP, em razão do constante no inciso I.\r
\r
Fixo o dia-multa na razão unitária mínima legal.\r
\r
Por outro lado, tendo em conta a gravidade dos fatos praticados pelo acusado, que ameaçam sobremaneira a ordem pública, a fim de manter-se a paz e a tranquilidade social, nego ao mesmo o direito de recorrer em liberdade.\r
\r
Condeno, ainda, o apenado ao pagamento da taxa judiciária e das custas processuais, nos termos do art. 804 do CPP.\r
\r
Ao contador para cálculo das custas processuais.\r
\r
Expeça-se CES provisória.\r
\r
Após o trânsito em julgado, expeça-se mandado de prisão decorrente de sentença condenatória e adite-se a CES provisória. Recolha-se ainda o mandado de prisão preventiva.\r
\r
Tudo feito, arquive-se.\r
\r
Determino ao Coordenador da Secretaria de Administração Penitenciária que providencie a transferência do condenado para estabelecimento prisional compatível com o regime fixado na sentença.\r
\r
Com o trânsito em julgado, procedam-se aos atos visando à destruição da droga apreendida, com fulcro no artigo 72 da Lei n° 11.343/2006, devendo ser providenciadas as anotações e comunicações pertinentes.\r
\r
P.I.''',
            'resumo': '"...Pelo exposto, JULGO PROCEDENTES os pedidos contidos na denúncia, para condenar o acusado LUIZ FERNANDO DA COSTA ARAÚJO ROSA como incurso nas penas dos artigos 33, caput e 35 da Lei 11.343/06, na forma do art. 69 do C...',
            'tipo': 'sentença',
            'titulo': 'Sentença - Julgado procedente o pedido'
        },
        {
            'data': GenericRepr('datetime.date(2018, 6, 26)'),
            'integra': 'Feito o pregão de estilo, foi apresentado o acusado(a), estando acompanhado pela Defensoria Pública. ABERTA A AUDIÊNCIA, lida a denúncia, foi realizado o interrogatório do acusado. Pela MMa. Juíza foi proferido o seguinte DESPACHO: Digam as partes em alegações finais.',
            'resumo': 'Pela MMa. Juíza foi proferido o seguinte DESPACHO: Digam as partes em alegações finais.',
            'tipo': 'despacho',
            'titulo': 'Despacho em Audiência  - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2018, 6, 12)'),
            'integra': '''Feito o pregão de estilo, ABERTA A AUDIÊNCIA, não foi apresentado o acusado, Presente seu advogado.\r
                    Pela defesa foi requerido: Reitera o pedido de revogação de prisão que estava para ser apreciado, conforme pendente última assentada e/ou relaxamento de prisão, tendo em vista a segunda audiência consecutiva sem apresentação do acusado, estando pendente somente o interrogatório.\r
 Pelo MP, em relação ao pedido de relaxamento de prisão, foi dito que o fato ocorreu em 14/01/2018. A autoridade policial dispõe de 30 dias para conclusão do inquérito. O MP dispõe de 10 dias para oferecimento de denúncia. Observa-se que o inquérito foi concluído e a denúncia foi oferecida em 23/01/2018, portanto em apenas 9 dias. A Defesa Prévia somente foi ofertada em 23/02/2018. A primeira audiência de instrução e julgamento foi designada para 08/05/2018, portanto, dentro do prazo previsto no artigo 400 do Código Penal. Recentemente, a SEAP alterou a apresentação de presos em todo o estado, o que começou a ser implementado neste mês de junho, e, evidentemente, que o processo se encontra em fase de ¿calibragem¿. Mesmo com toda a crise pelo qual o Estado do Ri ode Janeiro vem passando, no presente feito só falta o interrogatório do acusado. Em razão do exposto, não há que se falar em recesso de prazo, sobretudo porque tal construção é de natureza doutrinária e não pode avaliada de forma genérica, e sim analisados os elementos do caso concreto. Em diligências, o MP requer o laudo de descrição de bens apreendidos, conforme item 2-B de fls. 54.\r
Pela MMa. Juíza foi proferido a seguinte DECISÃO:\r
1 - Acolho as razões expostas pelo Ministério Público, ressaltando, outrossim, que o interrogatório do acusado não tardará visto que ora designado para o dia 26/06/2018 às 13:00h. Assim sendo, não há que se falar em excesso de prazo.\r
2 - Atenda-se ao MP no que tange a diligencia ora requerida.\r
3 ¿ Designo novo ato para o dia 26/06/2018 às 13:00h. Requisite-se apenas o acusado.''',
            'resumo': '''Pela MMa. Juíza foi proferido a seguinte DECISÃO:\r
1 - Acolho as razões expostas pelo Ministério Público, ressaltando, outrossim, que o interrogatório do acusado não tardará visto que ora designado para o dia 26/06/2018...''',
            'tipo': 'decisão',
            'titulo': 'Decisão em Audiência  - Decisão ou Despacho Não-Concessão'
        },
        {
            'data': GenericRepr('datetime.date(2018, 5, 8)'),
            'integra': '''Feito o pregão de estilo, não foram apresentados os acusados. ABERTA A AUDIÊNCIA, presentes os patronos de LUIZ FERNANDO E LUAN. A defesa de LUAN não concordou com a oitiva das testemunhas sem sua presença, ao revés da defesa de LUIZ FERNANDO, que não se opôs. lida a denúncia, foi procedida a oitiva das testemunhas EVELIN DA CONCEIÇÃO PINTO, CLEBER CORREA DA CONCEIÇÃO, NATHALIA SOARES SODRÉ, JEFFERSON FERREIRA DE OLIVEIRA E RODOLFO BARRETO PEIXOTO. Pela defesa do acusado LUIZ FERNANDO foi dito: ¿Requer a revogação da prisão, tendo em vista a contradição dos policiais, como por exemplo, um falou que demorou cinco minutos de deslocamento e o outro vinte minutos, um falou que não fez parada em local nenhum e o outro falou que houve duas paradas anteriores. E por outro lado, a defesa do acusado foi firme em dizer que viu o elemento que se evadiu do tráfico entrando na casa do acusado LUIZ FERNANDO com uma mochila. Também ficou comprovado que há meios de fuga na avenida que dá acesso para outra rua, fatos esses que também houve contradição dos policiais. Ademais, não há ainda a certeza ou prova robusta quanto a associação ao tráfico. Decaindo esta tipicidade restará somente o tráfico, onde com os demais elementos subjetivos do acusado poderá responder em liberdade.¿ Pelo MP foi dito que ¿Sem querer aprofundar na análise probatória, vez que não se trata ainda de alegações finais, passa o MP apenas a pontuar as argumentações expostas no pleito defensivo. Com relação à variação de tempo, trata-se de aspecto irrelevante pelo simples motivo de que a percepção de cada um pode variar, sendo razoável que uma determinada pessoa entenda ter havido 5 minutos e outra, tempo superior. Sendo assim, trata-se de aspecto de pouca credibilidade para se aferir o valor de depoimento. Com relação às duas paradas anteriores, se ocorreram ou não, tal análise depende do ponto de vista de quem está avaliando o depoimento, isso porque no entender de determinada testemunha a simples abordagem anterior de uma moradora com o intuito de localizar o endereço fornecido pelo primeiro acusado pode ser tida como irrelevante, ao passo que para outra testemunha pode se tratar de aspecto importante no depoimento. Vale lembrar que uma das testemunhas de defesa confirmou que a guarnição de fato esteve em outra residência, mas sem adentrá-la para fins de revista, apenas abordando a moradora do lado de fora. Com relação à possibilidade meios de fuga, também não se percebe qualquer contradição no depoimento dos policias, pelo simples motivo de que ambas as prisões os denunciados se encontravam na residência e não esboçavam qualquer tentativa de fuga. Por fim, contradição existe no depoimento da informante ora prestado, vez que foi categórica em afirmar que a região é perigosa, onde há constante movimento do tráfico, e ao mesmo tempo afirmou que no dia da prisão havia deixado o portão e a porta de sua residência abertos, o que teria permitido que suposto traficante adentrasse a residência e largar a mochila. Pelo exposto, e refutando todos os argumentos defensivo, opina contrariamente ao pleito de revogação da prisão.\r
Pela MMa. Juíza foi proferido o seguinte DESPACHO:\r
1 - Desmembre-se o feito em relação ao acusado LUAN DA SILVA diante da não concordância de seu patrono.\r
2- Designo novo ato para o dia 12/06/2018 às 13:00h. Requisite-se o acusado.\r
3 ¿ Após a preparação da audiência, venham conclusos para decisão.''',
            'resumo': '''Pela MMa. Juíza foi proferido o seguinte DESPACHO:\r
1 - Desmembre-se o feito em relação ao acusado LUAN DA SILVA diante da não concordância de seu patrono.\r
2- Designo novo ato para o dia 12/06/2018 às 13:00h. Requisit...''',
            'tipo': 'despacho',
            'titulo': 'Despacho em Audiência  - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2018, 4, 17)'),
            'integra': '''Cuida-se de pedido de concessão de liberdade provisória/revogação da prisão preventiva de LUIZ FERNANDO DA COSTA ARAUJO ROSA, formulado pela defesa, às fls. 91-97, que alega, em síntese, que estão ausentes os requisitos autorizadores da segregação cautelar preventiva.\r
\r
Ouvido, o Ministério Público opinou contrariamente ao pleito defensivo, às fls. 110-111.\r
É O BREVE RELATÓRIO. DECIDO.\r
\r
Assiste razão ao Ministério Público em relação à necessidade da manutenção da custódia cautelar do acusado. Frise-se que não houve qualquer alteração no contexto fático que deu ensejo à decisão que decretou a prisão preventiva.\r
\r
Resta-nos, portanto, verificar se há fundamento fático-jurídico para, no caso concreto, manter a custódia cautelar dos acusados, como requer o MP.\r
\r
Na hipótese, verifica-se que as peças de informação que integram estes autos contemplam sólidos elementos indicadores da existência material de fatos em tese delituoso (tráfico de entorpecentes ) e da autoria do acusado, que, diga-se, foi preso em flagrante na posse de quantidade significativa de entorpecentes consistente em 172 pinos de cocaína (Fls 09) e 33 tabletes de maconha (Fls.09) . Sobejamente configurado, portanto, o fumus comissi delicti (artigo 312, caput, parte final, do CPP).\r
\r
Quanto à necessidade da prisão, pode-se afirmar, com segurança, que a constrição da liberdade de locomoção do réu é medida que se impõe como forma de se garantir a ordem pública e a aplicação da lei penal.\r
\r
Note-se que estamos lidando com crime de extrema lesividade social, que afeta diretamente a população, seja por meio da destruição de instituições familiares fundamentais para o desenvolvimento individual e coletivo, seja pela atuação violenta dos narcotraficantes sobre os indefesos integrantes da cidade.\r
\r
Nesse contexto, sendo o réu apontado como vendedor de drogas, parece claro que sua liberdade contribuirá para o crescimento da nefasta atividade criminosa acima mencionada, incrementando o estado de insegurança social. Registre-se que não estamos falando de dados abstratos, mas de fatos concretos extraídos da indesejada e conhecida realidade da Comarca.\r
\r
Com base nestes fatos, entendo presentes os pressupostos autorizadores (artigos 312 e 313, inciso I e II do Código de Processo Penal) a justificar a manutenção da prisão cautelar.\r
\r
Ante o exposto, acolho os argumentos ministeriais e, por conseguinte, mantenho do decreto prisional, por seus próprios fundamentos e INDEFIRO O PEDIDO formulado pela defesa.''',
            'resumo': '...com crime de extrema lesividade social, que afeta diretamente a população, seja por meio da destruição de instituições familiares fundamentais para o desenvolvimento individual e coletivo, seja pela atuação violenta d...',
            'tipo': 'decisão',
            'titulo': 'Decisão - Decisão ou Despacho Não-Concessão'
        },
        {
            'data': GenericRepr('datetime.date(2018, 3, 22)'),
            'integra': '''Notificados regularmente, os denunciados apresentaram as peças de defesa técnica de fls. 70-71 e 78-81.\r
\r
Em que pese o empenho defensivo, as questões suscitadas não foram suficientes para fulminar as pretensões postas na inicial acusatória com toda as provas indiciárias ali contidas.\r
\r
O Processo está regular e válido, inexistindo vício a ensejar o reconhecimento de nulidade. Estão presentes as condições de ação e os pressupostos processuais. As questões pertinentes ao mérito da ação serão analisadas, oportunamente, quando do julgamento do mérito.\r
\r
Repise-se que os fatos e fundamentos deduzidos na defesa escrita não afastam os indícios de autoria e materialidade coligidos em sede extrajudicial, impondo-se a apuração dos fatos narrados na exordial da presente ação penal, garantindo-se ao(s) imputado(s) a ampla defesa e o contraditório.\r
\r
Destarte só a instrução processual penal futura poderá esclarecer os pontos controvertidos fixados pelas partes nestes autos.\r
\r
Isto posto, RECEBO A DENÚNCIA.\r
\r
Designo o dia 08/05/2018, 13;40 horas para realização da AIJ.\r
\r
Requisitem-se/intimem-se os réus e as testemunhas arroladas pelas partes.\r
\r
Dê-se ciência ao MP e à defesa técnica.''',
            'resumo': '''...tensões postas na inicial acusatória com toda as provas indiciárias ali contidas.\r
\r
O Processo está regular e válido, inexistindo vício a ensejar o reconhecimento de nulidade. Estão presentes as condições de ação e o...''',
            'tipo': 'decisão',
            'titulo': 'Decisão - Recebida a denúncia'
        },
        {
            'data': GenericRepr('datetime.date(2018, 1, 29)'),
            'integra': '''1) O MINISTÉRIO PÚBLICO ofereceu denúncia em desfavor de LUIZ FERNANDO DA COSTA ARAUJO ROSA e LUAN DA SILVA MENEZES, imputando-lhes a prática do delito descrito no artigo 33 caput e 35, ambos  da Lei 11.343/06.\r
\r
Em análise preliminar, presentes estão os pressupostos processuais, bem assim os requisitos de validade do processo e as condições da ação.\r
\r
A inicial acusatória preenche os requisitos formais enunciados pelo art. 41, do CPP, não se verificando, portanto, hipótese de rejeição liminar da denúncia.\r
\r
Assim, NOTIFIQUEM-SE os indiciados para que se manifestem em defesa prévia, no prazo de 10 (dez) dias, nos termos do art. 55, da Lei 11.343/06.Caso o indiciado não manifeste o desejo de patrocínio pela DP, e as respectivas peças defensivas não sejam apresentadas em tempo, remetam-se os autos à DP, nos termos do art. 396-A, § 2º, do CPP.\r
\r
2) DEFIRO os requerimentos ministeriais na manifestação que acompanha a denúncia.''',
            'resumo': '''1) O MINISTÉRIO PÚBLICO ofereceu denúncia em desfavor de LUIZ FERNANDO DA COSTA ARAUJO ROSA e LUAN DA SILVA MENEZES, imputando-lhes a prática do delito descrito no artigo 33 caput e 35, ambos  da Lei 11.343/06.\r
\r
Em aná...''',
            'tipo': 'despacho',
            'titulo': 'Despacho - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2018, 1, 16)'),
            'integra': '''Em 16 de janeiro de 2018, na sala de audiências deste Juízo, perante a MMª Juíza de Direito, Dr.(a). LETÍCIA D'AIUTO DE MORAES FERREIRA MICHELLI, realizou-se a Audiência de Custódia nestes autos, presentes o i. Membro do Ministério Público e o(s) custodiado(s), acompanhado(s) de sua(s) supracitada(s) defesa(s). Justificada a manutenção das algemas no(s) custodiado(s) em virtude da situação recente de flagrância, dimensões da sala de audiências, bem como pela necessidade de preservação da integridade física dos presentes. Aberta a audiência, foram os presentes cientificados da utilização do registro fonográfico/audiovisual. Após a(s) Defesa(s) ter(em) se entrevistado reservadamente com o(s) custodiado(s), procedeu-se à(s) entrevista(s), conforme termo(s) e registro(s) audiovisual. As declarações hoje colhidas, gravadas, foram salvas no CD que acompanha esta assentada e será acautelado no Cartório da CEAC.\r
\r
O MP opina pela conversão da prisão em flagrante em prisão preventiva.\r
\r
Pela Defesa foi requerida a liberdade provisória.\r
\r
Pela MMª Juíza de Direito foi proferida a seguinte DECISÃO: ´Inicialmente, cumpre consignar que pelo custodiado LUAN foi dito que foi agredido com um chute na costela no momento de sua prisão; que estava deitado e algemado no momento; que não ficou com marcas; que a agressão foi realizada por Policial Militar.\r
\r
Pelo custodiado LUIZ FERNANDO não foi informada qualquer agressão no ato prisional.\r
\r
Compulsando os autos, verifico que custodiado presos em flagrante delito pela prática, em tese do crime de TRAFICO E ASSOCIAÇAO PARA O TRÁFICO.\r
\r
Inicialmente, cabe ressaltar que não há nada que indique ilegalidade na prisão do acusado, tratando-se de flagrante formal e perfeito. A alegação defensiva de que os policiais teriam entrado na casa do custodiado e ´forjado´ o flagrante não possui qualquer guarida nos depoimentos prestados em sede policial, devendo-se ter em conta ainda que o estado flagrancial desde já afasta eventual alegação de nulidade pelo ingresso na residência deste sem mandado judicial.\r
\r
Em relação ao pedido de prisão preventiva formulado pelo Ministério Público, de se notar se trata de medida de cautela processual, cabível, excepcionalmente, quando presentes e demonstrados, ainda que sucintamente, os pressupostos e requisitos insertos no artigo 312 do Código de Processo Penal.\r
\r
Como medida cautelar, deve ser demonstrada a coexistência de fumus comissi delicti e periculum libertatis que justifiquem o cárcere antes do trânsito em julgado de decisão condenatória. No presente caso, atesta-se a presença do fumus comissi delicti pela prisão em flagrante dos custodiados na posse de mais de 100 ´sacolés´ de maconha e 172 ´sacolés´ de cocaína, nos termos do auto de apreensão e laudo prévio acostado aos autos, além de 06 rádios comunicadores.\r
\r
O periculum libertatis, definido como o risco provocado pela manutenção da acusada em liberdade, está igualmente presente: trata-se de crime grave, em que os custodiados traziam consigo quantidade considerável de droga para venda, consistente em quase 300 ´sacolés´ de droga, todos devidamente acondicionados para venda, além de meia dúzia de radiocomunicadores denotam a gravidade em concreto do delito.\r
\r
O periculum libertatis, definido como o risco provocado pela manutenção do acusado em liberdade, está igualmente presente: A FAC atesta que o custodiado LUAN é REINCIDENTE ESPECIFICO, o que evidencia a alta periculosidade do acusado e o grande risco de reiteração criminosa, de forma que sua liberdade enseja grande risco para a ordem pública.\r
\r
Ademais, não há que se falar em violação ao princípio da homogeneidade no caso em tela, visto que consideração dos elementos dispostos no art. 59 do Código Penal autoriza o eventual cumprimento de pena em regime fechado, nos termos do art. 33 § 3º do Código Penal.\r
\r
Deve-se ter em conta que a alegação defensiva de que a colaboração de LUAN deveria ensejar sua soltura por ofensa a tal princípio não pode ser ensejadora da liberdade provisória requerida, seja pela necessidade de analise nos termos acima aventados, seja pela condição de reincidente que este ostenta.\r
\r
Neste sentido é o posicionamento do Superior Tribunal de Justiça, senão vejamos:\r
\r
A alegação de desproporcionalidade da prisão preventiva somente poderá ser aferível após a prolação de sentença, não cabendo, durante o curso do processo, a antecipação da análise quanto a possibilidade de cumprimento de pena em regime menos gravoso, caso seja prolatada sentença condenatória, sob pena de exercício de adivinhação e futurologia, sem qualquer previsão legal. Assim, não há que se falar em ofensa ao princípio da homogeneidade das medidas cautelares porque não cabe ao STJ, em um exercício de futurologia, antecipar a provável colocação da paciente em regime aberto/semiaberto ou a substituição da sua pena de prisão por restritiva de direitos. STJ. 5ª Turma. RHC 77.070/MG, Rel. Min. Felix Fischer, julgado em 16/02/2017. STJ. 6ª Turma. RHC 79.041/MG, Rel. Min. Nefi Cordeiro, julgado em 28/03/2017.\r
\r
No mesmo sentido, não há nos autos a comprovação de que o acusado reside no endereço indicado ou mesmo que exerça ocupação lícita, de forma que a decretação da cautelar em questão assegura igualmente a aplicação da lei penal. Isto porque, ausente qualquer demonstração de vínculo com esta localidade, a colocação em liberdade poderia impedir sua localização posterior.\r
\r
Finalmente, os crimes de tráfico e associação para o tráfico cometidos pelo acusado enquadra-se no disposto no art. 313, I CPP, visto que possuem pena privativa de liberdade máxima superior a 4 anos, tendo sido observados os requisitos formais da presente conversão.\r
\r
No presente caso, a determinação de medida cautelar diversa da prisão, conforme art. 319 não seria adequada ou suficiente para a garantia da ordem pública e a aplicação da lei penal pelas razões acima expostas.\r
\r
Isto posto, por isso, CONVERTO a prisão em flagrante em preventiva, com base no art. 312, caput, do CPP, uma vez que a prisão cautelar é necessária para garantia da ordem pública, por conveniência da instrução criminal e para assegurar a aplicação da lei penal. Expeça-se mandado de prisão.\r
\r
Deve o cartório da CEAC enviar estes autos ao juízo competente por distribuição, bem como acautelar a mídia em local próprio. Intimados os presentes. Nada mais havendo, foi encerrada a audiência.''',
            'resumo': 'Isto posto, por isso, CONVERTO a prisão em flagrante em preventiva, com base no art. 312, caput, do CPP, uma vez que a prisão cautelar é necessária para garantia da ordem pública, por conveniência da instrução criminal e...',
            'tipo': 'decisão',
            'titulo': 'Decisão em Audiência  - Convertido(a) o(a)'
        }
    ],
    'numero': '0008242-13.2018.8.19.0001',
    'reus': [
        {
            'cpf': None,
            'nome': 'LUIZ FERNANDO DA COSTA ARAUJO ROSA'
        }
    ],
    'vara': '2ª Vara Criminal'
}

snapshots['test_parse_process_page6 1'] = {
    'advogados': [
        {
            'nome': 'LYDIO DA HORA SANTOS',
            'oab': 'RJ033191'
        },
        {
            'nome': 'LUCILIA BARROS RODRIGUES',
            'oab': 'RJ105692'
        },
        {
            'nome': 'DEFENSORIA PUBLICA',
            'oab': 'DP000001'
        },
        {
            'nome': 'HERALDO MACHADO PAUPERIO',
            'oab': 'DF012440'
        },
        {
            'nome': 'HERALDO MACHADO PAUPERIO',
            'oab': 'RJ002575'
        },
        {
            'nome': 'ERNANI M FURTADO',
            'oab': 'RJ075610'
        },
        {
            'nome': 'WELLINGTON C. COSTA JR.',
            'oab': 'RJ093311'
        },
        {
            'nome': 'ESIO LOPES NEVES',
            'oab': 'RJ027232'
        },
        {
            'nome': 'FRANCISCO ALVES DA CUNHA HORTA FILHO',
            'oab': 'RJ121153E'
        },
        {
            'nome': 'RICARDO GONTIJO BUXELIN',
            'oab': 'RJ100852'
        },
        {
            'nome': 'THIAGO MARCHI MARTINS',
            'oab': 'RJ137923'
        },
        {
            'nome': 'LUIZ CARLOS DA SILVA NETO',
            'oab': 'RJ071111'
        },
        {
            'nome': 'CELSO SILVA DA CRUZ',
            'oab': 'RJ066281'
        },
        {
            'nome': 'CARLA CRISTINA NOGUEIRA COUTO',
            'oab': 'RJ086566'
        },
        {
            'nome': 'MARCO AURELIO TORRES SANTOS',
            'oab': 'RJ132210'
        }
    ],
    'assunto': 'Associação Criminosa - Art.288 do Cod Penal (Redação Dada Pela Lei 12.850 de 2013)',
    'autor': 'MP',
    'classe': 'Ação Penal - Procedimento Ordinário',
    'comarca': 'Regional de Bangu',
    'movimentacoes': [
        {
            'data': GenericRepr('datetime.date(2008, 10, 30)'),
            'integra': 'SUBAM OS AUTOS AO E. TRIBUNAL DE JUSTIÇA COM AS HOMENAGENS DE ESTILO.',
            'resumo': 'SUBAM OS AUTOS AO E. TRIBUNAL DE JUSTIÇA COM AS HOMENAGENS DE ESTILO.',
            'tipo': 'despacho',
            'titulo': 'Despacho - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2007, 3, 5)'),
            'integra': '''1) Cobre-se a devolução das precatórias de fls. 2829 e 2831, com urgência por se tratar de réus presos;\r
\r
2) Recebo os recursos de fls. 2.836, 2837 e 2.844, devendo a Defesa do acusado MARCOS MARINHO DOS SANTOS, ser intimada para apresentação de suas razões;\r
\r
3) Com a vinda das precatórias acima bem como das razões do acusado MArcos Marinho, subam os autos ao E. Tribunal de Justiça, uma vez que as Defesas de fls. 2.836 e 2.837, requereram a apresentação de suas razões em Superior Instância.''',
            'resumo': '''1) Cobre-se a devolução das precatórias de fls. 2829 e 2831, com urgência por se tratar de réus presos;\r
\r
2) Recebo os recursos de fls. 2.836, 2837 e 2.844, devendo a Defesa do acusado MARCOS MARINHO DOS SANTOS, ser int...''',
            'tipo': 'decisão',
            'titulo': 'Decisão - Decisão interlocutória - Outras'
        },
        {
            'data': GenericRepr('datetime.date(2007, 1, 11)'),
            'integra': 'Após analisar o conteúdo do embargos de fls. 2820, hei por bem indeferí-lo, pois como esclareci as fls. 2817, a pena do art. 14 da LEI 6368/76 passdou a ser direcioanado pelo art. 8º da Lei 8072/90, o qual afastou a pena de multa para este crime específico.',
            'resumo': 'Após analisar o conteúdo do embargos de fls. 2820, hei por bem indeferí-lo, pois como esclareci as fls. 2817, a pena do art. 14 da LEI 6368/76 passdou a ser direcioanado pelo art. 8º da Lei 8072/90, o qual afastou a pena...',
            'tipo': 'decisão',
            'titulo': 'Decisão - Decisão interlocutória - Outras'
        },
        {
            'data': GenericRepr('datetime.date(2006, 12, 5)'),
            'integra': '''... (A) DECLARO EXTINTA A PUNIBILIDADE do acusado MARCOS ANTONIO DA SILVA TAVARES, vulgo ´MARQUINHOS PARAIBA´ ou ´MARQUINHOS NITERÓI´ em razão de sua morte...........\r
(B) JULGO PROCEDENTE  EM PARTE a pretensão punitiva estatal para CONDENAR os acusados LUIZ FERNANDO DA COSTA vulgo ´FERNANDINHO BEIRA-MAR´, MARCOS MARINHO DOS SANTOS vulgo ´CHAPOLIN´ e HÉLIO RODRIGUES MACEDO, qualificados nos autos, pela prática das condutas delituosas descritas pelos arts. 158 § 1º do CP (no que tange a vítima Leonardo) e 14 da lei 6368/76 ambos n/f do art. 69 CP.\r
(C) ABSOLVO os acusados acima da imputações descritas no art. 158 § 1º do CP ( no que tange a vítima João Carlos Dias Neto) e do art 288 § único do CP o que faço com base no inciso VI do art. 386 do CPP.\r
.................................................................................................................................\r
Para o acusado LUIZ FERNANDO DA COSTA, vulgo 'FERNANDINHO BEIRA-MAR´\r
.................................................................................................................................\r
Considerando a regra esculpida no art. 69 do CP a pena para este acusado torna-se DEFINITIVA em DEZENOVE ANOS DE RECLUSÃO E TREZENTOS DIAS-MULTA, fixada esta no mínimo legal ; PENAS ESTAS QUE SE TORNAM DEFINITIVAS para fins de execução.\r
pARA O ACUSADO ´MARCOS MARINHO DOS SANTOS´ vulgo ´CHAPOLIN´\r
.................................................................................................................................\r
Considerando a regra esculpida no art. 69 do CP a pena para este acusado torna-se definitiva em DEZENOVE ANOS DE RECLUSÃO e TREZENTOS DIAS-MULTA, fixada esta no mínimo legal, PENAS ESTAS QUE SE TORNAM DEFINITIVAS para fins de execução.\r
Para o acusado HÉLIO RODRIGUES MACEDO\r
...................................................................................................................................Considerando a regra esculpida no art. 69 do CP a pena para este acusado torna-se DEFINITIVA em DEZESETE ANOS E SEIS MESES DE RECLUSÃO E DUZENTOS E CINQUENTA DIAS-MULTA, fixada esta no mínimo legal, PENAS ESTAS QUE SE TORNAM DEFINITIVAS para fins de execução.\r
Apena ora irrogada em desfavor dos Réus será cumprida em regime fechado.\r
Nego aos acusados LUIZ FERNANDO DA COSTA vulgo ´FERNANDINHO BEIRA-MAR´e  MARCOS MARINHO DOS SANTOS vulgo ´CHAPOLIN´ o direito de recorrer em liberdade, ...................................\r
........ao acusado HÉLIO DORIGUES MACEDO, excepcionalmente concedo-lhe o direito de recorrer em liberdade da presente decisão,............\r
Após o trânsito em julgado, lance-se o nome do Réus no rol dos culpados, atendendo-se ao disposto no art. 5º inciso LVII da Cartha Magna e ainda, expeça-se Carta de Guia a VEP.\r
Transitado em Julgado, expeça-se MANDADO DE PRISÃO em desfavos do acusado HÉLIO RODRIGUES MACEDO.\r
Condeno os acusados nas custas processuais.\r
Façam-se as comunicações e anotações devidas.\r
Publicada esta em mãos do Sr. Escrivão, registre-se, publique-se e sejam as partes intimadas.\r
P.R.I.C.''',
            'resumo': '''... (A) DECLARO EXTINTA A PUNIBILIDADE do acusado MARCOS ANTONIO DA SILVA TAVARES, vulgo "MARQUINHOS PARAIBA" ou "MARQUINHOS NITERÓI" em razão de sua morte...........\r
(B) JULGO PROCEDENTE  EM PARTE a pretensão punitiva ...''',
            'tipo': 'sentença',
            'titulo': 'Sentença - Julgado procedente o pedido'
        },
        {
            'data': GenericRepr('datetime.date(2006, 6, 26)'),
            'integra': 'Indefiro o pedido de fls. 2165/2166, adotando par tanto os argumentos traçados pelo MP em sua cota de fls. 2715/2716, a qual torno parte integrante da presente decisão, devolvendo as partes o prazo para apresentação de alegações finais.',
            'resumo': 'Indefiro o pedido de fls. 2165/2166, adotando par tanto os argumentos traçados pelo MP em sua cota de fls. 2715/2716, a qual torno parte integrante da presente decisão, devolvendo as partes o prazo para apresentação de a...',
            'tipo': 'decisão',
            'titulo': 'Decisão - Decisão interlocutória - Outras'
        },
        {
            'data': GenericRepr('datetime.date(2006, 5, 4)'),
            'integra': 'Intime-se o Advogado contituído de fls. 2157 para apresentação de alegações finais, com urgência.',
            'resumo': 'Intime-se o Advogado contituído de fls. 2157 para apresentação de alegações finais, com urgência.',
            'tipo': 'despacho',
            'titulo': 'Despacho - Proferido despacho de mero expediente'
        },
        {
            'data': GenericRepr('datetime.date(2004, 9, 14)'),
            'integra': '''ASSISTE  RAZAO A DEFESA. O QUE CAUSA NULIDADE E A\r
FALTA  DE OPORTUNIDADE DA DEFESA MANIFESTAR-SE EM\r
DILIGENCIAS,  NOS  TERMOS  DO  ART.  499  NAO  DA\r
INERCIA.\r
ESCLARECA-SE REQUISICAO DE FLS. 934. QUAL A FINALI\r
DADE.''',
            'resumo': '''ASSISTE  RAZAO A DEFESA. O QUE CAUSA NULIDADE E A\r
FALTA  DE OPORTUNIDADE DA DEFESA MANIFESTAR-SE EM\r
DILIGENCIAS,  NOS  TERMOS  DO  ART.  499  NAO  DA\r
INERCIA.\r
ESCLARECA-SE REQUISICAO DE FLS. 934. QUAL A FINALI\r
D...''',
            'tipo': 'despacho',
            'titulo': 'Despacho - Proferido despacho de mero expediente'
        }
    ],
    'numero': '0002521-15.2002.8.19.0204 (2002.204.002450-8)',
    'reus': [
        {
            'cpf': None,
            'nome': 'LUIZ FERNANDO DA COSTA'
        },
        {
            'cpf': None,
            'nome': 'MARCOS MARINHO DOS SANTOS'
        },
        {
            'cpf': None,
            'nome': 'HELIO RODRIGUES MACEDO'
        }
    ],
    'vara': '1ª Vara Criminal'
}
