"""
Demo script - Tests the code structure without needing OpenAI API Key
Useful for testing the installation and basic functionality
"""

import sys
import whisper
from gtts import gTTS
import sounddevice as sd
import soundfile as sf
import numpy as np

LANGUAGE = 'pt'
RECORDING_SECONDS = 5
SAMPLE_RATE = 16000
WHISPER_MODEL = "tiny"  # Using tiny model for faster demo


def demo_record_audio(seconds=RECORDING_SECONDS, sample_rate=SAMPLE_RATE):
    """Record audio from microphone"""
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
        
        file_name = 'demo_audio.wav'
        sf.write(file_name, audio_data, sample_rate)
        
        print('✓ Gravação concluída!\n')
        return file_name, audio_data.flatten()
    
    except Exception as e:
        print(f'❌ Erro ao gravar áudio: {e}')
        sys.exit(1)


def demo_transcribe(audio_array, model, language=LANGUAGE):
    """Transcribe audio using Whisper"""
    print('🔄 Transcrevendo áudio...')
    
    try:
        result = model.transcribe(audio_array, fp16=False, language=language)
        transcription = result["text"]
        print(f'📝 Você disse: "{transcription}"\n')
        return transcription
    
    except Exception as e:
        print(f'❌ Erro ao transcrever: {e}')
        sys.exit(1)


def demo_simulate_chatgpt(transcription):
    """Simulate ChatGPT response (without API)"""
    print('💬 Simulando resposta do ChatGPT (modo demo)...')
    
    # Simple echo response for demo
    response = f"Você disse: {transcription}. Esta é uma resposta simulada, pois você está em modo demo. Configure sua API Key no arquivo .env para usar o ChatGPT real."
    
    print(f'🤖 Resposta simulada: "{response}"\n')
    return response


def demo_text_to_speech(text, language=LANGUAGE):
    """Convert text to speech"""
    print('🔊 Gerando resposta em áudio...')
    
    try:
        gtts_object = gTTS(text=text, lang=language, slow=False)
        response_audio = "demo_response.mp3"
        gtts_object.save(response_audio)
        print(f'✓ Áudio salvo em: {response_audio}\n')
        return response_audio
    
    except Exception as e:
        print(f'❌ Erro ao gerar áudio: {e}')
        sys.exit(1)


def demo_play_audio(audio_file):
    """Play audio file"""
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
    """Main demo function"""
    print("\n" + "="*60)
    print("🎙️  MODO DEMO - Voice Chat (sem necessidade de API Key)")
    print("="*60 + "\n")
    print("ℹ️  Este modo permite testar a instalação sem API Key.")
    print("   A resposta do ChatGPT será simulada.\n")
    print("   Para usar o ChatGPT real, configure sua API Key e")
    print("   execute: python voice_chat.py\n")
    print("="*60 + "\n")
    
    # Load Whisper model
    print(f'📥 Carregando modelo Whisper ({WHISPER_MODEL})...')
    try:
        model = whisper.load_model(WHISPER_MODEL)
        print('✓ Modelo carregado!\n')
    except Exception as e:
        print(f'❌ Erro ao carregar modelo Whisper: {e}')
        sys.exit(1)
    
    # Record audio
    record_file, audio_array = demo_record_audio()
    
    # Transcribe
    transcription = demo_transcribe(audio_array, model)
    
    # Simulate ChatGPT response
    response = demo_simulate_chatgpt(transcription)
    
    # Generate speech
    response_audio = demo_text_to_speech(response)
    
    # Play response
    demo_play_audio(response_audio)
    
    print("="*60)
    print("✅ Demo concluído com sucesso!")
    print("\n💡 Próximo passo: Configure sua API Key para usar o ChatGPT real")
    print("="*60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrompido pelo usuário.")
        sys.exit(0)
