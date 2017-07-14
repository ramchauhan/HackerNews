nstalling logstash

    # require java version 8.0

    wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
    sudo apt-get install apt-transport-https
    echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list
    sudo apt-get update && sudo apt-get install logstash

    # install the plugin to output the logs in logstash
    cd /usr/share/logstash
    sudo ./bin/logstash-plugin install logstash-input-beats

    # Running the logstash after installations as a Service
    # available in /etc/systemd/system
    sudo systemctl start logstash.service

    # check the status of the service
    sudo systemctl status logstash.service

    # stop the logstash service
    sudo systemctl stop logstash.service

    # Logstash location
    /usr/share/logstash
    # logstash conf file location
    /etc/logstash/conf.d/
    # log file location
    /var/log/logstash

    # test your installation
    cd /usr/share/logstash
    sudo bin/logstash -e 'input { stdin { } } output { stdout {} }' --path.settings=/etc/logstash

    # Configure the first pipline
    cd /etc/logstash
    vim first-pipeline.conf
    # add the below lines in the above configuration file
    input {
        beats {
            port => "5043"
        }
    }

    filter {
        grok {
            match => { "message" => "%{COMBINEDAPACHELOG}"}
        }
        geoip {
            source => "clientip"
        }
    }

    output {
        stdout {
            codec => rubydebug
        }
        file {
            path => "/home/ram/Work/ExperChatLog/logs/filetest.txt"
        }
        elasticsearch {
            hosts => ["http://127.0.0.1:9200"]
        }
    }

    # Run the logstash to print the logs
    cd /usr/share/logstash
    sudo bin/logstash -f /etc/logstash/first-pipeline.conf  --config.reload.automatic --path.settings=/etc/lotash

    # Install the elastic serach for output
    sudo apt-get update && sudo apt-get install elasticsearch

    # Directory structure
    home : /usr/share/elasticsearch
    cong : /etc/elasticsearch
    default conf: /etc/default/elasticsearch
    data: /var/lib/elasticsearch
    log: /var/log/elasticsearch
    plugins: /usr/share/elasticsearch/plugins
    scripts: /etc/elasticsearch/scripts

    # modify the elasticserch the yml to accessible from remote
    sudo su
    cd /etc/elasticsearch
    vim elasticsearch.yml
    update networkhost to like below
    network.host: 0.0.0.0

    # start elastic serach (run default on 9200) check this working by localhost:9200
    sudo systemctl start elasticsearch.service

    # stop elastic serach
    sudo systemctl stop elasticsearch.service

    # installing Kibana
    sudo apt-get update && sudo apt-get install kibana

    # kibana config file path
    cd /etc/kibana

    # Modify the kibanafile for your needs (uncomment and update the below settings)
    sudo vim kibana.yml
    # uncomment below settings

    server.port: 5601
    server.host: "localhost"
    elasticsearch.url: "http://localhost:9200"

    # loading kibana index pattern
    cd /usr/share/filebeat
    ./scripts/import_dashboards -only-index

    # running kibana (http://localhost:5601/)
    sudo systemctl start kibana.service
    sudo systemctl stop kibana.service
    sudo systemctl staus kibana.service


## configure Filebeat to send log lines to Logstash

    # installation
    curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.4.1-amd64.deb
    sudo dpkg -i filebeat-5.4.1-amd64.deb

    # run the below commad
    sudo /usr/bin/filebeat.sh -configtest -e

    # Filebeat Path Location

    home: /usr/share/filebeat
    bin: /usr/share/filebeat/bin
    conf: /etc/filebeat
    data: /var/lib/filebeat
    logs: /var/log/filebeat

    # configuration for logging
    cd /etc/filebeat/
    sudo vim filebeat.yml

    # change the configuration file to pic the logs from the file location

    # update the prospectors
    filebeat.prospectors:
    - input_type: log
        paths:
            - /var/log/experchat/experchat.log     (path of the log file where logstash is running)

        fields_under_root: true
        fields:
            #level: debug
            #review: 1
            app_name: Experchat

    - input_type: log
        paths:
            - /var/log/experchat/search.log      (path of the log file where logstash is running)

        fields_under_root: true
        fields:
            #level: debug
            #review: 1
            app_name: Search

    - input_type: log
        paths:
            - /var/log/experchat/connect.log      (path of the log file where logstash is running)

        fields_under_root: true
        fields:
            #level: debug
            #review: 1
            app_name: Connect

    # configure the file to send the logs in logstash, if using only elasticsearch and kibana comment this out
    output.logstash:
        # The Logstash hosts
        hosts: ["localhost:5043"]

    # configuration for elasticsearch output if using kibana
    output.elasticsearch:
        # Array of hosts to connect to.
        hosts: ["localhost:9200"]
        template.name: "filebeat"
        template.path: "filebeat.template.json"
        template.overwrite: false

    # Run the filebeat to get the logs from file and send the output to file/elasticsearch/s3 etc
    cd /usr/share/filebeat/bin
    sudo ./filebeat -e -path.home=/etc/filebeat/

    # check the data in logstash by going with this url
    http://localhost:9200/filebeat-*

