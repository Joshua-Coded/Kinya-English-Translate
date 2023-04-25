- script: |
    sudo apt-get update
    sudo apt-get install -y python3-pip
    sudo pip3 install -r requirements.txt
    sudo systemctl start app.yml
  displayName: 'Deploy application'