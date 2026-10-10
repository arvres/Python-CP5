# Passagem de plantão - Loja Arvre

Pedro Henrique Alves - RM 569192 |

## 1. Contexto e como executar

O sistema escolhido é a **LojaArvre**, uma loja virtual fictícia com módulos como login, pagamento, catálogo e relatório.
Quando uma equipe encerra o turno, o programa registra as ocorrências (problemas) em `ocorrencias.json` e as ações tentadas em `diario.txt`.
Ele gera `passagem.txt`, com as pendências que a próxima equipe deve tratar.
Todos os dados de teste são inventados, sem dados pessoais reais.

**Para executar:**
    - FAÇA O DOWLOAD DE TODOS OS ARQUIVOS (MAIN.PY, CONFIG.PY, UTILS/DIARIO.PY, UTILS/OCORRENCIAS.PY, UTILS/PASSAGEM.PY)
    - OU FAÇA DOWLOAD DO ZIP
    - ABRA A PASTA E RODE O MAIN.PY

## 2. Testes adicionais

| Teste | Como foi feito | Resultado observado | Evidência |
|---|---|---|---|
| Arquivos ausentes | Pasta de teste vazia (sem JSON, diário e passagem). Opção 2, depois 4. | O programa não encerrou com erro. Mostrou "Não há ocorrências registradas." e "Nenhuma anotação registrada". | evidencias.pdf, figura 1 |
| Nova geração | Opção 5 duas vezes seguidas, sem cadastrar nada entre elas. | `passagem.txt` ficou idêntico nas duas vezes (sem conteúdo duplicado). `diario.txt` não mudou (mesmas 3 linhas). | evidencias.pdf, figura 2 |
| Sem pendências | Em uma cópia, `ocorrencias.json` com `[]`. Opção 5. | Saiu "Ocorrências abertas: 0", "Abertas com prioridade alta: 0" e "Nenhuma pendência para o próximo plantão". | evidencias.pdf, figura 3 |
| JSON inválido | Em uma cópia, conteúdo trocado por `{erro}`. Opções 1, 5 e 2. | Cadastro, consulta e resumo foram bloqueados com mensagem de erro. O `ocorrencias.json` continuou com `{erro}` e o `passagem.txt` anterior não mudou. O diário (opções 3 e 4) continuou funcionando. | evidencias.pdf, figura 4 |

**Teste de JSON inválido - mensagem e conteúdo preservado**

Mensagem exibida ao tentar cadastrar ou consultar (opções 1 e 2):

```
ERRO: o arquivo ocorrencias.json está inválido.
Corrija o arquivo (ele não foi alterado).
Cadastro, consulta e resumo estão suspensos até lá.
```

Mensagem exibida ao tentar gerar o resumo (opção 5):

```
ERRO: ocorrencias.json inválido. O resumo anterior foi mantido.
```

Conteúdo de `ocorrencias.json` depois dos testes (inalterado):

```
{erro}
```

## 3. Problema encontrado durante o desenvolvimento

**Comportamento observado:** ao dividir o programa em vários arquivos (`main.py`, `sistema.py` e a pasta `utils/`), ele não iniciava. O Python mostrava um `ImportError` com a mensagem "cannot import name ... from partially initialized module ... (most likely due to a circular import)". Em seguida, ao consultar ocorrências, apareceu também um `KeyError`.

**Causa identificada:**
- `sistema.py` importava `main` de `main.py`, e `main.py` importava `NOME_SISTEMA` de `sistema.py`. Cada arquivo esperava o outro terminar de carregar (import circular). Os arquivos de `utils/` também importavam as constantes de `sistema.py`.
- Na função `consultar_ocorrencias`, a chave estava escrita como `oc["proxima_acao}"]`, com a chave `}` dentro das aspas. O Python procurava uma chave que não existe, o que causa o `KeyError`.
- Em `passagem.py`, o import estava como `from ocorrencias import ...`, mas o arquivo fica dentro de `utils/`.

**Correção:**
- As constantes (`NOME_SISTEMA`, `ARQ_JSON`, `ARQ_DIARIO`, `ARQ_PASSAGEM`) foram movidas para `config.py`, que não importa nenhum outro arquivo. Todos os módulos passaram a usar `from config import ...`.
- `main()` passou a ser chamada no fim do `main.py`, dentro de `if __name__ == "__main__":`.
- A chave foi corrigida para `oc['proxima_acao']`, e os f-strings passaram a usar aspas simples por dentro.
- O import em `passagem.py` virou `from utils.ocorrencias import carregar_ocorrencias`.
