# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box="ubuntu/xenial64"

  config.vm.provider :virtualbox do |vb|
    vb.customize ["setextradata", :id, "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled", 0]
  end

  # if Vagrant.has_plugin?("vagrant-proxyconf")
  #   config.proxy.http     = "http://{proxy_ip}:{proxy_port}"
  #   config.proxy.https    = "http://{proxy_ip}:{proxy_port}"
  #   config.proxy.no_proxy = "localhost,127.0.0.1"
  # end

  config.vm.define "lb", primary: true do |machine|
    machine.vm.hostname = "lb"

    machine.vm.synced_folder "./log/nginx", "/var/log/nginx", create: true
    
    machine.vm.network :private_network, ip:"192.168.30.10"
    machine.vm.network "forwarded_port", guest: 80, host: 8080
    machine.vm.provider "virtualbox" do |vb|
      vb.memory = "1028"
      vb.cpus=1
    end
  end

  config.vm.define "web1", primary: true do |machine|
    machine.vm.hostname = "web1"

    machine.vm.synced_folder "./src", "/var/www/html"
    machine.vm.synced_folder "./log/web1/apache2", "/var/log/apache2", create: true
    
    machine.vm.network :private_network, ip:"192.168.30.20"
    machine.vm.provider "virtualbox" do |vb|
      vb.memory = "1028"
      vb.cpus=1
    end
  end

  config.vm.define "web2", primary: true do |machine|
    machine.vm.hostname = "web2"

    machine.vm.synced_folder "./src", "/var/www/html"
    machine.vm.synced_folder "./log/web2/apache2", "/var/log/apache2", create: true
    
    machine.vm.network :private_network, ip:"192.168.30.21"
    machine.vm.provider "virtualbox" do |vb|
      vb.memory = "1028"
      vb.cpus=1
    end
  end

  config.vm.define "db" do |machine|
    machine.vm.hostname = "db"

    machine.vm.network :private_network, ip:"192.168.30.30"
    machine.vm.provider "virtualbox" do |vb|
      vb.memory = "1028"
      vb.cpus=1
    end
  end

  # once you do provisioning, you may change 'autostart' to false.
  config.vm.define "provisioner", autostart: true do |machine|
    machine.vm.hostname = "provisioner"

    machine.vm.network "private_network", ip: "192.168.30.100"
    # set file permissions so that only owner user can read the ssh private key.
    machine.vm.synced_folder ".", "/vagrant",  mount_options: ['dmode=700','fmode=700']
    machine.vm.provision :ansible_local do |ansible|
      ansible.inventory_path = "playbook/inventory/hosts"
      ansible.playbook       = "playbook/playbook.yml"
      ansible.config_file    = "playbook/ansible.cfg"
      ansible.install_mode   = :pip
      ansible.version        = "2.4.0.0" # needs to set install_mode :pip
      ansible.verbose        = true
      
      ansible.limit          = "all" # or group
    end
  end
end
 