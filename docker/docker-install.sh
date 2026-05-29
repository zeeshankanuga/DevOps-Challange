sudo apt-get update
sudo apt-get install docker.io -y
sudo apt-get install docker-compose-v2 -y
sudo usermod -aG docker $USER
sudo newgrp docker
echo "Docker and Docker Compose have been installed."
