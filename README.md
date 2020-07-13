
# DevOps Assignment

This project has tasks/programs satisfying the assignments

## Contents

* [Prerequisites](#prerequisites)
* [PythonTask](#pythontask)
* [AnsiblePostgresql](#ansiblepostgresql)
* [Techstack](#techstack)





## Prerequisites

* Docker, docker-compose installed
* Python installed(ideally 3.7+)
* Ansible 
* passwordless ssh login setup (Ansible Node --> Agent)

## PythonTask
> How to run/Steps to test the script(s)

```bash
bash-3.2$ pwd
/Users/anudeep.koliwad/pythonTask
bash-3.2$ mkdir filesDir
bash-3.2$ touch filesDir/files{1..20}.wav
bash-3.2$ touch filesDir/files{1..20}.mp4
bash-3.2$ python3 fileRename.py /Users/anudeep.koliwad/pythonTask/filesDir audiofile wav
bash-3.2$ cd /Users/anudeep.koliwad/pythonTask/filesDir
bash-3.2$ ls
audiofile_2020-07-13_000.wav    audiofile_2020-07-13_007.wav    audiofile_2020-07-13_014.wav    files10.mp4            files17.mp4            files5.mp4
audiofile_2020-07-13_001.wav    audiofile_2020-07-13_008.wav    audiofile_2020-07-13_015.wav    files11.mp4            files18.mp4            files6.mp4
audiofile_2020-07-13_002.wav    audiofile_2020-07-13_009.wav    audiofile_2020-07-13_016.wav    files12.mp4            files19.mp4            files7.mp4
audiofile_2020-07-13_003.wav    audiofile_2020-07-13_010.wav    audiofile_2020-07-13_017.wav    files13.mp4            files2.mp4            files8.mp4
audiofile_2020-07-13_004.wav    audiofile_2020-07-13_011.wav    audiofile_2020-07-13_018.wav    files14.mp4            files20.mp4            files9.mp4
audiofile_2020-07-13_005.wav    audiofile_2020-07-13_012.wav    audiofile_2020-07-13_019.wav    files15.mp4            files3.mp4
audiofile_2020-07-13_006.wav    audiofile_2020-07-13_013.wav    files1.mp4            files16.mp4            files4.mp4
bash-3.2$ cd -
/Users/anudeep.koliwad/pythonTask
bash-3.2$ python3 fileRename.py /Users/anudeep.koliwad/pythonTask/filesDir videofile mp4
bash-3.2$ cd /Users/anudeep.koliwad/pythonTask/filesDir
bash-3.2$ ls
audiofile_2020-07-13_000.wav    audiofile_2020-07-13_007.wav    audiofile_2020-07-13_014.wav    videofile_2020-07-13_001.mp4    videofile_2020-07-13_008.mp4    videofile_2020-07-13_015.mp4
audiofile_2020-07-13_001.wav    audiofile_2020-07-13_008.wav    audiofile_2020-07-13_015.wav    videofile_2020-07-13_002.mp4    videofile_2020-07-13_009.mp4    videofile_2020-07-13_016.mp4
audiofile_2020-07-13_002.wav    audiofile_2020-07-13_009.wav    audiofile_2020-07-13_016.wav    videofile_2020-07-13_003.mp4    videofile_2020-07-13_010.mp4    videofile_2020-07-13_017.mp4
audiofile_2020-07-13_003.wav    audiofile_2020-07-13_010.wav    audiofile_2020-07-13_017.wav    videofile_2020-07-13_004.mp4    videofile_2020-07-13_011.mp4    videofile_2020-07-13_018.mp4
audiofile_2020-07-13_004.wav    audiofile_2020-07-13_011.wav    audiofile_2020-07-13_018.wav    videofile_2020-07-13_005.mp4    videofile_2020-07-13_012.mp4    videofile_2020-07-13_019.mp4
audiofile_2020-07-13_005.wav    audiofile_2020-07-13_012.wav    audiofile_2020-07-13_019.wav    videofile_2020-07-13_006.mp4    videofile_2020-07-13_013.mp4
audiofile_2020-07-13_006.wav    audiofile_2020-07-13_013.wav    videofile_2020-07-13_000.mp4    videofile_2020-07-13_007.mp4    videofile_2020-07-13_014.mp4
bash-3.2$

##Below script is for renaming in reverse alphabetical order
bash-3.2$ pwd
/Users/anudeep.koliwad/pythonTask
bash-3.2$ mkdir filesDir
bash-3.2$ cd filesDir/
bash-3.2$ touch resolution.wav reflection.mp4 compromise.jpg decoration.mp3 literature.jpeg presidency.mp3 articulate.wav2 prevalence.gif accessible.png illustrate.nef
bash-3.2$ cd ..
bash-3.2$ python3 fileRenameAlpha.py /Users/anudeep.koliwad/pythonTask/filesDir mp3
bash-3.2$ cd /Users/anudeep.koliwad/pythonTask/filesDir
bash-3.2$ ls
accessible.png    articulate.wav2    compromise.jpg    illustrate.nef    literature.jpeg    prevalence.gif    reflection.mp4    resolution.wav    trooniedca.mp3    ysrpnieedc.mp3
bash-3.2$

```

## HaProxy Task
> How to run/start the docker-compose stack (and in what order)

```bash

bash-3.2$ pwd
/Users/anudeep.koliwad/haproxyTask/docker-elk
bash-3.2$ docker network create web ##create external network which haproxy stack and elk stack are bound
2d8daae33f5d3abcd654584ad10b2b1bfb449a9622713d9536c9ed7b761d8f2e
bash-3.2$ docker-compose up -d ##starting elk first as nginx containers fail if logstash isn't found
Creating elasticsearch ... done
Creating kibana        ... done
Creating logstash      ... done
bash-3.2$ cd /Users/anudeep.koliwad/haproxyTask/
bash-3.2$ docker-compose up -d
Creating blue  ... done
Creating green ... done
Creating lb    ... done
bash-3.2$ docker-compose ps
Name               Command               State                   Ports
---------------------------------------------------------------------------------------
blue    /docker-entrypoint.sh ngin ...   Up      80/tcp
green   /docker-entrypoint.sh ngin ...   Up      80/tcp
lb      /docker-entrypoint.sh hapr ...   Up      0.0.0.0:80->80/tcp, 0.0.0.0:81->81/tcp
bash-3.2$ cd -
/Users/anudeep.koliwad/haproxyTask/docker-elk
bash-3.2$ docker-compose ps
    Name                   Command               State                                          Ports
---------------------------------------------------------------------------------------------------------------------------------------------
elasticsearch   /usr/local/bin/docker-entr ...   Up      127.0.0.1:9200->9200/tcp, 127.0.0.1:9300->9300/tcp
kibana          /usr/local/bin/kibana-docker     Up      127.0.0.1:5601->5601/tcp
logstash        /usr/local/bin/docker-entr ...   Up      0.0.0.0:1025->1025/udp, 127.0.0.1:5000->5000/tcp, 5044/tcp, 127.0.0.1:9600->9600/tcp
bash-3.2$

```

> Goto http://localhost:5601 ---> Discover ---> Choose the index pattern as 'nginx' ---> 
  time filter as '@timestamp' ---> Create index pattern ---> Go to Discover and view the logs!


- [x] Blue Container

![bluecontainer](/images/bluecontainer.png)

- [x] Green Container

![greencontainer](/images/greencontainer.png)

- [x] HaProxy stats page

![HaProxy stats](/images/haproxystats.png)

- [x] Choose Index Pattern on kibana

![Choose_index_pattern](/images/createindex.png)

- [x] Select timestamp field on kibana

![Select_timestamp_field](/images/timestamp.png)



## AnsiblePostgresql

> Check the postgresqlRole/defaults/main.yml for default variables
  This role installs on versions of Ubuntu(18-20) and installs postgresql accordingly
  
> This role is tested on *Ubuntu 18.04* with 
  *postgresql_version: "10"* mentioned in postgresqlRole/defaults/main.yml

> The play *otherTasks.yml* consists of firewall rules,ssh deny password logins,postgresql dump scheduling  



```bash

bash-3.2$ pwd
/Users/anudeep.koliwad/ansibleTask
bash-3.2$ ls
otherTasks.yml    postgresqlRole    setup_tasks.yml
bash-3.2$ ansible-playbook setup_tasks.yml -e "whichhost=anudeeptestnode"

PLAY [anudeeptestnode] ***********************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************************
ok: [anudeeptestnode]

TASK [postgresqlRole : include_tasks] *************************************************************************************************************************************************************
included: /Users/anudeep.koliwad/ansibleTask/postgresqlRole/tasks/variables.yml for anudeeptestnode

TASK [postgresqlRole : Include OS-specific variables (Debian).] ***********************************************************************************************************************************
ok: [anudeeptestnode]

TASK [postgresqlRole : Define postgresql_packages.] ***********************************************************************************************************************************************
ok: [anudeeptestnode]

TASK [postgresqlRole : Define postgresql_version.] ************************************************************************************************************************************************
skipping: [anudeeptestnode]

TASK [postgresqlRole : Define postgresql_daemon.] *************************************************************************************************************************************************
skipping: [anudeeptestnode]

TASK [postgresqlRole : Define postgresql_data_dir.] ***********************************************************************************************************************************************
ok: [anudeeptestnode]

TASK [postgresqlRole : Define postgresql_bin_path.] ***********************************************************************************************************************************************
ok: [anudeeptestnode]

TASK [postgresqlRole : Define postgresql_config_path.] ********************************************************************************************************************************************
ok: [anudeeptestnode]

TASK [postgresqlRole : Define postgresql_unix_socket_directories_mode.] ***************************************************************************************************************************
ok: [anudeeptestnode]

TASK [postgresqlRole : include_tasks] *************************************************************************************************************************************************************
included: /Users/anudeep.koliwad/ansibleTask/postgresqlRole/tasks/setup-Ubuntu.yml for anudeeptestnode

TASK [postgresqlRole : Install PostgreSQL python libs] ********************************************************************************************************************************************
[WARNING]: Could not find aptitude. Using apt-get instead

changed: [anudeeptestnode]

TASK [postgresqlRole : Ensure PostgreSQL packages are installed.] *********************************************************************************************************************************
changed: [anudeeptestnode]

TASK [postgresqlRole : Ensure locales present] ****************************************************************************************************************************************************
ok: [anudeeptestnode] => (item=en_US.UTF-8)

TASK [postgresqlRole : Force-restart PostgreSQL (locales)] ****************************************************************************************************************************************
skipping: [anudeeptestnode]

TASK [postgresqlRole : include_tasks] *************************************************************************************************************************************************************
included: /Users/anudeep.koliwad/ansibleTask/postgresqlRole/tasks/initialize.yml for anudeeptestnode

TASK [postgresqlRole : PostgreSQL environment vars.] **********************************************************************************************************************************************
changed: [anudeeptestnode]

TASK [postgresqlRole : Check PostgreSQL data dir exists] ******************************************************************************************************************************************
ok: [anudeeptestnode]

TASK [postgresqlRole : Check PostgreSQL database initialized.] ************************************************************************************************************************************
ok: [anudeeptestnode]

TASK [postgresqlRole : Initialize PostgreSQL database] ********************************************************************************************************************************************
skipping: [anudeeptestnode]

TASK [postgresqlRole : include_tasks] *************************************************************************************************************************************************************
included: /Users/anudeep.koliwad/ansibleTask/postgresqlRole/tasks/configure.yml for anudeeptestnode

TASK [postgresqlRole : Configure global settings.] ************************************************************************************************************************************************
changed: [anudeeptestnode] => (item={'option': 'unix_socket_directories', 'value': '/var/run/postgresql'})

TASK [postgresqlRole : Configure pg_hba values] ***************************************************************************************************************************************************
changed: [anudeeptestnode]

TASK [postgresqlRole : Check postgresql unix sock dirs exist] *************************************************************************************************************************************
ok: [anudeeptestnode] => (item=/var/run/postgresql)

TASK [postgresqlRole : include_tasks] *************************************************************************************************************************************************************
included: /Users/anudeep.koliwad/ansibleTask/postgresqlRole/tasks/restart.yml for anudeeptestnode

TASK [postgresqlRole : start postgresql now and on boot] ******************************************************************************************************************************************
ok: [anudeeptestnode]

TASK [postgresqlRole : include_tasks] *************************************************************************************************************************************************************
included: /Users/anudeep.koliwad/ansibleTask/postgresqlRole/tasks/users.yml for anudeeptestnode

TASK [postgresqlRole : Ensure PostgreSQL users are present.] **************************************************************************************************************************************
changed: [anudeeptestnode] => (item=None)
changed: [anudeeptestnode]

TASK [postgresqlRole : include_tasks] *************************************************************************************************************************************************************
included: /Users/anudeep.koliwad/ansibleTask/postgresqlRole/tasks/databases.yml for anudeeptestnode

TASK [postgresqlRole : Create postgresql databases needed.] ***************************************************************************************************************************************
changed: [anudeeptestnode] => (item={'name': 'testdb'})

TASK [ssh no password logins] *********************************************************************************************************************************************************************
changed: [anudeeptestnode] => (item=PasswordAuthentication)
changed: [anudeeptestnode] => (item=ChallengeResponseAuthentication)

TASK [restart sshd] *******************************************************************************************************************************************************************************
changed: [anudeeptestnode]

TASK [Allow postgresql connections] ***************************************************************************************************************************************************************
changed: [anudeeptestnode]

TASK [Create postgresql backup dir] ***************************************************************************************************************************************************************
changed: [anudeeptestnode]

TASK [postgresql backup "daily time"] *************************************************************************************************************************************************************
changed: [anudeeptestnode]

RUNNING HANDLER [postgresqlRole : restart postgresql] *********************************************************************************************************************************************
changed: [anudeeptestnode]

PLAY RECAP ****************************************************************************************************************************************************************************************
anudeeptestnode : ok=32   changed=13   unreachable=0    failed=0    skipped=4    rescued=0    ignored=0

bash-3.2$

```



## Techstack

* Python
* Docker 
* HaProxy
* Ansible
