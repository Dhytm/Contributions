import youtube_dl

class DownloadMsc:
    """
    DownloadMsc - Classe que Realiza o Download de Músicas do YouTube

    Atributos:
        url (str): ;-;

    Installation packages:
        pip install --upgrade youtube_dl;
        pip install ffmpeg;
        pip install ffprobe;
        pip install avprobe;
        pip install avconv.
    """

    def __init__(self):
        self.url = input('Digite uma URL do YouTube: ')
        
    def download(self):
        """
        Método principal. Realiza o download do áudio.
        """

        try:
            ydl = youtube_dl.YoutubeDL({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
            
            with ydl:
                result = ydl.extract_info(self.url, download=True) 

            if 'entries' in result:
                audio = result['entries'][0]
            else:
                audio = result

            audio_url = audio['url']
            print(f'Downloaded: {audio_url}')
            
        except Exception:
            print('Operação finalziada!!')


if __name__ == '__main__':

    def _main():
        """
        Função (interna) de execução da classe
        """

        try:
            download_msc = DownloadMsc()
            download_msc.download()
            
            execution = input('Digite qualquer coisa para uma nova tentativa, ou pressione apenas "enter" para encerrar o programa: ')
            if execution != '':
                    _main()
            return
        
        except Exception:
                execution = input('Digite qualquer coisa para uma nova tentativa ou pressione apenas "enter" para encerrar o programa: ')
                if execution != '':
                    _main()
                return

    _main()
