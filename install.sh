#!/bin/bash

is_user_root ()
{
    [ "$(id -u)" -eq 0 ]
}


if is_user_root;
then (
  if [ -d "/opt/color_filter_editor" ]; then (
      echo "removing previous installation...";
      rm -rf "/opt/color_filter_editor";
      )
  fi

  mkdir /opt/color_filter_editor
  mkdir /opt/color_filter_editor/cfe
  cp ./cfe /opt/color_filter_editor -r
  cp ./run_cfe.sh /opt/color_filter_editor
  cp ./LICENSE.md /opt/color_filter_editor
  cp ./README.md /opt/color_filter_editor

  cp ./cfe.desktop /usr/local/share/applications/
  chmod 755 /usr/local/share/applications/cfe.desktop
  chmod 755 /opt/color_filter_editor
  chmod 755 /opt/color_filter_editor/run_cfe.sh
  chmod 755 /opt/color_filter_editor/cfe
  chmod 755 /opt/color_filter_editor/cfe/*

  echo -e "\033[32mdone\033[0m!"
)
  else echo -e "Please, run script as \033[31mroot\033[0m!";
fi
