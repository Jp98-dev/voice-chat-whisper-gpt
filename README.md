🎙️ Voice Chat com Whisper e ChatGPT
Um sistema de chat por voz que grava áudio, transcreve com Whisper, envia para ChatGPT e reproduz a resposta em áudio.
English version below
📋 Requisitos

Python 3.8 ou superior
OpenAI API Key (obtenha aqui)
Microfone funcional

🚀 Instalação

Clone o repositório

bashgit clone https://github.com/seu-usuario/voice-chat-whisper-gpt.git
cd voice-chat-whisper-gpt

Crie um ambiente virtual (recomendado)

bashpython -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

Instale as dependências

bashpip install -r requirements.txt

Configure a API Key

bash# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua OpenAI API Key
# OPENAI_API_KEY=sua-chave-aqui
💻 Uso
Execute o script principal:
bashpython voice_chat.py
O programa irá:

🎤 Gravar 5 segundos de áudio do seu microfone
📝 Transcrever o áudio usando Whisper
💬 Enviar a transcrição para o ChatGPT
🔊 Converter a resposta em áudio
▶️ Reproduzir a resposta

⚙️ Configuração
Você pode ajustar as configurações no arquivo voice_chat.py:
pythonLANGUAGE = 'pt'              # Idioma (pt, en, es, etc.)
RECORDING_SECONDS = 5        # Duração da gravação
SAMPLE_RATE = 16000          # Taxa de amostragem
WHISPER_MODEL = "small"      # Modelo Whisper (tiny, base, small, medium, large)
📁 Estrutura do Projeto
voice-chat-whisper-gpt/
├── voice_chat.py       # Script principal
├── requirements.txt    # Dependências Python
├── .env.example        # Template para variáveis de ambiente
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Este arquivo
🔧 Solução de Problemas
Erro: "OpenAI API Key não configurada"

Certifique-se de ter copiado .env.example para .env
Verifique se adicionou sua API Key válida no arquivo .env

Erro de permissão do microfone

Verifique as permissões do sistema para o microfone
No macOS/Linux, pode ser necessário conceder permissões ao terminal

Modelo Whisper muito lento

Use um modelo menor: WHISPER_MODEL = "tiny" ou "base"
Modelos maiores são mais precisos, mas mais lentos

📝 Licença
MIT License - veja o arquivo LICENSE para detalhes.
🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests.

English Version
🎙️ Voice Chat with Whisper and ChatGPT
A voice chat system that records audio, transcribes with Whisper, sends to ChatGPT, and plays back the audio response.
📋 Requirements

Python 3.8 or higher
OpenAI API Key (get it here)
Working microphone

🚀 Installation

Clone the repository

bashgit clone https://github.com/your-username/voice-chat-whisper-gpt.git
cd voice-chat-whisper-gpt

Create a virtual environment (recommended)

bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

bashpip install -r requirements.txt

Configure API Key

bash# Copy the example file
cp .env.example .env

# Edit the .env file and add your OpenAI API Key
# OPENAI_API_KEY=your-key-here
💻 Usage
Run the main script:
bashpython voice_chat.py
The program will:

🎤 Record 5 seconds of audio from your microphone
📝 Transcribe the audio using Whisper
💬 Send the transcription to ChatGPT
🔊 Convert the response to audio
▶️ Play the response

⚙️ Configuration
You can adjust settings in the voice_chat.py file:
pythonLANGUAGE = 'en'              # Language (pt, en, es, etc.)
RECORDING_SECONDS = 5        # Recording duration
SAMPLE_RATE = 16000          # Sample rate
WHISPER_MODEL = "small"      # Whisper model (tiny, base, small, medium, large)
📁 Project Structure
voice-chat-whisper-gpt/
├── voice_chat.py       # Main script
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore         # Git ignored files
└── README.md          # This file
🔧 Troubleshooting
Error: "OpenAI API Key not configured"

Make sure you copied .env.example to .env
Check that you added a valid API Key in the .env file

Microphone permission error

Check system permissions for the microphone
On macOS/Linux, you may need to grant permissions to the terminal

Whisper model too slow

Use a smaller model: WHISPER_MODEL = "tiny" or "base"
Larger models are more accurate but slower

📝 License
MIT License - see LICENSE file for details.
🤝 Contributing
Contributions are welcome! Feel free to open issues or pull requests. 
