# Инструкция по запуску

Запуск Ansible Playbook:

```ansible-playbook -i hosts playbook.yml```


> Могут возникнуть проблемы в несовместимости версий PostgreSQL-16 и Debian-10
>> В этом случае рекомендуется понизить версию PostgreSQL на 14 в roles/postgresql/tasks/main.yml
>>
``` 
- name: Ensure PostgreSQL is installed 
  apt:
    name: "{{ item }}"
    state: present
  with_items:
    - postgresql-14
    - postgresql-client-14 
```