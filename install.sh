#!/bin/bash

is_user_root ()
{
    [ "$(id -u)" -eq 0 ]
}


if is_user_root;
then (
  if [ -d "/opt/color-filter-editor" ]; then (
      echo "removing previous installation...";
      rm -rf "/opt/color-filter-editor";
      )
  fi

  mkdir /opt/color-filter-editor
  mkdir /opt/color-filter-editor/cfe
  cp ./cfe /opt/color-filter-editor -r
  cp ./run_cfe.sh /opt/color-filter-editor
  cp ./LICENSE.md /opt/color-filter-editor
  cp ./README.md /opt/color-filter-editor

  cp ./cfe.desktop /usr/local/share/applications/
  chmod 755 /usr/local/share/applications/cfe.desktop
  chmod 755 /opt/color-filter-editor
  chmod 755 /opt/color-filter-editor/run_cfe.sh
  chmod 755 /opt/color-filter-editor/cfe
  chmod 755 /opt/color-filter-editor/cfe/*

  echo -e "\033[32mdone\033[0m!"
)
  else echo -e "Please, run script as \033[31mroot\033[0m!";
fi
