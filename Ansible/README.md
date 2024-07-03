# Сценарий настройки сервера Debian 10 и запуска Postgresql
## Инструкция по запуску:
## Откройте терминал и выполните следующую команду:

```ansible-playbook -i hosts playbook.yml```


### При возникновении проблем с несовместимостью версий PostgreSQL-16 и Debian-10 рекомендуется понизить версию PostgreSQL до 14 в файле roles/postgresql/tasks/main.yml:
```- name: Ensure PostgreSQL is installed 
  apt:
    name: "{{ item }}"
    state: present
  with_items:
    - postgresql-14
    - postgresql-client-14 
```
