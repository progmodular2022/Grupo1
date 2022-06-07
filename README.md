# Documentação Arvore Trie

def insert(word,fromWhere,isWord):
  Comportamento:  
    Função que insere nova palavra na Árvore Trie
  Parâmetros:
    - Palavra a inserir (string word)
    - Lugar onde as palavras válidas são checadas (n fromWhere)
    - Função de verificação se a palavra e válida (boolean hotspot)
  Retorno:
    - True se conseguir inserir, do contrario False

def search(word):
  Comportamento:  
    Função que verifica se palavra está na Árvore Trie
  Parâmetros:
    - Palavra a ser procurada (string word)
  Retorno:
    - True se achar palavra na árvore, False se não achar

def delete(word):
  Comportamento:  
    Função que remove palavra da Árvore Trie
  Parâmetros:
    - Palavra a ser excluída (string word)
  Retorno:
    - retorna True se conseguir deletar, do contrário False

def showAllWords():
  Comportamento:  
    Função que exibe todas as palavra da Árvore Trie
  Parâmetros:
    - Não recebe Parâmentros
  Retorno:
    - Não há retorno

def wordsWith(prefix):
  Comportamento:
    Função que exibe todas as palavras da Árvore Trie com determinado prefixo
  Parâmetros:
    - Prefixo que será utilizado para exibição (string prefix)
  Retorno:
    - Lista com todas as palavras com prefixo requisitado

def random():
  Comportamento:
    Função que retorna uma palavra aleatória presente na Árvore Trie
  Parâmetros:
    - Não recebe Parâmetros
  Retorno:
    - retorna uma palavra aleatória da Árvore Trie
