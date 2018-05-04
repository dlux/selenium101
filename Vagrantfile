# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.require_version ">= 1.8.4"

Vagrant.configure(2) do |config|
  config.vm.box = 'ubuntu/xenial64'
  config.vm.hostname = 'kanboard-box'
  config.vm.network :private_network, ip: '172.16.88.10'
  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.synced_folder './shared/', '/home/ubuntu/shared', create: true

  if ENV['http_proxy'] != nil and ENV['https_proxy'] != nil and ENV['no_proxy'] != nil 
    if not Vagrant.has_plugin?('vagrant-proxyconf')
      system 'vagrant plugin install vagrant-proxyconf'
      raise 'vagrant-proxyconf was installed but it requires to execute again'
    end
    config.proxy.http     = ENV['http_proxy']
    config.proxy.https    = ENV['https_proxy']
    config.proxy.no_proxy = ENV['no_proxy']
  end

  config.vm.provider 'virtualbox' do |v|
    v.customize ['modifyvm', :id, '--memory', 512 ]
    v.customize ["modifyvm", :id, "--cpus", 1]
  end
  config.vm.provision 'shell' do |s|
    s.inline =
        'apt-get update
         apt-get install -y git
         git clone https://github.com/dlux/InstallScripts.git
         chown -R ubuntu:ubuntu InstallScripts
         pushd InstallScripts
         sudo ./install_kanboard.sh
         popd
         '
  end
end
