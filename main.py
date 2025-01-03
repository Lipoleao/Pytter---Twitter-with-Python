import menu
import funcoes
import acoes
from colorama import Fore, Back, Style, init

def main():
    stop = 1
    while True:
        menu.display_logo()
        menu.colorful_menu()
        choice = input(Fore.GREEN + "   Aperte " + Fore.YELLOW + "Enter " + Fore.GREEN + "para continuar:")
        if choice == '':
            while True:
                stop -= 1
                menu.display_cadastro()
                try:
                    escolha_mn = int(input("Qual ação deseja executar?: "))
                except:
                    print(Fore.RED+"Insira uma opção válida")
                    break
                if escolha_mn  == 1:
                    emailLogin= input(Fore.YELLOW+"\nDigite o seu email: "+Fore.WHITE)
                    senhaLogin = input(Fore.YELLOW+"Digite o sua senha: "+Fore.WHITE)
                    usuario_atual = funcoes.login_user(emailLogin,senhaLogin)
                    if usuario_atual == None:
                        break
                    stop = 0
                    while stop == 0:
                        menu.display_escolha_acao()
                        while True:
                            try:
                                acoes_escolha = int(input(Fore.LIGHTBLACK_EX+"Selecione sua ação: "+Fore.WHITE))
                                if acoes_escolha == None:
                                    break
                                elif acoes_escolha == 0:
                                    stop +=1
                                    break
                                elif acoes_escolha > 3:
                                    print(Fore.RED+"Insira uma opção válida")
                                    break
                                acoes.menu_acao(acoes_escolha, usuario_atual)
                                break
                            except:
                                print(Fore.RED+"Insira uma opção válida")
                                break
                elif escolha_mn  == 2:
                    nomeCadastro = input(Fore.YELLOW+"\nDigite seu nome: "+Fore.WHITE)
                    emailCadastro= input(Fore.YELLOW+"Digite o seu email: "+Fore.WHITE)
                    senhaCadastro = input(Fore.YELLOW+"Digite o sua senha: "+Fore.WHITE)
                    confirmar_senha= input(Fore.YELLOW+"Confirme sua senha: "+Fore.WHITE)
                    if confirmar_senha == senhaCadastro:
                        usuario_atual = funcoes.create_user(nomeCadastro, emailCadastro, senhaCadastro)
                        if usuario_atual == None:
                            break
                        if usuario_atual:
                            print(Fore.GREEN+f"Usuário criado com sucesso:"+Fore.WHITE+f" {usuario_atual.id}")
                        else:
                            print(Fore.RED+"Falha ao criar usuário")
                    else:
                        print(Fore.RED+"\nSenhas não correspondem")
                        break
                    stop = 0
                    while stop == 0:
                        menu.display_escolha_acao()
                        while True:
                            try:
                                acoes_escolha = int(input(Fore.LIGHTBLACK_EX+"Selecione sua ação: "+Fore.WHITE))
                                if acoes_escolha == None:
                                    break
                                elif acoes_escolha == 0:
                                    stop +=1
                                    break
                                elif acoes_escolha > 3:
                                    print(Fore.RED+"Insira uma opção válida")
                                    break
                                acoes.menu_acao(acoes_escolha, usuario_atual)
                                break
                            except:
                                print(Fore.RED+"Insira uma opção válida")
                                break
                else:
                    funcoes.fechar_programa()
        else:
            print(Fore.RED + "Fechando o programa...")
            break

if __name__ == '__main__':
    main()
