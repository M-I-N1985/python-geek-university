"""
Decoradores (Decorators)

O que são Decorators?
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Highet Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar  /  Açucar sintático)

  /------------------------------/
 /       Função Decorator       /
/------------------------------/

-----------------------------------------------
  /    /------------------------------/    /
 /    /       Função Decorada        /    /
/    /------------------------------/    /
------------------------------------------

#  Decorators como funções (Sintaxe não recomendada / Sem Açucar Sintático)

def seja_educada(funcao):
    def sendo():
        print('Fou um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('seja bem vindo a Geek University')

#  Testando 1

#  Saudacao()

teste = seja_educada(saudacao)
teste()

#  Testando 2

def raiva():
    print('Eu te odeio!')

raiva_educada = seja_educada(raiva)
raiva_educada()


def seja_educada_mesmo(funcao):
    def sendo_mesmo():
        print('Fou um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo_mesmo

@seja_educada_mesmo
def apresentando():
    print('Meu nome é Iuri')

#  Testando

apresentando()


@seja_educada_mesmo
def dormir():
    print('Quero dormir...')


dormir()

"""
"""
|-----------------------------------------------------|
|  Home  |  Serviços  |  Produtos  |  Administrativo  |
|-----------------------------------------------------|
http://www.suaempresa.com.br/home
htpp://www.suaempresa.com.br/servicos
htpp://www.suaempresa.com.br/produtos
htpp://www.suaempresa.com.br/admin


#  OBS: Não é código funcional (Que funcione) é apenas exemplo

def checa_login(request)

"""