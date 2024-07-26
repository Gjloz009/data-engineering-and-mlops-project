# Instance Configuration

## Steps to setting up the instance as required for the proyect
<p align="justify">
1. First you need to access to your instance.
</p>

---

<p align="justify">
2. Install <code>git</code> and clone the repository.
</p>

```
sudo apt install git
```
```
git clone https://github.com/Gjloz009/mlops_proyect_jaf.git
```
---

<p align="justify">
3. Install a distribution of <code>Anaconda</code>, for this case I chosed <code>Miniconda</code>. Please chose the one that suits for your machine. You can follow the Quick command line install section in the link to fast install.
</p>

> https://docs.anaconda.com/miniconda/

```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```
After installing, initialize <code>miniconda</code>.

```
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

<p align="center">
  <img src="images\conda_1.png">
</p>

<p align="center">
  <img src="images\conda_2.png">
</p>

One recomendation is to create an environment in Conda if you have more proyects in the machine. 

```
conda create -n name_enviornment python=3.12
``` 

---

<p align="justify">
4. Install <code>Docker</code>. I'm using wsl2 I'll show how to install it for this particular case and also in a more general case.
</p>

<p align="justify">
4.1 Typicall case 
</p>

Please update the libraries.

```
sudo apt-get update
```
Now install docker 

```
sudo apt-get install docker.io
```

If you don´t want to preface the docker command with sudo, create a Unix group called docker and add users to it.

```
sudo groupadd docker
```

add user to the docker group

```
sudo usermod -aG docker $USER
```

Log out and log back in so the changes persist.

Verifiy that you can run docker commands without sudo.

```
docker run hello-world
```
Please refer to the docker docs for faq or any doubt if I was not clear.

> https://docs.docker.com/engine/install/linux-postinstall/

<p align="justify">
4.2 <code>WSL</code> case 
</p>

If you are working with wsl you have to download the docker for windows package and install it, the docker desktop will connect with your distribution in wsl. You have to initalize docker desktop every time you want to use it .

Please add user to docker group

```
sudo usermod -aG docker $USER
```

> https://docs.docker.com/desktop/install/windows-install/

If you have problems using docker in your wsl environment please check the access settings on the docker desktop in enabled.

<p align="center">
  <img src="images\docker_desktop_1.png">
</p>

---

<p align="justify">
5. Install <code>Terraform</code> , download the binary from the hashicorp official page and unzipt it and save it in a location that is on your PATH variable
</p>

```
echo $PATH
```
```
mv ~/Downloads/terraform /usr/local/bin/
```
<p align="center">
  <img src="images\terraform.png">
</p>

Verify the installation

```
terraform -help
```

> https://developer.hashicorp.com/terraform/install?product_intent=terraform

