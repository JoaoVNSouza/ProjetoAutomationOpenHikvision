# Importar bibliotecas.
import pyautogui as pag
import os
import time as t

# Definições.
caminho_hikvision = r'C:\Hikvision\Hikcentral\Client\HikCentralControlClient.exe'
pag.PAUSE = 5
pag.FAILSAFE = True


# Métodos.
def abrir_hikvision() -> None:
    """
    Abre o Hikvision.

    Parameters:
        None

    Returns:
        None
    """

    t.sleep(2)
    pag.click(1000, 500)

    if not os.path.exists(caminho_hikvision):
        print('Hikvision não encontrado.')

    print('Abrindo Hikvision...')
    os.startfile(caminho_hikvision)

    # Abrir tela do Hikvision.
    t.sleep(40)
    print('Terminou de abrir o Hikvision...')
    # pag.click(1061, 589)  # Alerta OK.
    # t.sleep(10)


def abrir_cameras() -> None:
    """
    Abre as cameras.

    Parameters:
        None

    Returns:
        None
    """

    pag.click(1552, 154)     # Maximizar.
    print('Clicou maximizar.')
    pag.click(365, 394)     # Monitoring.
    t.sleep(2)
    print('Clicou Monitor.')
    pag.click(84, 163)      # Abrir Views.
    pag.click(883, 340)     # Clica no preto.
    # pag.click(109, 220)     # Minimiza Public.
    pag.click(300, 850)     # Maximizar Private.
    pag.click(390, 230, 2)  # Abrir VIEW.
    t.sleep(2)
    pag.click(1870, 56)     # Abrir Tela Cheia.


# Executar.
if __name__ == '__main__':
    abrir_hikvision()
    abrir_cameras()
