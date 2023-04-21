# Trabalho_Redes
atividade de redes de computadores 
                                                               -----------CLIENTE-------------
Primeiro, importei os módulos socket, random e time. O socket é usado para criar conexões de rede, o random é usado para gerar combinações aleatórias de números, e o time é usado para adicionar um intervalo de tempo entre envios de combinações para o servidor.

Criei uma função generate_combination() que gera uma combinação de números aleatórios com um tamanho aleatório entre 1 e 30. A combinação é uma string composta por dígitos numéricos de 0 a 9.

Criei um objeto socket do cliente usando o protocolo AF_INET e o tipo SOCK_STREAM. Em seguida, usei o método connect() para se conectar ao servidor especificado.

Iniciei um loop infinito que gera uma nova combinação a cada 10 segundos e envia para o servidor. Usei o método send() para enviar a combinação para o servidor. Em seguida, usei o método recv() para receber a resposta do servidor, que pode ser 'ok!!' se a combinação tiver mais de 10 caracteres, ou 'par' ou 'ímpar' se a combinação tiver menos de 10 caracteres. Imprimo a resposta na tela. Depois, adiciono a palavra "end" à combinação e a envio de volta para o servidor.

                                                              ----------SERVIDOR--------------
                                                              
Primeiro, importo o modulo socket.

Em seguida, defino o endereço IP e a porta do servidor que o cliente irá se conectar.

Criei um objeto socket no servidor usando o protocolo AF_INET e o tipo SOCK_STREAM. Em seguida, usei o método bind() para vincular o socket a um endereço e porta específicos. Por fim, usei o método listen() para permitir conexões de entrada.


