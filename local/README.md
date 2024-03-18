## Local

Folder med script som er beregnet på testkjøringer lokalt. 
Forutsetter   
- at scriptene kjøres med en bruker som har lesetilgang til datasourcen i config-filen (BigQuery)
- at pythonpakken `soda-core-bigquery` er installert

Eksempler på kommandoer å bruke i terminal:
- teste at connection til en datasource er ok: `soda test-connection -d oppgavestatistikk -c soda-config/config.yml`  
- kjøre testene som er definert på en datasource: `soda scan -d oppgavestatistikk -c soda-config/config.yml soda-checks/oppgavestatistikk.yml`