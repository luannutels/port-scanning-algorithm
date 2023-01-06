# port-scanning-algorithm

O port scanning é uma técnica utilizada por atacantes para identificar quais portas de um dispositivo estão abertas e, assim, encontrar possíveis vulnerabilidades que possam ser exploradas. 
Ele pode ser realizado de forma manual ou automatizada, usando ferramentas específicas para esse fim.

Esse código fica em loop por todas as portas possíveis (de 1 a 65535) e tenta se conectar a cada uma delas. 
Se a conexão for bem-sucedida, isso significa que a porta está aberta e pode ser explorada pelos atacantes.

O port scanning é uma técnica comummente utilizada por atacantes, mas também pode ser usada de forma legítima pelos responsáveis pela segurança de redes para identificar possíveis vulnerabilidades. 
