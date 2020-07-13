
# DevOps Assignment

This project has tasks/programs satisfying the assignments

## Contents

* [Prerequisites](#pre requisites)
* [PythonTask](#pythontask)


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







## Tech stack used

* Python
* Docker 
* HaProxy
* Ansible
