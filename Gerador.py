import edge_tts
import asyncio

# Roteiro extraído do seu arquivo .docx
texto = """
Você sabe o que é C C I H?
Não? Então vou te explicar, C C I H é a Comissão de Controle de Infecção Hospitalar, um grupo multidisciplinar responsável por elaborar, implementar e monitorar ações de prevenção e controle das infecções hospitalares.
A função da Comissão é:
- Elaborar o Plano de Prevenção e Controle de Infecções.
- Investigar surtos e notificar infecções hospitalares.
- Estabelecer protocolos e rotinas.
- Promover treinamentos para equipes.
- Avaliar produtos e procedimentos que envolvam risco de infecção.
Dentre todas as ações desenvolvidas pela C C I H a que mais se destaca é a Higienização das Mãos, sendo ela a principal medida para prevenir a transmissão de infecções.

Agora iremos apresentar os membros que compões a Comissão de Controle de Infecção Hospitalar do AME Dracena.

Doutor Rogério Bravo - Médico Infectologista: Responsável técnico pelas decisões clínicas, avaliação de casos e definição de condutas médicas frente às infecções.
Aline Souza, Enfermeira: Atua diretamente na vigilância epidemiológica, acompanha os pacientes que realizam procedimentos cirúrgicos, investigação de casos suspeitos de infecção e treinamento das equipes. Garante a organização dos processos de toda a equipe e apoio na implementação dos protocolos da C C I H.
Pamela Farrah, Enfermeira do Núcleo de Segurança do Paciente: Atua de forma integrada com a C C I H para fortalecer a cultura de segurança, acompanhar eventos adversos e desenvolver estratégias de prevenção de riscos e melhoria contínua dos cuidados.
Milene de Cinque, Enfermeira Assistencial: Aplica as medidas de prevenção no cuidado direto ao paciente, assegurando a adesão aos protocolos.
Marisa Brigo, Enfermeira da Oncologia: Garante a aplicação dos protocolos de prevenção em pacientes imunocomprometidos.
Lucas Bernardes, Enfermeiro da Oncologia: Alinha as ações da oncologia com as diretrizes da C C I H, garantindo segurança e qualidade no cuidado.
Lilian Severiano, Farmacêutica: Avalia o uso racional de antimicrobianos, participa de comissões e auxilia na prevenção da resistência bacteriana.
Cláudia Martin, Farmacêutica da Oncologia: Controle e monitoramento de medicamentos oncológicos, garantindo práticas seguras e livres de contaminação.
Fátima Costa, Equipe de Higiene e Limpeza: Responsável por aplicar corretamente as técnicas de limpeza e desinfecção, fundamentais para a prevenção.
Rosely Versegnossi, Técnica de Laboratório de Análises Clínicas: Responsável pela sala de coletas e exames laboratoriais, atuando com técnicas assépticas, contribuindo para o diagnóstico correto e ágil.

Você já pensou como pode contribuir com a C C I H?
Aqui estão algumas coisas que você pode realizar no dia-a-dia de trabalho. Isso irá impactar diretamente no atendimento e saúde dos pacientes e profissionais.

- Cumprir corretamente os protocolos de higienização das mãos e precauções padrão.
- Comunicar eventos adversos e situações de risco.
- Participar dos treinamentos promovidos pela C C I H.
- Colaborar com auditorias e avaliações.
- Incentivar colegas a manter boas práticas de segurança.


Portanto, em alusão ao dia Nacional da C C I H, através desse vídeo gostaríamos de reforçar que o controle de infecção é uma responsabilidade coletiva e incentivar o protagonismo de cada profissional na segurança do paciente.

"""

async def gerar_audio():
    communicate = edge_tts.Communicate(
        texto, 
        voice="pt-BR-AntonioNeural",  # Voz masculina natural em português do Brasil
        rate="+10%"  # Pode ajustar para "+10%" ou "-10%" se quiser mais rápido/lento
    )
    await communicate.save("ccih_audio.mp3")
    print("Áudio gerado com sucesso: ccih_audio.mp3")

asyncio.run(gerar_audio())
