import edge_tts  #Serviço online do Edge que permite a conversão de texto em fala diretamente no código
import asyncio   #Biblioteca para esperar a conversão de texto em fala para depois gerar o audio

# Roteiro extraído do seu arquivo .docx
texto = """ ADICIONAR AQUI O TEXTO QUE QUER QUE O CODIGO LEIA """

async def gerar_audio():
    communicate = edge_tts.Communicate(
        texto, 
        voice="pt-BR-AntonioNeural",  # Voz masculina natural em português do Brasil
        rate="+10%"  # Pode ajustar para "+10%" ou "-10%" se quiser mais rápido/lento
    )
    await communicate.save("ccih_audio.mp3")  # Utilização da asyncio que aguarda a conversão do texto para depois salvar
    print("Áudio gerado com sucesso: ccih_audio.mp3")

asyncio.run(gerar_audio())

