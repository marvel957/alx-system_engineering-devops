#!/usr/bin/env bash
# Creates an ssh config file to bypass passphrase
file_line { 'Declare_identity_file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Turn_off_passwd_auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
}
file { '~/.ssh/config':
  ensure  => present,
  path    => '~/.ssh/config',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => "Host *   PasswordAuthentication no\n    IdentityFile ~/.ssh/school\n    SendEnv LANG LC_*\n    HashKnownHosts yes\n    GSSAPIAuthentication yes\n    GSSAPIDelegateCredentials no"
}
