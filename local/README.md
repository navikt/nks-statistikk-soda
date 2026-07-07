## Local

Folder med script som er beregnet på testkjøringer lokalt. 
Forutsetter   
- at scriptene kjøres med en bruker som har lesetilgang til datasourcen i config-filen (BigQuery)
- at pythonpakken `soda-bigquery` er installert 

Eksempler på kommandoer å bruke i terminal:
- teste at connection til en datasource er ok: `soda data-source test -ds soda-config/config.yml`  
- kjøre testene som er definert på en tabell: `soda contract verify -ds soda-config/config.yml -c soda-checks/oppgavestatistikk___nks_oppgave_dag_hist.yml`