"""
Voice Chat with Whisper and ChatGPT
Records audio, transcribes with Whisper, sends to ChatGPT, and plays response
"""

import os
import sys
import whisper
import openai
from gtts import gTTS
import sounddevice as sd
import soundfile as sf
import numpy as np
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
LANGUAGE = 'pt'
RECORDING_SECONDS = 5
SAMPLE_RATE = 16000
WHISPER_MODEL = "small"  # Options: tiny, base, small, medium, large


def check_api_key():
    """Check if OpenAI API key is configured"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your-api-key-here':
        print("\n❌ ERRO: OpenAI API Key não configurada!")
        print("\nPor favor, siga estas etapas:")
        print("1. Copie o arquivo .env.example para .env")
        print("2. Edite o arquivo .env e adicione sua OpenAI API Key")
        print("3. Execute o script novamente")
        print("\nOu defina a variável de ambiente:")
        print("   export OPENAI_API_KEY='sua-chave-aqui'")
        return False
    return api_key


def record_audio(seconds=RECORDING_SECONDS, sample_rate=SAMPLE_RATE):
    """
    Record audio from microphone
    
    Args:
        seconds (int): Recording duration in seconds
        sample_rate (int): Sample rate for recording (Whisper prefers 16kHz)
    
    Returns:
        tuple: (filename, audio_array)
    """
    print(f'🎤 Gravando por {seconds} segundos...')
    print('Fale agora!\n')
    
    try:
        audio_data = sd.rec(
            int(seconds * sample_rate), 
            samplerate=sample_rate, 
            channels=1, 
            dtype='float32'
        )
        sd.wait()
        
        file_name = 'request_audio.wav'
        sf.write(file_name, audio_data, sample_rate)
        
        print('✓ Gravação concluída!\n')
        return file_name, audio_data.flatten()
    
    except Exception as e:
        print(f'❌ Erro ao gravar áudio: {e}')
        sys.exit(1)


def transcribe_audio(audio_array, model, language=LANGUAGE):
    """
    Transcribe audio using Whisper
    
    Args:
        audio_array (numpy.ndarray): Audio data
        model: Loaded Whisper model
        language (str): Language code
    
    Returns:
        str: Transcribed text
    """
    print('🔄 Transcrevendo áudio...')
    
    try:
        result = model.transcribe(audio_array, fp16=False, language=language)
        transcription = result["text"]
        print(f'📝 Você disse: "{transcription}"\n')
        return transcription
    
    except Exception as e:
        print(f'❌ Erro ao transcrever: {e}')
        sys.exit(1)


def get_chatgpt_response(transcription, api_key):
    """
    Send transcription to ChatGPT and get response
    
    Args:
        transcription (str): Transcribed text
        api_key (str): OpenAI API key
    
    Returns:
        str: ChatGPT response
    """
    print('💬 Enviando para ChatGPT...')
    
    try:
        openai.api_key = api_key
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil e amigável."},
                {"role": "user", "content": transcription}
            ]
        )
        
        chatgpt_response = response.choices[0].message.content
        print(f'🤖 ChatGPT: "{chatgpt_response}"\n')
        return chatgpt_response
    
    except openai.error.AuthenticationError:
        print('❌ Erro de autenticação: Verifique sua API Key')
        sys.exit(1)
    except openai.error.RateLimitError:
        print('❌ Limite de requisições atingido. Tente novamente mais tarde.')
        sys.exit(1)
    except Exception as e:
        print(f'❌ Erro ao chamar ChatGPT: {e}')
        sys.exit(1)


def text_to_speech(text, language=LANGUAGE):
    """
    Convert text to speech using gTTS
    
    Args:
        text (str): Text to convert
        language (str): Language code
    
    Returns:
        str: Path to audio file
    """
    print('🔊 Gerando resposta em áudio...')
    
    try:
        gtts_object = gTTS(text=text, lang=language, slow=False)
        response_audio = "response_audio.mp3"
        gtts_object.save(response_audio)
        print(f'✓ Áudio salvo em: {response_audio}\n')
        return response_audio
    
    except Exception as e:
        print(f'❌ Erro ao gerar áudio: {e}')
        sys.exit(1)


def play_audio(audio_file):
    """
    Play audio file
    
    Args:
        audio_file (str): Path to audio file
    """
    print('▶️  Reproduzindo resposta...\n')
    
    try:
        data, sample_rate = sf.read(audio_file)
        sd.play(data, sample_rate)
        sd.wait()
        print('✓ Reprodução concluída!\n')
    
    except Exception as e:
        print(f'❌ Erro ao reproduzir áudio: {e}')
        print(f'   Você pode reproduzir manualmente: {audio_file}')


def main():
    """Main function to run the voice chat"""
    print("\n" + "="*50)
    print("🎙️  Voice Chat com Whisper e ChatGPT")
    print("="*50 + "\n")
    
    # Check API key
    api_key = check_api_key()
    if not api_key:
        sys.exit(1)
    
    # Load Whisper model
    print(f'📥 Carregando modelo Whisper ({WHISPER_MODEL})...')
    try:
        model = whisper.load_model(WHISPER_MODEL)
        print('✓ Modelo carregado!\n')
    except Exception as e:
        print(f'❌ Erro ao carregar modelo Whisper: {e}')
        sys.exit(1)
    
    # Record audio
    record_file, audio_array = record_audio()
    
    # Transcribe
    transcription = transcribe_audio(audio_array, model)
    
    # Get ChatGPT response
    chatgpt_response = get_chatgpt_response(transcription, api_key)
    
    # Generate speech
    response_audio = text_to_speech(chatgpt_response)
    
    # Play response
    play_audio(response_audio)
    
    print("="*50)
    print("✅ Processo concluído com sucesso!")
    print("="*50 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
        sys.exit(0)
